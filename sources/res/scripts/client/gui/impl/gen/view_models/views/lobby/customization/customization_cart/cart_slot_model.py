from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_compound_price_model import UserCompoundPriceModel

class CartSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=20, commands=0):
        super(CartSlotModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return UserCompoundPriceModel

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def getTypeId(self):
        return self._getNumber(2)

    def setTypeId(self, value):
        self._setNumber(2, value)
        return

    def getLocked(self):
        return self._getBool(3)

    def setLocked(self, value):
        self._setBool(3, value)
        return

    def getSelected(self):
        return self._getBool(4)

    def setSelected(self, value):
        self._setBool(4, value)
        return

    def getIsFromStorage(self):
        return self._getBool(5)

    def setIsFromStorage(self, value):
        self._setBool(5, value)
        return

    def getIcon(self):
        return self._getString(6)

    def setIcon(self, value):
        self._setString(6, value)
        return

    def getQuantity(self):
        return self._getNumber(7)

    def setQuantity(self, value):
        self._setNumber(7, value)
        return

    def getTooltipId(self):
        return self._getString(8)

    def setTooltipId(self, value):
        self._setString(8, value)
        return

    def getIsWide(self):
        return self._getBool(9)

    def setIsWide(self, value):
        self._setBool(9, value)
        return

    def getIsDim(self):
        return self._getBool(10)

    def setIsDim(self, value):
        self._setBool(10, value)
        return

    def getFormFactor(self):
        return self._getString(11)

    def setFormFactor(self, value):
        self._setString(11, value)
        return

    def getCustomizationDisplayType(self):
        return self._getNumber(12)

    def setCustomizationDisplayType(self, value):
        self._setNumber(12, value)
        return

    def getIsSpecial(self):
        return self._getBool(13)

    def setIsSpecial(self, value):
        self._setBool(13, value)
        return

    def getShowUnsupportedAlert(self):
        return self._getBool(14)

    def setShowUnsupportedAlert(self, value):
        self._setBool(14, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(15)

    def setProgressionLevel(self, value):
        self._setNumber(15, value)
        return

    def getIsProgressionRewindEnabled(self):
        return self._getBool(16)

    def setIsProgressionRewindEnabled(self, value):
        self._setBool(16, value)
        return

    def getIsEdited(self):
        return self._getBool(17)

    def setIsEdited(self, value):
        self._setBool(17, value)
        return

    def getIsStyle(self):
        return self._getBool(18)

    def setIsStyle(self, value):
        self._setBool(18, value)
        return

    def getRarity(self):
        return self._getString(19)

    def setRarity(self, value):
        self._setString(19, value)
        return

    def _initialize(self):
        super(CartSlotModel, self)._initialize()
        self._addViewModelProperty(b'price', UserCompoundPriceModel())
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'typeId', 0)
        self._addBoolProperty(b'locked', False)
        self._addBoolProperty(b'selected', True)
        self._addBoolProperty(b'isFromStorage', False)
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'quantity', 0)
        self._addStringProperty(b'tooltipId', b'')
        self._addBoolProperty(b'isWide', False)
        self._addBoolProperty(b'isDim', False)
        self._addStringProperty(b'formFactor', b'')
        self._addNumberProperty(b'customizationDisplayType', 1)
        self._addBoolProperty(b'isSpecial', False)
        self._addBoolProperty(b'showUnsupportedAlert', False)
        self._addNumberProperty(b'progressionLevel', 0)
        self._addBoolProperty(b'isProgressionRewindEnabled', False)
        self._addBoolProperty(b'isEdited', False)
        self._addBoolProperty(b'isStyle', False)
        self._addStringProperty(b'rarity', b'')
        return
