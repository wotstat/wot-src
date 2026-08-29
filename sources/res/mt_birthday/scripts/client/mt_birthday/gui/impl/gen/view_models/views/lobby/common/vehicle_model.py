from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class VehicleType(Enum):
    HEAVY = b'heavyTank'
    MEDIUM = b'mediumTank'
    LIGHT = b'lightTank'
    SPG = b'SPG'
    ATSPG = b'AT-SPG'


class VehicleModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=23, commands=0):
        super(VehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(9)

    def setVehicleName(self, value):
        self._setString(9, value)
        return

    def getType(self):
        return VehicleType(self._getString(10))

    def setType(self, value):
        self._setString(10, value.value)
        return

    def getLevel(self):
        return self._getNumber(11)

    def setLevel(self, value):
        self._setNumber(11, value)
        return

    def getShortVehicleLabel(self):
        return self._getString(12)

    def setShortVehicleLabel(self, value):
        self._setString(12, value)
        return

    def getNationTag(self):
        return self._getString(13)

    def setNationTag(self, value):
        self._setString(13, value)
        return

    def getIsElite(self):
        return self._getBool(14)

    def setIsElite(self, value):
        self._setBool(14, value)
        return

    def getIsRent(self):
        return self._getBool(15)

    def setIsRent(self, value):
        self._setBool(15, value)
        return

    def getRentDays(self):
        return self._getNumber(16)

    def setRentDays(self, value):
        self._setNumber(16, value)
        return

    def getRentBattles(self):
        return self._getNumber(17)

    def setRentBattles(self, value):
        self._setNumber(17, value)
        return

    def getInInventory(self):
        return self._getBool(18)

    def setInInventory(self, value):
        self._setBool(18, value)
        return

    def getVehicleCD(self):
        return self._getNumber(19)

    def setVehicleCD(self, value):
        self._setNumber(19, value)
        return

    def getCompensatedBonus(self):
        return self._getString(20)

    def setCompensatedBonus(self, value):
        self._setString(20, value)
        return

    def getWasSold(self):
        return self._getBool(21)

    def setWasSold(self, value):
        self._setBool(21, value)
        return

    def getRole(self):
        return self._getString(22)

    def setRole(self, value):
        self._setString(22, value)
        return

    def _initialize(self):
        super(VehicleModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'type')
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'shortVehicleLabel', b'')
        self._addStringProperty(b'nationTag', b'')
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isRent', False)
        self._addNumberProperty(b'rentDays', 0)
        self._addNumberProperty(b'rentBattles', 0)
        self._addBoolProperty(b'inInventory', False)
        self._addNumberProperty(b'vehicleCD', 0)
        self._addStringProperty(b'compensatedBonus', b'')
        self._addBoolProperty(b'wasSold', False)
        self._addStringProperty(b'role', b'')
        return
