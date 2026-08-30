from enum import Enum, IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_chapter_model import ArmoryYardChapterModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_level_model import ArmoryYardLevelModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_quest_sub_model import ArmoryYardQuestSubModel

class State(Enum):
    BEFOREPROGRESSION = b'beforeProgression'
    ACTIVE = b'active'
    PURCHASESTAGE = b'purchaseStage'
    COMPLETED = b'completed'
    DISABLED = b'disabled'
    INTRO = b'intro'


class AnimationStatus(IntEnum):
    DISABLED = 0
    ACTIVE = 1


class RewardStatus(IntEnum):
    EMPTYREWARDS = 0
    READYREWARDS = 1
    ANIMATEDREWARDS = 2


class TabId(IntEnum):
    PROGRESS = 0
    QUESTS = 1
    SHOP = 2


class EscSource(IntEnum):
    KEYBOARD = 0
    MOUSE = 1


class SimpleTooltipStates(IntEnum):
    TAB = 0
    CHAPTER = 1
    SHOPINFO = 2
    STEP = 3


class BuyButtonState(IntEnum):
    HIDDEN = 0
    TOKENS = 1
    COINS = 2


class ArmoryYardMainViewModel(ViewModel):
    __slots__ = (b'onMoveSpace', b'onStartMoving', b'onTabChange', b'onClose', b'onPlayAnimation', b'onSkipAnimation', b'onAboutEvent', b'onCollectReward', b'onBuyTokens', b'onShowVehiclePreview', b'onShowStylePreview', b'onShopOpen', b'onPlayStageSound', b'onQuestReroll', b'onChapterSelect')
    TOOLTIP_ID_ARG = b'tooltipId'
    FINAL_REWARD_TOOLTIP_TYPE = b'finalReward'

    def __init__(self, properties=25, commands=15):
        super(ArmoryYardMainViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getTabId(self):
        return TabId(self._getNumber(1))

    def setTabId(self, value):
        self._setNumber(1, value.value)
        return

    def getCurrentLevel(self):
        return self._getNumber(2)

    def setCurrentLevel(self, value):
        self._setNumber(2, value)
        return

    def getStartStepOfPostProgression(self):
        return self._getNumber(3)

    def setStartStepOfPostProgression(self, value):
        self._setNumber(3, value)
        return

    def getViewedLevel(self):
        return self._getNumber(4)

    def setViewedLevel(self, value):
        self._setNumber(4, value)
        return

    def getRewardStatus(self):
        return RewardStatus(self._getNumber(5))

    def setRewardStatus(self, value):
        self._setNumber(5, value.value)
        return

    def getChapters(self):
        return self._getArray(6)

    def setChapters(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getChaptersType():
        return ArmoryYardChapterModel

    def getLevels(self):
        return self._getArray(7)

    def setLevels(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getLevelsType():
        return ArmoryYardLevelModel

    def getQuests(self):
        return self._getArray(8)

    def setQuests(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getQuestsType():
        return ArmoryYardQuestSubModel

    def getAnimationLevel(self):
        return self._getNumber(9)

    def setAnimationLevel(self, value):
        self._setNumber(9, value)
        return

    def getLevelDuration(self):
        return self._getNumber(10)

    def setLevelDuration(self, value):
        self._setNumber(10, value)
        return

    def getFromTimestamp(self):
        return self._getNumber(11)

    def setFromTimestamp(self, value):
        self._setNumber(11, value)
        return

    def getToTimestamp(self):
        return self._getNumber(12)

    def setToTimestamp(self, value):
        self._setNumber(12, value)
        return

    def getReceivedTokensCount(self):
        return self._getNumber(13)

    def setReceivedTokensCount(self, value):
        self._setNumber(13, value)
        return

    def getTotalTokensCount(self):
        return self._getNumber(14)

    def setTotalTokensCount(self, value):
        self._setNumber(14, value)
        return

    def getMaxNumberOfSteps(self):
        return self._getNumber(15)

    def setMaxNumberOfSteps(self, value):
        self._setNumber(15, value)
        return

    def getAnimationStatus(self):
        return AnimationStatus(self._getNumber(16))

    def setAnimationStatus(self, value):
        self._setNumber(16, value.value)
        return

    def getReplay(self):
        return self._getBool(17)

    def setReplay(self, value):
        self._setBool(17, value)
        return

    def getShopButtonVisible(self):
        return self._getBool(18)

    def setShopButtonVisible(self, value):
        self._setBool(18, value)
        return

    def getBuyButtonState(self):
        return BuyButtonState(self._getNumber(19))

    def setBuyButtonState(self, value):
        self._setNumber(19, value.value)
        return

    def getFreeRerollCount(self):
        return self._getNumber(20)

    def setFreeRerollCount(self, value):
        self._setNumber(20, value)
        return

    def getRerollCountDown(self):
        return self._getNumber(21)

    def setRerollCountDown(self, value):
        self._setNumber(21, value)
        return

    def getIsRerollEnabled(self):
        return self._getBool(22)

    def setIsRerollEnabled(self, value):
        self._setBool(22, value)
        return

    def getIsRerollButtonTriggerEnabled(self):
        return self._getBool(23)

    def setIsRerollButtonTriggerEnabled(self, value):
        self._setBool(23, value)
        return

    def getIsPostProgression(self):
        return self._getBool(24)

    def setIsPostProgression(self, value):
        self._setBool(24, value)
        return

    def _initialize(self):
        super(ArmoryYardMainViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'tabId')
        self._addNumberProperty(b'currentLevel', 0)
        self._addNumberProperty(b'startStepOfPostProgression', 0)
        self._addNumberProperty(b'viewedLevel', 0)
        self._addNumberProperty(b'rewardStatus')
        self._addArrayProperty(b'chapters', Array())
        self._addArrayProperty(b'levels', Array())
        self._addArrayProperty(b'quests', Array())
        self._addNumberProperty(b'animationLevel', 0)
        self._addNumberProperty(b'levelDuration', 0)
        self._addNumberProperty(b'fromTimestamp', 0)
        self._addNumberProperty(b'toTimestamp', 0)
        self._addNumberProperty(b'receivedTokensCount', 0)
        self._addNumberProperty(b'totalTokensCount', 0)
        self._addNumberProperty(b'maxNumberOfSteps', 0)
        self._addNumberProperty(b'animationStatus')
        self._addBoolProperty(b'replay', False)
        self._addBoolProperty(b'shopButtonVisible', False)
        self._addNumberProperty(b'buyButtonState')
        self._addNumberProperty(b'freeRerollCount', 0)
        self._addNumberProperty(b'rerollCountDown', 0)
        self._addBoolProperty(b'isRerollEnabled', False)
        self._addBoolProperty(b'isRerollButtonTriggerEnabled', False)
        self._addBoolProperty(b'isPostProgression', False)
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onStartMoving = self._addCommand(b'onStartMoving')
        self.onTabChange = self._addCommand(b'onTabChange')
        self.onClose = self._addCommand(b'onClose')
        self.onPlayAnimation = self._addCommand(b'onPlayAnimation')
        self.onSkipAnimation = self._addCommand(b'onSkipAnimation')
        self.onAboutEvent = self._addCommand(b'onAboutEvent')
        self.onCollectReward = self._addCommand(b'onCollectReward')
        self.onBuyTokens = self._addCommand(b'onBuyTokens')
        self.onShowVehiclePreview = self._addCommand(b'onShowVehiclePreview')
        self.onShowStylePreview = self._addCommand(b'onShowStylePreview')
        self.onShopOpen = self._addCommand(b'onShopOpen')
        self.onPlayStageSound = self._addCommand(b'onPlayStageSound')
        self.onQuestReroll = self._addCommand(b'onQuestReroll')
        self.onChapterSelect = self._addCommand(b'onChapterSelect')
        return
