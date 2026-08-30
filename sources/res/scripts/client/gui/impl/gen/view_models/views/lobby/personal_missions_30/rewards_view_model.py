from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class RewardsViewType(Enum):
    VEHICLE_PART = b'vehiclePart'
    OPERATION_WITH_HONORS = b'operationWithHonors'
    CAMPAIGN_WITH_HONORS = b'campaignWithHonors'
    OPERATION = b'operation'


class RewardsViewModel(ViewModel):
    __slots__ = (b'close', b'goToOperation', b'goToVehicle', b'disableVideoOverlaySound')
    ARG_REWARD_INDEX = b'tooltipId'

    def __init__(self, properties=8, commands=4):
        super(RewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return VehicleInfoModel

    def getType(self):
        return RewardsViewType(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def getVehicleDetailName(self):
        return self._getString(3)

    def setVehicleDetailName(self, value):
        self._setString(3, value)
        return

    def getCampaignName(self):
        return self._getString(4)

    def setCampaignName(self, value):
        self._setString(4, value)
        return

    def getOperationName(self):
        return self._getString(5)

    def setOperationName(self, value):
        self._setString(5, value)
        return

    def getNextOperationName(self):
        return self._getString(6)

    def setNextOperationName(self, value):
        self._setString(6, value)
        return

    def getOperationId(self):
        return self._getNumber(7)

    def setOperationId(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(RewardsViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicle', VehicleInfoModel())
        self._addStringProperty(b'type')
        self._addArrayProperty(b'rewards', Array())
        self._addStringProperty(b'vehicleDetailName', b'')
        self._addStringProperty(b'campaignName', b'')
        self._addStringProperty(b'operationName', b'')
        self._addStringProperty(b'nextOperationName', b'')
        self._addNumberProperty(b'operationId', 0)
        self.close = self._addCommand(b'close')
        self.goToOperation = self._addCommand(b'goToOperation')
        self.goToVehicle = self._addCommand(b'goToVehicle')
        self.disableVideoOverlaySound = self._addCommand(b'disableVideoOverlaySound')
        return
