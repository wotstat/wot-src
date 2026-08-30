from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class RewardScreenViewModel(ViewModel):
    __slots__ = (b'onClose', b'onNarrative')

    def __init__(self, properties=4, commands=2):
        super(RewardScreenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getAssetsPointer(self):
        return self._getString(0)

    def setAssetsPointer(self, value):
        self._setString(0, value)
        return

    def getMainRewards(self):
        return self._getArray(1)

    def setMainRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getMainRewardsType():
        return ItemBonusModel

    def getAdditionalRewards(self):
        return self._getArray(2)

    def setAdditionalRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getAdditionalRewardsType():
        return ItemBonusModel

    def getHasCompleted(self):
        return self._getBool(3)

    def setHasCompleted(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(RewardScreenViewModel, self)._initialize()
        self._addStringProperty(b'assetsPointer', b'')
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'additionalRewards', Array())
        self._addBoolProperty(b'hasCompleted', False)
        self.onClose = self._addCommand(b'onClose')
        self.onNarrative = self._addCommand(b'onNarrative')
        return
