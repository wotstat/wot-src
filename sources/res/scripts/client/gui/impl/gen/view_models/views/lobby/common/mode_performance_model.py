from enum import Enum
from frameworks.wulf import ViewModel

class PerformanceRiskEnum(Enum):
    LOWRISK = b'lowRisk'
    MEDIUMRISK = b'mediumRisk'
    HIGHRISK = b'highRisk'


class ModePerformanceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ModePerformanceModel, self).__init__(properties=properties, commands=commands)
        return

    def getShowPerfRisk(self):
        return self._getBool(0)

    def setShowPerfRisk(self, value):
        self._setBool(0, value)
        return

    def getPerformanceRisk(self):
        return PerformanceRiskEnum(self._getString(1))

    def setPerformanceRisk(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(ModePerformanceModel, self)._initialize()
        self._addBoolProperty(b'showPerfRisk', False)
        self._addStringProperty(b'performanceRisk')
        return
