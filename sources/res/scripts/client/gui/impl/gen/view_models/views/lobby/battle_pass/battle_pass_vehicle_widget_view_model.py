from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class BattlePassVehicleWidgetViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattlePassVehicleWidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getIsPaidReward(self):
        return self._getBool(1)

    def setIsPaidReward(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(BattlePassVehicleWidgetViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addBoolProperty(b'isPaidReward', False)
        return
