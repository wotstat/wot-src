from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class VehicleBonusModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(VehicleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsElite(self):
        return self._getBool(9)

    def setIsElite(self, value):
        self._setBool(9, value)
        return

    def getVehicleName(self):
        return self._getString(10)

    def setVehicleName(self, value):
        self._setString(10, value)
        return

    def getUserName(self):
        return self._getString(11)

    def setUserName(self, value):
        self._setString(11, value)
        return

    def getVehicleType(self):
        return self._getString(12)

    def setVehicleType(self, value):
        self._setString(12, value)
        return

    def getNation(self):
        return self._getString(13)

    def setNation(self, value):
        self._setString(13, value)
        return

    def getVehicleLvl(self):
        return self._getNumber(14)

    def setVehicleLvl(self, value):
        self._setNumber(14, value)
        return

    def getPriceDiscount(self):
        return self._getNumber(15)

    def setPriceDiscount(self, value):
        self._setNumber(15, value)
        return

    def getExpDiscount(self):
        return self._getNumber(16)

    def setExpDiscount(self, value):
        self._setNumber(16, value)
        return

    def _initialize(self):
        super(VehicleBonusModel, self)._initialize()
        self._addBoolProperty(b'isElite', True)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'nation', b'')
        self._addNumberProperty(b'vehicleLvl', 0)
        self._addNumberProperty(b'priceDiscount', 0)
        self._addNumberProperty(b'expDiscount', 0)
        return
