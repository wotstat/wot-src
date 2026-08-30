from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class ExtraIntroViewModel(ViewModel):
    __slots__ = (b'onViewLoaded', b'onClose')

    def __init__(self, properties=2, commands=2):
        super(ExtraIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getStyleName(self):
        return self._getString(1)

    def setStyleName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(ExtraIntroViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addStringProperty(b'styleName', b'')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onClose = self._addCommand(b'onClose')
        return
