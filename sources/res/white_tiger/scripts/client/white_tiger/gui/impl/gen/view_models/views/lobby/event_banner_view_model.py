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
    INANNOUNCEMENT = b'inAnnouncement'


class EventBannerViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=8, commands=1):
        super(EventBannerViewModel, self).__init__(properties=properties, commands=commands)
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

    def getIsNew(self):
        return self._getBool(2)

    def setIsNew(self, value):
        self._setBool(2, value)
        return

    def getPerformanceRisk(self):
        return PerformanceRiskEnum(self._getString(3))

    def setPerformanceRisk(self, value):
        self._setString(3, value.value)
        return

    def getMaxProgressionStep(self):
        return self._getNumber(4)

    def setMaxProgressionStep(self, value):
        self._setNumber(4, value)
        return

    def getFinishedLevelsCount(self):
        return self._getNumber(5)

    def setFinishedLevelsCount(self, value):
        self._setNumber(5, value)
        return

    def getNextTimeEnable(self):
        return self._getNumber(6)

    def setNextTimeEnable(self, value):
        self._setNumber(6, value)
        return

    def getState(self):
        return State(self._getString(7))

    def setState(self, value):
        self._setString(7, value.value)
        return

    def _initialize(self):
        super(EventBannerViewModel, self)._initialize()
        self._addNumberProperty(b'date', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addBoolProperty(b'isNew', False)
        self._addStringProperty(b'performanceRisk')
        self._addNumberProperty(b'maxProgressionStep', 1)
        self._addNumberProperty(b'finishedLevelsCount', 0)
        self._addNumberProperty(b'nextTimeEnable', 0)
        self._addStringProperty(b'state')
        self.onClick = self._addCommand(b'onClick')
        return
