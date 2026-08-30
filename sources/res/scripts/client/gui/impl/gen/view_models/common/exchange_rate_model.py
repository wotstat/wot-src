from frameworks.wulf import ViewModel

class ExchangeRateModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ExchangeRateModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrent(self):
        return self._getReal(0)

    def setCurrent(self, value):
        self._setReal(0, value)
        return

    def getDefault(self):
        return self._getReal(1)

    def setDefault(self, value):
        self._setReal(1, value)
        return

    def getDiscount(self):
        return self._getReal(2)

    def setDiscount(self, value):
        self._setReal(2, value)
        return

    def _initialize(self):
        super(ExchangeRateModel, self)._initialize()
        self._addRealProperty(b'current', 0.0)
        self._addRealProperty(b'default', 0.0)
        self._addRealProperty(b'discount', 0.0)
        return
