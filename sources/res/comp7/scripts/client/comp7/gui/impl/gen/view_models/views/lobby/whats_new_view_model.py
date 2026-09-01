from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class WhatsNewViewModel(ViewModel):
    __slots__ = (b'onClose', b'onVideoOpen')

    def __init__(self, properties=2, commands=2):
        super(WhatsNewViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def scheduleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getScheduleInfoType():
        return ScheduleInfoModel

    def getRentalVehicles(self):
        return self._getArray(1)

    def setRentalVehicles(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRentalVehiclesType():
        return VehicleModel

    def _initialize(self):
        super(WhatsNewViewModel, self)._initialize()
        self._addViewModelProperty(b'scheduleInfo', ScheduleInfoModel())
        self._addArrayProperty(b'rentalVehicles', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onVideoOpen = self._addCommand(b'onVideoOpen')
        return
