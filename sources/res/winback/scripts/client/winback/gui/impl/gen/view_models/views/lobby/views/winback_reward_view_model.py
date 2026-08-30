from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class RewardWindowType(Enum):
    WELCOME = b'welcome'
    PROGRESSION_STEP = b'progressionStep'
    SELECTED_REWARDS = b'selectedRewards'
    PROGRESSION_COMPLETED = b'progressionCompleted'


class RewardName(Enum):
    VEHICLE_FOR_GIFT = b'vehicleForGift'
    VEHICLE_DISCOUNT = b'vehicleDiscount'
    VEHICLE_FOR_RENT = b'vehicleForRent'
    SELECTABLE_VEHICLE_FOR_GIFT = b'selectableVehicleForGift'
    SELECTABLE_VEHICLE_DISCOUNT = b'selectableVehicleDiscount'


class WinbackRewardViewModel(ViewModel):
    __slots__ = (b'onSelectReward', b'onClose', b'showInHangar', b'showQuests')
    ARG_TOOLTIP_ID = b'tooltipId'

    def __init__(self, properties=5, commands=4):
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

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def getStageNumber(self):
        return self._getNumber(3)

    def setStageNumber(self, value):
        self._setNumber(3, value)
        return

    def getProgressionName(self):
        return self._getString(4)

    def setProgressionName(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(WinbackRewardViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isFirstProgressionStep', False)
        self._addArrayProperty(b'rewards', Array())
        self._addNumberProperty(b'stageNumber', 0)
        self._addStringProperty(b'progressionName', b'')
        self.onSelectReward = self._addCommand(b'onSelectReward')
        self.onClose = self._addCommand(b'onClose')
        self.showInHangar = self._addCommand(b'showInHangar')
        self.showQuests = self._addCommand(b'showQuests')
        return
