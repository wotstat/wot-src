import cPickle
from functools import partial, wraps
import AccountCommands, constants, items
from account_helpers.premium_info import PremiumInfo
from debug_utils import LOG_DEBUG_DEV, LOG_WARNING, LOG_ERROR
from helpers import time_utils
from piggy_bank_common.settings_constants import PIGGY_BANK_PDATA_KEY
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from items import vehicles
from gui.shared.money import Currency
_VEHICLE = items.ITEM_TYPE_INDICES[b'vehicle']
_CHASSIS = items.ITEM_TYPE_INDICES[b'vehicleChassis']
_TURRET = items.ITEM_TYPE_INDICES[b'vehicleTurret']
_GUN = items.ITEM_TYPE_INDICES[b'vehicleGun']
_ENGINE = items.ITEM_TYPE_INDICES[b'vehicleEngine']
_FUEL_TANK = items.ITEM_TYPE_INDICES[b'vehicleFuelTank']
_RADIO = items.ITEM_TYPE_INDICES[b'vehicleRadio']
_TANKMAN = items.ITEM_TYPE_INDICES[b'tankman']
_OPTIONALDEVICE = items.ITEM_TYPE_INDICES[b'optionalDevice']
_SHELL = items.ITEM_TYPE_INDICES[b'shell']
_EQUIPMENT = items.ITEM_TYPE_INDICES[b'equipment']
_SIMPLE_VALUE_STATS = (b'fortResource', b'slots', b'berths', b'freeXP', b'dossier', b'clanInfo', b'accOnline', b'accOffline', b'freeTMenLeft', b'freeVehiclesLeft', b'vehicleSellsLeft', b'captchaTriesLeft', b'hasFinPassword', b'finPswdAttemptsLeft', b'tkillIsSuspected', b'tutorialsCompleted', b'battlesTillCaptcha', b'dailyPlayHours', b'playLimits', b'applyAdditionalXPCount') + Currency.ALL
_DICT_STATS = (b'vehTypeXP', b'vehTypeLocks', b'restrictions', b'globalVehicleLocks', b'dummySessionStats', b'maxResearchedLevelByNation', b'weeklyVehicleCrystals', b'refSystem20', b'denunciations')
_GROWING_SET_STATS = (b'unlocks', b'eliteVehicles', b'multipliedXPVehs', b'multipliedRankedBattlesVehs')
_SHRINKABLE_SET_STATS = (b'unlocks',)
_ACCOUNT_STATS = (b'clanDBID', b'attrs', b'premiumExpiryTime', b'autoBanTime', b'globalRating')
_CACHE_STATS = (b'isFinPswdVerified', b'mayConsumeWalletResources', b'oldVehInvIDs', b'isSsrPlayEnabled', b'isEmergencyModeEnabled')
_CACHE_DICT_STATS = (b'SPA', b'entitlements', b'dynamicCurrencies', b'comp7')
_PREFERRED_MAPS_KEY = b'preferredMaps'
_ADDITIONAL_XP_CACHE_KEY = b'_additionalXPCache'
_LIMITED_UI = b'limitedUi'

def _checkIfNonPlayer(*args):

    def _decorator(func):

        @wraps(func)
        def _wrapper(self, *func_args, **func_kwargs):
            if self.ignore:
                callback = func_kwargs.get(b'callback')
                if callback is not None:
                    callback(AccountCommands.RES_NON_PLAYER, *args)
                return
            return func(self, *func_args, **func_kwargs)

        return _wrapper

    return _decorator


def _get_callback_proxy(callback=None):
    if callback is None:
        return
    else:
        return (lambda requestID, resultID, errorStr, ext=None: callback(resultID))


class Stats(object):

    def __init__(self, syncData):
        self.__account = None
        self.__syncData = syncData
        self.__cache = {}
        self.__ignore = True
        return

    @property
    def ignore(self):
        return self.__ignore

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
        cache = self.__cache
        statsDiff = diff.get(b'stats', None)
        if statsDiff is not None:
            for stat in _SIMPLE_VALUE_STATS:
                if stat in statsDiff:
                    cache[stat] = statsDiff[stat]

            for stat in _DICT_STATS:
                stat_r = (
                 stat, b'_r')
                if stat_r in statsDiff:
                    cache[stat] = statsDiff[stat_r]
                if stat in statsDiff:
                    synchronizeDicts(statsDiff[stat], cache.setdefault(stat, dict()))

            for stat in _GROWING_SET_STATS:
                stat_r = (
                 stat, b'_r')
                if stat_r in statsDiff:
                    cache[stat] = statsDiff[stat_r]
                if stat in statsDiff:
                    cache.setdefault(stat, set()).update(statsDiff[stat])
                if stat in _SHRINKABLE_SET_STATS:
                    statDiscardKey = (
                     stat, b'_d')
                    if statDiscardKey in statsDiff:
                        cache[stat].difference_update(statsDiff[statDiscardKey])

        accountDiff = diff.get(b'account', None)
        if accountDiff is not None:
            for stat in _ACCOUNT_STATS:
                if stat in accountDiff:
                    cache[stat] = accountDiff[stat]

            if _ADDITIONAL_XP_CACHE_KEY in accountDiff:
                synchronizeDicts(accountDiff[_ADDITIONAL_XP_CACHE_KEY], cache.setdefault(_ADDITIONAL_XP_CACHE_KEY, {}))
        if cache.get(b'premiumInfo') is None:
            cache[b'premiumInfo'] = PremiumInfo()
        premiumDiff = diff.get(b'premium')
        if premiumDiff is not None:
            cache[b'premiumInfo'].update(premiumDiff)
        economicsDiff = diff.get(b'economics', None)
        if economicsDiff is not None:
            for stat in (b'unlocks', b'eliteVehicles'):
                if stat in economicsDiff:
                    cache.setdefault(stat, set()).update(economicsDiff[stat])
                    cache.setdefault((b'initial', stat), set()).update(economicsDiff[stat])

        cacheDiff = diff.get(b'cache', None)
        if cacheDiff is not None:
            for stat in _CACHE_STATS:
                if stat in cacheDiff:
                    LOG_DEBUG_DEV(b'CACHE stat change', stat, cacheDiff[stat])
                    cache[stat] = cacheDiff[stat]

            for stat in _CACHE_DICT_STATS:
                statDiff = cacheDiff.get(stat, None)
                if statDiff:
                    synchronizeDicts(statDiff, cache.setdefault(stat, dict()))

        piggyBankDiff = diff.get(PIGGY_BANK_PDATA_KEY, None)
        if piggyBankDiff is not None:
            synchronizeDicts(piggyBankDiff, cache.setdefault(PIGGY_BANK_PDATA_KEY, dict()))
        if _PREFERRED_MAPS_KEY in diff:
            synchronizeDicts(diff[_PREFERRED_MAPS_KEY], cache.setdefault(_PREFERRED_MAPS_KEY, {}))
        if _LIMITED_UI in diff:
            synchronizeDicts(diff[_LIMITED_UI], cache.setdefault(_LIMITED_UI, {}))
        return

    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        return

    def get(self, statName, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetResponse, statName, callback))
        return

    def unlock(self, vehTypeCompDescr, unlockIdx, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_UNLOCK, vehTypeCompDescr, unlockIdx, 0, proxy)
        return

    def setCurrentVehicle(self, vehInvID, callback=None):
        LOG_WARNING(b'Deprecated. setCurrentVehicle')
        return

    def exchange(self, gold, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        self.__account.shop.getExchangeRate(partial(self.__exchange_onGetRate, gold, callback))
        return

    def convertToFreeXP(self, vehTypeCompDescrs, xp, callback=None, useDiscount=0):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        self.__account.shop.getFreeXPConversion(partial(self.__convertToFreeXP_onGetParameters, vehTypeCompDescrs, xp, callback, useDiscount))
        return

    def upgradeToPremium(self, days, arenaUniqueID, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        self.__account.shop.getPremiumCost(partial(self.__premium_onGetPremCost, days, arenaUniqueID, callback))
        return

    def buySlot(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        self.__account.shop.waitForSync(partial(self.__slot_onShopSynced, callback))
        return

    def buyBerths(self, countPacksBerths, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        self.__account.shop.waitForSync(partial(self.__berths_onShopSynced, countPacksBerths, callback))
        return

    def setMapsBlackList(self, selectedMaps, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        self.__account._doCmdIntArr(AccountCommands.CMD_SET_MAPS_BLACK_LIST, selectedMaps, None if callback is None else (lambda reqID, resID, errorStr, ext={}: callback(resID, errorStr, ext)))
        return

    def setMoney(self, credit, gold=0, freeXP=0, crystal=0, eventCoin=0, bpcoin=0, equipCoin=0, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_SET_MONEY, [
         credit, gold, freeXP, crystal, eventCoin, bpcoin, 
         equipCoin], proxy)
        return

    def setPremium(self, premType=constants.PREMIUM_TYPE.PLUS, seconds=time_utils.ONE_DAY, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_SET_PREMIUM, [premType, seconds], proxy)
        return

    def addExperience(self, vehTypeName, xp, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        vehTypeCompDescr = vehicles.makeIntCompactDescrByID(b'vehicle', *vehicles.g_list.getIDsByName(vehTypeName))
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_ADD_XP, vehTypeCompDescr, xp, 0, proxy)
        return

    def setDossierField(self, path, value, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntStr(AccountCommands.CMD_SET_DOSSIER_FIELD, value, path, proxy)
        return

    def addTokens(self, token, tokenCount=1, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntStr(AccountCommands.CMD_ADD_TOKENS, tokenCount, token, proxy)
        return

    def drawTokens(self, token, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdStr(AccountCommands.CMD_DRAW_TOKENS, token, proxy)
        return

    def unlockAll(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_UNLOCK_ALL, 0, 0, 0, proxy)
        return

    def unlockUpToVehicle(self, vehTypeCDFrom, vehTypeCDTo, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        parseCD = vehicles.parseIntCompactDescr
        itemTypeIdx, nationIdx, innationIdx = parseCD(vehTypeCDFrom)
        if itemTypeIdx != _VEHICLE:
            LOG_ERROR(b'Wrong vehicle type compact descriptor')
            return
        else:
            vehType = vehicles.g_cache.vehicle(nationIdx, innationIdx)
            unlocksGraph = {elem[1]: (elem[2:], idx) for idx, elem in enumerate(vehType.unlocksDescrs)}
            possibleVehsToUnlock = [k for k in unlocksGraph.iterkeys() if parseCD(k)[0] == _VEHICLE]
            LOG_DEBUG_DEV(b'__cmdUnlockForVehicle: possibleVehsToUnlock', possibleVehsToUnlock)
            if vehTypeCDTo not in possibleVehsToUnlock:
                LOG_ERROR(b'Wrong vehicle for unlocking TO', vehTypeCDTo, possibleVehsToUnlock)
                return

            def _dfs(visited, graph, node):
                if node not in graph:
                    return
                visited.append(node)
                for neighbour in graph[node][0]:
                    _dfs(visited, graph, neighbour)

                return

            account = self.__account

            def _sendCmd(_indices):
                if _indices:
                    account._doCmdInt3(AccountCommands.CMD_UNLOCK, vehTypeCDFrom, _indices[0][0], 0, proxy)
                return

            def proxy(requestID, resultID, errorStr, ext=None):
                LOG_DEBUG_DEV(b'__cmdUnlockForVehicle: response', requestID, resultID, errorStr, ext)
                if resultID != AccountCommands.RES_SUCCESS:
                    if b'is already unlocked' in ext.get(b'exception_message', b''):
                        pass
                    else:
                        LOG_DEBUG_DEV(b'__cmdUnlockForVehicle: something went wrong, stopping')
                        return
                if unlockIndicesUniq:
                    del unlockIndicesUniq[0]
                LOG_DEBUG_DEV(b'__cmdUnlockForVehicle: remaining unlocks', unlockIndicesUniq)
                _sendCmd(unlockIndicesUniq)
                return

            unlockOrder = []
            _dfs(unlockOrder, unlocksGraph, vehTypeCDTo)
            unlockIndices = []
            for itemToUnlock in reversed(unlockOrder):
                unlockIdx = unlocksGraph[itemToUnlock][1]
                unlockIndices.append((unlockIdx, itemToUnlock))

            LOG_DEBUG_DEV(b'__cmdUnlockForVehicle: unlockIndices for vehCD', vehTypeCDTo, unlockIndices)
            if not unlockIndices:
                return
            _seen = set()
            unlockIndicesUniq = [i for i in unlockIndices if i not in _seen and not _seen.add(i)]
            LOG_DEBUG_DEV(b'__cmdUnlockForVehicle: unlockIndicesUniq for vehCD', vehTypeCDTo, unlockIndicesUniq)
            _sendCmd(unlockIndicesUniq)
            return

    def unlockVPPTree(self, vehTypeCDs, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_VPP_UNLOCK_TREE, vehTypeCDs, proxy)
        return

    def setRankedInfo(self, data, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        data = cPickle.dumps(data)
        self.__account._doCmdStr(AccountCommands.CMD_SET_RANKED_INFO, data, proxy)
        return

    def addFreeAwardLists(self, count, branch=0, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_ADD_FREE_AWARD_LISTS, [count, branch], proxy)
        return

    def drawFreeAwardLists(self, count, branch=0, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_DRAW_FREE_AWARD_LISTS, [count, branch], proxy)
        return

    def completePersonalMission(self, questID, withAdditional=False, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_COMPLETE_PERSONAL_MISSION, [questID, int(withAdditional)], proxy)
        return

    def completeQuests(self, questIDs, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdStrArr(AccountCommands.CMD_COMPLETE_QUESTS_DEV, questIDs, proxy)
        return

    def rerollDailyQuest(self, token, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdStrArr(AccountCommands.CMD_REROLL_DAILY_QUESTS, token, proxy)
        return

    def rerollDailyQuestsDev(self, levels, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdStrArr(AccountCommands.CMD_REROLL_DAILY_QUESTS_DEV, levels, proxy)
        return

    def rerollDailyQuestDev(self, level, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdStr(AccountCommands.CMD_REROLL_DAILY_QUEST_DEV, level, proxy)
        return

    def resetRerollTimeout(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_RESET_REROLL_TIMEOUT, 0, 0, 0, proxy)
        return

    def resetRerollTimeoutPrem(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_RESET_REROLL_TIMEOUT_PREM, 0, 0, 0, proxy)
        return

    def completeDailyQuest(self, token, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdStr(AccountCommands.CMD_COMPLETE_DAILY_QUEST, token, proxy)
        return

    def setEpicRewardTokens(self, count, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_SET_EPIC_REWARD_TOKENS, count, 0, 0, proxy)
        return

    @_checkIfNonPlayer()
    def changeBRPoints(self, points, ignoreUnburnableTitles=False, callback=None):
        self.__account._doCmdInt3(AccountCommands.CMD_CHANGE_BR_POINTS, points, int(ignoreUnburnableTitles), 0, _get_callback_proxy(callback))
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

    def __exchange_onGetRate(self, gold, callback, resultID, exchRate, shopRev):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if exchRate is None:
            LOG_ERROR(b'Result of the getExchangeRate request is None')
            if callback is not None:
                callback(AccountCommands.RES_FAILURE)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_EXCHANGE, shopRev, gold, 0, proxy)
        return

    def __convertToFreeXP_onGetParameters(self, vehTypeCompDescrs, xp, callback, useDiscount, resultID, freeXPConversion, shopRev):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if freeXPConversion is None:
            LOG_ERROR(b'Result of the getFreeXPConversion request is None')
            if callback is not None:
                callback(AccountCommands.RES_FAILURE)
            return
        arr = [
         shopRev, xp, useDiscount] + list(vehTypeCompDescrs)
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_FREE_XP_CONV, arr, proxy)
        return

    def __premium_onGetPremCost(self, days, arenaUniqueID, callback, resultID, premCost, shopRev):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if premCost is None:
            LOG_ERROR(b'Result of the getPremiumCost request is None')
            if callback is not None:
                callback(AccountCommands.RES_FAILURE, None)
            return
        gold = premCost.get(days, None)
        if gold is None:
            LOG_ERROR(b'Wrong days number')
            if callback is not None:
                callback(AccountCommands.RES_WRONG_ARGS, None)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_PREMIUM, shopRev, days, arenaUniqueID, proxy)
        return

    def __slot_onShopSynced(self, callback, resultID, shopRev):
        if resultID < 0:
            if callback is not None:
                callback(resultID)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_BUY_SLOT, shopRev, 0, 0, proxy)
        return

    def __berths_onShopSynced(self, countPacksBerths, callback, resultID, shopRev):
        if resultID < 0:
            if callback is not None:
                callback(resultID)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_BUY_BERTHS, shopRev, countPacksBerths, 0, proxy)
        return
