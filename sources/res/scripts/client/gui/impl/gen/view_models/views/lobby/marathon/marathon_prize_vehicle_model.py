from frameworks.wulf import ViewModel

class MarathonPrizeVehicleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MarathonPrizeVehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(MarathonPrizeVehicleModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'level', 0)
        return
