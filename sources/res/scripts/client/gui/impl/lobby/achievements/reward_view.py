import typing, SoundGroups
from gui.server_events.bonuses import DogTagComponentBonus
from gui.shared.event_dispatcher import showAdvancedAchievementsRewardView, showAdvancedAchievementsView
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.shared.event_dispatcher import showAdvancedAchievementsCatalogView, showAnimatedDogTags
from gui.shared.tutorial_helper import getTutorialGlobalStorage
from gui.impl.lobby.achievements.profile_utils import createAdvancedAchievementsCatalogInitAchievementIDs, fillAdvancedAchievementModel, createBackportTooltipDecorator, createTooltipContentDecorator, getRewardViewBonusPacker
from gui.impl.gen.view_models.views.lobby.achievements.views.reward_view_model import RewardViewModel
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.Scaleform.daapi.view.lobby.profile.sound_constants import ACHIEVEMENTS_REWARD_SCREEN_EXIT_EVENT
from helpers import dependency
from PlayerEvents import g_playerEvents
from skeletons.gui.game_control import IAchievementsController
from tutorial.control.context import GLOBAL_FLAG
from uilogging.advanced_achievement.logger import AdvancedAchievementRewardLogger
from uilogging.advanced_achievement.logging_constants import AdvancedAchievementViewKey, AdvancedAchievementButtons
if typing.TYPE_CHECKING:
    from advanced_achievements_client.getters import BonusTuple
    from typing import List

class RewardView(ViewImpl):
    __slots__ = (b'__tooltipData', b'__bonusTuples', b'__isFirstEntry', b'__haveNewAnimatedDogTag', b'__uiLogger')
    __MAX_REWARDS_PER_SCREEN = 3
    __achievementsController = dependency.descriptor(IAchievementsController)

    def __init__(self, bonusTuples, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.achievements.RewardView())
        settings.flags = ViewFlags.VIEW
        settings.model = RewardViewModel()
        settings.args = args
        self.__bonusTuples = bonusTuples
        self.__isFirstEntry = kwargs.pop(b'isFirstEntry', self.__getIsFirstEntry())
        self.__haveNewAnimatedDogTag = kwargs.pop(b'haveNewAnimatedDogTag', self.__hasAnimatedDogtag())
        settings.kwargs = kwargs
        self.__tooltipData = {}
        self.__uiLogger = AdvancedAchievementRewardLogger(AdvancedAchievementViewKey.REWARD_SCREEN)
        super(RewardView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(RewardView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onGoToDogTag, self.__goToDogTag),
         (
          self.viewModel.onGoToAchievement, self.__onOpenAchievement),
         (
          self.viewModel.onOpenNextReward, self.__onOpenNextReward),
         (
          self.viewModel.onOpenAchievementsPage, self.__onOpenAchievementsPage),
         (
          self.viewModel.onClose, self.__onClose),
         (
          g_playerEvents.onDisconnected, self.__onClose))

    @createTooltipContentDecorator(AdvancedAchievementViewKey.REWARD_SCREEN)
    def createToolTipContent(self, event, contentID):
        return

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(RewardView, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipData.get(tooltipId)

    def _onLoading(self):
        super(RewardView, self)._onLoading()
        self.__fillModel()
        return

    def _finalize(self):
        SoundGroups.g_instance.playSound2D(ACHIEVEMENTS_REWARD_SCREEN_EXIT_EVENT)
        super(RewardView, self)._finalize()
        return

    def __getIsFirstEntry(self):
        return not self.__achievementsController.getMainAdvancedAchievementsPageVisited()

    def __hasAnimatedDogtag(self):
        for _, bonus in self.__bonusTuples:
            if isinstance(bonus, DogTagComponentBonus):
                if len(bonus.getValue()) == 2:
                    return True

        return False

    def __fillModel(self):
        with self.viewModel.transaction() as model:
            model.setIsFirstEntry(self.__isFirstEntry)
            bonusTuples = self.__getBonusTuples()
            self.__updateAchievements(model, bonusTuples)
            self.__updateRewards(model, bonusTuples)
            model.setRewardsBalance(len(self.__getNextBonusTuple()))
        return

    def __getBonusTuples(self):
        return self.__bonusTuples[:self.__MAX_REWARDS_PER_SCREEN]

    def __getNextBonusTuple(self):
        return self.__getBonusTuples()[self.__MAX_REWARDS_PER_SCREEN:]

    def __updateAchievements(self, model, bonusTuples):
        achievementArray = model.getAchievements()
        achievementArray.clear()
        for bonusTuple in bonusTuples:
            achievementArray.addViewModel(fillAdvancedAchievementModel(bonusTuple.achievement))

        achievementArray.invalidate()
        return

    def __updateRewards(self, model, bonusTuples):
        rewardArray = model.getRewards()
        rewardArray.clear()
        self.__tooltipData.clear()
        packBonusModelAndTooltipData([bonusTuple.bonus for bonusTuple in bonusTuples], rewardArray, tooltipData=self.__tooltipData, packer=getRewardViewBonusPacker())
        return

    def __onClose(self):
        if self.__haveNewAnimatedDogTag:
            getTutorialGlobalStorage().setValue(GLOBAL_FLAG.HAVE_NEW_ANIMATED_DOGTAG, True)
        self.destroyWindow()
        return

    def __goToDogTag(self, args):
        self.__uiLogger.logRewardClick(AdvancedAchievementButtons.TO_RECEIVED, len(self.__getBonusTuples()))
        showAnimatedDogTags(args[b'backgroundId'], args[b'engravingId'])
        self.destroyWindow()
        return

    def __onOpenAchievement(self, args):
        self.__onClose()
        initAchievementsIds = createAdvancedAchievementsCatalogInitAchievementIDs(args[b'id'], args[b'category'])
        showAdvancedAchievementsCatalogView(initAchievementsIds, args[b'category'], closeCallback=showAdvancedAchievementsView, parentScreen=AdvancedAchievementViewKey.REWARD_SCREEN)
        return

    def __onOpenNextReward(self):
        self.__uiLogger.logRewardClick(AdvancedAchievementButtons.MORE_REWARDS, len(self.__getBonusTuples()))
        self.destroyWindow()
        showAdvancedAchievementsRewardView(self.__getNextBonusTuple(), isFirstEntry=self.__isFirstEntry, haveNewAnimatedDogTag=self.__haveNewAnimatedDogTag)
        return

    def __onOpenAchievementsPage(self):
        self.__uiLogger.logRewardClick(AdvancedAchievementButtons.TO_ACHIEVEMENT, len(self.__getBonusTuples()))
        showAdvancedAchievementsView()
        self.__onClose()
        return


class RewardViewWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, bonusTuples, parent=None, *args, **kwargs):
        super(RewardViewWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=RewardView(bonusTuples, *args, **kwargs), parent=parent)
        return
