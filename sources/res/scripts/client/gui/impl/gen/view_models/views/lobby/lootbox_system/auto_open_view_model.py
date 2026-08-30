from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.reward_row_model import RewardRowModel

class AutoOpenViewModel(ViewModel):
    __slots__ = (b'onClose', b'onPreview')

    def __init__(self, properties=3, commands=2):
        super(AutoOpenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEventName(self):
        return self._getString(0)

    def setEventName(self, value):
        self._setString(0, value)
        return

    def getBoxesQuantity(self):
        return self._getNumber(1)

    def setBoxesQuantity(self, value):
        self._setNumber(1, value)
        return

    def getRewardRows(self):
        return self._getArray(2)

    def setRewardRows(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardRowsType():
        return RewardRowModel

    def _initialize(self):
        super(AutoOpenViewModel, self)._initialize()
        self._addStringProperty(b'eventName', b'')
        self._addNumberProperty(b'boxesQuantity', 0)
        self._addArrayProperty(b'rewardRows', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onPreview = self._addCommand(b'onPreview')
        return
