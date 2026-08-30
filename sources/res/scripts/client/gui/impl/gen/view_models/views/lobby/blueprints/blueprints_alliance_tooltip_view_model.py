from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_price import BlueprintPrice

class BlueprintsAllianceTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BlueprintsAllianceTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getPriceOptions(self):
        return self._getArray(0)

    def setPriceOptions(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getPriceOptionsType():
        return BlueprintPrice

    def getVehicleNationName(self):
        return self._getString(1)

    def setVehicleNationName(self, value):
        self._setString(1, value)
        return

    def getAllianceName(self):
        return self._getString(2)

    def setAllianceName(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(BlueprintsAllianceTooltipViewModel, self)._initialize()
        self._addArrayProperty(b'priceOptions', Array())
        self._addStringProperty(b'vehicleNationName', b'')
        self._addStringProperty(b'allianceName', b'')
        return
