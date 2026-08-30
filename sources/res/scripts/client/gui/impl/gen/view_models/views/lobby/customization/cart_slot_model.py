from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class CartSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=24, commands=0):
        super(CartSlotModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def buyPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getBuyPriceType():
        return PriceModel

    def getItemID(self):
        return self._getNumber(1)

    def setItemID(self, value):
        self._setNumber(1, value)
        return

    def getIntCD(self):
        return self._getNumber(2)

    def setIntCD(self, value):
        self._setNumber(2, value)
        return

    def getExtraName(self):
        return self._getString(3)

    def setExtraName(self, value):
        self._setString(3, value)
        return

    def getIsMainType(self):
        return self._getBool(4)

    def setIsMainType(self, value):
        self._setBool(4, value)
        return

    def getIsWithSerialNumber(self):
        return self._getBool(5)

    def setIsWithSerialNumber(self, value):
        self._setBool(5, value)
        return

    def getIsRental(self):
        return self._getBool(6)

    def setIsRental(self, value):
        self._setBool(6, value)
        return

    def getRentalInfoText(self):
        return self._getString(7)

    def setRentalInfoText(self, value):
        self._setString(7, value)
        return

    def getAutoRentEnabled(self):
        return self._getBool(8)

    def setAutoRentEnabled(self, value):
        self._setBool(8, value)
        return

    def getTypeId(self):
        return self._getNumber(9)

    def setTypeId(self, value):
        self._setNumber(9, value)
        return

    def getIsSelected(self):
        return self._getBool(10)

    def setIsSelected(self, value):
        self._setBool(10, value)
        return

    def getIsDisabled(self):
        return self._getBool(11)

    def setIsDisabled(self, value):
        self._setBool(11, value)
        return

    def getIsFromStorage(self):
        return self._getBool(12)

    def setIsFromStorage(self, value):
        self._setBool(12, value)
        return

    def getIcon(self):
        return self._getString(13)

    def setIcon(self, value):
        self._setString(13, value)
        return

    def getQuantity(self):
        return self._getNumber(14)

    def setQuantity(self, value):
        self._setNumber(14, value)
        return

    def getTooltip(self):
        return self._getString(15)

    def setTooltip(self, value):
        self._setString(15, value)
        return

    def getIsWide(self):
        return self._getBool(16)

    def setIsWide(self, value):
        self._setBool(16, value)
        return

    def getIsDim(self):
        return self._getBool(17)

    def setIsDim(self, value):
        self._setBool(17, value)
        return

    def getCustomizationDisplayType(self):
        return self._getNumber(18)

    def setCustomizationDisplayType(self, value):
        self._setNumber(18, value)
        return

    def getIsSpecial(self):
        return self._getBool(19)

    def setIsSpecial(self, value):
        self._setBool(19, value)
        return

    def getShowAlert(self):
        return self._getBool(20)

    def setShowAlert(self, value):
        self._setBool(20, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(21)

    def setProgressionLevel(self, value):
        self._setNumber(21, value)
        return

    def getIsProgressionRewindEnabled(self):
        return self._getBool(22)

    def setIsProgressionRewindEnabled(self, value):
        self._setBool(22, value)
        return

    def getIsEdited(self):
        return self._getBool(23)

    def setIsEdited(self, value):
        self._setBool(23, value)
        return

    def _initialize(self):
        super(CartSlotModel, self)._initialize()
        self._addViewModelProperty(b'buyPrice', PriceModel())
        self._addNumberProperty(b'itemID', 0)
        self._addNumberProperty(b'intCD', 0)
        self._addStringProperty(b'extraName', b'')
        self._addBoolProperty(b'isMainType', False)
        self._addBoolProperty(b'isWithSerialNumber', False)
        self._addBoolProperty(b'isRental', False)
        self._addStringProperty(b'rentalInfoText', b'')
        self._addBoolProperty(b'autoRentEnabled', False)
        self._addNumberProperty(b'typeId', 0)
        self._addBoolProperty(b'isSelected', True)
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'isFromStorage', False)
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'quantity', 0)
        self._addStringProperty(b'tooltip', b'')
        self._addBoolProperty(b'isWide', False)
        self._addBoolProperty(b'isDim', False)
        self._addNumberProperty(b'customizationDisplayType', 1)
        self._addBoolProperty(b'isSpecial', False)
        self._addBoolProperty(b'showAlert', False)
        self._addNumberProperty(b'progressionLevel', -1)
        self._addBoolProperty(b'isProgressionRewindEnabled', False)
        self._addBoolProperty(b'isEdited', False)
        return
