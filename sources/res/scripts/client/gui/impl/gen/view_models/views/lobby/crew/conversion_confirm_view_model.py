from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel

class ConversionConfirmViewModel(ViewModel):
    __slots__ = (b'onConfirm', b'onShowTankman', b'onClose', b'onCancel')

    def __init__(self, properties=2, commands=4):
        super(ConversionConfirmViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTankmanAmount(self):
        return self._getNumber(0)

    def setTankmanAmount(self, value):
        self._setNumber(0, value)
        return

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def _initialize(self):
        super(ConversionConfirmViewModel, self)._initialize()
        self._addNumberProperty(b'tankmanAmount', 0)
        self._addArrayProperty(b'rewards', Array())
        self.onConfirm = self._addCommand(b'onConfirm')
        self.onShowTankman = self._addCommand(b'onShowTankman')
        self.onClose = self._addCommand(b'onClose')
        self.onCancel = self._addCommand(b'onCancel')
        return
