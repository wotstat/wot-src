from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class TemplateType(Enum):
    VEHICLE = b'vehicle'
    BUNDLE = b'bundle'
    OTHER = b'other'
    MAINTAIN = b'maintain'
    CUSTOMIZATION = b'customization'
    ECONOMICBOOSTER = b'economicBooster'


class ArmoryYardShopItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=21, commands=0):
        super(ArmoryYardShopItem, self).__init__(properties=properties, commands=commands)
        return

    def getItemID(self):
        return self._getNumber(0)

    def setItemID(self, value):
        self._setNumber(0, value)
        return

    def getItemType(self):
        return self._getString(1)

    def setItemType(self, value):
        self._setString(1, value)
        return

    def getImage(self):
        return self._getString(2)

    def setImage(self, value):
        self._setString(2, value)
        return

    def getLargeImage(self):
        return self._getString(3)

    def setLargeImage(self, value):
        self._setString(3, value)
        return

    def getNationFlagIcon(self):
        return self._getString(4)

    def setNationFlagIcon(self, value):
        self._setString(4, value)
        return

    def getTitle(self):
        return self._getString(5)

    def setTitle(self, value):
        self._setString(5, value)
        return

    def getSpecializations(self):
        return self._getArray(6)

    def setSpecializations(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getSpecializationsType():
        return unicode

    def getCount(self):
        return self._getNumber(7)

    def setCount(self, value):
        self._setNumber(7, value)
        return

    def getLimit(self):
        return self._getNumber(8)

    def setLimit(self, value):
        self._setNumber(8, value)
        return

    def getAvailable(self):
        return self._getBool(9)

    def setAvailable(self, value):
        self._setBool(9, value)
        return

    def getExtraParams(self):
        return self._getArray(10)

    def setExtraParams(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getExtraParamsType():
        return unicode

    def getDescription(self):
        return self._getString(11)

    def setDescription(self, value):
        self._setString(11, value)
        return

    def getLongDescription(self):
        return self._getString(12)

    def setLongDescription(self, value):
        self._setString(12, value)
        return

    def getAdditionalInfo(self):
        return self._getString(13)

    def setAdditionalInfo(self, value):
        self._setString(13, value)
        return

    def getIsOnlyArmoryCoins(self):
        return self._getBool(14)

    def setIsOnlyArmoryCoins(self, value):
        self._setBool(14, value)
        return

    def getVehicleType(self):
        return self._getString(15)

    def setVehicleType(self, value):
        self._setString(15, value)
        return

    def getVehicleLevel(self):
        return self._getString(16)

    def setVehicleLevel(self, value):
        self._setString(16, value)
        return

    def getVehicleRoleName(self):
        return self._getString(17)

    def setVehicleRoleName(self, value):
        self._setString(17, value)
        return

    def getCoinsCost(self):
        return self._getNumber(18)

    def setCoinsCost(self, value):
        self._setNumber(18, value)
        return

    def getTemplate(self):
        return TemplateType(self._getString(19))

    def setTemplate(self, value):
        self._setString(19, value.value)
        return

    def getEffect(self):
        return self._getString(20)

    def setEffect(self, value):
        self._setString(20, value)
        return

    def _initialize(self):
        super(ArmoryYardShopItem, self)._initialize()
        self._addNumberProperty(b'itemID', 0)
        self._addStringProperty(b'itemType', b'')
        self._addStringProperty(b'image', b'')
        self._addStringProperty(b'largeImage', b'')
        self._addStringProperty(b'nationFlagIcon', b'')
        self._addStringProperty(b'title', b'')
        self._addArrayProperty(b'specializations', Array())
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'limit', 0)
        self._addBoolProperty(b'available', False)
        self._addArrayProperty(b'extraParams', Array())
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'longDescription', b'')
        self._addStringProperty(b'additionalInfo', b'')
        self._addBoolProperty(b'isOnlyArmoryCoins', False)
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleLevel', b'')
        self._addStringProperty(b'vehicleRoleName', b'')
        self._addNumberProperty(b'coinsCost', 0)
        self._addStringProperty(b'template')
        self._addStringProperty(b'effect', b'')
        return
