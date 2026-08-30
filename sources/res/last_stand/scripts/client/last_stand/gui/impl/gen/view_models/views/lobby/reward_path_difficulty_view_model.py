from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class RewardPathDifficultyViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(RewardPathDifficultyViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getIsLocked(self):
        return self._getBool(1)

    def setIsLocked(self, value):
        self._setBool(1, value)
        return

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)
        return

    def getIsCompleted(self):
        return self._getBool(3)

    def setIsCompleted(self, value):
        self._setBool(3, value)
        return

    def getAggregatedRewards(self):
        return self._getArray(4)

    def setAggregatedRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getAggregatedRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(RewardPathDifficultyViewModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isLocked', False)
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isCompleted', False)
        self._addArrayProperty(b'aggregatedRewards', Array())
        return
