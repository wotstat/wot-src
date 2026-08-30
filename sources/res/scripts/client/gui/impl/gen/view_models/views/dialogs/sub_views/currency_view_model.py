from enum import Enum
from frameworks.wulf import ViewModel

class CurrencySize(Enum):
    SMALL = b'small'
    BIG = b'big'
    LARGE = b'large'


class CurrencyType(Enum):
    CREDITS = b'credits'
    GOLD = b'gold'
    CRYSTAL = b'crystal'
    XP = b'xp'
    FREEXP = b'freeXP'
    EQUIPCOIN = b'equipCoin'
    ELITEXP = b'eliteXP'


class CurrencyViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(CurrencyViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)
        return

    def getIsEnough(self):
        return self._getBool(1)

    def setIsEnough(self, value):
        self._setBool(1, value)
        return

    def getIsDiscount(self):
        return self._getBool(2)

    def setIsDiscount(self, value):
        self._setBool(2, value)
        return

    def getDiscountValue(self):
        return self._getReal(3)

    def setDiscountValue(self, value):
        self._setReal(3, value)
        return

    def getShowPlus(self):
        return self._getBool(4)

    def setShowPlus(self, value):
        self._setBool(4, value)
        return

    def getSize(self):
        return CurrencySize(self._getString(5))

    def setSize(self, value):
        self._setString(5, value.value)
        return

    def getType(self):
        return CurrencyType(self._getString(6))

    def setType(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(CurrencyViewModel, self)._initialize()
        self._addNumberProperty(b'value', 0)
        self._addBoolProperty(b'isEnough', False)
        self._addBoolProperty(b'isDiscount', False)
        self._addRealProperty(b'discountValue', 0.0)
        self._addBoolProperty(b'showPlus', False)
        self._addStringProperty(b'size')
        self._addStringProperty(b'type')
        return
