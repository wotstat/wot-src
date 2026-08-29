from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class CustomizationBonusModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(CustomizationBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getCustomizationID(self):
        return self._getNumber(9)

    def setCustomizationID(self, value):
        self._setNumber(9, value)
        return

    def getStyleCD(self):
        return self._getNumber(10)

    def setStyleCD(self, value):
        self._setNumber(10, value)
        return

    def getItem(self):
        return self._getString(11)

    def setItem(self, value):
        self._setString(11, value)
        return

    def getIcon(self):
        return self._getString(12)

    def setIcon(self, value):
        self._setString(12, value)
        return

    def _initialize(self):
        super(CustomizationBonusModel, self)._initialize()
        self._addNumberProperty(b'customizationID', 0)
        self._addNumberProperty(b'styleCD', 0)
        self._addStringProperty(b'item', b'')
        self._addStringProperty(b'icon', b'')
        return
