from enum import Enum, IntEnum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.awards_widget_model import AwardsWidgetModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_buy_rewards_view_model import BattlePassBuyRewardsViewModel

class ChapterStates(IntEnum):
    ACTIVE = 0
    PAUSED = 1
    COMPLETED = 2
    NOTSTARTED = 3


class FinalRewardTypes(Enum):
    VEHICLE = b'vehicle'
    STYLE = b'style'
    TANKMAN = b'tankman'


class HolidayFinalViewModel(ViewModel):
    __slots__ = (b'onTakeRewardsClick', b'showTankmen', b'onPreviewVehicle', b'showHangar', b'onClose')
    BUY_STATE = b'buyState'
    REWARDS_STATE = b'rewardsState'
    TANKMEN_STATE = b'tankmenState'
    SELECTABLE_REWARDS_STATE = b'selectableRewardsState'
    FINAL_STATE = b'finalState'

    def __init__(self, properties=10, commands=5):
        super(HolidayFinalViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return BattlePassBuyRewardsViewModel

    @property
    def awardsWidget(self):
        return self._getViewModel(1)

    @staticmethod
    def getAwardsWidgetType():
        return AwardsWidgetModel

    def getState(self):
        return self._getString(2)

    def setState(self, value):
        self._setString(2, value)
        return

    def getNotChosenRewardCount(self):
        return self._getNumber(3)

    def setNotChosenRewardCount(self, value):
        self._setNumber(3, value)
        return

    def getIsChooseRewardsEnabled(self):
        return self._getBool(4)

    def setIsChooseRewardsEnabled(self, value):
        self._setBool(4, value)
        return

    def getChapterID(self):
        return self._getNumber(5)

    def setChapterID(self, value):
        self._setNumber(5, value)
        return

    def getCurrentLevel(self):
        return self._getNumber(6)

    def setCurrentLevel(self, value):
        self._setNumber(6, value)
        return

    def getChapterState(self):
        return ChapterStates(self._getNumber(7))

    def setChapterState(self, value):
        self._setNumber(7, value.value)
        return

    def getFinalRewardType(self):
        return FinalRewardTypes(self._getString(8))

    def setFinalRewardType(self, value):
        self._setString(8, value.value)
        return

    def getIsSeasonEndingSoon(self):
        return self._getBool(9)

    def setIsSeasonEndingSoon(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(HolidayFinalViewModel, self)._initialize()
        self._addViewModelProperty(b'rewards', BattlePassBuyRewardsViewModel())
        self._addViewModelProperty(b'awardsWidget', AwardsWidgetModel())
        self._addStringProperty(b'state', b'buyState')
        self._addNumberProperty(b'notChosenRewardCount', 0)
        self._addBoolProperty(b'isChooseRewardsEnabled', True)
        self._addNumberProperty(b'chapterID', 0)
        self._addNumberProperty(b'currentLevel', 0)
        self._addNumberProperty(b'chapterState')
        self._addStringProperty(b'finalRewardType')
        self._addBoolProperty(b'isSeasonEndingSoon', False)
        self.onTakeRewardsClick = self._addCommand(b'onTakeRewardsClick')
        self.showTankmen = self._addCommand(b'showTankmen')
        self.onPreviewVehicle = self._addCommand(b'onPreviewVehicle')
        self.showHangar = self._addCommand(b'showHangar')
        self.onClose = self._addCommand(b'onClose')
        return
