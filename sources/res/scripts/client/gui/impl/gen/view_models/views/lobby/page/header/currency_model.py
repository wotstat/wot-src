from frameworks.wulf import ViewModel

class CurrencyModel(ViewModel):
    __slots__ = ()
    STATUS_SYNCING = b'SYNCING'
    STATUS_NOT_AVAILABLE = b'NOT_AVAILABLE'
    STATUS_AVAILABLE = b'AVAILABLE'

    def __init__(self, properties=4, commands=0):
        super(CurrencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)
        return

    def getDiscount(self):
        return self._getNumber(1)

    def setDiscount(self, value):
        self._setNumber(1, value)
        return

    def getStatus(self):
        return self._getString(2)

    def setStatus(self, value):
        self._setString(2, value)
        return

    def getTooltipType(self):
        return self._getString(3)

    def setTooltipType(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(CurrencyModel, self)._initialize()
        self._addNumberProperty(b'value', 0)
        self._addNumberProperty(b'discount', 0)
        self._addStringProperty(b'status', b'')
        self._addStringProperty(b'tooltipType', b'')
        return
