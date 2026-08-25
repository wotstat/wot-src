from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class VehicleType(Enum):
    HEAVY = b'heavyTank'
    MEDIUM = b'mediumTank'
    LIGHT = b'lightTank'
    SPG = b'SPG'
    ATSPG = b'AT-SPG'


class BonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=20, commands=0):
        super(BonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(9)

    def setId(self, value):
        self._setNumber(9, value)
        return

    def getStyleID(self):
        return self._getNumber(10)

    def setStyleID(self, value):
        self._setNumber(10, value)
        return

    def getCount(self):
        return self._getNumber(11)

    def setCount(self, value):
        self._setNumber(11, value)
        return

    def getOverlayType(self):
        return self._getString(12)

    def setOverlayType(self, value):
        self._setString(12, value)
        return

    def getDescription(self):
        return self._getString(13)

    def setDescription(self, value):
        self._setString(13, value)
        return

    def getType(self):
        return VehicleType(self._getString(14))

    def setType(self, value):
        self._setString(14, value.value)
        return

    def getLevel(self):
        return self._getNumber(15)

    def setLevel(self, value):
        self._setNumber(15, value)
        return

    def getIsElite(self):
        return self._getBool(16)

    def setIsElite(self, value):
        self._setBool(16, value)
        return

    def getIsRent(self):
        return self._getBool(17)

    def setIsRent(self, value):
        self._setBool(17, value)
        return

    def getIsInHangar(self):
        return self._getBool(18)

    def setIsInHangar(self, value):
        self._setBool(18, value)
        return

    def getVehicleShortName(self):
        return self._getString(19)

    def setVehicleShortName(self, value):
        self._setString(19, value)
        return

    def _initialize(self):
        super(BonusModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'styleID', 0)
        self._addNumberProperty(b'count', 0)
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'type')
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isRent', False)
        self._addBoolProperty(b'isInHangar', False)
        self._addStringProperty(b'vehicleShortName', b'')
        return
