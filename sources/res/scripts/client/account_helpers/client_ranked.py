from functools import partial
import AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from debug_utils import LOG_DEBUG_DEV
from helpers import time_utils
import season_common

def _skipResponse(resultID, errorCode):
    LOG_DEBUG_DEV(b'_skipResponse', resultID, errorCode)
    return


class ClientRanked(object):

    def __init__(self, syncData):
        self.__account = None
        self.__syncData = syncData
        self.__cache = {}
        self.__ignore = True
        return

    def isEnabled(self):
        rankedConfig = self.__account.serverSettings[b'ranked_config']
        return rankedConfig is not None and rankedConfig.get(b'isEnabled', False)

    def getSeason(self):
        rankedConfig = self.__account.serverSettings[b'ranked_config']
        return season_common.getSeason(rankedConfig, time_utils.getCurrentLocalServerTimestamp())

    def getConfigs(self):
        rankedConfig = self.__account.serverSettings[b'ranked_config']
        cycleConfig = season_common.getActiveCycleConfig(rankedConfig, time_utils.getCurrentLocalServerTimestamp())
        return (rankedConfig, cycleConfig)

    def onAccountBecomePlayer(self):
        self.__ignore = False
        return

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True
        return

    def setAccount(self, account):
        self.__account = account
        return

    def synchronize(self, _, diff):
        for item in (b'ranked',):
            itemDiff = diff.get(item, None)
            if itemDiff is not None:
                synchronizeDicts(itemDiff, self.__cache.setdefault(item, {}))

        return

    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        return

    def get(self, itemName, callback):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetResponse, itemName, callback))
        return

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return

    def __onGetResponse(self, itemName, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache[b'ranked'].get(itemName, None))
        return
