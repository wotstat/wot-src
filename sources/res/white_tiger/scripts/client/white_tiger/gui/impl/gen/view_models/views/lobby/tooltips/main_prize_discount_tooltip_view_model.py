from frameworks.wulf import ViewModel

class MainPrizeDiscountTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MainPrizeDiscountTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getOldPrice(self):
        return self._getNumber(0)

    def setOldPrice(self, value):
        self._setNumber(0, value)
        return

    def getCurrentPrice(self):
        return self._getNumber(1)

    def setCurrentPrice(self, value):
        self._setNumber(1, value)
        return

    def getDiscount(self):
        return self._getNumber(2)

    def setDiscount(self, value):
        self._setNumber(2, value)
        return

    def getActiveDiscount(self):
        return self._getNumber(3)

    def setActiveDiscount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(MainPrizeDiscountTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'oldPrice', 0)
        self._addNumberProperty(b'currentPrice', 0)
        self._addNumberProperty(b'discount', 0)
        self._addNumberProperty(b'activeDiscount', 0)
        return
