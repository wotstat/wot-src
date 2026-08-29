from battle_royale_progression.gui.impl.gen.view_models.views.lobby.views.progression.progress_level_model import ProgressLevelModel
from battle_royale_progression.gui.impl.gen.view_models.views.lobby.views.progression.progression_view_model import ProgressionViewModel
from battle_royale_progression.gui.impl.lobby.views.bonus_packer import getBonusPacker
from battle_royale_progression.gui.impl.lobby.views.quests_packer import getEventUIDataPacker
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.server_events.events_helpers import EventInfoModel, questsSortFunc
from gui.shared import event_dispatcher
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController, IBRProgressionOnTokensController
from skeletons.gui.server_events import IEventsCache

class ProgressionView(SubModelPresenter):
    battleRoyale = dependency.descriptor(IBattleRoyaleController)
    brProgression = dependency.descriptor(IBRProgressionOnTokensController)
    eventsCache = dependency.descriptor(IEventsCache)
    __slots__ = (b'__tooltipData',)

    def __init__(self, viewModel, parentView):
        super(ProgressionView, self).__init__(viewModel, parentView)
        self.__tooltipData = {}
        return

    @property
    def viewModel(self):
        return super(ProgressionView, self).getViewModel()

    def getParentWindow(self):
        return self.parentView.getParentWindow()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(ProgressionView, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipData.get(tooltipId)

    def initialize(self, *args, **kwargs):
        super(ProgressionView, self).initialize(args, kwargs)
        self.__updateModel()
        return

    def finalize(self):
        self.brProgression.saveCurPoints()
        super(ProgressionView, self).finalize()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onAboutClicked, self.__onAboutClicked),
         (
          self.brProgression.onProgressPointsUpdated, self.__updateProgressionPoints),
         (
          self.brProgression.onSettingsChanged, self.__updateModel),
         (
          self.eventsCache.onSyncCompleted, self.__onSyncCompleted))

    def __onClose(self):
        event_dispatcher.showHangar()
        return

    def __onAboutClicked(self):
        self.battleRoyale.openURL()
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
        data = self.brProgression.getProgressionData()
        with self.viewModel.transaction() as model:
            self.__updateBattleQuestsCards(model.battleQuests, data)
            self.__updateMissionVisitedArray(model.battleQuests.getMissionsCompletedVisited(), data[b'battleQuests'].keys())
            self.__markAsVisited(data)
        return

    def __updateProgressionPoints(self):
        if not self.brProgression.isEnabled:
            return
        data = self.brProgression.getProgessionPointsData()
        with self.viewModel.transaction() as model:
            model.setCurProgressPoints(data[b'curPoints'])
        return

    def __updateModel(self):
        if not self.brProgression.isEnabled:
            return
        data = self.brProgression.getProgressionData()
        with self.viewModel.transaction() as model:
            self.__updateBattleQuestsCards(model.battleQuests, data)
            self.__updateProgression(data, model)
            self.__updateMissionVisitedArray(model.battleQuests.getMissionsCompletedVisited(), data[b'battleQuests'].keys())
            self.__markAsVisited(data)
        return

    def __updateProgression(self, data, model):
        model.setCurProgressPoints(data[b'curPoints'])
        model.setPrevProgressPoints(data[b'prevPoints'])
        model.setPointsForLevel(data[b'pointsForLevel'])
        progressionLevels = model.getProgressLevels()
        progressionLevels.clear()
        for levelData in data[b'progressionLevels']:
            level = ProgressLevelModel()
            rewards = level.getRewards()
            bonuses = levelData[b'rewards']
            packBonusModelAndTooltipData(bonuses, rewards, self.__tooltipData, getBonusPacker())
            progressionLevels.addViewModel(level)

        progressionLevels.invalidate()
        return

    def __updateBattleQuestsCards(self, battleQuestsModel, data):
        newCountdownVal = EventInfoModel.getDailyProgressResetTimeDelta()
        battleQuestsModel.setCurrentTimerDate(newCountdownVal)
        questsList = battleQuestsModel.getTasksBattle()
        questsList.clear()
        bonusIndexTotal = len(self.__tooltipData)
        for quest in sorted(data[b'battleQuests'].values(), key=questsSortFunc):
            packer = getEventUIDataPacker(quest)
            questModels = packer.pack()
            bonusTooltipList = packer.getTooltipData()
            for bonusIndex, item in enumerate(questModels.getBonuses()):
                tooltipIdx = str(bonusIndexTotal)
                item.setTooltipId(tooltipIdx)
                if bonusTooltipList:
                    self.__tooltipData[tooltipIdx] = bonusTooltipList[str(bonusIndex)]
                bonusIndexTotal += 1

            questsList.addViewModel(questModels)

        questsList.invalidate()
        return

    def __markAsVisited(self, data):
        for seenQuestID in data[b'battleQuests'].keys():
            self.eventsCache.questsProgress.markQuestProgressAsViewed(seenQuestID)

        return
