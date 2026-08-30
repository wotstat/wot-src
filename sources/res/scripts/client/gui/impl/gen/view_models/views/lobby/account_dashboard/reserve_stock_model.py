from frameworks.wulf import ViewModel

class ReserveStockModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=11, commands=1):
        super(ReserveStockModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getIsEnabledGold(self):
        return self._getBool(1)

    def setIsEnabledGold(self, value):
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

    def getOpeningTime(self):
        return self._getNumber(4)

    def setOpeningTime(self, value):
        self._setNumber(4, value)
        return

    def getOpeningSoonThreshold(self):
        return self._getNumber(5)

    def setOpeningSoonThreshold(self, value):
        self._setNumber(5, value)
        return

    def getIsPremiumActive(self):
        return self._getBool(6)

    def setIsPremiumActive(self, value):
        self._setBool(6, value)
        return

    def getIsSubscriptionActive(self):
        return self._getBool(7)

    def setIsSubscriptionActive(self, value):
        self._setBool(7, value)
        return

    def getIsSubscriptionAvailable(self):
        return self._getBool(8)

    def setIsSubscriptionAvailable(self, value):
        self._setBool(8, value)
        return

    def getGoldCurrentAmount(self):
        return self._getNumber(9)

    def setGoldCurrentAmount(self, value):
        self._setNumber(9, value)
        return

    def getGoldMaxAmount(self):
        return self._getNumber(10)

    def setGoldMaxAmount(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(ReserveStockModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', True)
        self._addBoolProperty(b'isEnabledGold', False)
        self._addNumberProperty(b'creditCurrentAmount', 0)
        self._addNumberProperty(b'creditMaxAmount', 0)
        self._addNumberProperty(b'openingTime', 0)
        self._addNumberProperty(b'openingSoonThreshold', 0)
        self._addBoolProperty(b'isPremiumActive', False)
        self._addBoolProperty(b'isSubscriptionActive', False)
        self._addBoolProperty(b'isSubscriptionAvailable', False)
        self._addNumberProperty(b'goldCurrentAmount', 0)
        self._addNumberProperty(b'goldMaxAmount', 0)
        self.onClick = self._addCommand(b'onClick')
        return
