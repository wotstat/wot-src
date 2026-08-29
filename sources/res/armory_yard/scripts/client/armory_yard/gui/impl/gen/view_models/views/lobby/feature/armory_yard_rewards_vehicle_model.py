from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class ArmoryYardRewardsVehicleModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=27, commands=0):
        super(ArmoryYardRewardsVehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getIndex(self):
        return self._getNumber(9)

    def setIndex(self, value):
        self._setNumber(9, value)
        return

    def getVehicleImg(self):
        return self._getString(10)

    def setVehicleImg(self, value):
        self._setString(10, value)
        return

    def getTooltipId(self):
        return self._getString(11)

    def setTooltipId(self, value):
        self._setString(11, value)
        return

    def getTooltipContentId(self):
        return self._getString(12)

    def setTooltipContentId(self, value):
        self._setString(12, value)
        return

    def getVehicleName(self):
        return self._getString(13)

    def setVehicleName(self, value):
        self._setString(13, value)
        return

    def getType(self):
        return self._getString(14)

    def setType(self, value):
        self._setString(14, value)
        return

    def getLevel(self):
        return self._getNumber(15)

    def setLevel(self, value):
        self._setNumber(15, value)
        return

    def getShortVehicleLabel(self):
        return self._getString(16)

    def setShortVehicleLabel(self, value):
        self._setString(16, value)
        return

    def getNationTag(self):
        return self._getString(17)

    def setNationTag(self, value):
        self._setString(17, value)
        return

    def getIsElite(self):
        return self._getBool(18)

    def setIsElite(self, value):
        self._setBool(18, value)
        return

    def getIsRent(self):
        return self._getBool(19)

    def setIsRent(self, value):
        self._setBool(19, value)
        return

    def getRentDays(self):
        return self._getNumber(20)

    def setRentDays(self, value):
        self._setNumber(20, value)
        return

    def getRentBattles(self):
        return self._getNumber(21)

    def setRentBattles(self, value):
        self._setNumber(21, value)
        return

    def getInInventory(self):
        return self._getBool(22)

    def setInInventory(self, value):
        self._setBool(22, value)
        return

    def getVehicleCD(self):
        return self._getNumber(23)

    def setVehicleCD(self, value):
        self._setNumber(23, value)
        return

    def getCompensatedBonus(self):
        return self._getString(24)

    def setCompensatedBonus(self, value):
        self._setString(24, value)
        return

    def getWasSold(self):
        return self._getBool(25)

    def setWasSold(self, value):
        self._setBool(25, value)
        return

    def getRole(self):
        return self._getString(26)

    def setRole(self, value):
        self._setString(26, value)
        return

    def _initialize(self):
        super(ArmoryYardRewardsVehicleModel, self)._initialize()
        self._addNumberProperty(b'index', 0)
        self._addStringProperty(b'vehicleImg', b'')
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'tooltipContentId', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'type', b'')
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
