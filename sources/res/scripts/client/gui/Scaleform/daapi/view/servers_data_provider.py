from __future__ import absolute_import
import logging
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import icons
from gui.shared.formatters.servers import formatPingStatus
from helpers import dependency
from predefined_hosts import AUTO_LOGIN_QUERY_URL
from predefined_hosts import HOST_AVAILABILITY, PING_STATUSES, g_preDefinedHosts
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.connection_mgr import IConnectionManager
_logger = logging.getLogger(__name__)

class _INDICATOR_STATUSES(object):
    WAITING = -1
    IGNORED = -2
    ALL = (
     PING_STATUSES.UNDEFINED, PING_STATUSES.HIGH, PING_STATUSES.NORM, PING_STATUSES.LOW, WAITING, IGNORED)


class ServersDataProvider(SortableDAAPIDataProvider):
    __PING_MAX_VALUE = 999
    __settingsCore = dependency.descriptor(ISettingsCore)
    __connectionManager = dependency.descriptor(IConnectionManager)

    def __init__(self):
        super(ServersDataProvider, self).__init__()
        self._list = []
        self.__mapping = {}
        self.__selectedID = None
        self.__isColorBlind = self.__settingsCore.getSetting(b'isColorBlind')
        self.__settingsCore.onSettingsChanged += self.__onSettingsChanged
        return

    @property
    def collection(self):
        return self._list

    @property
    def isColorBlind(self):
        return self.__isColorBlind

    def emptyItem(self):
        return

    def clear(self):
        self.__clearLists()
        self.__selectedID = None
        return

    def fini(self):
        self.__settingsCore.onSettingsChanged -= self.__onSettingsChanged
        self.clear()
        self.destroy()
        return

    def getSelectedIdx(self):
        if self.__selectedID in self.__mapping:
            return self.__mapping[self.__selectedID]
        return -1

    def getSelectedID(self):
        return self.__selectedID

    def setSelectedID(self, sid):
        self.__selectedID = sid
        return

    def resetSelectedIndex(self):
        self.flashObject.resetSelectedIndex(self.getSelectedIdx())
        return

    def getVO(self, index):
        vo = None
        if index > -1:
            try:
                vo = self.sortedCollection[index]
            except IndexError:
                _logger.error(b'Item not found %i', index)

        return vo

    def buildList(self, cache):
        self.__clearLists()
        for index, item in enumerate(cache):
            vo = self._makeVO(index, item)
            self._list.append(vo)
            self.__mapping[vo[b'id']] = index

        if self.__selectedID not in self.__mapping:
            if len(self._list) == 1:
                vo = self.getVO(0)
                self.setSelectedID(vo[b'id'])
            else:
                self.__selectedID = None
        return

    def rebuildList(self, cache):
        self.buildList(cache)
        self.refresh()
        return

    def pyGetSelectedIdx(self):
        return self.getSelectedIdx()

    def refreshRandomItems(self, indexes, items):
        self.flashObject.invalidateItems(indexes, items)
        return

    def refreshSingleItem(self, index, item):
        self.flashObject.invalidateItem(index, item)
        return

    def requestItemAtHandler(self, idx):
        item = super(ServersDataProvider, self).requestItemAtHandler(idx)
        if item is None:
            _logger.debug(b'Item with id %i is None', idx)
        return item

    def _makeVO(self, index, item):
        hostName = item[b'data']
        pingValue, pingStatus = g_preDefinedHosts.getHostPingData(hostName)
        pingValue = min(pingValue, self.__PING_MAX_VALUE)
        csisStatus = item[b'csisStatus']
        serverName = item[b'label']
        pingIndicatorState = self.__getUpdatedPingStatus(pingStatus, item)
        enabled = item.get(b'enabled', csisStatus != HOST_AVAILABILITY.NOT_AVAILABLE)
        pingValueStr = formatPingStatus(csisStatus, self.__isColorBlind, False, pingStatus, pingValue)
        host = g_preDefinedHosts.byName(serverName)
        haveAccess = not host.peripheryID or self.__connectionManager.isAvailablePeriphery(host.peripheryID)
        vo = {b'id': (item.get(b'id', 0)), 
           b'data': hostName, 
           b'csisStatus': csisStatus, 
           b'label': serverName, 
           b'pingState': pingIndicatorState, 
           b'pingValue': pingValueStr, 
           b'enabled': (enabled and haveAccess), 
           b'haveAccess': haveAccess}
        if not haveAccess:
            vo[b'tooltip'] = {b'tooltip': (backport.text(R.strings.tooltips.server.notAccess()))}
        elif csisStatus == HOST_AVAILABILITY.NOT_RECOMMENDED:
            vo[b'tooltip'] = {b'tooltip': (backport.text(R.strings.tooltips.server.notRecomended(), icon=icons.serverAlert(), server=serverName))}
        elif b'tooltip' in item:
            vo[b'tooltip'] = item[b'tooltip']
        return vo

    def __clearLists(self):
        self._list = []
        self.__mapping.clear()
        return

    def __onSettingsChanged(self, diff):
        if b'isColorBlind' in diff:
            self.__isColorBlind = diff[b'isColorBlind']
            for item in self._list:
                pingValue, pingStatus = g_preDefinedHosts.getHostPingData(item[b'data'])
                pingValueStr = formatPingStatus(item[b'csisStatus'], self.__isColorBlind, False, pingStatus, pingValue)
                item[b'pingValue'] = pingValueStr

            self.refresh()
        return

    def __getUpdatedPingStatus(self, pingStatus, item):
        csisStatus = item[b'csisStatus']
        if pingStatus == PING_STATUSES.REQUESTED:
            return _INDICATOR_STATUSES.WAITING
        if csisStatus in (HOST_AVAILABILITY.RECOMMENDED, HOST_AVAILABILITY.UNKNOWN):
            return self.__checkPingForValidStatus(pingStatus)
        if csisStatus in (HOST_AVAILABILITY.NOT_AVAILABLE, HOST_AVAILABILITY.NOT_RECOMMENDED):
            return _INDICATOR_STATUSES.IGNORED
        if csisStatus == HOST_AVAILABILITY.REQUESTED:
            return _INDICATOR_STATUSES.WAITING
        if item[b'data'] == AUTO_LOGIN_QUERY_URL:
            return _INDICATOR_STATUSES.IGNORED
        return self.__checkPingForValidStatus(pingStatus)

    @staticmethod
    def __checkPingForValidStatus(incomeStatus):
        if incomeStatus in _INDICATOR_STATUSES.ALL:
            return incomeStatus
        else:
            _logger.error(b'Mismatch ping status "%s" and available indicator statuses.', incomeStatus)
            return
