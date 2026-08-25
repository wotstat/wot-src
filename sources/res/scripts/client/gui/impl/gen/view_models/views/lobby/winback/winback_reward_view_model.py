from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class RewardWindowType(Enum):
    WELCOME = b'welcome'
    PROGRESSION_STEP = b'progressionStep'
    SELECTED_REWARDS = b'selectedRewards'
    WINBACK_PROGRESSION_COMPLETED = b'winbackProgressionCompleted'
    REGULAR_PROGRESSION_COMPLETED = b'regularProgressionCompleted'


class RewardName(Enum):
    VEHICLE_FOR_GIFT = b'vehicleForGift'
    VEHICLE_DISCOUNT = b'vehicleDiscount'
    VEHICLE_FOR_RENT = b'vehicleForRent'
    SELECTABLE_VEHICLE_FOR_GIFT = b'selectableVehicleForGift'
    SELECTABLE_VEHICLE_DISCOUNT = b'selectableVehicleDiscount'


class WinbackRewardViewModel(ViewModel):
    __slots__ = (b'onSelectReward', b'onClose', b'showInHangar', b'showQuests')
    ARG_TOOLTIP_ID = b'tooltipId'

    def __init__(self, properties=4, commands=4):
        super(WinbackRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return RewardWindowType(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getIsFirstProgressionStep(self):
        return self._getBool(1)

    def setIsFirstProgressionStep(self, value):
        self._setBool(1, value)
        return

    def getIsSelectableAwardAvailable(self):
        return self._getBool(2)

    def setIsSelectableAwardAvailable(self, value):
        self._setBool(2, value)
        return

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(WinbackRewardViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isFirstProgressionStep', False)
        self._addBoolProperty(b'isSelectableAwardAvailable', False)
        self._addArrayProperty(b'rewards', Array())
        self.onSelectReward = self._addCommand(b'onSelectReward')
        self.onClose = self._addCommand(b'onClose')
        self.showInHangar = self._addCommand(b'showInHangar')
        self.showQuests = self._addCommand(b'showQuests')
        return
