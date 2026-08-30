from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_reward_item_model import Pm3RewardItemModel

class OperationState(Enum):
    COMPLETEWITHHONOR = b'completeWithHonor'
    COMPLETE = b'complete'
    COMPANYCOMPLETE = b'companyComplete'


class PersonalMissionsVideoRewardsViewModel(VehicleInfoModel):
    __slots__ = (b'onClose', b'onError', b'onShowVehicle', b'onVideoStarted')

    def __init__(self, properties=15, commands=4):
        super(PersonalMissionsVideoRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsWindowAccessible(self):
        return self._getBool(10)

    def setIsWindowAccessible(self, value):
        self._setBool(10, value)
        return

    def getVideoName(self):
        return self._getString(11)

    def setVideoName(self, value):
        self._setString(11, value)
        return

    def getIsFinalPm3Rewards(self):
        return self._getBool(12)

    def setIsFinalPm3Rewards(self, value):
        self._setBool(12, value)
        return

    def getState(self):
        return OperationState(self._getString(13))

    def setState(self, value):
        self._setString(13, value.value)
        return

    def getRewards(self):
        return self._getArray(14)

    def setRewards(self, value):
        self._setArray(14, value)
        return

    @staticmethod
    def getRewardsType():
        return Pm3RewardItemModel

    def _initialize(self):
        super(PersonalMissionsVideoRewardsViewModel, self)._initialize()
        self._addBoolProperty(b'isWindowAccessible', True)
        self._addStringProperty(b'videoName', b'')
        self._addBoolProperty(b'isFinalPm3Rewards', False)
        self._addStringProperty(b'state')
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onError = self._addCommand(b'onError')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        self.onVideoStarted = self._addCommand(b'onVideoStarted')
        return
