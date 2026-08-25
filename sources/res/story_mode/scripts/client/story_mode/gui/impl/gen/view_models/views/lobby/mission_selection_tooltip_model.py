from frameworks.wulf import ViewModel
from gui.impl.gen import R

class MissionSelectionTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MissionSelectionTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)
        return

    def getVehicleIcon(self):
        return self._getResource(1)

    def setVehicleIcon(self, value):
        self._setResource(1, value)
        return

    def getVehicleDescription(self):
        return self._getString(2)

    def setVehicleDescription(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(MissionSelectionTooltipModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addResourceProperty(b'vehicleIcon', R.invalid())
        self._addStringProperty(b'vehicleDescription', b'')
        return
