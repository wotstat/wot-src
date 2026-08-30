from comp7.gui.impl.gen.view_models.views.lobby.enums import StatisticsMode
from frameworks.wulf import ViewModel

class PrestigeIndicatorTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PrestigeIndicatorTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatisticsMode(self):
        return StatisticsMode(self._getNumber(0))

    def setStatisticsMode(self, value):
        self._setNumber(0, value.value)
        return

    def getAveragePrestige(self):
        return self._getReal(1)

    def setAveragePrestige(self, value):
        self._setReal(1, value)
        return

    def getRecordPrestige(self):
        return self._getReal(2)

    def setRecordPrestige(self, value):
        self._setReal(2, value)
        return

    def getRecordPrestigeVehicleName(self):
        return self._getString(3)

    def setRecordPrestigeVehicleName(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(PrestigeIndicatorTooltipModel, self)._initialize()
        self._addNumberProperty(b'statisticsMode')
        self._addRealProperty(b'averagePrestige', 0.0)
        self._addRealProperty(b'recordPrestige', 0.0)
        self._addStringProperty(b'recordPrestigeVehicleName', b'')
        return
