from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class RewardItemModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(RewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(10)

    def setIcon(self, value):
        self._setString(10, value)
        return

    def getType(self):
        return self._getString(11)

    def setType(self, value):
        self._setString(11, value)
        return

    def _initialize(self):
        super(RewardItemModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'type', b'')
        return
