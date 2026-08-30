from __future__ import absolute_import
import logging
from collections import defaultdict
from future.utils import lfilter, viewitems
from past.builtins import long
from constants import ARENA_BONUS_TYPE, DEATH_REASON_ALIVE
from gui.battle_control.battle_constants import WinStatus
from gui.battle_results.components import base
from gui.battle_results.components.personal import PersonalVehiclesBlock
from gui.battle_results.progress.progress_helpers import isQuestCompleted
from gui.battle_results.reusable import sort_keys
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events import IEventsCache
from gui.server_events.battle_royale_formatters import SOLO_ITEMS_ORDER, SQUAD_ITEMS_ORDER, StatsItemType
from gui.server_events.events_helpers import isBattleRoyale
from gui.shared.utils.functions import replaceHyphenToUnderscore
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IBattleRoyaleController
from ValueReplay import ValueReplay, ValueReplayConnector
from battle_results import g_config as battleResultsConfig
from gui.battle_results.reusable import records
from skeletons.gui.shared import IItemsCache
from gui.shared.money import Currency
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())
_THE_BEST_RANK = 1

def _isSquadMode(reusable):
    return reusable.common.arenaBonusType in (ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD,
     ARENA_BONUS_TYPE.BATTLE_ROYALE_TRN_SQUAD)


class BattleRoyaleArenaNameBlock(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        geometryName = replaceHyphenToUnderscore(reusable.common.arenaType.getGeometryName())
        return backport.text(R.strings.arenas.num(geometryName).name())


class ArenaBonusTypeNameBlock(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        arenaBonusType = reusable.common.arenaVisitor.getArenaBonusType()
        return arenaBonusType


class PersonalPlayerNameBlock(base.StatsBlock):
    __slots__ = (b'userName', b'clanAbbrev')

    def __init__(self, meta=None, field=b'', *path):
        super(PersonalPlayerNameBlock, self).__init__(meta, field, *path)
        self.userName = b''
        self.clanAbbrev = b''
        return

    def setRecord(self, result, reusable):
        player = reusable.getPlayerInfo()
        self.userName = player.realName
        self.clanAbbrev = player.clanAbbrev
        return


class BattleRoyalePlayerPlaceBlock(base.StatsItem):
    __slots__ = ()
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _convert(self, value, reusable):
        playerRank = reusable.personal.avatar.extensionInfo.get(b'playerRank', 0)
        if self.__sessionProvider.getCtx().extractLastArenaWinStatus() is not None:
            winStatus = WinStatus.WIN if playerRank == _THE_BEST_RANK else WinStatus.LOSE
            self.__sessionProvider.getCtx().setLastArenaWinStatus(WinStatus(winStatus))
        return playerRank


class BattleRoyaleIsSquadModeBlock(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return _isSquadMode(reusable)


class BattleRoyalePersonalVehicleBlock(base.StatsBlock):
    __slots__ = (b'vehicleName', b'vehicleType', b'isObserver')

    def __init__(self, meta=None, field=b'', *path):
        super(BattleRoyalePersonalVehicleBlock, self).__init__(meta, field, *path)
        self.vehicleName = b''
        self.vehicleType = b''
        self.isObserver = False
        return

    def setVehicle(self, item):
        if item is not None:
            self.vehicleName = item.shortUserName
            self.vehicleType = item.type
            self.isObserver = item.isObserver
        return

    def setRecord(self, result, reusable):
        return


class BattleRoyaleVehiclesBlock(PersonalVehiclesBlock):
    __slots__ = ()

    def _createComponent(self):
        return BattleRoyalePersonalVehicleBlock()


class BattleRoyaleIsPremiumBlock(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return reusable.isPostBattlePremium or reusable.isPostBattlePremiumPlus


class BattleRoyaleDailyBonusFactorBlock(base.StatsBlock):
    __slots__ = (b'dailyBonusFactor',)

    def __init__(self, meta=None, field=b'', *path):
        super(BattleRoyaleDailyBonusFactorBlock, self).__init__(meta, field, *path)
        self.dailyBonusFactor = 0
        return

    def setRecord(self, result, reusable):
        vehicleCD = [key for key in result[b'personal'].keys() if isinstance(key, (int, long, float))][0]
        info = result[b'personal'][vehicleCD]
        stpCoinInfo = info[b'currencies'].get(Currency.STPCOIN, {})
        self.dailyBonusFactor = stpCoinInfo.get(b'dailyBonusFactor', 0)
        return


class BattleRoyaleVehicleStatusBlock(base.StatsBlock):
    __itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = (b'killer', b'vehicleState', b'isSelfDestroyer')

    def __init__(self, meta=None, field=b'', *path):
        super(BattleRoyaleVehicleStatusBlock, self).__init__(meta, field, *path)
        self.killer = None
        self.vehicleState = DEATH_REASON_ALIVE
        self.isSelfDestroyer = False
        return

    def setRecord(self, result, reusable):
        playerInfo = reusable.getPlayerInfo()
        vehicleId = reusable.vehicles.getVehicleID(playerInfo.dbID)
        vehicleInfo = reusable.vehicles.getVehicleInfo(vehicleId)
        self.vehicleState = vehicleInfo.deathReason
        getter = self.__itemsCache.items.getItemByCD
        killerVehicleID = result[vehicleInfo.intCD][b'killerID']
        if killerVehicleID:
            killerInfo = reusable.getPlayerInfoByVehicleID(killerVehicleID)
            isSelf = playerInfo.realName == killerInfo.realName
            isSquad = playerInfo.squadIndex > 0 and playerInfo.squadIndex == killerInfo.squadIndex or isSelf
            isBot = killerInfo.dbID == 0
            if killerInfo.realName == killerInfo.fakeName or isSquad:
                userName = killerInfo.realName
                if isBot:
                    vehicle = getter(reusable.vehicles.getVehicleInfo(killerVehicleID).intCD)
                    userName = vehicle.shortUserName
                self.killer = {b'userName': userName, b'clanAbbrev': (killerInfo.clanAbbrev), 
                   b'isBot': isBot}
            else:
                self.killer = {b'userName': (killerInfo.fakeName), b'clanAbbrev': b'', 
                   b'isBot': isBot}
            self.isSelfDestroyer = killerInfo.realName == playerInfo.realName
        return


class _BRCoinReplayRecords(records.ReplayRecords):
    __slots__ = ()

    def __init__(self, replay, results):
        super(_BRCoinReplayRecords, self).__init__(replay, b'count')
        self._addRecord(ValueReplay.FACTOR, b'premiumFactor100', results[b'premiumFactor100'], 0)
        self._addRecord(ValueReplay.FACTOR, b'premiumVipFactor100', results[b'premiumVipFactor100'], 0)
        self._addRecord(ValueReplay.FACTOR, b'premiumPlusFactor100', results[b'premiumPlusFactor100'], 0)
        self._addRecord(ValueReplay.FACTOR, b'appliedPremiumFactor100', results[b'appliedPremiumFactor100'], 0)
        return


class _STPCoinReplayRecords(records.ReplayRecords):
    __slots__ = ()

    def __init__(self, replay, results):
        super(_STPCoinReplayRecords, self).__init__(replay, b'count')
        self._addRecord(ValueReplay.FACTOR, b'dailyBonusFactor', results[b'dailyBonusFactor'], 0)
        return


class BattleRoyaleFinancialBlock(base.StatsBlock):
    __slots__ = (b'credits', b'xp', b'crystal', b'brcoin', b'stpcoin')
    __eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, meta=None, field=b'', *path):
        super(BattleRoyaleFinancialBlock, self).__init__(meta, field, *path)
        self.credits = 0
        self.xp = 0
        self.crystal = 0
        self.brcoin = 0
        self.stpcoin = 0
        return

    def setRecord(self, result, reusable):
        avatarInfo = result[b'personal'][b'avatar']
        self.credits = avatarInfo[b'credits']
        self.xp = avatarInfo[b'xp']
        self.crystal = avatarInfo[b'crystal']
        self.brcoin = self._getBrCoins(result, reusable, isPremium=False)
        self.stpcoin = self._getStpCoins(result, reusable)
        return

    def _getBrCoins(self, result, reusable, isPremium):
        questBonus = self.__getCoinsQuestBonus(reusable.personal.getQuestsProgress(), Currency.BRCOIN)
        vehicleCD = [key for key in result[b'personal'].keys() if isinstance(key, (int, long, float))][0]
        info = result[b'personal'][vehicleCD]
        for code, data in viewitems(info[b'currencies']):
            if code == Currency.BRCOIN and data:
                meta = battleResultsConfig[b'allResults'].meta(b'currencies').meta(b'brcoin')
                replayConnector = ValueReplayConnector(data, meta)
                replay = ValueReplay(replayConnector, recordName=b'count', replay=data[b'replay'])
                if not isPremium:
                    return _BRCoinReplayRecords(replay, data).getRecord(b'count') + questBonus
                if b'appliedPremiumFactor100' in replay:
                    replay[b'appliedPremiumFactor100'] = data[b'premiumPlusFactor100']
                return _BRCoinReplayRecords(replay, data).getRecord(b'count') + questBonus

        return questBonus

    def _getStpCoins(self, result, reusable):
        questBonus = self.__getCoinsQuestBonus(reusable.personal.getQuestsProgress(), Currency.STPCOIN)
        vehicleCD = [key for key in result[b'personal'].keys() if isinstance(key, (int, long, float))][0]
        info = result[b'personal'][vehicleCD]
        for code, data in viewitems(info[b'currencies']):
            if code == Currency.STPCOIN and data:
                meta = battleResultsConfig[b'allResults'].meta(b'currencies').meta(code)
                replayConnector = ValueReplayConnector(data, meta)
                replay = ValueReplay(replayConnector, recordName=b'count', replay=data[b'replay'])
                return _STPCoinReplayRecords(replay, data).getRecord(b'count') + questBonus

        return questBonus

    def __getCoinsQuestBonus(self, questProgress, currencyCode):
        questBonus = 0
        allQuests = self.__eventsCache.getAllQuests()
        for qID, qProgress in viewitems(questProgress):
            if isQuestCompleted(*qProgress):
                quest = allQuests.get(qID)
                if quest is None:
                    continue
                for bonus in quest.getBonuses(b'currencies'):
                    if bonus.getCode() == currencyCode:
                        questBonus += bonus.getCount()

        return questBonus


class BattleRoyaleFinancialPremBlock(BattleRoyaleFinancialBlock):

    def setRecord(self, result, reusable):
        for rec in reusable.personal.getMoneyRecords():
            _, premiumCredits = rec[:2]
            self.credits = premiumCredits.getRecord(b'credits', b'originalCreditsToDraw')

        for rec in reusable.personal.getCrystalRecords():
            _, premiumCrystal = rec[:2]
            self.crystal = premiumCrystal.getRecord(b'crystal')

        for rec in reusable.personal.getXPRecords():
            _, premiumXP = rec[:2]
            self.xp = premiumXP.getRecord(b'xpToShow')

        self.brcoin = self._getBrCoins(result, reusable, isPremium=True)
        self.stpcoin = self._getStpCoins(result, reusable)
        return


class BattleRoyaleStatsItemBlock(base.StatsBlock):
    __slots__ = (b'type', b'value', b'maxValue', b'wreathImage')
    _ICON_PATH = R.images.battle_royale.gui.maps.icons.battleResults.stat_list
    _DEFAULT_ICON = _ICON_PATH.wreath_transparent

    def __init__(self, itemType, meta=None, field=b'', *path):
        super(BattleRoyaleStatsItemBlock, self).__init__(meta, field, *path)
        self.type = itemType
        self.value = 0
        self.maxValue = 0
        self.wreathImage = R.invalid()
        return

    def setRecord(self, result, reusable):
        self.value = self._getValue(result, reusable)
        self.maxValue = self._getMaxValue(result, reusable)
        self.wreathImage = self._getWreathImage(result, reusable)
        return

    def _getValue(self, result, reusable):
        return 0

    def _getMaxValue(self, result, reusable):
        return -1

    def _getWreathImage(self, result, reusable):
        if self._isTop(result, reusable):
            return self._ICON_PATH.wreath_silver()
        return self._DEFAULT_ICON()

    def _isTop(self, result, reusable):
        return False


class SimpleEfficiencyParameter(BattleRoyaleStatsItemBlock):
    __slots__ = ()

    def _getValue(self, result, reusable):
        personalInfo = reusable.getPersonalVehiclesInfo(result[b'personal'])
        return getattr(personalInfo, self.type)

    def _isTop(self, result, reusable):
        if self.value == 0:
            return False
        for player in reusable.getAllPlayersIterator(result[b'vehicles']):
            playerValue = getattr(player, self.type)
            if playerValue > 0 and playerValue > self.value:
                return False

        return True


class PlaceParameter(BattleRoyaleStatsItemBlock):
    __slots__ = ()

    def _getValue(self, result, reusable):
        personalInfo = reusable.getPersonalVehiclesInfo(result[b'personal'])
        avatar = personalInfo.avatar
        return avatar.extensionInfo.get(b'playerRank', 0)

    def _getMaxValue(self, result, reusable):

        def playerFilter(player):
            return not player.vehicle.isObserver and player.player.dbID != 0

        allPlayers = lfilter(playerFilter, reusable.getAllPlayersIterator(result[b'vehicles']))
        if _isSquadMode(reusable):
            return len(set(item.player.team for item in allPlayers))
        return len(allPlayers)

    def _getWreathImage(self, result, reusable):
        if self.value == _THE_BEST_RANK:
            return self._ICON_PATH.wreath_gold()
        return self._DEFAULT_ICON()


class KilledBySquadParameter(BattleRoyaleStatsItemBlock):
    __slots__ = ()

    def _getValue(self, result, reusable):
        allPlayers = reusable.getAllPlayersIterator(result[b'vehicles'])
        team = reusable.getPlayerInfo().team
        return sum(list(item.kills for item in allPlayers if team != 0 and team == item.player.team))

    def _isTop(self, result, reusable):
        if self.value == 0:
            return False
        killesBySquads = defaultdict(int)
        for item in reusable.getAllPlayersIterator(result[b'vehicles']):
            killesBySquads[item.player.team] += item.kills
            if killesBySquads[item.player.team] > self.value:
                return False

        return True


class BattleRoyaleStatsBlock(base.StatsBlock):
    __slots__ = ()
    _itemsFactory = {(StatsItemType.PLACE): PlaceParameter, 
       (StatsItemType.KILLS_SOLO): SimpleEfficiencyParameter, 
       (StatsItemType.KILLS_SQUAD): KilledBySquadParameter, 
       (StatsItemType.DAMAGE_DEAL): SimpleEfficiencyParameter, 
       (StatsItemType.DAMAGE_BLOCK): SimpleEfficiencyParameter}

    def setRecord(self, result, reusable):
        items = SQUAD_ITEMS_ORDER if _isSquadMode(reusable) else SOLO_ITEMS_ORDER
        for itemType in items:
            classType = self._itemsFactory.get(itemType)
            if classType is None:
                _logger.error(b'Incorrect parameter of personal efficiency')
            component = classType(itemType)
            component.setRecord(result, reusable)
            self.addComponent(self.getNextComponentIndex(), component)

        return


class BattleRoyaleRewardsBlock(base.StatsBlock):
    __slots__ = (b'achievements', b'bonuses', b'completedQuestsCount', b'completedQuests', b'brAwardTokens')
    __eventsCache = dependency.descriptor(IEventsCache)
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)
    __QUESTS_WITH_MEDALS = frozenset([b'br_battle_result_solo_1', b'br_battle_result_squad_1'])

    def __init__(self, meta=None, field=b'', *path):
        super(BattleRoyaleRewardsBlock, self).__init__(meta, field, *path)
        self.achievements = []
        self.bonuses = []
        self.completedQuestsCount = 0
        self.completedQuests = {}
        self.brAwardTokens = {}
        return

    def setRecord(self, result, reusable):
        questProgress = reusable.personal.getQuestsProgress()
        allQuests = self.__eventsCache.getAllQuests()
        self.achievements = self.__getAchievements(questProgress, allQuests)
        self.completedQuests = self.__getCompletedQuests(questProgress, self.__getDailyQuestsCondition, allQuests)
        self.completedQuestsCount = len(self.completedQuests)
        self.bonuses = self.__getBonuses(allQuests, self.completedQuests)
        self.brAwardTokens = self.__getBrAwardTokens(result)
        return

    def __getAchievements(self, questProgress, allQuests):
        completedQuestsWithMedals = self.__getCompletedQuests(questProgress, self.__getAchievementQuestsCondition, allQuests)
        if completedQuestsWithMedals:
            allBonuses = self.__getBonuses(allQuests, completedQuestsWithMedals)
            allAchievements = [bonus.getAchievements() for bonuses in allBonuses for bonus in bonuses if bonus.getName() == b'dossier']
            return [achievement.getName() for achievementList in allAchievements for achievement in achievementList]
        return []

    def __getAchievementQuestsCondition(self, qID, _):
        return qID in self.__QUESTS_WITH_MEDALS

    def __getDailyQuestsCondition(self, qID, allQuests):
        return isBattleRoyale(allQuests.get(qID).getGroupID())

    @staticmethod
    def __getCompletedQuests(questProgress, condition, allQuests):
        return {qID: qProgress for qID, qProgress in viewitems(questProgress) if condition(qID, allQuests) and isQuestCompleted(*qProgress)}

    @staticmethod
    def __getBonuses(allQuests, completedQuests):
        return [allQuests.get(qID).getBonuses() for qID in completedQuests]

    @staticmethod
    def __getBrAwardTokens(result):
        return result[b'personal'][b'avatar'][b'brAwardTokens']


class BattlePassBlock(base.StatsBlock):
    __slots__ = (b'bpTopPoints',)

    def __init__(self, meta=None, field=b'', *path):
        super(BattlePassBlock, self).__init__(meta, field, *path)
        self.bpTopPoints = 0
        return

    def setRecord(self, result, reusable):
        if reusable.common.arenaBonusType in ARENA_BONUS_TYPE.BATTLE_ROYALE_RANGE:
            self.bpTopPoints = reusable.battlePassProgress.bpTopPoints
        return


class BattleRoyalePlayerBlock(base.StatsBlock):
    __slots__ = (b'isPersonal', b'userName', b'clanAbbrev', b'place', b'isPersonalSquad', b'squadIdx', b'hiddenName', b'achievedLevel', b'kills', b'damage', b'vehicleName', b'vehicleType', b'databaseID', b'prebattleID')

    def __init__(self, meta=None, field=b'', *path):
        super(BattleRoyalePlayerBlock, self).__init__(meta, field, *path)
        self.isPersonal = False
        self.userName = b''
        self.hiddenName = b''
        self.clanAbbrev = b''
        self.place = 0
        self.squadIdx = 0
        self.isPersonalSquad = False
        self.achievedLevel = 0
        self.kills = 0
        self.damage = 0
        self.vehicleName = b''
        self.vehicleType = b''
        self.databaseID = 0
        self.prebattleID = 0
        return

    def setRecord(self, result, reusable):
        player = result.player
        dbID = player.dbID
        if player.realName == player.fakeName:
            self.userName = player.realName
            self.clanAbbrev = player.clanAbbrev
        elif self.isPersonal or self.isPersonalSquad:
            self.userName = player.realName
            self.clanAbbrev = player.clanAbbrev
            self.hiddenName = player.fakeName
        else:
            self.userName = player.fakeName
            self.hiddenName = player.realName
            self.clanAbbrev = b''
        avatarInfo = reusable.avatars.getAvatarInfo(dbID)
        if avatarInfo is not None and avatarInfo.extensionInfo is not None:
            self.place = avatarInfo.extensionInfo.get(b'playerRank', 0)
        return


class BattleRoyaleTeamStatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        allPlayers = reusable.getAllPlayersIterator(result, sortKey=sort_keys.placeSortKey)
        personalInfo = reusable.getPlayerInfo()
        personalDBID = personalInfo.dbID
        team = personalInfo.team if reusable.isSquadSupported else 0
        for item in allPlayers:
            if item.vehicle is not None and item.vehicle.isObserver:
                continue
            player = item.player
            if player.dbID == 0:
                continue
            block = BattleRoyalePlayerBlock()
            block.isPersonal = player.dbID == personalDBID
            block.squadIdx = player.team
            block.isPersonalSquad = team != 0 and team == player.team
            block.achievedLevel = item.vehicles[0].achievedLevel
            block.damage = item.damageDealt
            block.kills = item.kills
            block.vehicleName = item.vehicle.shortUserName
            block.vehicleType = item.vehicle.type
            block.databaseID = item.player.dbID
            block.prebattleID = item.player.prebattleID
            block.setRecord(item, reusable)
            self.addComponent(self.getNextComponentIndex(), block)

        return
