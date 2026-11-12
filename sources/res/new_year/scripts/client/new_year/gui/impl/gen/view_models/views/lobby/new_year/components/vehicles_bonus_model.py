from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class VehicleType(Enum):
    HEAVY = b'heavyTank'
    MEDIUM = b'mediumTank'
    LIGHT = b'lightTank'
    SPG = b'SPG'
    ATSPG = b'AT-SPG'


class VehiclesBonusModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(VehiclesBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(7)

    def setVehicleName(self, value):
        self._setString(7, value)
        return

    def getType(self):
        return VehicleType(self._getString(8))

    def setType(self, value):
        self._setString(8, value.value)
        return

    def getLevel(self):
        return self._getNumber(9)

    def setLevel(self, value):
        self._setNumber(9, value)
        return

    def getNationTag(self):
        return self._getString(10)

    def setNationTag(self, value):
        self._setString(10, value)
        return

    def getVehicleCD(self):
        return self._getNumber(11)

    def setVehicleCD(self, value):
        self._setNumber(11, value)
        return

    def getIsInInventory(self):
        return self._getBool(12)

    def setIsInInventory(self, value):
        self._setBool(12, value)
        return

    def _initialize(self):
        super(VehiclesBonusModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'type')
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'nationTag', b'')
        self._addNumberProperty(b'vehicleCD', 0)
        self._addBoolProperty(b'isInInventory', False)
        return
