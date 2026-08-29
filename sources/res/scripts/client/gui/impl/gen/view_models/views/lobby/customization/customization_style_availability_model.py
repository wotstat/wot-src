from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class CustomizationStyleAvailabilityModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CustomizationStyleAvailabilityModel, self).__init__(properties=properties, commands=commands)
        return

    def getNations(self):
        return self._getArray(0)

    def setNations(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getNationsType():
        return unicode

    def getIsPremium(self):
        return self._getBool(1)

    def setIsPremium(self, value):
        self._setBool(1, value)
        return

    def getIsPremiumIGR(self):
        return self._getBool(2)

    def setIsPremiumIGR(self, value):
        self._setBool(2, value)
        return

    def getLevels(self):
        return self._getArray(3)

    def setLevels(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getLevelsType():
        return unicode

    def getVehTypes(self):
        return self._getArray(4)

    def setVehTypes(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getVehTypesType():
        return unicode

    def getTankNames(self):
        return self._getString(5)

    def setTankNames(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(CustomizationStyleAvailabilityModel, self)._initialize()
        self._addArrayProperty(b'nations', Array())
        self._addBoolProperty(b'isPremium', False)
        self._addBoolProperty(b'isPremiumIGR', False)
        self._addArrayProperty(b'levels', Array())
        self._addArrayProperty(b'vehTypes', Array())
        self._addStringProperty(b'tankNames', b'')
        return
