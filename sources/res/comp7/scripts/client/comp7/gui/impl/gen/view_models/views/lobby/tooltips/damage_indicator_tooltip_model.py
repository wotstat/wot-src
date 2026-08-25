from comp7.gui.impl.gen.view_models.views.lobby.enums import StatisticsMode
from frameworks.wulf import ViewModel

class DamageIndicatorTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DamageIndicatorTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatisticsMode(self):
        return StatisticsMode(self._getNumber(0))

    def setStatisticsMode(self, value):
        self._setNumber(0, value.value)
        return

    def getAverageDamageDealt(self):
        return self._getReal(1)

    def setAverageDamageDealt(self, value):
        self._setReal(1, value)
        return

    def getRecordDamageDealt(self):
        return self._getReal(2)

    def setRecordDamageDealt(self, value):
        self._setReal(2, value)
        return

    def getRecordDamageDealtVehicleName(self):
        return self._getString(3)

    def setRecordDamageDealtVehicleName(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(DamageIndicatorTooltipModel, self)._initialize()
        self._addNumberProperty(b'statisticsMode')
        self._addRealProperty(b'averageDamageDealt', 0.0)
        self._addRealProperty(b'recordDamageDealt', 0.0)
        self._addStringProperty(b'recordDamageDealtVehicleName', b'')
        return
