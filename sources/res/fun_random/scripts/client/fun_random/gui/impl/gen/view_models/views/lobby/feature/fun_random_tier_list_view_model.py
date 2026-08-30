from frameworks.wulf import Array, ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_lootbox import FunRandomLootbox

class FunRandomTierListViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=2, commands=1):
        super(FunRandomTierListViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLootBoxes(self):
        return self._getArray(0)

    def setLootBoxes(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getLootBoxesType():
        return FunRandomLootbox

    def getAssetsPointer(self):
        return self._getString(1)

    def setAssetsPointer(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(FunRandomTierListViewModel, self)._initialize()
        self._addArrayProperty(b'lootBoxes', Array())
        self._addStringProperty(b'assetsPointer', b'undefined')
        self.onClose = self._addCommand(b'onClose')
        return
