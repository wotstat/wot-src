from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class VehicleSpecialSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehicleSpecialSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getProbability(self):
        return self._getReal(0)

    def setProbability(self, value):
        self._setReal(0, value)
        return

    def getGarant(self):
        return self._getNumber(1)

    def setGarant(self, value):
        self._setNumber(1, value)
        return

    def getMaxLevel(self):
        return self._getNumber(2)

    def setMaxLevel(self, value):
        self._setNumber(2, value)
        return

    def getMinLevel(self):
        return self._getNumber(3)

    def setMinLevel(self, value):
        self._setNumber(3, value)
        return

    def getVehicleNames(self):
        return self._getArray(4)

    def setVehicleNames(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getVehicleNamesType():
        return unicode

    def getVehicleLevels(self):
        return self._getArray(5)

    def setVehicleLevels(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getVehicleLevelsType():
        return int

    def _initialize(self):
        super(VehicleSpecialSlotModel, self)._initialize()
        self._addRealProperty(b'probability', 0.0)
        self._addNumberProperty(b'garant', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addNumberProperty(b'minLevel', 0)
        self._addArrayProperty(b'vehicleNames', Array())
        self._addArrayProperty(b'vehicleLevels', Array())
        return
