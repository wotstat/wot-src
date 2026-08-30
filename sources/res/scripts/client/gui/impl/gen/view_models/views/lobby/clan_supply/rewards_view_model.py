from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class RewardingType(IntEnum):
    COMMON = 0
    ELITE = 1
    ELITE_WITH_VEHICLE = 2


class RewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onGoToHangar')

    def __init__(self, properties=3, commands=2):
        super(RewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return RewardingType(self._getNumber(0))

    def setType(self, value):
        self._setNumber(0, value.value)
        return

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def getAdditionalRewards(self):
        return self._getArray(2)

    def setAdditionalRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getAdditionalRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(RewardsViewModel, self)._initialize()
        self._addNumberProperty(b'type')
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'additionalRewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onGoToHangar = self._addCommand(b'onGoToHangar')
        return
