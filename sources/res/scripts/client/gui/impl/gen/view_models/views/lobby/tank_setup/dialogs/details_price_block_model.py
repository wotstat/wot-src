from frameworks.wulf import ViewModel

class DetailsPriceBlockModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(DetailsPriceBlockModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrencyName(self):
        return self._getString(0)

    def setCurrencyName(self, value):
        self._setString(0, value)
        return

    def getCountDevice(self):
        return self._getNumber(1)

    def setCountDevice(self, value):
        self._setNumber(1, value)
        return

    def getPriceDevice(self):
        return self._getNumber(2)

    def setPriceDevice(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(DetailsPriceBlockModel, self)._initialize()
        self._addStringProperty(b'currencyName', b'')
        self._addNumberProperty(b'countDevice', 0)
        self._addNumberProperty(b'priceDevice', 0)
        return
