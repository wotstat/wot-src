from frameworks.wulf import ViewModel

class ReserveStockModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=10, commands=1):
        super(ReserveStockModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCreditReserveEnabled(self):
        return self._getBool(0)

    def setIsCreditReserveEnabled(self, value):
        self._setBool(0, value)
        return

    def getIsGoldReserveEnabled(self):
        return self._getBool(1)

    def setIsGoldReserveEnabled(self, value):
        self._setBool(1, value)
        return

    def getCreditCurrentAmount(self):
        return self._getNumber(2)

    def setCreditCurrentAmount(self, value):
        self._setNumber(2, value)
        return

    def getCreditMaxAmount(self):
        return self._getNumber(3)

    def setCreditMaxAmount(self, value):
        self._setNumber(3, value)
        return

    def getGoldCurrentAmount(self):
        return self._getNumber(4)

    def setGoldCurrentAmount(self, value):
        self._setNumber(4, value)
        return

    def getGoldMaxAmount(self):
        return self._getNumber(5)

    def setGoldMaxAmount(self, value):
        self._setNumber(5, value)
        return

    def getOpeningTime(self):
        return self._getNumber(6)

    def setOpeningTime(self, value):
        self._setNumber(6, value)
        return

    def getOpeningSoonThreshold(self):
        return self._getNumber(7)

    def setOpeningSoonThreshold(self, value):
        self._setNumber(7, value)
        return

    def getIsPremiumActive(self):
        return self._getBool(8)

    def setIsPremiumActive(self, value):
        self._setBool(8, value)
        return

    def getIsWotPlusActive(self):
        return self._getBool(9)

    def setIsWotPlusActive(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(ReserveStockModel, self)._initialize()
        self._addBoolProperty(b'isCreditReserveEnabled', True)
        self._addBoolProperty(b'isGoldReserveEnabled', True)
        self._addNumberProperty(b'creditCurrentAmount', 0)
        self._addNumberProperty(b'creditMaxAmount', 0)
        self._addNumberProperty(b'goldCurrentAmount', 0)
        self._addNumberProperty(b'goldMaxAmount', 0)
        self._addNumberProperty(b'openingTime', 0)
        self._addNumberProperty(b'openingSoonThreshold', 0)
        self._addBoolProperty(b'isPremiumActive', False)
        self._addBoolProperty(b'isWotPlusActive', False)
        self.onClick = self._addCommand(b'onClick')
        return
