from comp7.gui.impl.gen.view_models.views.lobby.enums import StatisticsMode
from frameworks.wulf import ViewModel

class WinsIndicatorTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(WinsIndicatorTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatisticsMode(self):
        return StatisticsMode(self._getNumber(0))

    def setStatisticsMode(self, value):
        self._setNumber(0, value.value)
        return

    def getWinRate(self):
        return self._getReal(1)

    def setWinRate(self, value):
        self._setReal(1, value)
        return

    def getWinsCount(self):
        return self._getNumber(2)

    def setWinsCount(self, value):
        self._setNumber(2, value)
        return

    def getLossCount(self):
        return self._getNumber(3)

    def setLossCount(self, value):
        self._setNumber(3, value)
        return

    def getDrawCount(self):
        return self._getNumber(4)

    def setDrawCount(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(WinsIndicatorTooltipModel, self)._initialize()
        self._addNumberProperty(b'statisticsMode')
        self._addRealProperty(b'winRate', 0.0)
        self._addNumberProperty(b'winsCount', 0)
        self._addNumberProperty(b'lossCount', 0)
        self._addNumberProperty(b'drawCount', 0)
        return
