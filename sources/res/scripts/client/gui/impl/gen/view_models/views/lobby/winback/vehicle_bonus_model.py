from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class VehicleBonusModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=0):
        super(VehicleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsElite(self):
        return self._getBool(10)

    def setIsElite(self, value):
        self._setBool(10, value)
        return

    def getIsFromStorage(self):
        return self._getBool(11)

    def setIsFromStorage(self, value):
        self._setBool(11, value)
        return

    def getVehicleName(self):
        return self._getString(12)

    def setVehicleName(self, value):
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

    def getNation(self):
        return self._getString(15)

    def setNation(self, value):
        self._setString(15, value)
        return

    def getVehicleLvl(self):
        return self._getNumber(16)

    def setVehicleLvl(self, value):
        self._setNumber(16, value)
        return

    def getPriceDiscount(self):
        return self._getNumber(17)

    def setPriceDiscount(self, value):
        self._setNumber(17, value)
        return

    def getExpDiscount(self):
        return self._getNumber(18)

    def setExpDiscount(self, value):
        self._setNumber(18, value)
        return

    def _initialize(self):
        super(VehicleBonusModel, self)._initialize()
        self._addBoolProperty(b'isElite', True)
        self._addBoolProperty(b'isFromStorage', False)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'nation', b'')
        self._addNumberProperty(b'vehicleLvl', 0)
        self._addNumberProperty(b'priceDiscount', 0)
        self._addNumberProperty(b'expDiscount', 0)
        return
