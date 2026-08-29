from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_rewards_vehicle_model import ArmoryYardRewardsVehicleModel

class State(Enum):
    STAGE = b'stage'
    STYLE = b'style'
    SHOP = b'shop'


class ArmoryYardRewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onShowVehicle')
    ARG_REWARD_INDEX = b'tooltipId'
    MAX_REWARDS = 10

    def __init__(self, properties=8, commands=2):
        super(ArmoryYardRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getStages(self):
        return self._getNumber(1)

    def setStages(self, value):
        self._setNumber(1, value)
        return

    def getHasAllRewards(self):
        return self._getBool(2)

    def setHasAllRewards(self, value):
        self._setBool(2, value)
        return

    def getIsAciveState(self):
        return self._getBool(3)

    def setIsAciveState(self, value):
        self._setBool(3, value)
        return

    def getIsFinalReward(self):
        return self._getBool(4)

    def setIsFinalReward(self, value):
        self._setBool(4, value)
        return

    def getVehicles(self):
        return self._getArray(5)

    def setVehicles(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getVehiclesType():
        return ArmoryYardRewardsVehicleModel

    def getMainRewards(self):
        return self._getArray(6)

    def setMainRewards(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getMainRewardsType():
        return ItemBonusModel

    def getRewards(self):
        return self._getArray(7)

    def setRewards(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(ArmoryYardRewardsViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'stages', 0)
        self._addBoolProperty(b'hasAllRewards', False)
        self._addBoolProperty(b'isAciveState', False)
        self._addBoolProperty(b'isFinalReward', False)
        self._addArrayProperty(b'vehicles', Array())
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        return
