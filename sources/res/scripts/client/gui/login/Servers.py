import BigWorld, Settings
from gui import GUI_SETTINGS
from Event import Event
from predefined_hosts import g_preDefinedHosts, REQUEST_RATE

class Servers(object):
    onServersStatusChanged = Event()

    def __init__(self, loginPreferences):
        self._loginPreferences = loginPreferences
        s = Settings.g_instance
        g_preDefinedHosts.readScriptConfig(s.scriptConfig, s.userPrefs)
        g_preDefinedHosts.onCsisQueryStart += self.__onServerUpdate
        g_preDefinedHosts.onPingPerformed += self.__onServerUpdate
        g_preDefinedHosts.onCsisQueryComplete += self.__onServerUpdate
        if GUI_SETTINGS.csisRequestRate == REQUEST_RATE.ALWAYS:
            g_preDefinedHosts.startCSISUpdate()
        g_preDefinedHosts.requestPing()
        self._serverList = []
        self._selectedServerIdx = 0
        self.updateServerList()
        return

    def fini(self):
        g_preDefinedHosts.stopCSISUpdate()
        g_preDefinedHosts.onCsisQueryStart -= self.__onServerUpdate
        g_preDefinedHosts.onPingPerformed -= self.__onServerUpdate
        g_preDefinedHosts.onCsisQueryComplete -= self.__onServerUpdate
        self._serverList = None
        return

    def updateServerList(self):
        self._setServerList(g_preDefinedHosts.shortList())
        return

    def _setServerList(self, baseServerList):
        self._serverList = []
        self._selectedServerIdx = 0
        serverName = self._loginPreferences[b'server_name']
        for idx, (hostName, friendlyName, csisStatus, _) in enumerate(baseServerList):
            if serverName == hostName:
                self._selectedServerIdx = idx
            self._serverList.append({b'label': friendlyName, 
               b'data': hostName, 
               b'csisStatus': csisStatus})

        return

    def startListenCsisQuery(self, startListen):
        if GUI_SETTINGS.csisRequestRate == REQUEST_RATE.ON_REQUEST:
            if startListen:
                g_preDefinedHosts.startCSISUpdate()
            else:
                g_preDefinedHosts.stopCSISUpdate()
        if startListen:
            g_preDefinedHosts.requestPing(True)
        return

    def setServerPreselection(self, peripheryId):
        hostItem = g_preDefinedHosts.periphery(peripheryId)
        if hostItem is not None:
            self._loginPreferences[b'server_name'] = hostItem.url
            self.updateServerList()
        return

    @property
    def serverList(self):
        return self._serverList

    @property
    def selectedServerIdx(self):
        return self._selectedServerIdx

    @property
    def selectedServer(self):
        if self._selectedServerIdx < len(self._serverList):
            return self._serverList[self._selectedServerIdx]
        else:
            return

    def __onServerUpdate(self, _=None):
        self.updateServerList()
        self.onServersStatusChanged(self._serverList)
        return


class DevelopmentServers(Servers):

    def __init__(self, loginPreferences):
        Servers.__init__(self, loginPreferences)
        BigWorld.serverDiscovery.changeNotifier = self.updateServerList
        return

    def fini(self):
        Servers.fini(self)
        BigWorld.serverDiscovery.searching = 0
        return

    def updateServerList(self):

        def _serverDottedHost(ip):
            return b'%d.%d.%d.%d' % (
             ip >> 24 & 255,
             ip >> 16 & 255,
             ip >> 8 & 255,
             ip >> 0 & 255)

        def _serverNetName(details):
            name = _serverDottedHost(details.ip)
            if details.port:
                name += b':%d' % details.port
                return name
            return

        def _serverNiceName(details):
            name = details.hostName
            if not name:
                name = _serverNetName(details)
            elif details.port:
                name += b':%d' % details.port
            if details.ownerName:
                name += b' (' + details.ownerName + b')'
            return name

        servers = [(_serverNiceName(server), server.serverString) for server in BigWorld.serverDiscovery.servers]
        baseServerList = g_preDefinedHosts.shortList()
        for friendlyName, hostName in servers:
            if not g_preDefinedHosts.predefined(hostName):
                baseServerList.append((
                 hostName,
                 friendlyName,
                 g_preDefinedHosts.getDefaultCSISStatus(),
                 None))

        self._setServerList(baseServerList)
        return
