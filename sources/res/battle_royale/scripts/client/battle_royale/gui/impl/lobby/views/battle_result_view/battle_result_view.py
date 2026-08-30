from __future__ import absolute_import
from collections import OrderedDict
from future.utils import viewvalues, viewitems
from typing import Any, Dict, TYPE_CHECKING
import SoundGroups
from constants import ARENA_BONUS_TYPE
from battle_royale.gui.impl.lobby.tooltips.reward_currency_tooltip_view import RewardCurrencyTooltipView
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController
from frameworks.wulf import WindowFlags
from gui.impl import backport
from gui.impl.backport import BackportTooltipWindow, createTooltipData
from gui.impl.gen import R
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.battle_result_view_model import BattleResultViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.tooltip_constants_model import TooltipConstantsModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.stat_item_model import StatItemModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.leaderboard.leaderboard_constants import LeaderboardConstants
from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.battle_reward_item_model import BattleRewardItemModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.place_model import PlaceModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.row_model import RowModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.battle_pass_progress import BattlePassProgress
from gui.impl.pub import WindowImpl
from gui.impl.pub.view_component import ViewComponent
from gui.shared import event_dispatcher, EVENT_BUS_SCOPE
from gui.shared.events import BattleRoyalePlatoonEvent
from gui.server_events.battle_royale_formatters import BRSections
from gui.Scaleform.genConsts.HANGAR_HEADER_QUESTS import HANGAR_HEADER_QUESTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from helpers import dependency
from skeletons.gui.battle_results import IBattleResultsService
from skeletons.gui.game_control import IBattleRoyaleController, IPlatoonController
from skeletons.gui.lobby_context import ILobbyContext
from shared_utils import first
from soft_exception import SoftException
from gui.sounds.ambients import BattleResultsEnv
from battle_royale.gui.battle_control.controllers.br_battle_sounds import BREvents
from battle_royale.gui.constants import BattleRoyaleSubMode
from gui.impl.backport.backport_context_menu import BackportContextMenuWindow
from gui.impl.backport.backport_context_menu import createContextMenuData
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from skeletons.connection_mgr import IConnectionManager
from messenger.storage import UsersStorage, MessengerStorageDescriptor
from messenger.formatters.service_channel_helpers import parseTokenBonusCount
from gui.impl.gen.view_models.views.battle_royale.battle_results.player_battle_type_status_model import BattleType
from gui.prb_control.entities.base.listener import IPrbListener
if TYPE_CHECKING:
    from gui.impl.gen.view_models.views.battle_royale.battle_results.player_battle_type_status_model import PlayerBattleTypeStatusModel
    from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.leaderboard_model import LeaderboardModel
_THE_BEST_PLACE = 1
_BR_POINTS_ICON = R.images.battle_royale.gui.maps.icons.battleResults.leaderboard.br_selector_16()
_BATTLE_REWARD_TYPES = [
 BattleRewardItemModel.XP, BattleRewardItemModel.CREDITS,
 BattleRewardItemModel.BATTLE_PASS_POINTS, BattleRewardItemModel.CRYSTALS,
 BattleRewardItemModel.ST_PATRICK_COIN, BattleRewardItemModel.BATTLE_ROYALE_COIN,
 BattleRewardItemModel.BR_PROGRESSION_TOKEN]
_HIDDEN_BONUSES_WITH_ZERO_VALUES = frozenset([
 BattleRewardItemModel.CRYSTALS, BattleRewardItemModel.BATTLE_PASS_POINTS])
_TOURNAMENT_ARENA_BONUS_TYPES = (
 ARENA_BONUS_TYPE.BATTLE_ROYALE_TRN_SOLO, ARENA_BONUS_TYPE.BATTLE_ROYALE_TRN_SQUAD)
_INVALID_PREBATTLE_ID = 0

class BattleRoyaleBattleResultsWindow(WindowImpl):

    def __init__(self, layer, **kwargs):
        super(BattleRoyaleBattleResultsWindow, self).__init__(content=BattleRoyaleBattleResultsView(**kwargs), wndFlags=WindowFlags.WINDOW, layer=layer)
        return


class BattleRoyaleBattleResultsView(ViewComponent[BattleResultViewModel], IPrbListener):
    __slots__ = (b'__arenaUniqueID', b'__tooltipsData', b'__tooltipParametersCreator', b'__data', b'__isObserverResult', b'__arenaBonusType', b'__ally', b'__squadCreatedByInvite')
    __battleResults = dependency.descriptor(IBattleResultsService)
    __brController = dependency.descriptor(IBattleRoyaleController)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __connectionMgr = dependency.descriptor(IConnectionManager)
    __brProgressionController = dependency.descriptor(IBRProgressionOnTokensController)
    __platoonCtrl = dependency.descriptor(IPlatoonController)
    usersStorage = MessengerStorageDescriptor(UsersStorage)
    __sound_env__ = BattleResultsEnv

    def __init__(self, *args, **kwargs):
        super(BattleRoyaleBattleResultsView, self).__init__(R.views.battle_royale.mono.lobby.battle_results(), BattleResultViewModel)
        self.__arenaUniqueID = kwargs.get(b'arenaUniqueID')
        if self.__arenaUniqueID is None:
            raise SoftException(b'There is not arenaUniqueID in battleResults context')
        self.__data = self.__battleResults.getResultsVO(self.__arenaUniqueID)
        if not self.__data:
            raise SoftException(b'There is not battleResults')
        commonData = self.__data.get(BRSections.COMMON)
        if commonData is None:
            raise SoftException(b'There is no common info in battle results')
        vehicleInfo = first(commonData.get(b'playerVehicles', []))
        self.__isObserverResult = vehicleInfo.get(b'isObserver', False) if vehicleInfo else False
        self.__arenaBonusType = self.__data[BRSections.COMMON].get(b'arenaBonusType', 0)
        self.__tooltipsData = {}
        self.__tooltipParametersCreator = self.__getTooltipParametersCreator()
        self.__ally = {}
        self.__squadCreatedByInvite = False
        return

    @property
    def viewModel(self):
        return super(BattleRoyaleBattleResultsView, self).getViewModel()

    @property
    def arenaUniqueID(self):
        return self.__arenaUniqueID

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.battle_royale.mono.lobby.tooltips.reward_currency_tooltip():
            currencyType = event.getArgument(b'currencyType')
            return RewardCurrencyTooltipView(currencyType, self.__arenaUniqueID)
        return super(BattleRoyaleBattleResultsView, self).createToolTipContent(event, contentID)

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipID = self.__normalizeTooltipID(event.getArgument(b'tooltipId', b''))
            parametersCreator = self.__tooltipParametersCreator.get(tooltipID)
            if parametersCreator is None:
                raise SoftException((b'Invalid arguments to create an old flash tooltip with id {}').format(tooltipID))
            tooltipParameters = parametersCreator(event)
            window = BackportTooltipWindow(tooltipParameters, self.getParentWindow())
            window.load()
            return window
        else:
            return super(BattleRoyaleBattleResultsView, self).createToolTip(event)

    def createContextMenu(self, event):
        if event.contentID == R.views.common.BackportContextMenu():
            contextMenuArgs = {}
            contextMenuArgs[b'databaseID'] = event.getArgument(b'databaseID')
            if self.__connectionMgr.databaseID == contextMenuArgs[b'databaseID']:
                return super(BattleRoyaleBattleResultsView, self).createContextMenu(event)
            hiddenUserName = event.getArgument(b'hiddenUserName')
            contextMenuArgs[b'userName'] = hiddenUserName if hiddenUserName else event.getArgument(b'userName')
            contextMenuData = createContextMenuData(CONTEXT_MENU_HANDLER_TYPE.BR_BATTLE_RESULT_CONTEXT_MENU, contextMenuArgs)
            currentPlayer = self.usersStorage.getUser(self.__connectionMgr.databaseID)
            isCurrentPlayer = currentPlayer.getName() == contextMenuArgs[b'userName']
            if contextMenuData is not None and not isCurrentPlayer:
                window = BackportContextMenuWindow(contextMenuData, self.getParentWindow())
                window.load()
                return window
        return super(BattleRoyaleBattleResultsView, self).createContextMenu(event)

    def _initialize(self, *args, **kwargs):
        super(BattleRoyaleBattleResultsView, self)._initialize(*args, **kwargs)
        event_dispatcher.hideSquadWindow()
        return

    def _finalize(self):
        BREvents.playSound(BREvents.BR_RESULT_PROGRESS_BAR_STOP)
        SoundGroups.g_instance.playSound2D(backport.sound(R.sounds.bp_progress_bar_stop()))
        self.__tooltipsData = None
        self.__tooltipParametersCreator = None
        self.__data = None
        self.__ally = None
        self.__squadCreatedByInvite = False
        super(BattleRoyaleBattleResultsView, self)._finalize()
        return

    def _onLoading(self, *args, **kwargs):
        super(BattleRoyaleBattleResultsView, self)._onLoading(*args, **kwargs)
        self.__update()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.personalResults.battlePassProgress.onSubmitClick, self.__onBattlePassClick),
         (
          self.viewModel.playerBattleTypeStatus.onInviteToPlatoon, self.__onInviteToPlatoonClick),
         (
          self.__brController.onUpdated, self.__updateBattlePass),
         (
          self.__platoonCtrl.onMembersUpdate, self.__updateSquadState))

    def _getListeners(self):
        return (
         (
          BattleRoyalePlatoonEvent.LEAVED_PLATOON, self.__onLeavedPlatoon, EVENT_BUS_SCOPE.LOBBY),)

    def __update(self):
        with self.viewModel.transaction() as model:
            setEventInfo(model.eventInfo)
            self.__setPlayerBattleTypeStatus(model.playerBattleTypeStatus)
            self.__setPersonalResult(model.personalResults)
            self.__setLeaderboard(model.leaderboardLobbyModel)
        return

    def __onBattlePassClick(self):
        self.destroyWindow()
        event_dispatcher.showBattlePass()
        return

    def __updateBattlePass(self):
        self.__setBattleRewards(self.viewModel.personalResults)
        self.__setBattleRewardsWithPremium(self.viewModel.personalResults)
        return

    def __updateSquadState(self):
        if not self.__squadCreatedByInvite or not self.__isCommander():
            if self.__brController.isInBattleRoyaleSquad():
                if all(slot.get(b'player') is not None for slot in self.__platoonCtrl.getPlatoonSlotsData()):
                    self.__setIsPlatoonWindowOpen(True)
                    return
            self.__setIsPlatoonWindowOpen(False)
        return

    def __onInviteToPlatoonClick(self):
        self.__brController.selectSubModeBattle(BattleRoyaleSubMode.SQUAD_MODE_ID, accountsToInvite=(self.__ally.get(b'databaseID', 0),))
        self.__squadCreatedByInvite = True
        self.__setIsPlatoonWindowOpen(True)
        return

    def __onLeavedPlatoon(self, *_):
        if self.__squadCreatedByInvite or not self.__isCommander():
            self.__squadCreatedByInvite = False
            self.__setIsPlatoonWindowOpen(False)
        return

    def __setPlayerBattleTypeStatus(self, statusModel):
        commonInfo = self.__data.get(BRSections.COMMON)
        if commonInfo is None:
            raise SoftException(b'There is no vehicle status info in battle results')
        leaderboard = self.__data.get(BRSections.LEADERBOARD)
        if leaderboard is None:
            raise SoftException(b"There is no players' table in battle results")
        if self.__isSquadMode():
            for vehicle in leaderboard:
                if vehicle[b'place'] == commonInfo[b'playerPlace'] and not vehicle[b'isPersonal']:
                    self.__ally = vehicle
                    break

            self.__setUserName(statusModel.user, self.__ally)
            statusModel.setBattleType(BattleType.PLATOON if self.__ally.get(b'prebattleID', 0) != _INVALID_PREBATTLE_ID or self.__isTournament() else BattleType.RANDOMPLATOON)
        else:
            statusModel.setBattleType(BattleType.SOLO)
        self.__updateSquadState()
        return

    def __setPersonalResult(self, personalModel):
        self.__setMapName()
        self.__setCommonInfo()
        if not self.__isObserverResult:
            self.__setFinishResult(personalModel)
            self.__setStats(personalModel)
            self.__setBattleRewards(personalModel)
            self.__setBattleRewardsWithPremium(personalModel)
            self.__setCompletedQuests(personalModel)
        personalModel.battlePassProgress.setBattlePassState(BattlePassProgress.BP_STATE_DISABLED)
        return

    def __setLeaderboard(self, leaderboardModel):
        leaderboard = self.__data.get(BRSections.LEADERBOARD)
        if leaderboard is None:
            raise SoftException(b"There is no players' table in battle results")
        placesData = []
        if self.__isSquadMode():
            vehiclesBySquad = {}
            for vehicle in leaderboard:
                vehiclesBySquad.setdefault(vehicle[b'squadIdx'], []).append(vehicle)

            placesData = list(viewvalues(vehiclesBySquad))
        else:
            for vehicle in leaderboard:
                placesData.append([vehicle])

        placesData.sort(key=(lambda v: v[0].get(b'place', 0)))
        groupList = leaderboardModel.getPlacesList()
        groupList.clear()
        for placeData in placesData:
            placeModel = PlaceModel()
            firstVehicle = placeData[0]
            placeModel.setPlace(str(firstVehicle.get(b'place', 0)))
            placeModel.setIsSquadMode(self.__isSquadMode())
            rowList = placeModel.getPlayersList()
            rowList.clear()
            for rowData in placeData:
                rowModel = RowModel()
                if rowData[b'isPersonal']:
                    rowModel.setType(LeaderboardConstants.ROW_TYPE_BR_PLAYER)
                elif rowData[b'isPersonalSquad']:
                    rowModel.setType(LeaderboardConstants.ROW_TYPE_BR_PLATOON)
                else:
                    rowModel.setType(LeaderboardConstants.ROW_TYPE_BR_ENEMY)
                rowModel.setAnonymizerNick(rowData[b'hiddenName'])
                self.__setUserName(rowModel.user, rowData)
                rowModel.user.setKills(rowData[b'kills'])
                rowModel.user.setDamage(rowData[b'damage'])
                rowModel.user.setVehicleLevel(rowData[b'achievedLevel'])
                rowModel.user.setVehicleType(rowData[b'vehicleType'])
                rowModel.user.setVehicleName(rowData[b'vehicleName'])
                rowList.addViewModel(rowModel)

            rowList.invalidate()
            groupList.addViewModel(placeModel)

        groupList.invalidate()
        return

    def __getFinishReason(self):
        isWinner = self.__data[BRSections.COMMON][b'playerPlace'] == _THE_BEST_PLACE
        isWinnerPlace = self.__data[BRSections.COMMON][b'playerPlace'] in (2, 3, 4, 5)
        isInSquad = self.__data[BRSections.COMMON][b'isSquadMode']
        if isWinner:
            finishReason = R.strings.battle_royale.battleResult.title.victoryFirst()
        elif isWinnerPlace:
            finishReason = R.strings.battle_royale.battleResult.title.victoryOther()
        elif isInSquad:
            finishReason = R.strings.battle_royale.battleResult.title.squadDestroyed()
        else:
            finishReason = R.strings.battle_royale.battleResult.title.vehicleDestroyed()
        return finishReason

    def __isSquadMode(self):
        return self.__data[BRSections.COMMON][b'isSquadMode']

    def __hasPremium(self):
        return self.__data[BRSections.COMMON][b'hasPremium']

    def __getStats(self):
        return self.__data[BRSections.PERSONAL][BRSections.STATS]

    def __getFinancialData(self, section):
        financialData = self.__data.get(BRSections.PERSONAL, {}).get(section, {})
        return financialData

    def __getBattlePassPointsTotal(self):
        questsBonuses = self.__data[BRSections.PERSONAL][BRSections.REWARDS].get(BRSections.BONUSES)
        questPoints = sum([bonus.getCount() for bonuses in questsBonuses for bonus in bonuses if bonus.getName() == b'battlePassPoints']) if questsBonuses else 0
        return self.__data[BRSections.PERSONAL][BRSections.BATTLE_PASS][b'bpTopPoints'] + questPoints

    def __setFinishResult(self, personalResultsModel):
        finishReason = self.__getFinishReason()
        personalResultsModel.setFinishResultLabel(finishReason)
        return

    def __setStats(self, statsModel):
        statsInfo = self.__getStats()
        if statsInfo is None:
            raise SoftException(b"There is no player's efficiency in battle results")
        statList = statsModel.getStatsList()
        statList.clear()
        for statData in statsInfo:
            statModel = StatItemModel()
            statModel.setType(statData[b'type'])
            statModel.setWreathImage(statData.get(b'wreathImage', R.invalid()))
            statModel.setCurrentValue(statData[b'value'])
            statModel.setMaxValue(statData[b'maxValue'])
            statList.addViewModel(statModel)

        statList.invalidate()
        return

    def __setBattleRewards(self, rewardsModel):
        rewardList = rewardsModel.getBattleRewardsList()
        rewardList.clear()
        rewards = self.__getEarnedRewards(BRSections.FINANCE)
        for reward in rewards:
            rewardList.addViewModel(reward)

        rewardList.invalidate()
        return

    def __setBattleRewardsWithPremium(self, rewardsModel):
        rewardList = rewardsModel.getBattleRewardsListWithPremium()
        rewardList.clear()
        rewards = self.__getEarnedRewards(BRSections.FINANCE_PREM)
        for reward in rewards:
            rewardList.addViewModel(reward)

        rewardList.invalidate()
        return

    def __setIsPlatoonWindowOpen(self, isOpen):
        with self.viewModel.transaction() as model:
            model.playerBattleTypeStatus.setIsPlatoonWindowOpen(isOpen)
        return

    def __getBrProgressionTokenCount(self):
        total = 0
        rewardsSection = self.__data.get(BRSections.PERSONAL, {}).get(BRSections.REWARDS, {})
        awardTokens = rewardsSection.get(BRSections.BR_AWARD_TOKENS, {})
        total += self.__parseProgressionTokenCount(awardTokens)
        bonusesData = rewardsSection.get(BRSections.BONUSES, {})
        for questBonuses in bonusesData:
            for bonus in questBonuses:
                total += parseTokenBonusCount(bonus, self.__brProgressionController.progressionToken)

        return total

    def __getEarnedRewards(self, section):
        earned = self.__getFinancialData(section)
        if self.__brController.isBattlePassAvailable(self.__arenaBonusType):
            earned.update({(BattleRewardItemModel.BATTLE_PASS_POINTS): (self.__getBattlePassPointsTotal())})
        if section == BRSections.FINANCE and self.__brProgressionController.isEnabled:
            progressionTokensEarned = self.__getBrProgressionTokenCount()
            if progressionTokensEarned:
                earned[BattleRewardItemModel.BR_PROGRESSION_TOKEN] = progressionTokensEarned
        sortedEarned = OrderedDict(sorted(viewitems(earned), key=(lambda x: _BATTLE_REWARD_TYPES.index(x[0]))))
        financialList = []
        if self.__brController.isStPatrick():
            additionalHiddenZeroBonuses = (
             BattleRewardItemModel.BATTLE_ROYALE_COIN,)
        else:
            additionalHiddenZeroBonuses = (
             BattleRewardItemModel.ST_PATRICK_COIN,)
        for bonusType, value in sortedEarned.items():
            if bonusType in _HIDDEN_BONUSES_WITH_ZERO_VALUES or bonusType in additionalHiddenZeroBonuses:
                if value == 0:
                    continue
            statModel = BattleRewardItemModel()
            statModel.setType(bonusType)
            statModel.setValue(value)
            financialList.append(statModel)

        return financialList

    def __setCommonInfo(self):
        commonData = self.__data.get(BRSections.COMMON)
        if commonData is None:
            raise SoftException(b'There is no common info in battle results')
        model = self.viewModel.personalResults
        self.viewModel.personalResults.setPlace(commonData[b'playerPlace'])
        vehicleInfo = first(commonData[b'playerVehicles'])
        model.setVehicleName(vehicleInfo[b'vehicleName'])
        model.setVehicleType(vehicleInfo[b'vehicleType'])
        model.setHasPremium(self.__hasPremium())
        model.setIsObserver(vehicleInfo[b'isObserver'])
        return

    def __setMapName(self):
        commonData = self.__data.get(BRSections.COMMON, {})
        self.viewModel.setMapName(commonData.get(b'arenaStr', b''))
        return

    def __setCompletedQuests(self, personalModel):
        questsCount = self.__data[BRSections.PERSONAL][BRSections.REWARDS].get(b'completedQuestsCount', 0)
        personalModel.setQuestCompleted(questsCount)
        return

    def __getTooltipParametersCreator(self):
        return {(TooltipConstantsModel.ACHIEVEMENT_TOOLTIP): (self.__getAchievementTooltipParameters), 
           (TooltipConstantsModel.QUEST_COMPLETE_TOOLTIP): (self.__getQuestsTooltipParameters), 
           (TooltipConstantsModel.BONUS_TOOLTIP): (self.__getBonusTooltipParameters)}

    def __getAchievementTooltipParameters(self, event):
        achievementName = event.getArgument(b'achievementName')
        if achievementName is None:
            raise SoftException(b'There is no achievement info in tooltip arguments')
        return createTooltipData(isSpecial=True, specialAlias=TooltipConstantsModel.ACHIEVEMENT_TOOLTIP, specialArgs=[
         0, achievementName, False, [], 0, 0])

    def __getQuestsTooltipParameters(self, _):
        completedQuestIDs = self.__data[BRSections.PERSONAL][BRSections.REWARDS][b'completedQuests'].keys()
        return createTooltipData(isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.BATTLE_ROYALE_COMPLETED_QUESTS_INFO, specialArgs=[
         HANGAR_HEADER_QUESTS.QUEST_TYPE_COMMON, completedQuestIDs])

    def __getBonusTooltipParameters(self, event):
        _, bonusID = event.getArgument(b'tooltipId', b'').split(b':')
        tooltipData = self.__tooltipsData.get(bonusID)
        if tooltipData is None:
            return
        else:
            return tooltipData

    @staticmethod
    def __normalizeTooltipID(tooltipID):
        if tooltipID.startswith(TooltipConstantsModel.BONUS_TOOLTIP):
            return TooltipConstantsModel.BONUS_TOOLTIP
        return tooltipID

    def __parseProgressionTokenCount(self, tokens):
        return tokens.get(self.__brProgressionController.progressionToken, {}).get(b'count', 0)

    @staticmethod
    def __setUserName(model, info):
        model.setUserName(info.get(b'userName', b''))
        model.setDatabaseID(info.get(b'databaseID', 0))
        model.setClanAbbrev(info.get(b'clanAbbrev', info.get(b'userClanAbbrev', b'')))
        model.setHiddenUserName(info.get(b'hiddenName', b''))
        return

    def __isCommander(self):
        return self.prbEntity is not None and self.prbEntity.isCommander()

    def __isTournament(self):
        return self.__arenaBonusType in _TOURNAMENT_ARENA_BONUS_TYPES
