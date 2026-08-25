from frameworks.wulf import ViewModel

class WotPlusPiggyBankCardModel(ViewModel):
    __slots__ = (b'onCardClick',)

    def __init__(self, properties=7, commands=1):
        super(WotPlusPiggyBankCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getPremState(self):
        return self._getString(0)

    def setPremState(self, value):
        self._setString(0, value)
        return

    def getCreditMaxAmount(self):
        return self._getString(1)

    def setCreditMaxAmount(self, value):
        self._setString(1, value)
        return

    def getCreditCurrentAmount(self):
        return self._getString(2)

    def setCreditCurrentAmount(self, value):
        self._setString(2, value)
        return

    def getWotPlusState(self):
        return self._getString(3)

    def setWotPlusState(self, value):
        self._setString(3, value)
        return

    def getGoldMaxAmount(self):
        return self._getString(4)

    def setGoldMaxAmount(self, value):
        self._setString(4, value)
        return

    def getGoldCurrentAmount(self):
        return self._getString(5)

    def setGoldCurrentAmount(self, value):
        self._setString(5, value)
        return

    def getTimeToOpen(self):
        return self._getNumber(6)

    def setTimeToOpen(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(WotPlusPiggyBankCardModel, self)._initialize()
        self._addStringProperty(b'premState', b'')
        self._addStringProperty(b'creditMaxAmount', b'')
        self._addStringProperty(b'creditCurrentAmount', b'0')
        self._addStringProperty(b'wotPlusState', b'')
        self._addStringProperty(b'goldMaxAmount', b'')
        self._addStringProperty(b'goldCurrentAmount', b'0')
        self._addNumberProperty(b'timeToOpen', 0)
        self.onCardClick = self._addCommand(b'onCardClick')
        return
