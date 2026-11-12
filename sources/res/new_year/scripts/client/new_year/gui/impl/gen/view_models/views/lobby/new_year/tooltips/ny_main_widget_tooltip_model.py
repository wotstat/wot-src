from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.common.ny_event_state_model import NyEventStateModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.tooltips.pet_stats_model import PetStatsModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_indicator_model import NyPetIndicatorModel

class WidgetBlock(Enum):
    MAINBLOCK = b'mainBlock'
    PROGRESSBLOCK = b'progressBlock'
    BONUSBLOCK = b'bonusBlock'
    SURPRISEMACHINE = b'surpriseMachine'


class NyMainWidgetTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(NyMainWidgetTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def eventState(self):
        return self._getViewModel(0)

    @staticmethod
    def getEventStateType():
        return NyEventStateModel

    def getCurrentLevel(self):
        return self._getNumber(1)

    def setCurrentLevel(self, value):
        self._setNumber(1, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(2)

    def setCurrentPoints(self, value):
        self._setNumber(2, value)
        return

    def getNextLevelPoints(self):
        return self._getNumber(3)

    def setNextLevelPoints(self, value):
        self._setNumber(3, value)
        return

    def getTimeLeft(self):
        return self._getNumber(4)

    def setTimeLeft(self, value):
        self._setNumber(4, value)
        return

    def getIsNeedTimer(self):
        return self._getBool(5)

    def setIsNeedTimer(self, value):
        self._setBool(5, value)
        return

    def getBonuses(self):
        return self._getArray(6)

    def setBonuses(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getBonusesType():
        return PetStatsModel

    def getBonus(self):
        return self._getNumber(7)

    def setBonus(self, value):
        self._setNumber(7, value)
        return

    def getMaxBonus(self):
        return self._getNumber(8)

    def setMaxBonus(self, value):
        self._setNumber(8, value)
        return

    def getRewardsCount(self):
        return self._getNumber(9)

    def setRewardsCount(self, value):
        self._setNumber(9, value)
        return

    def getIsPetPaused(self):
        return self._getBool(10)

    def setIsPetPaused(self, value):
        self._setBool(10, value)
        return

    def getIsWithLeaderboard(self):
        return self._getBool(11)

    def setIsWithLeaderboard(self, value):
        self._setBool(11, value)
        return

    def getIsProgressPaused(self):
        return self._getBool(12)

    def setIsProgressPaused(self, value):
        self._setBool(12, value)
        return

    def getIsFirstEntry(self):
        return self._getBool(13)

    def setIsFirstEntry(self, value):
        self._setBool(13, value)
        return

    def getBlockState(self):
        return WidgetBlock(self._getString(14))

    def setBlockState(self, value):
        self._setString(14, value.value)
        return

    def getIndicators(self):
        return self._getArray(15)

    def setIndicators(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getIndicatorsType():
        return NyPetIndicatorModel

    def getIsReadyRaid(self):
        return self._getBool(16)

    def setIsReadyRaid(self, value):
        self._setBool(16, value)
        return

    def _initialize(self):
        super(NyMainWidgetTooltipModel, self)._initialize()
        self._addViewModelProperty(b'eventState', NyEventStateModel())
        self._addNumberProperty(b'currentLevel', 1)
        self._addNumberProperty(b'currentPoints', 0)
        self._addNumberProperty(b'nextLevelPoints', 0)
        self._addNumberProperty(b'timeLeft', 0)
        self._addBoolProperty(b'isNeedTimer', False)
        self._addArrayProperty(b'bonuses', Array())
        self._addNumberProperty(b'bonus', 0)
        self._addNumberProperty(b'maxBonus', 0)
        self._addNumberProperty(b'rewardsCount', 0)
        self._addBoolProperty(b'isPetPaused', False)
        self._addBoolProperty(b'isWithLeaderboard', True)
        self._addBoolProperty(b'isProgressPaused', False)
        self._addBoolProperty(b'isFirstEntry', False)
        self._addStringProperty(b'blockState')
        self._addArrayProperty(b'indicators', Array())
        self._addBoolProperty(b'isReadyRaid', False)
        return
