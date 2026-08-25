from enum import Enum
from frameworks.wulf import ViewModel

class CurrencyType(Enum):
    CREDITS = b'credits'
    GOLD = b'gold'
    CRYSTAL = b'crystal'
    FREEXP = b'freeXP'


class CurrencyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CurrencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrencyType(self):
        return CurrencyType(self._getString(0))

    def setCurrencyType(self, value):
        self._setString(0, value.value)
        return

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)
        return

    def getTooltipId(self):
        return self._getNumber(2)

    def setTooltipId(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(CurrencyModel, self)._initialize()
        self._addStringProperty(b'currencyType', CurrencyType.GOLD.value)
        self._addNumberProperty(b'value', 0)
        self._addNumberProperty(b'tooltipId', 0)
        return
