from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class VehicleInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(VehicleInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsElite(self):
        return self._getBool(0)

    def setIsElite(self, value):
        self._setBool(0, value)
        return

    def getVehicleName(self):
        return self._getString(1)

    def setVehicleName(self, value):
        self._setString(1, value)
        return

    def getVehicleShortName(self):
        return self._getString(2)

    def setVehicleShortName(self, value):
        self._setString(2, value)
        return

    def getVehicleNation(self):
        return self._getString(3)

    def setVehicleNation(self, value):
        self._setString(3, value)
        return

    def getVehicleType(self):
        return self._getString(4)

    def setVehicleType(self, value):
        self._setString(4, value)
        return

    def getVehicleLvl(self):
        return self._getNumber(5)

    def setVehicleLvl(self, value):
        self._setNumber(5, value)
        return

    def getIsPremiumIGR(self):
        return self._getBool(6)

    def setIsPremiumIGR(self, value):
        self._setBool(6, value)
        return

    def getTags(self):
        return self._getArray(7)

    def setTags(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getTagsType():
        return unicode

    def getVehicleTechName(self):
        return self._getString(8)

    def setVehicleTechName(self, value):
        self._setString(8, value)
        return

    def getVehicleCD(self):
        return self._getNumber(9)

    def setVehicleCD(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(VehicleInfoModel, self)._initialize()
        self._addBoolProperty(b'isElite', True)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleShortName', b'')
        self._addStringProperty(b'vehicleNation', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'vehicleLvl', 0)
        self._addBoolProperty(b'isPremiumIGR', False)
        self._addArrayProperty(b'tags', Array())
        self._addStringProperty(b'vehicleTechName', b'')
        self._addNumberProperty(b'vehicleCD', 0)
        return
