from gui.impl.gen import R
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel

class BuySellItemsDialogModel(FullScreenDialogWindowModel):
    __slots__ = ()

    def __init__(self, properties=24, commands=3):
        super(BuySellItemsDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getBackgroundImg(self):
        return self._getResource(11)

    def setBackgroundImg(self, value):
        self._setResource(11, value)
        return

    def getDescription(self):
        return self._getResource(12)

    def setDescription(self, value):
        self._setResource(12, value)
        return

    def getUpperDescription(self):
        return self._getResource(13)

    def setUpperDescription(self, value):
        self._setResource(13, value)
        return

    def getLowerDescription(self):
        return self._getResource(14)

    def setLowerDescription(self, value):
        self._setResource(14, value)
        return

    def getIsAlert(self):
        return self._getBool(15)

    def setIsAlert(self, value):
        self._setBool(15, value)
        return

    def getCurrencyType(self):
        return self._getString(16)

    def setCurrencyType(self, value):
        self._setString(16, value)
        return

    def getItemPrice(self):
        return self._getNumber(17)

    def setItemPrice(self, value):
        self._setNumber(17, value)
        return

    def getItemCount(self):
        return self._getNumber(18)

    def setItemCount(self, value):
        self._setNumber(18, value)
        return

    def getItemMaxCount(self):
        return self._getNumber(19)

    def setItemMaxCount(self, value):
        self._setNumber(19, value)
        return

    def getItemMinCount(self):
        return self._getNumber(20)

    def setItemMinCount(self, value):
        self._setNumber(20, value)
        return

    def getItemTotalPrice(self):
        return self._getNumber(21)

    def setItemTotalPrice(self, value):
        self._setNumber(21, value)
        return

    def getTooltipMsg(self):
        return self._getString(22)

    def setTooltipMsg(self, value):
        self._setString(22, value)
        return

    def getSpecialType(self):
        return self._getString(23)

    def setSpecialType(self, value):
        self._setString(23, value)
        return

    def _initialize(self):
        super(BuySellItemsDialogModel, self)._initialize()
        self._addResourceProperty(b'backgroundImg', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addResourceProperty(b'upperDescription', R.invalid())
        self._addResourceProperty(b'lowerDescription', R.invalid())
        self._addBoolProperty(b'isAlert', False)
        self._addStringProperty(b'currencyType', b'')
        self._addNumberProperty(b'itemPrice', 0)
        self._addNumberProperty(b'itemCount', 1)
        self._addNumberProperty(b'itemMaxCount', 1)
        self._addNumberProperty(b'itemMinCount', 1)
        self._addNumberProperty(b'itemTotalPrice', 0)
        self._addStringProperty(b'tooltipMsg', b'')
        self._addStringProperty(b'specialType', b'')
        return
