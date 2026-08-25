from enum import Enum
from frameworks.wulf import Array
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.awards_widget_model import AwardsWidgetModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_widget_3d_style_view_model import BattlePassWidget3DStyleViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_widget_final_rewards_view_model import BattlePassWidgetFinalRewardsViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.character_widget_view_model import CharacterWidgetViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.common_view_model import CommonViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_level_model import RewardLevelModel

class ChapterStates(Enum):
    ACTIVE = b'active'
    PAUSED = b'paused'
    COMPLETED = b'completed'
    NOTSTARTED = b'notStarted'


class ActionTypes(Enum):
    NOACTION = b'noAction'
    BUY = b'buy'
    BUYLEVEL = b'buyLevel'
    ACTIVATECHAPTER = b'activateChapter'


class ChapterType(Enum):
    COMMON = b'common'
    EXTRA = b'extra'
    HOLIDAY = b'holiday'


class BattlePassProgressionsViewModel(CommonViewModel):
    __slots__ = (b'onClose', b'onChapterActivate', b'onTakeClick', b'onTakeAllClick', b'onOpenShopClick', b'onAboutClick', b'onPointsInfoClick', b'onFinishedAnimation', b'onLevelsAnimationFinished', b'onStyleBonusPreview', b'onChapterChoice', b'onViewLoaded')

    def __init__(self, properties=41, commands=13):
        super(BattlePassProgressionsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def levels(self):
        return self._getViewModel(4)

    @staticmethod
    def getLevelsType():
        return RewardLevelModel

    @property
    def starterPackRewards(self):
        return self._getViewModel(5)

    @staticmethod
    def getStarterPackRewardsType():
        return RewardItemModel

    @property
    def widget3dStyle(self):
        return self._getViewModel(6)

    @staticmethod
    def getWidget3dStyleType():
        return BattlePassWidget3DStyleViewModel

    @property
    def chapterCharacter(self):
        return self._getViewModel(7)

    @staticmethod
    def getChapterCharacterType():
        return CharacterWidgetViewModel

    @property
    def widgetFinalRewards(self):
        return self._getViewModel(8)

    @staticmethod
    def getWidgetFinalRewardsType():
        return BattlePassWidgetFinalRewardsViewModel

    @property
    def awardsWidget(self):
        return self._getViewModel(9)

    @staticmethod
    def getAwardsWidgetType():
        return AwardsWidgetModel

    def getChapterID(self):
        return self._getNumber(10)

    def setChapterID(self, value):
        self._setNumber(10, value)
        return

    def getChapterState(self):
        return ChapterStates(self._getString(11))

    def setChapterState(self, value):
        self._setString(11, value.value)
        return

    def getFreeFinalRewards(self):
        return self._getArray(12)

    def setFreeFinalRewards(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getFreeFinalRewardsType():
        return unicode

    def getPaidFinalRewards(self):
        return self._getArray(13)

    def setPaidFinalRewards(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getPaidFinalRewardsType():
        return unicode

    def getPreviousPointsInChapter(self):
        return self._getNumber(14)

    def setPreviousPointsInChapter(self, value):
        self._setNumber(14, value)
        return

    def getCurrentPointsInChapter(self):
        return self._getNumber(15)

    def setCurrentPointsInChapter(self, value):
        self._setNumber(15, value)
        return

    def getPreviousFreePointsInChapter(self):
        return self._getNumber(16)

    def setPreviousFreePointsInChapter(self, value):
        self._setNumber(16, value)
        return

    def getFreePointsInChapter(self):
        return self._getNumber(17)

    def setFreePointsInChapter(self, value):
        self._setNumber(17, value)
        return

    def getPreviousPointsInLevel(self):
        return self._getNumber(18)

    def setPreviousPointsInLevel(self, value):
        self._setNumber(18, value)
        return

    def getCurrentPointsInLevel(self):
        return self._getNumber(19)

    def setCurrentPointsInLevel(self, value):
        self._setNumber(19, value)
        return

    def getPreviousFreePointsInLevel(self):
        return self._getNumber(20)

    def setPreviousFreePointsInLevel(self, value):
        self._setNumber(20, value)
        return

    def getFreePointsInLevel(self):
        return self._getNumber(21)

    def setFreePointsInLevel(self, value):
        self._setNumber(21, value)
        return

    def getPreviousLevel(self):
        return self._getNumber(22)

    def setPreviousLevel(self, value):
        self._setNumber(22, value)
        return

    def getPotentialLevel(self):
        return self._getNumber(23)

    def setPotentialLevel(self, value):
        self._setNumber(23, value)
        return

    def getPreviousPotentialLevel(self):
        return self._getNumber(24)

    def setPreviousPotentialLevel(self, value):
        self._setNumber(24, value)
        return

    def getIsPaused(self):
        return self._getBool(25)

    def setIsPaused(self, value):
        self._setBool(25, value)
        return

    def getIsChooseDeviceEnabled(self):
        return self._getBool(26)

    def setIsChooseDeviceEnabled(self, value):
        self._setBool(26, value)
        return

    def getIsWalletAvailable(self):
        return self._getBool(27)

    def setIsWalletAvailable(self, value):
        self._setBool(27, value)
        return

    def getShowBuyAnimations(self):
        return self._getBool(28)

    def setShowBuyAnimations(self, value):
        self._setBool(28, value)
        return

    def getShowLevelsAnimations(self):
        return self._getBool(29)

    def setShowLevelsAnimations(self, value):
        self._setBool(29, value)
        return

    def getShowReplaceRewardsAnimations(self):
        return self._getBool(30)

    def setShowReplaceRewardsAnimations(self, value):
        self._setBool(30, value)
        return

    def getActionType(self):
        return ActionTypes(self._getString(31))

    def setActionType(self, value):
        self._setString(31, value.value)
        return

    def getIsStyleTaken(self):
        return self._getBool(32)

    def setIsStyleTaken(self, value):
        self._setBool(32, value)
        return

    def getIsSeasonEndingSoon(self):
        return self._getBool(33)

    def setIsSeasonEndingSoon(self, value):
        self._setBool(33, value)
        return

    def getChapterType(self):
        return ChapterType(self._getString(34))

    def setChapterType(self, value):
        self._setString(34, value.value)
        return

    def getHasExtra(self):
        return self._getBool(35)

    def setHasExtra(self, value):
        self._setBool(35, value)
        return

    def getExpireTime(self):
        return self._getNumber(36)

    def setExpireTime(self, value):
        self._setNumber(36, value)
        return

    def getTimeLeft(self):
        return self._getNumber(37)

    def setTimeLeft(self, value):
        self._setNumber(37, value)
        return

    def getSeasonNum(self):
        return self._getNumber(38)

    def setSeasonNum(self, value):
        self._setNumber(38, value)
        return

    def getTankmenScreenID(self):
        return self._getNumber(39)

    def setTankmenScreenID(self, value):
        self._setNumber(39, value)
        return

    def getIsStarterPack(self):
        return self._getBool(40)

    def setIsStarterPack(self, value):
        self._setBool(40, value)
        return

    def _initialize(self):
        super(BattlePassProgressionsViewModel, self)._initialize()
        self._addViewModelProperty(b'levels', UserListModel())
        self._addViewModelProperty(b'starterPackRewards', UserListModel())
        self._addViewModelProperty(b'widget3dStyle', BattlePassWidget3DStyleViewModel())
        self._addViewModelProperty(b'chapterCharacter', CharacterWidgetViewModel())
        self._addViewModelProperty(b'widgetFinalRewards', BattlePassWidgetFinalRewardsViewModel())
        self._addViewModelProperty(b'awardsWidget', AwardsWidgetModel())
        self._addNumberProperty(b'chapterID', 0)
        self._addStringProperty(b'chapterState')
        self._addArrayProperty(b'freeFinalRewards', Array())
        self._addArrayProperty(b'paidFinalRewards', Array())
        self._addNumberProperty(b'previousPointsInChapter', 0)
        self._addNumberProperty(b'currentPointsInChapter', 0)
        self._addNumberProperty(b'previousFreePointsInChapter', 0)
        self._addNumberProperty(b'freePointsInChapter', 0)
        self._addNumberProperty(b'previousPointsInLevel', 0)
        self._addNumberProperty(b'currentPointsInLevel', 0)
        self._addNumberProperty(b'previousFreePointsInLevel', 0)
        self._addNumberProperty(b'freePointsInLevel', 0)
        self._addNumberProperty(b'previousLevel', 0)
        self._addNumberProperty(b'potentialLevel', 0)
        self._addNumberProperty(b'previousPotentialLevel', 0)
        self._addBoolProperty(b'isPaused', False)
        self._addBoolProperty(b'isChooseDeviceEnabled', True)
        self._addBoolProperty(b'isWalletAvailable', True)
        self._addBoolProperty(b'showBuyAnimations', False)
        self._addBoolProperty(b'showLevelsAnimations', False)
        self._addBoolProperty(b'showReplaceRewardsAnimations', False)
        self._addStringProperty(b'actionType')
        self._addBoolProperty(b'isStyleTaken', False)
        self._addBoolProperty(b'isSeasonEndingSoon', False)
        self._addStringProperty(b'chapterType')
        self._addBoolProperty(b'hasExtra', False)
        self._addNumberProperty(b'expireTime', 0)
        self._addNumberProperty(b'timeLeft', 0)
        self._addNumberProperty(b'seasonNum', 0)
        self._addNumberProperty(b'tankmenScreenID', 0)
        self._addBoolProperty(b'isStarterPack', False)
        self.onClose = self._addCommand(b'onClose')
        self.onChapterActivate = self._addCommand(b'onChapterActivate')
        self.onTakeClick = self._addCommand(b'onTakeClick')
        self.onTakeAllClick = self._addCommand(b'onTakeAllClick')
        self.onOpenShopClick = self._addCommand(b'onOpenShopClick')
        self.onAboutClick = self._addCommand(b'onAboutClick')
        self.onPointsInfoClick = self._addCommand(b'onPointsInfoClick')
        self.onFinishedAnimation = self._addCommand(b'onFinishedAnimation')
        self.onLevelsAnimationFinished = self._addCommand(b'onLevelsAnimationFinished')
        self.onStyleBonusPreview = self._addCommand(b'onStyleBonusPreview')
        self.onChapterChoice = self._addCommand(b'onChapterChoice')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        return
