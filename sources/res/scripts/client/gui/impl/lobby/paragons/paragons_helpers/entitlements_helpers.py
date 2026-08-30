from abc import ABCMeta, abstractmethod
from enum import Enum
import logging
from typing import Dict
import th_async
from Event import Event
from helpers import dependency
from paragons_common import ParagonsEntitlements, getParagonsEntitlement
from skeletons.gui.game_control import IEntitlementsController
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

class EntitlementsRequestState(Enum):
    AGATE = 0
    STATS = 1


class ParagonsEntitlementsContext(object):

    def __init__(self, state=EntitlementsRequestState.AGATE):
        self.__state = state
        self.__stateDict = {(EntitlementsRequestState.AGATE): (ParagonsEntitlementsAgate()), 
           (EntitlementsRequestState.STATS): (ParagonsEntitlementsStats())}
        return

    def init(self):
        self.state.init()
        return

    def fin(self):
        self.state.fin()
        return

    @property
    def state(self):
        return self.__stateDict.get(self.__state)


class ParagonsEntitlementState(object):
    __metaclass__ = ABCMeta
    onEntitlementsUpdated = Event()

    @abstractmethod
    def init(self):
        return

    @abstractmethod
    def fin(self):
        return

    @abstractmethod
    def getEntitlementsByID(self, entitlementID):
        return

    @abstractmethod
    def update(self, force=False):
        return


class ParagonsEntitlementsAgate(ParagonsEntitlementState):
    __entitlementsController = dependency.descriptor(IEntitlementsController)

    def __init__(self):
        self.__entCodes = [getParagonsEntitlement(code) for code in ParagonsEntitlements.all()]
        self.__cache = {}
        return

    def init(self):
        self.__entitlementsController.onCacheUpdated += self.__onCacheUpdated
        return

    def fin(self):
        self.__entitlementsController.onCacheUpdated -= self.__onCacheUpdated
        return

    def getEntitlementsByID(self, entitlementID):
        if entitlementID not in self.__entCodes:
            return
        if entitlementID not in self.__cache:
            self.update(force=True)
        return self.__cache.get(entitlementID, 0)

    def isCached(self):
        return self.__entitlementsController.isCacheInited()

    @th_async.th_async
    def update(self, force=False):
        if not self.__entitlementsController.isCacheInited():
            force = True
        else:
            force = all(self.__entitlementsController.getBalanceEntitlementFromCache(code) is not None for code in self.__entCodes)
        if force:
            yield th_async.th_await(self.__entitlementsController.forceUpdateCache(self.__entCodes))
            for code in self.__entCodes:
                balance = self.__entitlementsController.getBalanceEntitlementFromCache(code)
                amount = balance.getAmount() if balance is not None else 0
                self.__cache[code] = amount

        return

    def storeGranted(self, entitlements):
        if not self.__cache:
            return
        for entitlementID, amount in entitlements.iteritems():
            self.__cache[entitlementID] += amount

        self.__onCacheUpdated()
        return

    def consumeGranted(self, entitlementID):
        if entitlementID not in self.__cache:
            return
        self.__cache[entitlementID] -= 1
        self.__onCacheUpdated()
        return

    def __onCacheUpdated(self):
        self.onEntitlementsUpdated()
        return

    def onDisconnect(self):
        self.__cache = {}
        return


class ParagonsEntitlementsStats(ParagonsEntitlementState):
    __itemsCache = dependency.descriptor(IItemsCache)

    def init(self):
        self.__itemsCache.onSyncCompleted += self.__onCacheUpdated
        return

    def fin(self):
        self.__itemsCache.onSyncCompleted -= self.__onCacheUpdated
        return

    def getEntitlementsByID(self, entitlementID):
        if entitlementID not in ParagonsEntitlements.all():
            _logger.error(b"[Paragons]: requested entitlementID doesn't exist IDs=%s", entitlementID)
            return 0
        return self.__itemsCache.items.stats.entitlements.get(getParagonsEntitlement(entitlementID), 0)

    def update(self, force=False):
        return

    def __onCacheUpdated(self):
        self.onEntitlementsUpdated()
        return
