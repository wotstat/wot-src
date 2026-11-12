from frameworks.wulf import ViewModel

class BuyToyViewModel(ViewModel):
    __slots__ = (b'onClose', b'onBuy')

    def __init__(self, properties=4, commands=2):
        super(BuyToyViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getToyName(self):
        return self._getString(0)

    def setToyName(self, value):
        self._setString(0, value)
        return

    def getToyIcon(self):
        return self._getString(1)

    def setToyIcon(self, value):
        self._setString(1, value)
        return

    def getCost(self):
        return self._getNumber(2)

    def setCost(self, value):
        self._setNumber(2, value)
        return

    def getIsBuyBtnDisable(self):
        return self._getBool(3)

    def setIsBuyBtnDisable(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(BuyToyViewModel, self)._initialize()
        self._addStringProperty(b'toyName', b'')
        self._addStringProperty(b'toyIcon', b'')
        self._addNumberProperty(b'cost', 0)
        self._addBoolProperty(b'isBuyBtnDisable', True)
        self.onClose = self._addCommand(b'onClose')
        self.onBuy = self._addCommand(b'onBuy')
        return
