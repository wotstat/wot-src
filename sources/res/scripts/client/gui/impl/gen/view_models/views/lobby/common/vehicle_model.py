from frameworks.wulf import Array
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
    INTUNION = b'intunion'
    LIGHT_TANK = b'lightTank'
    MEDIUM_TANK = b'mediumTank'
    HEAVY_TANK = b'heavyTank'
    SPG = b'SPG'
    AT_SPG = b'AT-SPG'

    def __init__(self, properties=9, commands=0):
        super(VehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getTechName(self):
        return self._getString(1)

    def setTechName(self, value):
        self._setString(1, value)
        return

    def getTier(self):
        return self._getNumber(2)

    def setTier(self, value):
        self._setNumber(2, value)
        return

    def getType(self):
        return self._getString(3)

    def setType(self, value):
        self._setString(3, value)
        return

    def getIsPremium(self):
        return self._getBool(4)

    def setIsPremium(self, value):
        self._setBool(4, value)
        return

    def getTags(self):
        return self._getArray(5)

    def setTags(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getTagsType():
        return unicode

    def getNation(self):
        return self._getString(6)

    def setNation(self, value):
        self._setString(6, value)
        return

    def getRoleKey(self):
        return self._getString(7)

    def setRoleKey(self, value):
        self._setString(7, value)
        return

    def getVehicleCD(self):
        return self._getNumber(8)

    def setVehicleCD(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(VehicleModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'techName', b'')
        self._addNumberProperty(b'tier', 0)
        self._addStringProperty(b'type', b'')
        self._addBoolProperty(b'isPremium', False)
        self._addArrayProperty(b'tags', Array())
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'roleKey', b'')
        self._addNumberProperty(b'vehicleCD', 0)
        return
