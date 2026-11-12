from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_final_reward_model import NyFinalRewardModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_top_reward_model import NyTopRewardModel

class StageState(Enum):
    ACTIVE = b'active'
    FINISHED = b'finished'
    NOTSTARTED = b'notStarted'


class StageInfoTip(Enum):
    ACTIVE = b'active'
    FINISHED = b'finished'
    NOTSTARTED = b'notStarted'
    NOTENOUGHPOINTS = b'notEnoughPoints'
    LEADERBOARDCOMPLETED = b'leaderBoardCompleted'


class NyStageModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(NyStageModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def finalReward(self):
        return self._getViewModel(0)

    @staticmethod
    def getFinalRewardType():
        return NyFinalRewardModel

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def getStartDate(self):
        return self._getNumber(2)

    def setStartDate(self, value):
        self._setNumber(2, value)
        return

    def getEndDate(self):
        return self._getNumber(3)

    def setEndDate(self, value):
        self._setNumber(3, value)
        return

    def getState(self):
        return StageState(self._getString(4))

    def setState(self, value):
        self._setString(4, value.value)
        return

    def getInfoTip(self):
        return StageInfoTip(self._getString(5))

    def setInfoTip(self, value):
        self._setString(5, value.value)
        return

    def getPosition(self):
        return self._getNumber(6)

    def setPosition(self, value):
        self._setNumber(6, value)
        return

    def getCurrentTop(self):
        return self._getNumber(7)

    def setCurrentTop(self, value):
        self._setNumber(7, value)
        return

    def getIsRecalc(self):
        return self._getBool(8)

    def setIsRecalc(self, value):
        self._setBool(8, value)
        return

    def getIsFinalReward(self):
        return self._getBool(9)

    def setIsFinalReward(self, value):
        self._setBool(9, value)
        return

    def getStageNum(self):
        return self._getNumber(10)

    def setStageNum(self, value):
        self._setNumber(10, value)
        return

    def getTops(self):
        return self._getArray(11)

    def setTops(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getTopsType():
        return NyTopRewardModel

    def _initialize(self):
        super(NyStageModel, self)._initialize()
        self._addViewModelProperty(b'finalReward', NyFinalRewardModel())
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addStringProperty(b'state')
        self._addStringProperty(b'infoTip')
        self._addNumberProperty(b'position', 0)
        self._addNumberProperty(b'currentTop', -1)
        self._addBoolProperty(b'isRecalc', False)
        self._addBoolProperty(b'isFinalReward', False)
        self._addNumberProperty(b'stageNum', 0)
        self._addArrayProperty(b'tops', Array())
        return
