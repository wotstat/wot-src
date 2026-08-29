from enum import Enum
from frameworks.wulf import Array
from gui.impl.wrappers.user_compound_price_model import UserCompoundPriceModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_off_season_view_model import BattlePassOffSeasonViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_widget_3d_style_view_model import BattlePassWidget3DStyleViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.character_widget_view_model import CharacterWidgetViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.collection_entry_point_view_model import CollectionEntryPointViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.common_view_model import CommonViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_level_model import RewardLevelModel

class ChapterStates(Enum):
    ACTIVE = b'active'
    PAUSED = b'paused'
    COMPLETED = b'completed'
    NOTSTARTED = b'notStarted'
    DISABLED = b'disabled'


class ButtonStates(Enum):
    HIDE = b'hide'
    BUY = b'buy'
    LEVEL = b'level'
    ACTIVATE = b'activate'


class ChapterType(Enum):
    DEFAULT = b'default'
    MARATHON = b'marathon'
    RESOURCE = b'resource'


class BattlePassProgressionsViewModel(CommonViewModel):
    __slots__ = (b'onClose', b'onActionClick', b'onTakeClick', b'onTakeAllClick', b'onOpenShopClick', b'onAboutClick', b'onPointsInfoClick', b'onBpbitClick', b'onBpcoinClick', b'onTakeRewardsClick', b'onFinishedAnimation', b'onLevelsAnimationFinished', b'onChapterChoice', b'onViewLoaded', b'onTasksClick', b'onBuyBP', b'onBuyStages')

    def __init__(self, properties=52, commands=18):
        super(BattlePassProgressionsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def offSeason(self):
        return self._getViewModel(4)

    @staticmethod
    def getOffSeasonType():
        return BattlePassOffSeasonViewModel

    @property
    def levels(self):
        return self._getViewModel(5)

    @staticmethod
    def getLevelsType():
        return RewardLevelModel

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
    def collectionEntryPoint(self):
        return self._getViewModel(8)

    @staticmethod
    def getCollectionEntryPointType():
        return CollectionEntryPointViewModel

    @property
    def price(self):
        return self._getViewModel(9)

    @staticmethod
    def getPriceType():
        return UserCompoundPriceModel

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

    def getFinalReward(self):
        return self._getString(12)

    def setFinalReward(self, value):
        self._setString(12, value)
        return

    def getShowOffSeason(self):
        return self._getBool(13)

    def setShowOffSeason(self, value):
        self._setBool(13, value)
        return

    def getSeasonText(self):
        return self._getString(14)

    def setSeasonText(self, value):
        self._setString(14, value)
        return

    def getExpireTimeStr(self):
        return self._getString(15)

    def setExpireTimeStr(self, value):
        self._setString(15, value)
        return

    def getPreviousPointsInChapter(self):
        return self._getNumber(16)

    def setPreviousPointsInChapter(self, value):
        self._setNumber(16, value)
        return

    def getCurrentPointsInChapter(self):
        return self._getNumber(17)

    def setCurrentPointsInChapter(self, value):
        self._setNumber(17, value)
        return

    def getPreviousFreePointsInChapter(self):
        return self._getNumber(18)

    def setPreviousFreePointsInChapter(self, value):
        self._setNumber(18, value)
        return

    def getFreePointsInChapter(self):
        return self._getNumber(19)

    def setFreePointsInChapter(self, value):
        self._setNumber(19, value)
        return

    def getPreviousPointsInLevel(self):
        return self._getNumber(20)

    def setPreviousPointsInLevel(self, value):
        self._setNumber(20, value)
        return

    def getCurrentPointsInLevel(self):
        return self._getNumber(21)

    def setCurrentPointsInLevel(self, value):
        self._setNumber(21, value)
        return

    def getPreviousFreePointsInLevel(self):
        return self._getNumber(22)

    def setPreviousFreePointsInLevel(self, value):
        self._setNumber(22, value)
        return

    def getFreePointsInLevel(self):
        return self._getNumber(23)

    def setFreePointsInLevel(self, value):
        self._setNumber(23, value)
        return

    def getBpbitCount(self):
        return self._getNumber(24)

    def setBpbitCount(self, value):
        self._setNumber(24, value)
        return

    def getNotChosenRewardCount(self):
        return self._getNumber(25)

    def setNotChosenRewardCount(self, value):
        self._setNumber(25, value)
        return

    def getIsBattlePassCompleted(self):
        return self._getBool(26)

    def setIsBattlePassCompleted(self, value):
        self._setBool(26, value)
        return

    def getIsChooseRewardsEnabled(self):
        return self._getBool(27)

    def setIsChooseRewardsEnabled(self, value):
        self._setBool(27, value)
        return

    def getPreviousLevel(self):
        return self._getNumber(28)

    def setPreviousLevel(self, value):
        self._setNumber(28, value)
        return

    def getPotentialLevel(self):
        return self._getNumber(29)

    def setPotentialLevel(self, value):
        self._setNumber(29, value)
        return

    def getPreviousPotentialLevel(self):
        return self._getNumber(30)

    def setPreviousPotentialLevel(self, value):
        self._setNumber(30, value)
        return

    def getIsPaused(self):
        return self._getBool(31)

    def setIsPaused(self, value):
        self._setBool(31, value)
        return

    def getIsChooseDeviceEnabled(self):
        return self._getBool(32)

    def setIsChooseDeviceEnabled(self, value):
        self._setBool(32, value)
        return

    def getBpcoinCount(self):
        return self._getNumber(33)

    def setBpcoinCount(self, value):
        self._setNumber(33, value)
        return

    def getIsWalletAvailable(self):
        return self._getBool(34)

    def setIsWalletAvailable(self, value):
        self._setBool(34, value)
        return

    def getShowBuyAnimations(self):
        return self._getBool(35)

    def setShowBuyAnimations(self, value):
        self._setBool(35, value)
        return

    def getShowLevelsAnimations(self):
        return self._getBool(36)

    def setShowLevelsAnimations(self, value):
        self._setBool(36, value)
        return

    def getShowReplaceRewardsAnimations(self):
        return self._getBool(37)

    def setShowReplaceRewardsAnimations(self, value):
        self._setBool(37, value)
        return

    def getButtonState(self):
        return ButtonStates(self._getString(38))

    def setButtonState(self, value):
        self._setString(38, value.value)
        return

    def getIsStyleTaken(self):
        return self._getBool(39)

    def setIsStyleTaken(self, value):
        self._setBool(39, value)
        return

    def getIsStyleProgressive(self):
        return self._getBool(40)

    def setIsStyleProgressive(self, value):
        self._setBool(40, value)
        return

    def getIsSeasonEndingSoon(self):
        return self._getBool(41)

    def setIsSeasonEndingSoon(self, value):
        self._setBool(41, value)
        return

    def getIsSingleChapter(self):
        return self._getBool(42)

    def setIsSingleChapter(self, value):
        self._setBool(42, value)
        return

    def getChapterType(self):
        return ChapterType(self._getString(43))

    def setChapterType(self, value):
        self._setString(43, value.value)
        return

    def getAvailableChapterTypes(self):
        return self._getArray(44)

    def setAvailableChapterTypes(self, value):
        self._setArray(44, value)
        return

    def getAvailableBattleTypes(self):
        return self._getArray(45)

    def setAvailableBattleTypes(self, value):
        self._setArray(45, value)
        return

    @staticmethod
    def getAvailableBattleTypesType():
        return int

    def getExpireTime(self):
        return self._getNumber(46)

    def setExpireTime(self, value):
        self._setNumber(46, value)
        return

    def getHasActiveChapter(self):
        return self._getBool(47)

    def setHasActiveChapter(self, value):
        self._setBool(47, value)
        return

    def getShowHint(self):
        return self._getBool(48)

    def setShowHint(self, value):
        self._setBool(48, value)
        return

    def getIsBpCoinShopEntryPointActive(self):
        return self._getBool(49)

    def setIsBpCoinShopEntryPointActive(self, value):
        self._setBool(49, value)
        return

    def getIsBpPointsShopEntryPointActive(self):
        return self._getBool(50)

    def setIsBpPointsShopEntryPointActive(self, value):
        self._setBool(50, value)
        return

    def getProgressionQuestVehicleName(self):
        return self._getString(51)

    def setProgressionQuestVehicleName(self, value):
        self._setString(51, value)
        return

    def _initialize(self):
        super(BattlePassProgressionsViewModel, self)._initialize()
        self._addViewModelProperty(b'offSeason', BattlePassOffSeasonViewModel())
        self._addViewModelProperty(b'levels', UserListModel())
        self._addViewModelProperty(b'widget3dStyle', BattlePassWidget3DStyleViewModel())
        self._addViewModelProperty(b'chapterCharacter', CharacterWidgetViewModel())
        self._addViewModelProperty(b'collectionEntryPoint', CollectionEntryPointViewModel())
        self._addViewModelProperty(b'price', UserCompoundPriceModel())
        self._addNumberProperty(b'chapterID', 0)
        self._addStringProperty(b'chapterState')
        self._addStringProperty(b'finalReward', b'')
        self._addBoolProperty(b'showOffSeason', False)
        self._addStringProperty(b'seasonText', b'')
        self._addStringProperty(b'expireTimeStr', b'')
        self._addNumberProperty(b'previousPointsInChapter', 0)
        self._addNumberProperty(b'currentPointsInChapter', 0)
        self._addNumberProperty(b'previousFreePointsInChapter', 0)
        self._addNumberProperty(b'freePointsInChapter', 0)
        self._addNumberProperty(b'previousPointsInLevel', 0)
        self._addNumberProperty(b'currentPointsInLevel', 0)
        self._addNumberProperty(b'previousFreePointsInLevel', 0)
        self._addNumberProperty(b'freePointsInLevel', 0)
        self._addNumberProperty(b'bpbitCount', 0)
        self._addNumberProperty(b'notChosenRewardCount', 0)
        self._addBoolProperty(b'isBattlePassCompleted', False)
        self._addBoolProperty(b'isChooseRewardsEnabled', True)
        self._addNumberProperty(b'previousLevel', 0)
        self._addNumberProperty(b'potentialLevel', 0)
        self._addNumberProperty(b'previousPotentialLevel', 0)
        self._addBoolProperty(b'isPaused', False)
        self._addBoolProperty(b'isChooseDeviceEnabled', True)
        self._addNumberProperty(b'bpcoinCount', 0)
        self._addBoolProperty(b'isWalletAvailable', True)
        self._addBoolProperty(b'showBuyAnimations', False)
        self._addBoolProperty(b'showLevelsAnimations', False)
        self._addBoolProperty(b'showReplaceRewardsAnimations', False)
        self._addStringProperty(b'buttonState')
        self._addBoolProperty(b'isStyleTaken', False)
        self._addBoolProperty(b'isStyleProgressive', False)
        self._addBoolProperty(b'isSeasonEndingSoon', False)
        self._addBoolProperty(b'isSingleChapter', False)
        self._addStringProperty(b'chapterType')
        self._addArrayProperty(b'availableChapterTypes', Array())
        self._addArrayProperty(b'availableBattleTypes', Array())
        self._addNumberProperty(b'expireTime', 0)
        self._addBoolProperty(b'hasActiveChapter', False)
        self._addBoolProperty(b'showHint', False)
        self._addBoolProperty(b'isBpCoinShopEntryPointActive', False)
        self._addBoolProperty(b'isBpPointsShopEntryPointActive', False)
        self._addStringProperty(b'progressionQuestVehicleName', b'')
        self.onClose = self._addCommand(b'onClose')
        self.onActionClick = self._addCommand(b'onActionClick')
        self.onTakeClick = self._addCommand(b'onTakeClick')
        self.onTakeAllClick = self._addCommand(b'onTakeAllClick')
        self.onOpenShopClick = self._addCommand(b'onOpenShopClick')
        self.onAboutClick = self._addCommand(b'onAboutClick')
        self.onPointsInfoClick = self._addCommand(b'onPointsInfoClick')
        self.onBpbitClick = self._addCommand(b'onBpbitClick')
        self.onBpcoinClick = self._addCommand(b'onBpcoinClick')
        self.onTakeRewardsClick = self._addCommand(b'onTakeRewardsClick')
        self.onFinishedAnimation = self._addCommand(b'onFinishedAnimation')
        self.onLevelsAnimationFinished = self._addCommand(b'onLevelsAnimationFinished')
        self.onChapterChoice = self._addCommand(b'onChapterChoice')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onTasksClick = self._addCommand(b'onTasksClick')
        self.onBuyBP = self._addCommand(b'onBuyBP')
        self.onBuyStages = self._addCommand(b'onBuyStages')
        return
