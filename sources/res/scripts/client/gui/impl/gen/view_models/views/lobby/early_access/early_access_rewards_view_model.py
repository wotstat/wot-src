from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class EarlyAccessRewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onShowVehicle')
    ARG_REWARD_INDEX = b'tooltipId'
    MAX_REWARDS = 10

    def __init__(self, properties=3, commands=2):
        super(EarlyAccessRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasAllRewards(self):
        return self._getBool(0)

    def setHasAllRewards(self, value):
        self._setBool(0, value)
        return

    def getMainRewards(self):
        return self._getArray(1)

    def setMainRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getMainRewardsType():
        return ItemBonusModel

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(EarlyAccessRewardsViewModel, self)._initialize()
        self._addBoolProperty(b'hasAllRewards', False)
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        return
