from constants import SwitchState
import Event
from account_helpers.AccountSettings import AccountSettings, DEMOUNT_KIT_SEEN, RECERTIFICATION_FORM_SEEN
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.storage_novelty import IStorageNovelty
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class StorageNovelty(IStorageNovelty):
    __goodiesCache = dependency.descriptor(IGoodiesCache)
    __itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        self.onUpdated = Event.Event()
        self.__showNovelty = 0
        return

    @property
    def __noveltyData(self):
        return [{b'f': (self.__goodiesCache.getDemountKits), b'seen': DEMOUNT_KIT_SEEN},
         {b'f': (self.__goodiesCache.getRecertificationForms), b'seen': RECERTIFICATION_FORM_SEEN, b'status': (self.__isRecertificationFormsEnabled)}]

    @property
    def showNovelty(self):
        return self.__showNovelty

    @property
    def noveltyCount(self):
        return self.__showNovelty

    def init(self):
        g_clientUpdateManager.addCallbacks({b'goodies': (self.__onGoodiesUpdated)})
        self.__itemsCache.onSyncCompleted += self.__onCacheResync
        self.__resolveNovelty()
        return

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__itemsCache.onSyncCompleted -= self.__onCacheResync
        return

    def setAsSeen(self, item):
        if self.noveltyCount:
            AccountSettings.setCounters(item, True)
            self.__resolveNovelty()
        return

    @staticmethod
    def getItemsStatus(args):
        items = args[b'f'](REQ_CRITERIA.DEMOUNT_KIT.IN_ACCOUNT | REQ_CRITERIA.DEMOUNT_KIT.IS_ENABLED)
        return not AccountSettings.getCounters(args[b'seen']) and items is not None and len(items)

    @staticmethod
    def isItemsEnabled(args):
        func = args.get(b'status')
        if func is not None:
            return func()
        else:
            return True

    def __isRecertificationFormsEnabled(self):
        return self.__lobbyContext.getServerSettings().recertificationFormState() != SwitchState.DISABLED.value

    def __resolveNovelty(self):
        showNovelty = 0
        for item in self.__noveltyData:
            if self.isItemsEnabled(item) and self.getItemsStatus(item):
                showNovelty += 1

        if showNovelty != self.__showNovelty:
            self.__showNovelty = showNovelty
            self.onUpdated()
        return

    def __onGoodiesUpdated(self, *_):
        self.__resolveNovelty()
        return

    def __onCacheResync(self, *_):
        self.__resolveNovelty()
        return
