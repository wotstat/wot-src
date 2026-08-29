from frameworks.wulf import ViewModel

class FreeXpBookModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FreeXpBookModel, self).__init__(properties=properties, commands=commands)
        return

    def getPlayerXp(self):
        return self._getNumber(0)

    def setPlayerXp(self, value):
        self._setNumber(0, value)
        return

    def getDiscountSize(self):
        return self._getNumber(1)

    def setDiscountSize(self, value):
        self._setNumber(1, value)
        return

    def getCurrentXpValue(self):
        return self._getNumber(2)

    def setCurrentXpValue(self, value):
        self._setNumber(2, value)
        return

    def getCurrentMaxValue(self):
        return self._getNumber(3)

    def setCurrentMaxValue(self, value):
        self._setNumber(3, value)
        return

    def getExchangeRate(self):
        return self._getNumber(4)

    def setExchangeRate(self, value):
        self._setNumber(4, value)
        return

    def getIsEligibleToApplyFreeXp(self):
        return self._getBool(5)

    def setIsEligibleToApplyFreeXp(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(FreeXpBookModel, self)._initialize()
        self._addNumberProperty(b'playerXp', 0)
        self._addNumberProperty(b'discountSize', 0)
        self._addNumberProperty(b'currentXpValue', 0)
        self._addNumberProperty(b'currentMaxValue', 0)
        self._addNumberProperty(b'exchangeRate', 1)
        self._addBoolProperty(b'isEligibleToApplyFreeXp', False)
        return
