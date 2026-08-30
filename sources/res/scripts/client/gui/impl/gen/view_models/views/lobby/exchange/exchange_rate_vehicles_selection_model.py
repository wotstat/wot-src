from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class ExchangeRateVehiclesSelectionModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(ExchangeRateVehiclesSelectionModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFieldModernizationAvailable(self):
        return self._getBool(10)

    def setIsFieldModernizationAvailable(self, value):
        self._setBool(10, value)
        return

    def getIsFieldModernizationComplited(self):
        return self._getBool(11)

    def setIsFieldModernizationComplited(self, value):
        self._setBool(11, value)
        return

    def getLevelOfFieldModernization(self):
        return self._getNumber(12)

    def setLevelOfFieldModernization(self, value):
        self._setNumber(12, value)
        return

    def getAmountOfCombatXp(self):
        return self._getNumber(13)

    def setAmountOfCombatXp(self, value):
        self._setNumber(13, value)
        return

    def getNationOrder(self):
        return self._getNumber(14)

    def setNationOrder(self, value):
        self._setNumber(14, value)
        return

    def _initialize(self):
        super(ExchangeRateVehiclesSelectionModel, self)._initialize()
        self._addBoolProperty(b'isFieldModernizationAvailable', False)
        self._addBoolProperty(b'isFieldModernizationComplited', False)
        self._addNumberProperty(b'levelOfFieldModernization', 1)
        self._addNumberProperty(b'amountOfCombatXp', 1)
        self._addNumberProperty(b'nationOrder', 1)
        return
