from frameworks.wulf import ViewModel

class PurchaseDialogModel(ViewModel):
    __slots__ = (b'onAccept', b'onCancel')

    def __init__(self, properties=7, commands=2):
        super(PurchaseDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getDayId(self):
        return self._getNumber(0)

    def setDayId(self, value):
        self._setNumber(0, value)
        return

    def getIsWalletAvailable(self):
        return self._getBool(1)

    def setIsWalletAvailable(self, value):
        self._setBool(1, value)
        return

    def getCurrentResource(self):
        return self._getString(2)

    def setCurrentResource(self, value):
        self._setString(2, value)
        return

    def getBalanceCurrencyValue(self):
        return self._getNumber(3)

    def setBalanceCurrencyValue(self, value):
        self._setNumber(3, value)
        return

    def getPrice(self):
        return self._getNumber(4)

    def setPrice(self, value):
        self._setNumber(4, value)
        return

    def getNotEnoughResource(self):
        return self._getBool(5)

    def setNotEnoughResource(self, value):
        self._setBool(5, value)
        return

    def getCurrencyTooltipId(self):
        return self._getString(6)

    def setCurrencyTooltipId(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(PurchaseDialogModel, self)._initialize()
        self._addNumberProperty(b'dayId', 0)
        self._addBoolProperty(b'isWalletAvailable', True)
        self._addStringProperty(b'currentResource', b'')
        self._addNumberProperty(b'balanceCurrencyValue', 0)
        self._addNumberProperty(b'price', 0)
        self._addBoolProperty(b'notEnoughResource', False)
        self._addStringProperty(b'currencyTooltipId', b'')
        self.onAccept = self._addCommand(b'onAccept')
        self.onCancel = self._addCommand(b'onCancel')
        return
