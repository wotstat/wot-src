from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class VehicleType(Enum):
    HEAVY = b'heavyTank'
    MEDIUM = b'mediumTank'
    LIGHT = b'lightTank'
    SPG = b'SPG'
    ATSPG = b'AT-SPG'


class RewardBonusModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=0):
        super(RewardBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return VehicleType(self._getString(9))

    def setType(self, value):
        self._setString(9, value.value)
        return

    def getLevel(self):
        return self._getNumber(10)

    def setLevel(self, value):
        self._setNumber(10, value)
        return

    def getVehicleName(self):
        return self._getString(11)

    def setVehicleName(self, value):
        self._setString(11, value)
        return

    def getNationTag(self):
        return self._getString(12)

    def setNationTag(self, value):
        self._setString(12, value)
        return

    def getIsElite(self):
        return self._getBool(13)

    def setIsElite(self, value):
        self._setBool(13, value)
        return

    def getIsRent(self):
        return self._getBool(14)

    def setIsRent(self, value):
        self._setBool(14, value)
        return

    def getRentDays(self):
        return self._getNumber(15)

    def setRentDays(self, value):
        self._setNumber(15, value)
        return

    def getRentBattles(self):
        return self._getNumber(16)

    def setRentBattles(self, value):
        self._setNumber(16, value)
        return

    def getCompensatedBonus(self):
        return self._getString(17)

    def setCompensatedBonus(self, value):
        self._setString(17, value)
        return

    def getIcon(self):
        return self._getString(18)

    def setIcon(self, value):
        self._setString(18, value)
        return

    def _initialize(self):
        super(RewardBonusModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'nationTag', b'')
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isRent', False)
        self._addNumberProperty(b'rentDays', 0)
        self._addNumberProperty(b'rentBattles', 0)
        self._addStringProperty(b'compensatedBonus', b'')
        self._addStringProperty(b'icon', b'')
        return
