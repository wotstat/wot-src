from frameworks.wulf import ViewModel

class VehicleCompareModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(VehicleCompareModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleCount(self):
        return self._getNumber(0)

    def setVehicleCount(self, value):
        self._setNumber(0, value)
        return

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(VehicleCompareModel, self)._initialize()
        self._addNumberProperty(b'vehicleCount', 0)
        self._addBoolProperty(b'isEnabled', False)
        return
