from __future__ import absolute_import
from battle_royale.gui.impl.gen.view_models.views.lobby.views.progression.progress_level_model import ProgressLevelModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.progression.progression_view_model import ProgressionViewModel, ProgressionState
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo
from battle_royale.gui.impl.lobby.tooltips.proxy_currency_tooltip_view import ProxyCurrencyTooltipView
from battle_royale.gui.impl.lobby.views.bonus_packer import getBonusPacker
from battle_royale.gui.impl.lobby.views.quests_packer import getEventUIDataPacker
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import sortQuestsByProgressionPointBonus
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData
from gui.impl.backport import createTooltipData
from gui.impl.gen import R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.lobby.missions.missions_helpers import needToUpdateQuestsInModel
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip
from gui.server_events.events_helpers import EventInfoModel
from gui.shared import event_dispatcher
from gui.shared.utils.scheduled_notifications import SimpleNotifier
from helpers import dependency, time_utils
from helpers.time_utils import ONE_DAY, ONE_MINUTE, getServerUTCTime
from math_common import round_py2_style_int
from skeletons.gui.game_control import IBattleRoyaleController
from skeletons.gui.server_events import IEventsCache

class ProgressionView(SubModelPresenter):
    battleRoyale = dependency.descriptor(IBattleRoyaleController)
    brProgression = dependency.descriptor(IBRProgressionOnTokensController)
    eventsCache = dependency.descriptor(IEventsCache)
    _UPDATE_TIMER_DELAY = ONE_MINUTE
    __slots__ = (b'__tooltipData', b'__notifier', b'__bonuses')

    def __init__(self, viewModel, parentView):
        super(ProgressionView, self).__init__(viewModel, parentView)
        self.__tooltipData = {}
        self.__notifier = None
        self.__bonuses = {}
        return

    @property
    def viewModel(self):
        return super(ProgressionView, self).getViewModel()

    def getParentWindow(self):
        return self.parentView.getParentWindow()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.battle_royale.mono.lobby.tooltips.proxy_currency_tooltip():
            return ProxyCurrencyTooltipView()
        if contentID == R.views.lobby.tooltips.AdditionalRewardsTooltip():
            fromIndex = int(event.getArgument(b'fromIndex'))
            index = int(event.getArgument(b'index'))
            bonuses = list(self.__bonuses[index][fromIndex:])
            return AdditionalRewardsTooltip(bonuses)
        return super(ProgressionView, self).createToolTipContent(event, contentID)

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(ProgressionView, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId is None:
            return
        else:
            if tooltipId == TOOLTIPS_CONSTANTS.BATTLE_ROYALE_SELECTOR_CALENDAR_INFO:
                return createTooltipData(specialAlias=tooltipId, isSpecial=True, specialArgs=(None,))
            return self.__tooltipData.get(tooltipId)

    def initialize(self, *args, **kwargs):
        super(ProgressionView, self).initialize(args, kwargs)
        self.__updateModel()
        return

    def finalize(self):
        self.__stopNotification()
        self.__bonuses.clear()
        super(ProgressionView, self).finalize()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.pollServerTime, self.__onPollServerTime),
         (
          self.brProgression.onProgressPointsUpdated, self.__updateProgressionPoints),
         (
          self.brProgression.onSettingsChanged, self.__updateModel),
         (
          self.eventsCache.onSyncCompleted, self.__onSyncCompleted))

    def __restartNotifier(self, updateTime):
        self.__stopNotification()
        self.__notifier = SimpleNotifier((lambda : updateTime), self.__updateQuestTimer)
        self.__notifier.startNotification()
        return

    def __stopNotification(self):
        if self.__notifier is not None:
            self.__notifier.stopNotification()
            self.__notifier.clear()
            self.__notifier = None
        return

    def __onClose(self):
        event_dispatcher.showHangar()
        return

    def __updateQuestTimer(self):
        with self.viewModel.transaction() as model:
            self.__setBattleQuestTimeLeft(model.battleQuests)
        return

    def __updateMissionVisitedArray(self, missionVisitedArray, questsIDs):
        missionVisitedArray.clear()
        missionVisitedArray.reserve(len(questsIDs))
        for questID in questsIDs:
            missionCompletedVisited = not self.eventsCache.questsProgress.getQuestCompletionChanged(questID)
            missionVisitedArray.addBool(missionCompletedVisited)

        missionVisitedArray.invalidate()
        return

    def __onSyncCompleted(self, *_):
        if not self.brProgression.isEnabled:
            return
        self.__restartNotifier(self._UPDATE_TIMER_DELAY)
        with self.viewModel.transaction() as model:
            self.__updateBattleQuestsIfNeeded(model.battleQuests)
        return

    def __updateProgressionPoints(self):
        if not self.brProgression.isEnabled:
            return
        curPoints = self.brProgression.getCurPoints()
        with self.viewModel.transaction() as model:
            state = ProgressionState.COMPLETED if self.brProgression.isFinished else ProgressionState.INPROGRESS
            model.setState(state)
            model.setCurProgressPoints(curPoints)
            self.__updateBattleQuestsIfNeeded(model.battleQuests)
        return

    def __updateModel(self):
        if not self.brProgression.isEnabled:
            return
        data = self.brProgression.getProgressionData()
        pointsData = self.brProgression.getProgessionPointsData()
        with self.viewModel.transaction() as model:
            state = ProgressionState.COMPLETED if self.brProgression.isFinished else ProgressionState.INPROGRESS
            model.setState(state)
            model.setStartTimestamp(self.battleRoyale.getStartTime())
            model.setEndTimestamp(self.battleRoyale.getEndTime())
            model.setServerTimestamp(round_py2_style_int(getServerUTCTime()))
            model.setCalendarTooltipId(TOOLTIPS_CONSTANTS.BATTLE_ROYALE_SELECTOR_CALENDAR_INFO)
            setEventInfo(model.eventInfo)
            self.__updateBattleQuestsCards(model.battleQuests, data)
            self.__updateProgression(data, pointsData, model)
            self.__updateMissionVisitedArray(model.battleQuests.getMissionsCompletedVisited(), data[b'battleQuests'].keys())
            self.__markAsVisited(data)
        return

    def __onPollServerTime(self):
        self.viewModel.setServerTimestamp(int(getServerUTCTime()))
        self.__updateQuestTimer()
        return

    def __updateProgression(self, data, pointsData, model):
        progressionLevelsList = data[b'progressionLevels']
        totalLevels = len(progressionLevelsList)
        model.setCurProgressPoints(pointsData[b'curPoints'])
        model.setPrevProgressPoints(pointsData[b'prevPoints'])
        if totalLevels > 0:
            model.setPointsForLevel(pointsData[b'totalPoints'] // totalLevels)
        progressionLevels = model.getProgressLevels()
        progressionLevels.clear()
        for levelData in progressionLevelsList:
            level = ProgressLevelModel()
            rewards = level.getRewards()
            bonuses = levelData[b'rewards']
            packBonusModelAndTooltipData(bonuses, rewards, self.__tooltipData, getBonusPacker())
            progressionLevels.addViewModel(level)

        progressionLevels.invalidate()
        return

    def __updateBattleQuestsCards(self, battleQuestsModel, data):
        self.__setBattleQuestTimeLeft(battleQuestsModel)
        questsList = battleQuestsModel.getTasksBattle()
        questsList.clear()
        bonusIndexTotal = len(self.__tooltipData)
        sortedQuests = sortQuestsByProgressionPointBonus(data[b'battleQuests'].values())
        for index, quest in enumerate(sortedQuests):
            packer = getEventUIDataPacker(quest)
            questModels = packer.pack()
            bonusTooltipList = packer.getTooltipData()
            self.__bonuses[index] = questModels.getBonuses()
            for bonusIndex, item in enumerate(questModels.getBonuses()):
                tooltipIdx = str(bonusIndexTotal)
                item.setTooltipId(tooltipIdx)
                if bonusTooltipList:
                    self.__tooltipData[tooltipIdx] = bonusTooltipList[str(bonusIndex)]
                bonusIndexTotal += 1

            questsList.addViewModel(questModels)

        questsList.invalidate()
        return

    def __setBattleQuestTimeLeft(self, battleQuestsModel):
        questsTimer = self.battleRoyale.getQuestsTimerLeft()
        if questsTimer < 0:
            battleQuestsModel.setShowEventEnded(True)
            self.__stopNotification()
        dailyQuestProgressDelta = EventInfoModel.getDailyProgressResetTimeDelta()
        currentCycleEndTime = self.battleRoyale.getEndTime()
        currServerTime = time_utils.getCurrentLocalServerTimestamp()
        cycleTimeLeft = currentCycleEndTime - currServerTime
        isShowPrimeTime = cycleTimeLeft < ONE_DAY and cycleTimeLeft < dailyQuestProgressDelta
        battleQuestsModel.setCurrentTimerDate(questsTimer)
        battleQuestsModel.setShowPrimeTime(isShowPrimeTime)
        self.__restartNotifier(questsTimer + (self._UPDATE_TIMER_DELAY if questsTimer > 0 else 0))
        return

    def __markAsVisited(self, data):
        for seenQuestID in data[b'battleQuests'].keys():
            self.eventsCache.questsProgress.markQuestProgressAsViewed(seenQuestID)

        return

    def __updateBattleQuestsIfNeeded(self, battleQuestsModel):
        data = self.brProgression.getProgressionData()
        battleQuests = data[b'battleQuests']
        isNeedToUpdate = needToUpdateQuestsInModel(battleQuests.values(), self.viewModel.battleQuests.getTasksBattle())
        if not isNeedToUpdate:
            return
        self.__updateBattleQuestsCards(battleQuestsModel, data)
        self.__updateMissionVisitedArray(battleQuestsModel.getMissionsCompletedVisited(), battleQuests.keys())
        self.__markAsVisited(data)
        return
