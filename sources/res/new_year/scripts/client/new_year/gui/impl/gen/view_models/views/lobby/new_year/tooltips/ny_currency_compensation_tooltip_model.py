from frameworks.wulf import ViewModel

class NyCurrencyCompensationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NyCurrencyCompensationTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrencyAmount(self):
        return self._getNumber(0)

    def setCurrencyAmount(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(NyCurrencyCompensationTooltipModel, self)._initialize()
        self._addNumberProperty(b'currencyAmount', 0)
        return
