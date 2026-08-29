from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class EliteViewModel(ViewModel):
    __slots__ = (b'onGoToPostProgression', b'onClose')

    def __init__(self, properties=2, commands=2):
        super(EliteViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getIsPostProgressionExists(self):
        return self._getBool(1)

    def setIsPostProgressionExists(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(EliteViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addBoolProperty(b'isPostProgressionExists', False)
        self.onGoToPostProgression = self._addCommand(b'onGoToPostProgression')
        self.onClose = self._addCommand(b'onClose')
        return
