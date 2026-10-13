from enum import Enum
from frameworks.wulf import ViewModel

class PerformanceRiskEnum(Enum):
    LOWRISK = b'lowRisk'
    MEDIUMRISK = b'mediumRisk'
    HIGHRISK = b'highRisk'


class EventBannerViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=3, commands=1):
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

    def getPerformanceRisk(self):
        return PerformanceRiskEnum(self._getString(2))

    def setPerformanceRisk(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(EventBannerViewModel, self)._initialize()
        self._addNumberProperty(b'date', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addStringProperty(b'performanceRisk')
        self.onClick = self._addCommand(b'onClick')
        return
