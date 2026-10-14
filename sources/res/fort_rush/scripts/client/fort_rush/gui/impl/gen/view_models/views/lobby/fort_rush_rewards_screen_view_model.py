from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class FortRushRewardsScreenViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=2, commands=1):
        super(FortRushRewardsScreenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def getIsCompleted(self):
        return self._getBool(1)

    def setIsCompleted(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(FortRushRewardsScreenViewModel, self)._initialize()
        self._addArrayProperty(b'rewards', Array())
        self._addBoolProperty(b'isCompleted', False)
        self.onClose = self._addCommand(b'onClose')
        return
