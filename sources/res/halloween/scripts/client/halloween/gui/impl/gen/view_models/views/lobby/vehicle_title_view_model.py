from enum import Enum
from frameworks.wulf import ViewModel

class VehicleTypes(Enum):
    NONE = b'none'
    LIGHTTANK = b'lightTank'
    MEDIUMTANK = b'mediumTank'
    HEAVYTANK = b'heavyTank'
    SPG = b'SPG'
    AT_SPG = b'AT-SPG'


class VehicleTitleViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(VehicleTitleViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)
        return

    def getRole(self):
        return self._getNumber(3)

    def setRole(self, value):
        self._setNumber(3, value)
        return

    def getNation(self):
        return self._getString(4)

    def setNation(self, value):
        self._setString(4, value)
        return

    def getIsPremium(self):
        return self._getBool(5)

    def setIsPremium(self, value):
        self._setBool(5, value)
        return

    def getVehicleType(self):
        return VehicleTypes(self._getString(6))

    def setVehicleType(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(VehicleTitleViewModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'role', 0)
        self._addStringProperty(b'nation', b'')
        self._addBoolProperty(b'isPremium', False)
        self._addStringProperty(b'vehicleType')
        return
