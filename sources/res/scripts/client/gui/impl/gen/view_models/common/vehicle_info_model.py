from frameworks.wulf import ViewModel

class VehicleInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(VehicleInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleId(self):
        return self._getNumber(0)

    def setVehicleId(self, value):
        self._setNumber(0, value)
        return

    def getInventoryId(self):
        return self._getNumber(1)

    def setInventoryId(self, value):
        self._setNumber(1, value)
        return

    def getIsElite(self):
        return self._getBool(2)

    def setIsElite(self, value):
        self._setBool(2, value)
        return

    def getIsPremium(self):
        return self._getBool(3)

    def setIsPremium(self, value):
        self._setBool(3, value)
        return

    def getVehicleName(self):
        return self._getString(4)

    def setVehicleName(self, value):
        self._setString(4, value)
        return

    def getVehicleShortName(self):
        return self._getString(5)

    def setVehicleShortName(self, value):
        self._setString(5, value)
        return

    def getVehicleLongName(self):
        return self._getString(6)

    def setVehicleLongName(self, value):
        self._setString(6, value)
        return

    def getVehicleNation(self):
        return self._getString(7)

    def setVehicleNation(self, value):
        self._setString(7, value)
        return

    def getVehicleType(self):
        return self._getString(8)

    def setVehicleType(self, value):
        self._setString(8, value)
        return

    def getVehicleRole(self):
        return self._getNumber(9)

    def setVehicleRole(self, value):
        self._setNumber(9, value)
        return

    def getVehicleLvl(self):
        return self._getNumber(10)

    def setVehicleLvl(self, value):
        self._setNumber(10, value)
        return

    def getTags(self):
        return self._getString(11)

    def setTags(self, value):
        self._setString(11, value)
        return

    def getRentLeftTime(self):
        return self._getNumber(12)

    def setRentLeftTime(self, value):
        self._setNumber(12, value)
        return

    def getRentLeftBattles(self):
        return self._getNumber(13)

    def setRentLeftBattles(self, value):
        self._setNumber(13, value)
        return

    def getRentLeftWins(self):
        return self._getNumber(14)

    def setRentLeftWins(self, value):
        self._setNumber(14, value)
        return

    def getState(self):
        return self._getString(15)

    def setState(self, value):
        self._setString(15, value)
        return

    def getFromWotPlus(self):
        return self._getBool(16)

    def setFromWotPlus(self, value):
        self._setBool(16, value)
        return

    def _initialize(self):
        super(VehicleInfoModel, self)._initialize()
        self._addNumberProperty(b'vehicleId', 0)
        self._addNumberProperty(b'inventoryId', 0)
        self._addBoolProperty(b'isElite', True)
        self._addBoolProperty(b'isPremium', False)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleShortName', b'')
        self._addStringProperty(b'vehicleLongName', b'')
        self._addStringProperty(b'vehicleNation', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'vehicleRole', 0)
        self._addNumberProperty(b'vehicleLvl', 0)
        self._addStringProperty(b'tags', b'')
        self._addNumberProperty(b'rentLeftTime', 0)
        self._addNumberProperty(b'rentLeftBattles', 0)
        self._addNumberProperty(b'rentLeftWins', 0)
        self._addStringProperty(b'state', b'')
        self._addBoolProperty(b'fromWotPlus', False)
        return
