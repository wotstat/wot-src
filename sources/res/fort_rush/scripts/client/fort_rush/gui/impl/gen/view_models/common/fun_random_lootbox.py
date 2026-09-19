from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class FunRandomLootbox(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FunRandomLootbox, self).__init__(properties=properties, commands=commands)
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

    def getShowRewardsNames(self):
        return self._getBool(2)

    def setShowRewardsNames(self, value):
        self._setBool(2, value)
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
        super(FunRandomLootbox, self)._initialize()
        self._addStringProperty(b'label', b'')
        self._addStringProperty(b'iconKey', b'')
        self._addBoolProperty(b'showRewardsNames', False)
        self._addArrayProperty(b'rewards', Array())
        return
