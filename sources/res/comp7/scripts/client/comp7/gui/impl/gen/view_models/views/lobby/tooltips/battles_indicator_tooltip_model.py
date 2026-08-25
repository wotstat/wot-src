from comp7.gui.impl.gen.view_models.views.lobby.enums import StatisticsMode
from frameworks.wulf import ViewModel

class BattlesIndicatorTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattlesIndicatorTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatisticsMode(self):
        return StatisticsMode(self._getNumber(0))

    def setStatisticsMode(self, value):
        self._setNumber(0, value.value)
        return

    def getSoloBattlesCount(self):
        return self._getNumber(1)

    def setSoloBattlesCount(self, value):
        self._setNumber(1, value)
        return

    def getSuperPlatoonBattlesCount(self):
        return self._getNumber(2)

    def setSuperPlatoonBattlesCount(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(BattlesIndicatorTooltipModel, self)._initialize()
        self._addNumberProperty(b'statisticsMode')
        self._addNumberProperty(b'soloBattlesCount', 0)
        self._addNumberProperty(b'superPlatoonBattlesCount', 0)
        return
