from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class FunRandomLootBoxTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FunRandomLootBoxTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabel(self):
        return self._getString(0)

    def setLabel(self, value):
        self._setString(0, value)
        return

    def getIconKey(self):
        return self._getString(1)

    def setIconKey(self, value):
        self._setString(1, value)
        return

    def getAssetsPointer(self):
        return self._getString(2)

    def setAssetsPointer(self, value):
        self._setString(2, value)
        return

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(FunRandomLootBoxTooltipViewModel, self)._initialize()
        self._addStringProperty(b'label', b'')
        self._addStringProperty(b'iconKey', b'')
        self._addStringProperty(b'assetsPointer', b'undefined')
        self._addArrayProperty(b'rewards', Array())
        return
