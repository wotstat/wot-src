from frameworks.wulf import ViewModel

class VehicleItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehicleItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleType(self):
        return self._getString(0)

    def setVehicleType(self, value):
        self._setString(0, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(1)

    def setVehicleLevel(self, value):
        self._setNumber(1, value)
        return

    def getVehicleName(self):
        return self._getString(2)

    def setVehicleName(self, value):
        self._setString(2, value)
        return

    def getVehicleBonus(self):
        return self._getNumber(3)

    def setVehicleBonus(self, value):
        self._setNumber(3, value)
        return

    def getVehicleTop(self):
        return self._getNumber(4)

    def setVehicleTop(self, value):
        self._setNumber(4, value)
        return

    def getTextResourceID(self):
        return self._getNumber(5)

    def setTextResourceID(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(VehicleItemModel, self)._initialize()
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addStringProperty(b'vehicleName', b'')
        self._addNumberProperty(b'vehicleBonus', 0)
        self._addNumberProperty(b'vehicleTop', 0)
        self._addNumberProperty(b'textResourceID', 0)
        return
