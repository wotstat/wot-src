from frameworks.wulf import ViewModel

class SpecialCurrencyModel(ViewModel):
    __slots__ = (b'onGetMoreCurrency',)

    def __init__(self, properties=2, commands=1):
        super(SpecialCurrencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)
        return

    def _initialize(self):
        super(SpecialCurrencyModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addRealProperty(b'value', 0.0)
        self.onGetMoreCurrency = self._addCommand(b'onGetMoreCurrency')
        return
