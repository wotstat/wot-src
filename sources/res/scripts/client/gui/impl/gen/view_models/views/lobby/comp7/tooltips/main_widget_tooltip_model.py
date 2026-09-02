from enum import IntEnum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.comp7.division_info_model import DivisionInfoModel
from gui.impl.gen.view_models.views.lobby.comp7.qualification_model import QualificationModel

class Rank(IntEnum):
    FIRST = 6
    SECOND = 5
    THIRD = 4
    FOURTH = 3
    FIFTH = 2
    SIXTH = 1


class State(IntEnum):
    INITIAL = 0
    SUCCESS = 1
    LOADING = 2
    ERROR = 3


class MainWidgetTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(MainWidgetTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def divisionInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getDivisionInfoType():
        return DivisionInfoModel

    @property
    def qualificationModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getQualificationModelType():
        return QualificationModel

    def getRank(self):
        return Rank(self._getNumber(2))

    def setRank(self, value):
        self._setNumber(2, value.value)
        return

    def getExternalDataState(self):
        return State(self._getNumber(3))

    def setExternalDataState(self, value):
        self._setNumber(3, value.value)
        return

    def getCurrentScore(self):
        return self._getNumber(4)

    def setCurrentScore(self, value):
        self._setNumber(4, value)
        return

    def getMyPosition(self):
        return self._getNumber(5)

    def setMyPosition(self, value):
        self._setNumber(5, value)
        return

    def getLeaderboardUpdateTimestamp(self):
        return self._getNumber(6)

    def setLeaderboardUpdateTimestamp(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(MainWidgetTooltipModel, self)._initialize()
        self._addViewModelProperty(b'divisionInfo', DivisionInfoModel())
        self._addViewModelProperty(b'qualificationModel', QualificationModel())
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'externalDataState', State.INITIAL.value)
        self._addNumberProperty(b'currentScore', 0)
        self._addNumberProperty(b'myPosition', -1)
        self._addNumberProperty(b'leaderboardUpdateTimestamp', 0)
        return
