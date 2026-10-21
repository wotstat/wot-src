from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.tooltips.vehicle_crew import VehicleCrew
from portal.gui.impl.gen.view_models.views.lobby.tooltips.vehicle_ttx import VehicleTtx

class VehicleTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleTtx(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleTtxType():
        return VehicleTtx

    @property
    def vehicleCrew(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleCrewType():
        return VehicleCrew

    def getVehicleName(self):
        return self._getString(2)

    def setVehicleName(self, value):
        self._setString(2, value)
        return

    def getVehicleType(self):
        return self._getString(3)

    def setVehicleType(self, value):
        self._setString(3, value)
        return

    def getVehicleDescription(self):
        return self._getString(4)

    def setVehicleDescription(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(VehicleTooltipModel, self)._initialize()
        self._addViewModelProperty(b'vehicleTtx', VehicleTtx())
        self._addViewModelProperty(b'vehicleCrew', VehicleCrew())
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleDescription', b'')
        return
