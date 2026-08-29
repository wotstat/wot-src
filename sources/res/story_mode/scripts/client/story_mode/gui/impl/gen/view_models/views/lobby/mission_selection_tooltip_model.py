from gui.impl.gen import R
from frameworks.wulf import ViewModel

class MissionSelectionTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MissionSelectionTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getResource(0)

    def setVehicleName(self, value):
        self._setResource(0, value)
        return

    def getVehicleIcon(self):
        return self._getResource(1)

    def setVehicleIcon(self, value):
        self._setResource(1, value)
        return

    def getVehicleDescription(self):
        return self._getResource(2)

    def setVehicleDescription(self, value):
        self._setResource(2, value)
        return

    def _initialize(self):
        super(MissionSelectionTooltipModel, self)._initialize()
        self._addResourceProperty(b'vehicleName', R.invalid())
        self._addResourceProperty(b'vehicleIcon', R.invalid())
        self._addResourceProperty(b'vehicleDescription', R.invalid())
        return
