from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.resource_well.loading_resource_model import LoadingResourceModel
from gui.impl.gen.view_models.views.lobby.resource_well.vehicle_counter_model import VehicleCounterModel

class OperationType(IntEnum):
    RETURN = 0
    CONTRIBUTE = 1


class ResourcesLoadingConfirmModel(ViewModel):
    __slots__ = (b'confirm', b'cancel', b'close')

    def __init__(self, properties=4, commands=3):
        super(ResourcesLoadingConfirmModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleCounter(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleCounterType():
        return VehicleCounterModel

    def getOperationType(self):
        return OperationType(self._getNumber(1))

    def setOperationType(self, value):
        self._setNumber(1, value.value)
        return

    def getProgressDiff(self):
        return self._getNumber(2)

    def setProgressDiff(self, value):
        self._setNumber(2, value)
        return

    def getResources(self):
        return self._getArray(3)

    def setResources(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getResourcesType():
        return LoadingResourceModel

    def _initialize(self):
        super(ResourcesLoadingConfirmModel, self)._initialize()
        self._addViewModelProperty(b'vehicleCounter', VehicleCounterModel())
        self._addNumberProperty(b'operationType')
        self._addNumberProperty(b'progressDiff', 0)
        self._addArrayProperty(b'resources', Array())
        self.confirm = self._addCommand(b'confirm')
        self.cancel = self._addCommand(b'cancel')
        self.close = self._addCommand(b'close')
        return
