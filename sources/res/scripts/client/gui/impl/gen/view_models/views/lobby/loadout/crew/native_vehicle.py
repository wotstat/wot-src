from frameworks.wulf import ViewModel

class NativeVehicle(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NativeVehicle, self).__init__(properties=properties, commands=commands)
        return

    def getShortName(self):
        return self._getString(0)

    def setShortName(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getTier(self):
        return self._getNumber(2)

    def setTier(self, value):
        self._setNumber(2, value)
        return

    def getNation(self):
        return self._getString(3)

    def setNation(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(NativeVehicle, self)._initialize()
        self._addStringProperty(b'shortName', b'')
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'tier', 0)
        self._addStringProperty(b'nation', b'')
        return
