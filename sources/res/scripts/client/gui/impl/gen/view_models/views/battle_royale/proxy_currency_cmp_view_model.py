from frameworks.wulf import ViewModel

class ProxyCurrencyCmpViewModel(ViewModel):
    __slots__ = (b'onGotoShopBtnClicked',)

    def __init__(self, properties=1, commands=1):
        super(ProxyCurrencyCmpViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBalance(self):
        return self._getNumber(0)

    def setBalance(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(ProxyCurrencyCmpViewModel, self)._initialize()
        self._addNumberProperty(b'balance', 0)
        self.onGotoShopBtnClicked = self._addCommand(b'onGotoShopBtnClicked')
        return
