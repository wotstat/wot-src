from frameworks.wulf import ViewModel

class VehicleItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleItemViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getIsElite(self):
        return self._getBool(1)

    def setIsElite(self, value):
        self._setBool(1, value)
        return

    def getIsIGR(self):
        return self._getBool(2)

    def setIsIGR(self, value):
        self._setBool(2, value)
        return

    def getType(self):
        return self._getString(3)

    def setType(self, value):
        self._setString(3, value)
        return

    def getName(self):
        return self._getString(4)

    def setName(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(VehicleItemViewModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isIGR', False)
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'name', b'')
        return
