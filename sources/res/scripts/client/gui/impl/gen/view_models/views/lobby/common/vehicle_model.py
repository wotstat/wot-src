from frameworks.wulf import ViewModel

class VehicleModel(ViewModel):
    __slots__ = ()
    USSR = b'ussr'
    GERMANY = b'germany'
    USA = b'usa'
    CHINA = b'china'
    FRANCE = b'france'
    UK = b'uk'
    JAPAN = b'japan'
    CZECH = b'czech'
    SWEDEN = b'sweden'
    POLAND = b'poland'
    ITALY = b'italy'
    LIGHT_TANK = b'lightTank'
    MEDIUM_TANK = b'mediumTank'
    HEAVY_TANK = b'heavyTank'
    SPG = b'SPG'
    AT_SPG = b'AT-SPG'
    PREMIUM_TAG = b'premium'
    SPECIAL = b'special'
    EARN_CRYSTALS = b'earn_crystals'
    PREMIUM_IGR_TAG = b'premiumIGR'
    WOT_PLUS_TAG = b'wotPlus'
    COLLECTOR_VEHICLES_TAG = b'collectorVehicle'

    def __init__(self, properties=10, commands=0):
        super(VehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getLongName(self):
        return self._getString(1)

    def setLongName(self, value):
        self._setString(1, value)
        return

    def getTechName(self):
        return self._getString(2)

    def setTechName(self, value):
        self._setString(2, value)
        return

    def getTier(self):
        return self._getNumber(3)

    def setTier(self, value):
        self._setNumber(3, value)
        return

    def getType(self):
        return self._getString(4)

    def setType(self, value):
        self._setString(4, value)
        return

    def getIsPremium(self):
        return self._getBool(5)

    def setIsPremium(self, value):
        self._setBool(5, value)
        return

    def getTags(self):
        return self._getString(6)

    def setTags(self, value):
        self._setString(6, value)
        return

    def getNation(self):
        return self._getString(7)

    def setNation(self, value):
        self._setString(7, value)
        return

    def getRoleKey(self):
        return self._getString(8)

    def setRoleKey(self, value):
        self._setString(8, value)
        return

    def getVehicleCD(self):
        return self._getNumber(9)

    def setVehicleCD(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(VehicleModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'longName', b'')
        self._addStringProperty(b'techName', b'')
        self._addNumberProperty(b'tier', 0)
        self._addStringProperty(b'type', b'')
        self._addBoolProperty(b'isPremium', False)
        self._addStringProperty(b'tags', b'')
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'roleKey', b'')
        self._addNumberProperty(b'vehicleCD', 0)
        return
