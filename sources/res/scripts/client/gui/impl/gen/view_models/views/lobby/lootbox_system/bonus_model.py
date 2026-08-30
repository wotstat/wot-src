from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.compensation_model import CompensationModel

class VehicleType(Enum):
    HEAVY = b'heavyTank'
    MEDIUM = b'mediumTank'
    LIGHT = b'lightTank'
    SPG = b'SPG'
    ATSPG = b'AT-SPG'


class BonusRarity(Enum):
    COMMON = b'common'
    RARE = b'rare'
    EPIC = b'epic'


class BonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=26, commands=0):
        super(BonusModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def compensation(self):
        return self._getViewModel(9)

    @staticmethod
    def getCompensationType():
        return CompensationModel

    def getName(self):
        return self._getString(10)

    def setName(self, value):
        self._setString(10, value)
        return

    def getId(self):
        return self._getNumber(11)

    def setId(self, value):
        self._setNumber(11, value)
        return

    def getStyleID(self):
        return self._getNumber(12)

    def setStyleID(self, value):
        self._setNumber(12, value)
        return

    def getCount(self):
        return self._getNumber(13)

    def setCount(self, value):
        self._setNumber(13, value)
        return

    def getOverlayType(self):
        return self._getString(14)

    def setOverlayType(self, value):
        self._setString(14, value)
        return

    def getDescription(self):
        return self._getString(15)

    def setDescription(self, value):
        self._setString(15, value)
        return

    def getType(self):
        return VehicleType(self._getString(16))

    def setType(self, value):
        self._setString(16, value.value)
        return

    def getLevel(self):
        return self._getNumber(17)

    def setLevel(self, value):
        self._setNumber(17, value)
        return

    def getIsElite(self):
        return self._getBool(18)

    def setIsElite(self, value):
        self._setBool(18, value)
        return

    def getIsWheeled(self):
        return self._getBool(19)

    def setIsWheeled(self, value):
        self._setBool(19, value)
        return

    def getIsRent(self):
        return self._getBool(20)

    def setIsRent(self, value):
        self._setBool(20, value)
        return

    def getIsInHangar(self):
        return self._getBool(21)

    def setIsInHangar(self, value):
        self._setBool(21, value)
        return

    def getRarity(self):
        return BonusRarity(self._getString(22))

    def setRarity(self, value):
        self._setString(22, value.value)
        return

    def getSpecialAwardName(self):
        return self._getString(23)

    def setSpecialAwardName(self, value):
        self._setString(23, value)
        return

    def getVehicleShortName(self):
        return self._getString(24)

    def setVehicleShortName(self, value):
        self._setString(24, value)
        return

    def getVehicle3DStyleName(self):
        return self._getString(25)

    def setVehicle3DStyleName(self, value):
        self._setString(25, value)
        return

    def _initialize(self):
        super(BonusModel, self)._initialize()
        self._addViewModelProperty(b'compensation', CompensationModel())
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'styleID', 0)
        self._addNumberProperty(b'count', 0)
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'type')
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isWheeled', False)
        self._addBoolProperty(b'isRent', False)
        self._addBoolProperty(b'isInHangar', False)
        self._addStringProperty(b'rarity')
        self._addStringProperty(b'specialAwardName', b'')
        self._addStringProperty(b'vehicleShortName', b'')
        self._addStringProperty(b'vehicle3DStyleName', b'')
        return
