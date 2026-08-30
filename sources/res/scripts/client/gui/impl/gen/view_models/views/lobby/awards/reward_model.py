from enum import IntEnum
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class RentTypeEnum(IntEnum):
    NONE = 0
    DAYS = 1
    BATTLES = 2
    WINS = 3


class RewardModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=21, commands=0):
        super(RewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getItem(self):
        return self._getString(9)

    def setItem(self, value):
        self._setString(9, value)
        return

    def getIcon(self):
        return self._getString(10)

    def setIcon(self, value):
        self._setString(10, value)
        return

    def getIconSmall(self):
        return self._getString(11)

    def setIconSmall(self, value):
        self._setString(11, value)
        return

    def getIconBig(self):
        return self._getString(12)

    def setIconBig(self, value):
        self._setString(12, value)
        return

    def getUserName(self):
        return self._getString(13)

    def setUserName(self, value):
        self._setString(13, value)
        return

    def getVehicleType(self):
        return self._getString(14)

    def setVehicleType(self, value):
        self._setString(14, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(15)

    def setVehicleLevel(self, value):
        self._setNumber(15, value)
        return

    def getVehicleRentType(self):
        return RentTypeEnum(self._getNumber(16))

    def setVehicleRentType(self, value):
        self._setNumber(16, value.value)
        return

    def getVehicleRentValue(self):
        return self._getNumber(17)

    def setVehicleRentValue(self, value):
        self._setNumber(17, value)
        return

    def getIsFromStorage(self):
        return self._getBool(18)

    def setIsFromStorage(self, value):
        self._setBool(18, value)
        return

    def getIsVehicleOnChoice(self):
        return self._getBool(19)

    def setIsVehicleOnChoice(self, value):
        self._setBool(19, value)
        return

    def getItemID(self):
        return self._getNumber(20)

    def setItemID(self, value):
        self._setNumber(20, value)
        return

    def _initialize(self):
        super(RewardModel, self)._initialize()
        self._addStringProperty(b'item', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'iconSmall', b'')
        self._addStringProperty(b'iconBig', b'')
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addNumberProperty(b'vehicleRentType')
        self._addNumberProperty(b'vehicleRentValue', 0)
        self._addBoolProperty(b'isFromStorage', False)
        self._addBoolProperty(b'isVehicleOnChoice', False)
        self._addNumberProperty(b'itemID', 0)
        return
