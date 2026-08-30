from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class DifficultyWindowViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(DifficultyWindowViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getModifier(self):
        return self._getNumber(1)

    def setModifier(self, value):
        self._setNumber(1, value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(DifficultyWindowViewModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'modifier', 0)
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        return
