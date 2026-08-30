from frameworks.wulf import ViewModel

class RankInactivityTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RankInactivityTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getRankInactivityCount(self):
        return self._getNumber(0)

    def setRankInactivityCount(self, value):
        self._setNumber(0, value)
        return

    def getRankInactivityPointsCount(self):
        return self._getNumber(1)

    def setRankInactivityPointsCount(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(RankInactivityTooltipModel, self)._initialize()
        self._addNumberProperty(b'rankInactivityCount', -1)
        self._addNumberProperty(b'rankInactivityPointsCount', 0)
        return
