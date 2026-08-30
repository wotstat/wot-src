from frameworks.wulf import Array, ViewModel

class DeconstructFromVehicleTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DeconstructFromVehicleTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getEquipmentName(self):
        return self._getString(0)

    def setEquipmentName(self, value):
        self._setString(0, value)
        return

    def getVehicleNames(self):
        return self._getArray(1)

    def setVehicleNames(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getVehicleNamesType():
        return unicode

    def _initialize(self):
        super(DeconstructFromVehicleTooltipModel, self)._initialize()
        self._addStringProperty(b'equipmentName', b'')
        self._addArrayProperty(b'vehicleNames', Array())
        return
