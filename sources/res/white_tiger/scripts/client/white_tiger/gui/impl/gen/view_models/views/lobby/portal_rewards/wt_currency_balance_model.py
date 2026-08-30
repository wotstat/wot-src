from frameworks.wulf import ViewModel

class WtCurrencyBalanceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(WtCurrencyBalanceModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsWalletAvailable(self):
        return self._getBool(0)

    def setIsWalletAvailable(self, value):
        self._setBool(0, value)
        return

    def getCrystal(self):
        return self._getNumber(1)

    def setCrystal(self, value):
        self._setNumber(1, value)
        return

    def getGold(self):
        return self._getNumber(2)

    def setGold(self, value):
        self._setNumber(2, value)
        return

    def getCredits(self):
        return self._getNumber(3)

    def setCredits(self, value):
        self._setNumber(3, value)
        return

    def getFreeXp(self):
        return self._getNumber(4)

    def setFreeXp(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(WtCurrencyBalanceModel, self)._initialize()
        self._addBoolProperty(b'isWalletAvailable', False)
        self._addNumberProperty(b'crystal', 0)
        self._addNumberProperty(b'gold', 0)
        self._addNumberProperty(b'credits', 0)
        self._addNumberProperty(b'freeXp', 0)
        return
