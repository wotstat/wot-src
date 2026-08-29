from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.leaderboard_reward_tooltip_model import LeaderboardRewardTooltipModel

class PerformanceRisk(Enum):
    HIGH = b'high'
    MEDIUM = b'medium'
    LOW = b'low'


class ProgressionState(Enum):
    COMPLETED = b'completed'
    INPROGRESS = b'inProgress'


class WidgetTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(WidgetTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def leaderBoard(self):
        return self._getViewModel(0)

    @staticmethod
    def getLeaderBoardType():
        return LeaderboardRewardTooltipModel

    def getProgressionState(self):
        return ProgressionState(self._getString(1))

    def setProgressionState(self, value):
        self._setString(1, value.value)
        return

    def getPerformance(self):
        return PerformanceRisk(self._getString(2))

    def setPerformance(self, value):
        self._setString(2, value.value)
        return

    def getTime(self):
        return self._getNumber(3)

    def setTime(self, value):
        self._setNumber(3, value)
        return

    def getBattleSchedule(self):
        return self._getArray(4)

    def setBattleSchedule(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getBattleScheduleType():
        return int

    def _initialize(self):
        super(WidgetTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'leaderBoard', LeaderboardRewardTooltipModel())
        self._addStringProperty(b'progressionState', ProgressionState.INPROGRESS.value)
        self._addStringProperty(b'performance', PerformanceRisk.LOW.value)
        self._addNumberProperty(b'time', 0)
        self._addArrayProperty(b'battleSchedule', Array())
        return
