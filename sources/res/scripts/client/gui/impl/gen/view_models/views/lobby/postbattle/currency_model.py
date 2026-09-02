from frameworks.wulf import ViewModel

class CurrencyModel(ViewModel):
    __slots__ = ()
    CREDITS = b'credits'
    CRYSTALS = b'crystal'
    XP = b'xp'
    FREE_XP = b'freeXp'

    def __init__(self, properties=2, commands=0):
        super(CurrencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getAmount(self):
        return self._getNumber(0)

    def setAmount(self, value):
        self._setNumber(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(CurrencyModel, self)._initialize()
        self._addNumberProperty(b'amount', 0)
        self._addStringProperty(b'type', b'')
        return
