from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class AwardViewModel(ViewModel):
    __slots__ = (b'showInHangar', b'close')

    def __init__(self, properties=3, commands=2):
        super(AwardViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getPersonalNumber(self):
        return self._getString(1)

    def setPersonalNumber(self, value):
        self._setString(1, value)
        return

    def getRewardIndex(self):
        return self._getNumber(2)

    def setRewardIndex(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(AwardViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addStringProperty(b'personalNumber', b'')
        self._addNumberProperty(b'rewardIndex', 0)
        self.showInHangar = self._addCommand(b'showInHangar')
        self.close = self._addCommand(b'close')
        return
