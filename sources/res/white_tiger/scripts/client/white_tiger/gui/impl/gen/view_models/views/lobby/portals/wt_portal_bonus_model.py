from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class VehicleType(Enum):
    HEAVY = b'heavyTank'
    MEDIUM = b'mediumTank'
    LIGHT = b'lightTank'
    SPG = b'SPG'
    ATSPG = b'AT-SPG'


class WtPortalBonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(WtPortalBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCollected(self):
        return self._getBool(8)

    def setIsCollected(self, value):
        self._setBool(8, value)
        return

    def getIsCustom(self):
        return self._getBool(9)

    def setIsCustom(self, value):
        self._setBool(9, value)
        return

    def getIsSpecial(self):
        return self._getBool(10)

    def setIsSpecial(self, value):
        self._setBool(10, value)
        return

    def getName(self):
        return self._getString(11)

    def setName(self, value):
        self._setString(11, value)
        return

    def getVehicleLvl(self):
        return self._getNumber(12)

    def setVehicleLvl(self, value):
        self._setNumber(12, value)
        return

    def getVehicleCD(self):
        return self._getNumber(13)

    def setVehicleCD(self, value):
        self._setNumber(13, value)
        return

    def getStyleCD(self):
        return self._getNumber(14)

    def setStyleCD(self, value):
        self._setNumber(14, value)
        return

    def getVehicleType(self):
        return VehicleType(self._getString(15))

    def setVehicleType(self, value):
        self._setString(15, value.value)
        return

    def _initialize(self):
        super(WtPortalBonusModel, self)._initialize()
        self._addBoolProperty(b'isCollected', False)
        self._addBoolProperty(b'isCustom', False)
        self._addBoolProperty(b'isSpecial', False)
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'vehicleLvl', 0)
        self._addNumberProperty(b'vehicleCD', 0)
        self._addNumberProperty(b'styleCD', 0)
        self._addStringProperty(b'vehicleType')
        return
