from frameworks.wulf import ViewModel

class VehicleInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehicleInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getIsPremium(self):
        return self._getBool(3)

    def setIsPremium(self, value):
        self._setBool(3, value)
        return

    def getPrestigeLevel(self):
        return self._getNumber(4)

    def setPrestigeLevel(self, value):
        self._setNumber(4, value)
        return

    def getIsBroken(self):
        return self._getBool(5)

    def setIsBroken(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(VehicleInfoModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isPremium', False)
        self._addNumberProperty(b'prestigeLevel', 0)
        self._addBoolProperty(b'isBroken', False)
        return
