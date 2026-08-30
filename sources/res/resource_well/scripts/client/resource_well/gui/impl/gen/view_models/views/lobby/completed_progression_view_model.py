from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class CompletedProgressionViewModel(ViewModel):
    __slots__ = (b'onViewLoaded', b'onClose', b'onShowVehicle', b'onAboutClick')

    def __init__(self, properties=3, commands=4):
        super(CompletedProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getHasStyle(self):
        return self._getBool(1)

    def setHasStyle(self, value):
        self._setBool(1, value)
        return

    def getPersonalNumber(self):
        return self._getString(2)

    def setPersonalNumber(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(CompletedProgressionViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addBoolProperty(b'hasStyle', False)
        self._addStringProperty(b'personalNumber', b'')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onClose = self._addCommand(b'onClose')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        self.onAboutClick = self._addCommand(b'onAboutClick')
        return
