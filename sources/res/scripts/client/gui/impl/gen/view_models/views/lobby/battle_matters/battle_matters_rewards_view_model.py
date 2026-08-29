from enum import Enum, IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_vehicle_model import BattleMattersVehicleModel

class State(IntEnum):
    REGULAR = 0
    INTERMEDIATE = 1
    TOKEN = 2
    TOKENVEHICLE = 3
    FINAL = 4


class RewardViewsSequenceNumber(IntEnum):
    SINGLE = 0
    FIRST = 1
    MIDDLE = 2
    LAST = 3


class RewardType(Enum):
    REGULAR = b'regular'
    INTERMEDIATE = b'intermediate'
    VEHICLE = b'vehicle'


class BattleMattersRewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onNextTask', b'onShowVehicle', b'onChooseVehicle')
    ARG_REWARD_TYPE = b'type'
    ARG_REWARD_INDEX = b'tooltipId'
    ARG_REWARD_TOKEN = b'rewardToken'

    def __init__(self, properties=6, commands=4):
        super(BattleMattersRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getNumber(0))

    def setState(self, value):
        self._setNumber(0, value.value)
        return

    def getRewardViewsSequenceNumber(self):
        return RewardViewsSequenceNumber(self._getNumber(1))

    def setRewardViewsSequenceNumber(self, value):
        self._setNumber(1, value.value)
        return

    def getQuestNumber(self):
        return self._getNumber(2)

    def setQuestNumber(self, value):
        self._setNumber(2, value)
        return

    def getVehicles(self):
        return self._getArray(3)

    def setVehicles(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getVehiclesType():
        return BattleMattersVehicleModel

    def getRegularRewards(self):
        return self._getArray(4)

    def setRegularRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRegularRewardsType():
        return ItemBonusModel

    def getIntermediateRewards(self):
        return self._getArray(5)

    def setIntermediateRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getIntermediateRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(BattleMattersRewardsViewModel, self)._initialize()
        self._addNumberProperty(b'state')
        self._addNumberProperty(b'rewardViewsSequenceNumber')
        self._addNumberProperty(b'questNumber', 0)
        self._addArrayProperty(b'vehicles', Array())
        self._addArrayProperty(b'regularRewards', Array())
        self._addArrayProperty(b'intermediateRewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onNextTask = self._addCommand(b'onNextTask')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        self.onChooseVehicle = self._addCommand(b'onChooseVehicle')
        return
