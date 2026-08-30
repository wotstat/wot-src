from enum import Enum
from frameworks.wulf import Array, ViewModel
from comp7_light.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel

class ErrorReason(Enum):
    DEFAULT = b'vehicleUnavailable'
    NOT_BOUGHT_VEHICLES = b'vehicleAvailableForBuy'
    CAN_RECOVER_VEHICLES = b'vehicleAvailableForRestore'


class NoVehiclesScreenModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(NoVehiclesScreenModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def scheduleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getScheduleInfoType():
        return ScheduleInfoModel

    def getVehicleLevels(self):
        return self._getArray(1)

    def setVehicleLevels(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getVehicleLevelsType():
        return int

    def getErrorReason(self):
        return ErrorReason(self._getString(2))

    def setErrorReason(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(NoVehiclesScreenModel, self)._initialize()
        self._addViewModelProperty(b'scheduleInfo', ScheduleInfoModel())
        self._addArrayProperty(b'vehicleLevels', Array())
        self._addStringProperty(b'errorReason')
        self.onClose = self._addCommand(b'onClose')
        return
