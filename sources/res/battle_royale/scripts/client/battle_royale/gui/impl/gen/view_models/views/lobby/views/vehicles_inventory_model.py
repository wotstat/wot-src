from frameworks.wulf import Map, ViewModel

class VehiclesInventoryModel(ViewModel):
    __slots__ = (b'onSelect',)
    NO_VEHICLE_ID = -1

    def __init__(self, properties=3, commands=1):
        super(VehiclesInventoryModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentVehicleIntCD(self):
        return self._getNumber(0)

    def setCurrentVehicleIntCD(self, value):
        self._setNumber(0, value)
        return

    def getCurrentVehicleInventoryId(self):
        return self._getNumber(1)

    def setCurrentVehicleInventoryId(self, value):
        self._setNumber(1, value)
        return

    def getVehicles(self):
        return self._getMap(2)

    def setVehicles(self, value):
        self._setMap(2, value)
        return

    @staticmethod
    def getVehiclesType():
        return (unicode, unicode)

    def _initialize(self):
        super(VehiclesInventoryModel, self)._initialize()
        self._addNumberProperty(b'currentVehicleIntCD', -1)
        self._addNumberProperty(b'currentVehicleInventoryId', -1)
        self._addMapProperty(b'vehicles', Map(unicode, unicode))
        self.onSelect = self._addCommand(b'onSelect')
        return
