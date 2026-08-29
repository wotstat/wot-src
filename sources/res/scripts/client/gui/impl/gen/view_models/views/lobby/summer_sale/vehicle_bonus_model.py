from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
from gui.impl.gen.view_models.views.lobby.summer_sale.price_model import PriceModel

class VehicleType(Enum):
    HEAVY = b'heavyTank'
    MEDIUM = b'mediumTank'
    LIGHT = b'lightTank'
    SPG = b'SPG'
    ATSPG = b'AT-SPG'


class VehicleBonusModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=24, commands=0):
        super(VehicleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(9)

    @staticmethod
    def getPriceType():
        return PriceModel

    def getVehicleName(self):
        return self._getString(10)

    def setVehicleName(self, value):
        self._setString(10, value)
        return

    def getTechName(self):
        return self._getString(11)

    def setTechName(self, value):
        self._setString(11, value)
        return

    def getType(self):
        return VehicleType(self._getString(12))

    def setType(self, value):
        self._setString(12, value.value)
        return

    def getLevel(self):
        return self._getNumber(13)

    def setLevel(self, value):
        self._setNumber(13, value)
        return

    def getShortVehicleLabel(self):
        return self._getString(14)

    def setShortVehicleLabel(self, value):
        self._setString(14, value)
        return

    def getNationTag(self):
        return self._getString(15)

    def setNationTag(self, value):
        self._setString(15, value)
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

    def getRentDays(self):
        return self._getNumber(18)

    def setRentDays(self, value):
        self._setNumber(18, value)
        return

    def getRentBattles(self):
        return self._getNumber(19)

    def setRentBattles(self, value):
        self._setNumber(19, value)
        return

    def getIntCD(self):
        return self._getNumber(20)

    def setIntCD(self, value):
        self._setNumber(20, value)
        return

    def getInInventory(self):
        return self._getBool(21)

    def setInInventory(self, value):
        self._setBool(21, value)
        return

    def getWasSold(self):
        return self._getBool(22)

    def setWasSold(self, value):
        self._setBool(22, value)
        return

    def getProductCode(self):
        return self._getString(23)

    def setProductCode(self, value):
        self._setString(23, value)
        return

    def _initialize(self):
        super(VehicleBonusModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'techName', b'')
        self._addStringProperty(b'type')
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'shortVehicleLabel', b'')
        self._addStringProperty(b'nationTag', b'')
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isRent', False)
        self._addNumberProperty(b'rentDays', 0)
        self._addNumberProperty(b'rentBattles', 0)
        self._addNumberProperty(b'intCD', 0)
        self._addBoolProperty(b'inInventory', False)
        self._addBoolProperty(b'wasSold', False)
        self._addStringProperty(b'productCode', b'')
        return
