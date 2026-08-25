from functools import partial
import AccountCommands
from account_helpers.settings_core import longToInt32
from debug_utils import LOG_DEBUG, LOG_ERROR

class IntUserSettings(object):

    def __init__(self):
        self.__proxy = None
        self.__syncData = None
        self.__cache = {}
        return

    def setProxy(self, proxy, syncData):
        self.__proxy = proxy
        self.__syncData = syncData
        return

    def onProxyBecomePlayer(self):
        return

    def onProxyBecomeNonPlayer(self):
        return

    def isSynchronized(self):
        return bool(self.__cache)

    def synchronize(self, isFullSync, diff):
        cache = self.__cache
        if isFullSync:
            cache.clear()
        settingsFull = diff.get((b'intUserSettings', b'_r'), {})
        if settingsFull:
            self.__cache = dict(settingsFull)
        settingsDiff = diff.get(b'intUserSettings', {})
        if settingsDiff:
            for key, value in settingsDiff.iteritems():
                if value is not None:
                    cache[key] = value
                else:
                    cache.pop(key, None)

        LOG_DEBUG(b'IntUserSettings synchronize: cache now=%s' % self.__cache)
        return

    def getCache(self, callback=None):
        if self.__syncData:
            self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        elif callback:
            callback(AccountCommands.RES_NON_PLAYER)
        return

    def get(self, key, callback=None):
        if self.__syncData:
            self.__syncData.waitForSync(partial(self.__onGetResponse, key, callback))
        elif callback:
            callback(AccountCommands.RES_NON_PLAYER)
        return

    def addIntSettings(self, dictIntSettings, callback=None):
        if dictIntSettings:
            arr = []
            for k, v in dictIntSettings.iteritems():
                key = longToInt32(k)
                value = longToInt32(v)
                if isinstance(key, int) and isinstance(value, int):
                    arr.append(key)
                    arr.append(value)
                else:
                    import traceback
                    traceback.print_stack()
                    LOG_ERROR(b'Bad key:value pair in addIntUserSettings: %r:%r (should be int:int)' % (k, v))
                    return

        else:
            import traceback
            traceback.print_stack()
            LOG_ERROR(b'Bad dictIntSettings: %r (should be {int:int} dictionary)' % dictIntSettings)
            return
        if callback is not None:
            proxyCallback = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxyCallback = None
        if self.__proxy:
            self.__proxy._doCmdIntArr(AccountCommands.CMD_ADD_INT_USER_SETTINGS, arr, proxyCallback)
        elif callback:
            callback(AccountCommands.RES_NON_PLAYER)
        return

    def delIntSettings(self, listIntKeys, callback=None):
        arr = []
        for k in listIntKeys:
            if isinstance(k, int):
                arr.append(k)
            else:
                LOG_ERROR(b'Bad key in delIntSettings: %r (should be int)' % k)
                return

        if arr:
            if callback is not None:
                proxyCallback = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
            else:
                proxyCallback = None
            if self.__proxy:
                self.__proxy._doCmdIntArr(AccountCommands.CMD_DEL_INT_USER_SETTINGS, arr, proxyCallback)
            elif callback:
                callback(AccountCommands.RES_NON_PLAYER)
        else:
            LOG_ERROR(b'Bad delIntSettings arr: %r (should be [int] list)' % arr)
            return
        return

    def __onGetResponse(self, statName, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache.get(statName, None))
        return

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return
