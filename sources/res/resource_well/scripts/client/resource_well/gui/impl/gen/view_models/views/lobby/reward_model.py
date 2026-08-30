from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class RewardState(Enum):
    ACTIVE = b'ACTIVE'
    NOT_AVAILABLE = b'NOT_AVAILABLE'
    ALREADY_IN_GARAGE = b'ALREADY_IN_GARAGE'
    ALREADY_RECEIVED = b'ALREADY_RECEIVED'
    SOLD_OUT = b'SOLD_OUT'
    COUNT_NOT_AVAILABLE = b'COUNT_NOT_AVAILABLE'


class RewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(RewardModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getRewardId(self):
        return self._getString(1)

    def setRewardId(self, value):
        self._setString(1, value)
        return

    def getHasStyle(self):
        return self._getBool(2)

    def setHasStyle(self, value):
        self._setBool(2, value)
        return

    def getVehiclesLeftCount(self):
        return self._getNumber(3)

    def setVehiclesLeftCount(self, value):
        self._setNumber(3, value)
        return

    def getVehiclesLimit(self):
        return self._getNumber(4)

    def setVehiclesLimit(self, value):
        self._setNumber(4, value)
        return

    def getPersonalNumber(self):
        return self._getString(5)

    def setPersonalNumber(self, value):
        self._setString(5, value)
        return

    def getState(self):
        return RewardState(self._getString(6))

    def setState(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(RewardModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addStringProperty(b'rewardId', b'')
        self._addBoolProperty(b'hasStyle', False)
        self._addNumberProperty(b'vehiclesLeftCount', 0)
        self._addNumberProperty(b'vehiclesLimit', 0)
        self._addStringProperty(b'personalNumber', b'')
        self._addStringProperty(b'state')
        return
