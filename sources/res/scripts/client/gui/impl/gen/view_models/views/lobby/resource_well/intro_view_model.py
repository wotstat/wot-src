from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class IntroViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(IntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getTopRewardPlayersCount(self):
        return self._getNumber(1)

    def setTopRewardPlayersCount(self, value):
        self._setNumber(1, value)
        return

    def getRegularRewardVehiclesCount(self):
        return self._getNumber(2)

    def setRegularRewardVehiclesCount(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(IntroViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addNumberProperty(b'topRewardPlayersCount', 0)
        self._addNumberProperty(b'regularRewardVehiclesCount', 0)
        self.onClose = self._addCommand(b'onClose')
        return
