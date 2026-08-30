from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_rewards_vehicle_model import ArmoryYardRewardsVehicleModel

class RewardType(Enum):
    COMMON = b'common'
    PROGRESSION = b'progression'
    POSTPROGRESSION = b'postProgression'


class ArmoryYardLevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ArmoryYardLevelModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getRewardType(self):
        return RewardType(self._getString(1))

    def setRewardType(self, value):
        self._setString(1, value.value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return ArmoryYardRewardsVehicleModel

    def _initialize(self):
        super(ArmoryYardLevelModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'rewardType', RewardType.COMMON.value)
        self._addArrayProperty(b'rewards', Array())
        return
