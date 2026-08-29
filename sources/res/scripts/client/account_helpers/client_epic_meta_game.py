from functools import partial
import AccountCommands
from debug_utils import LOG_DEBUG_DEV
from shared_utils.account_helpers.diff_utils import synchronizeDicts

def _skipResponse(resultID, errorCode):
    LOG_DEBUG_DEV(b'_skipResponse', resultID, errorCode)
    return


class ClientEpicMetaGame(object):
    __DATA_KEY = b'epicMetaGame'

    def __init__(self, syncData):
        self.__account = None
        self.__syncData = syncData
        self.__cache = {}
        self.__ignore = True
        return

    def setSelectedAbilities(self, listOfAbilities, vehicleCD, callback=_skipResponse):
        self.__account._doCmdIntArr(AccountCommands.CMD_UPDATE_SELECTED_EPIC_META_ABILITY, listOfAbilities + [vehicleCD], (lambda requestID, resultID, errorCode: callback(resultID, errorCode)))
        return

    def setSelectedAbilitiesVehsClass(self, listOfAbilities, vehicleCD, callback=_skipResponse):
        self.__account._doCmdIntArr(AccountCommands.CMD_UPDATE_SELECTED_EPIC_META_ABILITY_VEHICLES, listOfAbilities + [vehicleCD], (lambda requestID, resultID, errorCode: callback(resultID, errorCode)))
        return

    def increaseAbility(self, abilityID, callback=_skipResponse):
        self.__account._doCmdInt(AccountCommands.CMD_INCREASE_EPIC_META_ABILITY, abilityID, (lambda requestID, resultID, errorCode: callback(resultID, errorCode)))
        return

    def resetEpicMetaGame(self, metaLevel=0, abilityPoints=0, callback=_skipResponse):
        self.__account._doCmdInt2(AccountCommands.CMD_RESET_EPIC_META_GAME, metaLevel, abilityPoints, (lambda requestID, resultID, errorCode: callback(resultID, errorCode)))
        return

    def getStoredDiscount(self):
        return self.__cache[self.__DATA_KEY].get(b'freeEpicDiscount', {})

    def onAccountBecomePlayer(self):
        self.__ignore = False
        return

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True
        return

    def setAccount(self, account):
        self.__account = account
        return

    def synchronize(self, isFullSync, diff):
        if isFullSync:
            self.__cache.clear()
        dataResetKey = (
         self.__DATA_KEY, b'_r')
        if dataResetKey in diff:
            self.__cache[self.__DATA_KEY] = diff[dataResetKey]
        if self.__DATA_KEY in diff:
            synchronizeDicts(diff[self.__DATA_KEY], self.__cache.setdefault(self.__DATA_KEY, {}))
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
            callback(resultID, self.__cache[self.__DATA_KEY].get(itemName, None))
        return
