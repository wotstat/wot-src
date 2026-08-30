from frameworks.wulf import ViewModel

class VehicleBtnModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehicleBtnModel, self).__init__(properties=properties, commands=commands)
        return

    def getFlag(self):
        return self._getString(0)

    def setFlag(self, value):
        self._setString(0, value)
        return

    def getVehType(self):
        return self._getString(1)

    def setVehType(self, value):
        self._setString(1, value)
        return

    def getVehLvl(self):
        return self._getString(2)

    def setVehLvl(self, value):
        self._setString(2, value)
        return

    def getVehIcon(self):
        return self._getString(3)

    def setVehIcon(self, value):
        self._setString(3, value)
        return

    def getVehName(self):
        return self._getString(4)

    def setVehName(self, value):
        self._setString(4, value)
        return

    def getVisible(self):
        return self._getBool(5)

    def setVisible(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(VehicleBtnModel, self)._initialize()
        self._addStringProperty(b'flag', b'')
        self._addStringProperty(b'vehType', b'')
        self._addStringProperty(b'vehLvl', b'')
        self._addStringProperty(b'vehIcon', b'')
        self._addStringProperty(b'vehName', b'')
        self._addBoolProperty(b'visible', False)
        return
