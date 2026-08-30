import cPickle, logging
from functools import partial, wraps
import AccountCommands, constants, items, personal_missions
from account_helpers.premium_info import PremiumInfo
from debug_utils import LOG_DEBUG_DEV, LOG_WARNING, LOG_ERROR
from helpers import time_utils, dependency
from piggy_bank_common.settings_constants import PIGGY_BANK_PDATA_KEY
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from items import vehicles
from gui.shared.money import Currency
from skeletons.gui.server_events import IEventsCache
_logger = logging.getLogger(__name__)
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
_SIMPLE_VALUE_STATS = (b'fortResource', b'slots', b'berths', b'freeXP', b'dossier', b'clanInfo', b'accOnline', b'accOffline', b'freeTMenLeft', b'freeVehiclesLeft', b'vehicleSellsLeft', b'captchaTriesLeft', b'hasFinPassword', b'finPswdAttemptsLeft', b'tkillIsSuspected', b'denunciationsLeft', b'battlesTillCaptcha', b'dailyPlayHours', b'playLimits', b'applyAdditionalXPCount', b'applyAdditionalWoTPlusXPCount', b'XPpp') + Currency.ALL
_DICT_STATS = (b'vehTypeXP', b'vehTypeLocks', b'restrictions', b'globalVehicleLocks', b'dummySessionStats', b'maxResearchedLevelByNation', b'weeklyVehicleCrystals', b'prestigeMilestonesAchieved')
_GROWING_SET_STATS = (b'unlocks', b'eliteVehicles', b'multipliedXPVehs', b'multipliedRankedBattlesVehs')
_ACCOUNT_STATS = (b'clanDBID', b'attrs', b'premiumExpiryTime', b'autoBanTime', b'globalRating')
_CACHE_STATS = (b'isFinPswdVerified', b'mayConsumeWalletResources', b'oldVehInvIDs', b'isSsrPlayEnabled', b'isEmergencyModeEnabled')
_CACHE_DICT_STATS = (b'SPA', b'entitlements', b'dynamicCurrencies', b'comp7')
_PREFERRED_MAPS_KEY = b'preferredMaps'
_ADDITIONAL_XP_CACHE_KEY = b'_additionalXPCache'
_LIMITED_UI = b'limitedUi'
_AB_FEATURE_TEST = b'abFeatureTest'

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
    _eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, syncData, commandsProxy):
        self.__account = None
        self.__syncData = syncData
        self.__commandsProxy = commandsProxy
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
        if _AB_FEATURE_TEST in diff:
            synchronizeDicts(diff[_AB_FEATURE_TEST], cache.setdefault(_AB_FEATURE_TEST, {}))
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

    def exchange(self, gold, credits, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        self.__account.shop.getExchangeRate(partial(self.__exchange_onGetRate, gold, credits, callback))
        return

    def convertToFreeXP(self, vehTypeCompDescrs, xp, gold, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        self.__account.shop.getFreeXPConversion(partial(self.__convertToFreeXP_onGetParameters, vehTypeCompDescrs, xp, gold, callback))
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

    def setMapsBlackList(self, toAddMapID=0, toRemoveMapID=0, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        self.__account._doCmdInt2(AccountCommands.CMD_UPDATE_MAPS_BLACK_LIST, toAddMapID, toRemoveMapID, None if callback is None else (lambda reqID, resID, errorStr, ext={}: callback(resID, errorStr, ext)))
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

    def addTokens(self, token, tokenCount=1, limit=0, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt2Str(AccountCommands.CMD_ADD_TOKENS, tokenCount, limit, token, proxy)
        return

    def addLootboxes(self, lootboxID, count=1, limit=0, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt2Str(AccountCommands.CMD_ADD_TOKENS, count, limit, b'lootBox:' + str(lootboxID), proxy)
        return

    def drawTokens(self, token, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdStr(AccountCommands.CMD_DRAW_TOKENS, token, proxy)
        return

    def updateEntitlementInTemporaryCache(self, entitlementCode, amount, expirationDate=0, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt2Str(AccountCommands.CMD_UPDATE_ENTITLEMENT_IN_TEMPORARY_CACHE, amount, expirationDate, entitlementCode, proxy)
        return

    def grantEntitlement(self, entitlementCode, amount, expirationDate=0, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt2Str(AccountCommands.CMD_GRANT_ENTITLEMENT, amount, expirationDate, entitlementCode, proxy)
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

    def addFreeAwardLists(self, count, season=1, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_ADD_FREE_AWARD_LISTS, [count, season], proxy)
        return

    def drawFreeAwardLists(self, count, season=1, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_DRAW_FREE_AWARD_LISTS, [count, season], proxy)
        return

    def addBattlePassPoints(self, points, vehTypeCD=0, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt2(AccountCommands.CMD_ADD_BATTLE_PASS_POINTS, vehTypeCD, points, proxy)
        return

    def completePersonalMission(self, questID, withAdditional=False, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        pmCache = personal_missions.g_cache
        if not self._eventsCache.getPersonalMissions().isCampaignActive(pmCache.branchByMissionID(questID)):
            _logger.error(b'No active campaign for personal mission with id: %s', questID)
            return
        else:
            if callback is not None:
                proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
            else:
                proxy = None
            self.__account._doCmdIntArr(AccountCommands.CMD_COMPLETE_PERSONAL_MISSION, [questID, int(withAdditional)], proxy)
            return

    def completePersonalMissionRange(self, missionIdRange, withAdditional=False, callback=None):
        missionsId = missionIdRange.split(b'-')
        if len(missionsId) == 2:
            if self.__ignore:
                if callback is not None:
                    callback(AccountCommands.RES_NON_PLAYER)
                return
            if callback is not None:
                proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
            else:
                proxy = None
            pmCache = personal_missions.g_cache
            startMissionRange = int(missionsId[0])
            endMissionRange = int(missionsId[1]) + 1
            for missionID in range(startMissionRange, endMissionRange):
                if not self._eventsCache.getPersonalMissions().isCampaignActive(pmCache.branchByMissionID(missionID)):
                    _logger.error(b'No active campaign for personal mission with id: %s', missionID)
                    continue
                self.__account._doCmdIntArr(AccountCommands.CMD_COMPLETE_PERSONAL_MISSION, [
                 missionID, int(withAdditional)], proxy)

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

    def completePremiumDaily(self):
        from gui import SystemMessages
        from gui.server_events.events_helpers import premMissionsSortFunc
        from gui.shared.notifications import NotificationPriorityLevel
        quests = sorted(self._eventsCache.getPremiumQuests().values(), cmp=premMissionsSortFunc)
        for q in quests:
            if not q.isCompleted():
                questID = q.getID()
                self.completeQuests([questID])
                SystemMessages.pushI18nMessage((b'Premium daily quest completed: "{}".').format(questID), priority=NotificationPriorityLevel.HIGH)
                return

        SystemMessages.pushI18nMessage(b'All premium daily quests are already completed.', priority=NotificationPriorityLevel.HIGH)
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
        self.__account._doCmdStr(AccountCommands.CMD_REROLL_DAILY_QUEST, token, proxy)
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

    def resetBonusQuest(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt3(AccountCommands.CMD_RESET_BONUS_QUEST, 0, 0, 0, proxy)
        return

    def weeklyQuestsNewWeek(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdNoArgs(AccountCommands.CMD_WEEKLY_QUEST_NEW_WEEK, proxy)
        return

    def weeklyQuestsRerollAll(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdNoArgs(AccountCommands.CMD_WEEKLY_QUEST_REROLL_ALL, proxy)
        return

    def rerollWeeklyQuest(self, token, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr)
        else:
            proxy = None
        self.__account._doCmdStr(AccountCommands.CMD_REROLL_WEEKLY_QUEST, token, proxy)
        return

    def rerollWeeklyQuestDev(self, id, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt(AccountCommands.CMD_REROLL_WEEKLY_QUEST_DEV, id, proxy)
        return

    def resetWeeklyQuestsRerollTimeout(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdNoArgs(AccountCommands.CMD_RESET_WEEKLY_REROLL_TIMEOUT, proxy)
        return

    def completeWeeklyQuestDev(self, id, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 0)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
        else:
            proxy = None
        self.__account._doCmdInt(AccountCommands.CMD_COMPLETE_WEEKLY_QUEST_DEV, id, proxy)
        return

    @_checkIfNonPlayer()
    def changeBRPoints(self, points, ignoreUnburnableTitles=False, callback=None):
        self.__account._doCmdInt3(AccountCommands.CMD_CHANGE_BR_POINTS, points, int(ignoreUnburnableTitles), 0, _get_callback_proxy(callback))
        return

    @_checkIfNonPlayer()
    def updateVehiclePrestige(self, vehCD=46849, points=10, callback=None):
        if not isinstance(points, int):
            LOG_ERROR(b'Wrong type of points.')
            return
        else:
            if self.__ignore:
                if callback is not None:
                    callback(AccountCommands.RES_NON_PLAYER, 0)
                return

            def response(code, errStr=b'', ctx=None):
                if code >= 0:
                    _logger.info(b'Server success response: code=%r, error=%r, ctx=%r', code, errStr, ctx)
                    return
                _logger.warning(b'Server fail response: code=%r, error=%r, ctx=%r', code, errStr, ctx)
                return

            if callback is not None:
                proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
            else:
                proxy = lambda requestID, resultID, errorStr, ext={}: response(resultID, errorStr, ext)
            self.__commandsProxy.perform(AccountCommands.CMD_RECOMPUTE_PRESTIGE_POINTS, vehCD, points, proxy)
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

    def __exchange_onGetRate(self, gold, credits, callback, resultID, exchRate, shopRev):
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
        self.__account._doCmdInt4(AccountCommands.CMD_EXCHANGE, shopRev, gold, credits, 0, proxy)
        return

    def __convertToFreeXP_onGetParameters(self, vehTypeCompDescrs, xp, gold, callback, resultID, freeXPConversion, shopRev):
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
         shopRev, xp, gold] + list(vehTypeCompDescrs)
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
