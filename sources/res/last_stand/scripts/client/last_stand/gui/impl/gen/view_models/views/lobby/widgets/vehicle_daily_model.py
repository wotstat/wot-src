from frameworks.wulf import ViewModel

class VehicleDailyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(VehicleDailyModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIsActive(self):
        return self._getBool(1)

    def setIsActive(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(VehicleDailyModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addBoolProperty(b'isActive', False)
        return
