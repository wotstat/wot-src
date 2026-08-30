from debug_utils import LOG_DEBUG, LOG_ERROR
from gui.Scaleform.Waiting import Waiting
from gui.prb_control import prb_getters
from gui.prb_control.entities.base.cooldown import PrbCooldownManager
from gui.prb_control.entities.base.requester import IPrbListRequester
from gui.prb_control.items.unit_seqs import UnitsListIterator, UnitsUpdateIterator
from gui.prb_control.settings import REQUEST_TYPE
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class UnitsListRequester(IPrbListRequester):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        self.__selectedID = None
        self.__callback = None
        self.__callbackUpdate = None
        self.__isSubscribed = False
        self.__cooldown = PrbCooldownManager()
        self.__handlers = {}
        self.__cache = {}
        return

    def __del__(self):
        LOG_DEBUG(b'Units list requester deleted:', self)
        return

    def start(self, callback):
        self.__cache.clear()
        if callback is not None and callable(callback):
            self.__callback = callback
        else:
            LOG_ERROR(b'Callback is None or is not callable')
            return
        if self.__cooldown.isInProcess(REQUEST_TYPE.UNITS_LIST):
            self.__cooldown.fireEvent(REQUEST_TYPE.UNITS_LIST)
        browser = prb_getters.getClientUnitBrowser()
        if browser:
            self.__unitBrowser_onUnitsListReceived(browser.results)
        return

    def stop(self):
        self.__cache.clear()
        self.__callback = None
        self.__callbackUpdate = None
        return

    def request(self, **kwargs):
        if self.__cooldown.validate(REQUEST_TYPE.UNITS_LIST):
            return
        LOG_DEBUG(b'Request list of units', kwargs)
        self.__cooldown.process(REQUEST_TYPE.UNITS_LIST)
        self.__cache.clear()
        browser = prb_getters.getClientUnitBrowser()
        if browser:
            if b'req' in kwargs:
                req = kwargs[b'req']
                if req in self.__handlers:
                    if self.__handlers[req](browser, **kwargs):
                        Waiting.show(b'prebattle/auto_search')
                else:
                    LOG_ERROR(b'Request is not supported', kwargs)
            else:
                LOG_ERROR(b'Request is not found', self.__handlers.keys(), kwargs)
        else:
            LOG_ERROR(b'Unit browser is not defined')
        return

    def subscribe(self, unitTypeFlags):
        if self.__isSubscribed:
            return
        self.__isSubscribed = True
        browser = prb_getters.getClientUnitBrowser()
        if browser:
            self.__cooldown.process(REQUEST_TYPE.UNITS_LIST)
            self.__handlers = {(REQUEST_TYPE.UNITS_RECENTER): (self.__recenter), 
               (REQUEST_TYPE.UNITS_REFRESH): (self.__refresh), 
               (REQUEST_TYPE.UNITS_NAV_LEFT): (self.__navLeft), 
               (REQUEST_TYPE.UNITS_NAV_RIGHT): (self.__navRight)}
            browser.subscribe(unitTypeFlags=unitTypeFlags)
            browser.onResultsReceived += self.__unitBrowser_onUnitsListReceived
            browser.onResultsUpdated += self.__unitBrowser_onUnitsListUpdated
        else:
            LOG_ERROR(b'Unit browser is not defined')
        return

    def unsubscribe(self):
        self.__handlers.clear()
        browser = prb_getters.getClientUnitBrowser()
        if browser:
            if self.__isSubscribed:
                browser.unsubscribe()
            browser.onResultsReceived -= self.__unitBrowser_onUnitsListReceived
            browser.onResultsUpdated -= self.__unitBrowser_onUnitsListUpdated
        self.__isSubscribed = False
        self.__selectedID = None
        return

    def setSelectedID(self, selectedID):
        self.__selectedID = selectedID
        return

    def addCacheItem(self, item):
        self.__cache[item.cfdUnitID] = item
        return

    def getCacheItem(self, cfdUnitID):
        try:
            item = self.__cache[cfdUnitID]
        except KeyError:
            LOG_ERROR(b'Item not found in cache', cfdUnitID)
            item = None

        return item

    def removeCacheItem(self, cfdUnitID):
        self.__cache.pop(cfdUnitID, None)
        return

    def __navLeft(self, browser, **kwargs):
        browser.left()
        return True

    def __navRight(self, browser, **kwargs):
        browser.right()
        return True

    def __recenter(self, browser, **kwargs):
        result = False
        if b'unitTypeFlags' in kwargs:
            browser.recenter(self.itemsCache.items.stats.globalRating, unitTypeFlags=kwargs[b'unitTypeFlags'])
            result = True
        else:
            LOG_ERROR(b'Types of units are not defined', kwargs)
        return result

    def __refresh(self, browser, **kwargs):
        browser.refresh()
        return True

    def __unitBrowser_onUnitsListReceived(self, data):
        Waiting.hide(b'prebattle/auto_search')
        if self.__callback:
            self.__callback(self.__selectedID, True, self.__cooldown.isInProcess(REQUEST_TYPE.UNITS_LIST), UnitsListIterator(self, data))
        return

    def __unitBrowser_onUnitsListUpdated(self, data):
        if self.__callback:
            self.__callback(self.__selectedID, False, False, UnitsUpdateIterator(self, data))
        return
