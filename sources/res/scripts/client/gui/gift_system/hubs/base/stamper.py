import typing
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.gift_system.hubs.subsystems import BaseHubSubsystem
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from helpers.server_settings import GiftEventConfig

class IGiftEventStamper(BaseHubSubsystem):

    def isBalanceAvailable(self):
        raise NotImplementedError
        return

    def wasBalanceAvailable(self):
        raise NotImplementedError
        return

    def getStampCount(self, stampName):
        raise NotImplementedError
        return


class GiftEventBaseStamper(IGiftEventStamper):
    __slots__ = (b'__updateCallback', b'__isBalanceAvailable', b'__wasBalanceAvailable')
    _STAMPS = set()
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, eventSettings, updateCallback):
        super(GiftEventBaseStamper, self).__init__(eventSettings)
        self.__updateCallback = updateCallback
        self.__isBalanceAvailable = self.__wasBalanceAvailable = False
        self.__initBalanceWatchers()
        g_clientUpdateManager.addCallbacks({b'cache.mayConsumeWalletResources': (self.__updateBalanceAvailability), 
           b'cache.entitlements': (self.__updateBalanceContent)})
        return

    def destroy(self):
        self.__itemsCache.onSyncCompleted -= self.__onItemsSyncCompleted
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__updateCallback = None
        return

    def isBalanceAvailable(self):
        return self.__isBalanceAvailable

    def wasBalanceAvailable(self):
        return self.__wasBalanceAvailable

    def getStampCount(self, stampName):
        return self.__itemsCache.items.stats.entitlements.get(stampName, 0)

    def _isNotificationsEnabled(self):
        return self._settings.isEnabled

    def __initBalanceWatchers(self):
        if not self.__itemsCache.isSynced():
            self.__itemsCache.onSyncCompleted += self.__onItemsSyncCompleted
            return
        self.__onItemsSyncCompleted()
        return

    def __onItemsSyncCompleted(self, *_):
        mayConsumeWalletResources = self.__itemsCache.items.stats.mayConsumeWalletResources
        self.__isBalanceAvailable = self.__wasBalanceAvailable = mayConsumeWalletResources
        self.__itemsCache.onSyncCompleted -= self.__onItemsSyncCompleted
        self.__notifyGiftEventHub()
        return

    def __notifyGiftEventHub(self):
        if self._isNotificationsEnabled():
            self.__updateCallback()
        return

    def __updateBalanceAvailability(self, isAvailable):
        if self.__isBalanceAvailable != isAvailable:
            self.__isBalanceAvailable = isAvailable
            self.__wasBalanceAvailable = self.__wasBalanceAvailable or isAvailable
            self.__notifyGiftEventHub()
        return

    def __updateBalanceContent(self, entitlementsData):
        if self._STAMPS & set(entitlementsData.keys()):
            self.__notifyGiftEventHub()
        return
