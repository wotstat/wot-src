from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.resource_well.vehicle_counter_model import VehicleCounterModel

class NoSerialVehiclesConfirmModel(ViewModel):
    __slots__ = (b'confirm', b'cancel', b'close')

    def __init__(self, properties=2, commands=3):
        super(NoSerialVehiclesConfirmModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleCounter(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleCounterType():
        return VehicleCounterModel

    def getVehicleName(self):
        return self._getString(1)

    def setVehicleName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(NoSerialVehiclesConfirmModel, self)._initialize()
        self._addViewModelProperty(b'vehicleCounter', VehicleCounterModel())
        self._addStringProperty(b'vehicleName', b'')
        self.confirm = self._addCommand(b'confirm')
        self.cancel = self._addCommand(b'cancel')
        self.close = self._addCommand(b'close')
        return
