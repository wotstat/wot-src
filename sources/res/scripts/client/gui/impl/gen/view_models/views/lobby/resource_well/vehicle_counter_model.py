from frameworks.wulf import ViewModel

class VehicleCounterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(VehicleCounterModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVehicleCountAvailable(self):
        return self._getBool(0)

    def setIsVehicleCountAvailable(self, value):
        self._setBool(0, value)
        return

    def getVehicleCount(self):
        return self._getNumber(1)

    def setVehicleCount(self, value):
        self._setNumber(1, value)
        return

    def getIsTopVehicle(self):
        return self._getBool(2)

    def setIsTopVehicle(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(VehicleCounterModel, self)._initialize()
        self._addBoolProperty(b'isVehicleCountAvailable', True)
        self._addNumberProperty(b'vehicleCount', 0)
        self._addBoolProperty(b'isTopVehicle', False)
        return
