from enum import Enum
from frameworks.wulf import ViewModel

class PerformanceRiskEnum(Enum):
    LOWRISK = b'lowRisk'
    MEDIUMRISK = b'mediumRisk'
    HIGHRISK = b'highRisk'


class State(Enum):
    INTRO = b'intro'
    INPROGRESS = b'inProgress'
    FROZEN = b'frozen'


class FortRushEventBannerViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(FortRushEventBannerViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDate(self):
        return self._getNumber(0)

    def setDate(self, value):
        self._setNumber(0, value)
        return

    def getEndDate(self):
        return self._getNumber(1)

    def setEndDate(self, value):
        self._setNumber(1, value)
        return

    def getPerformanceRisk(self):
        return PerformanceRiskEnum(self._getString(2))

    def setPerformanceRisk(self, value):
        self._setString(2, value.value)
        return

    def getCurLevel(self):
        return self._getNumber(3)

    def setCurLevel(self, value):
        self._setNumber(3, value)
        return

    def getMaxLevel(self):
        return self._getNumber(4)

    def setMaxLevel(self, value):
        self._setNumber(4, value)
        return

    def getCurPoints(self):
        return self._getNumber(5)

    def setCurPoints(self, value):
        self._setNumber(5, value)
        return

    def getMaxPoints(self):
        return self._getNumber(6)

    def setMaxPoints(self, value):
        self._setNumber(6, value)
        return

    def getState(self):
        return State(self._getString(7))

    def setState(self, value):
        self._setString(7, value.value)
        return

    def _initialize(self):
        super(FortRushEventBannerViewModel, self)._initialize()
        self._addNumberProperty(b'date', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addStringProperty(b'performanceRisk')
        self._addNumberProperty(b'curLevel', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addNumberProperty(b'curPoints', 0)
        self._addNumberProperty(b'maxPoints', 0)
        self._addStringProperty(b'state')
        return
