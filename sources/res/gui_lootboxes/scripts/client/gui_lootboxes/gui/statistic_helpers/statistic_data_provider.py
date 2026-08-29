import weakref
from collections import defaultdict
import typing, Event
from constants import VERY_BIG_TIME
from debug_utils import LOG_WARNING
from helpers import dependency
from helpers.dependency import replace_none_kwargs
from helpers.time_utils import getServerUTCTime
from lootboxes_common import mergeDiffStat
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from th_async import th_async, th_await, await_callback
if typing.TYPE_CHECKING:
    from typing import Dict

@replace_none_kwargs(itemsCache=IItemsCache)
def makeDefaultData(lbId, itemsCache=None):
    lootBox = itemsCache.items.tokens.getLootBoxByID(int(lbId))
    expires = lootBox.getAutoOpenTime() or VERY_BIG_TIME
    return {b'expires': expires, b'ver': 0, b'stat': {}}


class LootBoxStatFetcher(object):

    def __init__(self, storage):
        self._storage = storage
        return

    def requestData(self, callback):
        raise NotImplementedError
        return

    def onAccountBecomePlayer(self):
        raise NotImplementedError
        return

    def onAccountBecomeNonPlayer(self):
        raise NotImplementedError
        return

    def processResult(self, *args, **kwargs):
        raise NotImplementedError
        return

    def onServerSettingsChanged(self, diff):
        raise NotImplementedError
        return


class StatisticDataCache(object):
    _providers = {}
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        self.__cacheStat = defaultdict((lambda : {b'expires': 0, b'ver': 0, b'stat': {}}))
        self.__isFirstSync = True
        self.__em = Event.EventManager()
        self.onBaseStatCollect = Event.Event(self.__em)
        return

    @property
    def allCacheStat(self):
        res = []
        for data in self.__cacheStat.values():
            if data[b'expires'] > getServerUTCTime():
                res.append(data[b'stat'])

        return res

    @property
    def expiresInfo(self):
        res = {}
        for lbID, data in self.__cacheStat.iteritems():
            if data[b'expires'] > getServerUTCTime():
                res[lbID] = data[b'expires']

        return res

    def getStatByLootboxID(self, lootboxID):
        if lootboxID in self.__cacheStat:
            data = self.__cacheStat[lootboxID]
            if data[b'expires'] > getServerUTCTime():
                return data[b'stat']
        return {}

    def getVersionByLootboxID(self, lootboxID=None):
        if lootboxID is not None and lootboxID in self.__cacheStat:
            return self.__cacheStat[lootboxID][b'ver']
        else:
            return sum(stat.get(b'ver', 0) for stat in self.__cacheStat.values())

    def canApplySnapshot(self, boxID, startVer):
        if boxID in self.__cacheStat:
            return self.__cacheStat[boxID][b'ver'] == startVer
        return

    def applyOpenResult(self, lootboxID, result, count):
        if lootboxID not in self.__cacheStat:
            self.__cacheStat[lootboxID] = makeDefaultData(lootboxID)
        lootboxStat = self.__cacheStat[lootboxID]
        for diff in result:
            mergeDiffStat(lootboxStat[b'stat'], diff)

        lootboxStat[b'ver'] += count
        return

    @th_async
    def requestBaseStat(self):
        if not self.__lobbyContext.getServerSettings().getLootBoxStatisticsConfig().get(b'enabled'):
            return
        futures = [await_callback((lambda callback, p=prov: p.requestData((lambda *a: (p.processResult(*a), callback(*a))))))() for prov in self._providers.values()]
        if not futures:
            return
        for fut in futures:
            yield th_await(fut)

        self.onBaseStatCollect()
        return

    def onAccountBecomePlayer(self):
        for provider in self._providers.values():
            provider.onAccountBecomePlayer()

        if self.__isFirstSync:
            self.requestBaseStat()
            self.__isFirstSync = False
        return

    def onAccountBecomeNonPlayer(self):
        for provider in self._providers.values():
            provider.onAccountBecomeNonPlayer()

        return

    def onServerSettingsChanged(self, diff):
        for provider in self._providers.values():
            provider.onServerSettingsChanged(diff)

        return

    def onDisconnected(self):
        self.__clear()
        return

    def registerProvider(self, key, provider):
        if key not in self._providers:
            self._providers[key] = provider(weakref.proxy(self))
        else:
            LOG_WARNING((b'Provider: {} is already registered').format(key))
        return

    def fillCache(self, statData):
        for lbID, data in statData.iteritems():
            lootboxInfo = self.__cacheStat[lbID]
            lootboxInfo[b'expires'] = data[0]
            lootboxInfo[b'ver'] = data[1]
            lootboxInfo[b'stat'] = data[2]

        return

    def __clear(self):
        self.__cacheStat.clear()
        self.__isFirstSync = True
        return

    def fini(self):
        self.__clear()
        self.__em.clear()
        return
