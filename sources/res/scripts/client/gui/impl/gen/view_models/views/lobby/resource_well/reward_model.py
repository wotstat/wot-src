from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class RewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(RewardModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getIsTop(self):
        return self._getBool(1)

    def setIsTop(self, value):
        self._setBool(1, value)
        return

    def getVehiclesLeftCount(self):
        return self._getNumber(2)

    def setVehiclesLeftCount(self, value):
        self._setNumber(2, value)
        return

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)
        return

    def getIsCountAvailable(self):
        return self._getBool(4)

    def setIsCountAvailable(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(RewardModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addBoolProperty(b'isTop', False)
        self._addNumberProperty(b'vehiclesLeftCount', 0)
        self._addBoolProperty(b'isEnabled', False)
        self._addBoolProperty(b'isCountAvailable', False)
        return
