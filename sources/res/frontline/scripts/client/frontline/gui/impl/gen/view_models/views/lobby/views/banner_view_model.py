from enum import IntEnum
from frameworks.wulf import ViewModel

class PerformanceRiskEnum(IntEnum):
    HIGHRISK = 1
    MEDIUMRISK = 2
    LOWRISK = 3


class BannerViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=4, commands=1):
        super(BannerViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getFrontlineState(self):
        return self._getString(0)

    def setFrontlineState(self, value):
        self._setString(0, value)
        return

    def getPhaseEndDate(self):
        return self._getNumber(1)

    def setPhaseEndDate(self, value):
        self._setNumber(1, value)
        return

    def getRewardsCount(self):
        return self._getNumber(2)

    def setRewardsCount(self, value):
        self._setNumber(2, value)
        return

    def getPerformanceRisk(self):
        return PerformanceRiskEnum(self._getNumber(3))

    def setPerformanceRisk(self, value):
        self._setNumber(3, value.value)
        return

    def _initialize(self):
        super(BannerViewModel, self)._initialize()
        self._addStringProperty(b'frontlineState', b'')
        self._addNumberProperty(b'phaseEndDate', 0)
        self._addNumberProperty(b'rewardsCount', 0)
        self._addNumberProperty(b'performanceRisk')
        self.onClick = self._addCommand(b'onClick')
        return
