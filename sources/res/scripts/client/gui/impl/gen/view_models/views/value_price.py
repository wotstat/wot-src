from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ValuePrice(ViewModel):
    __slots__ = ()
    CUSTOM = b'custom'
    CREDITS = b'credits'
    GOLD = b'gold'
    EXP = b'exp'
    FREE_XP = b'freeXP'
    CRYSTAL = b'crystal'

    def __init__(self, properties=4, commands=0):
        super(ValuePrice, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)
        return

    def getNotEnough(self):
        return self._getBool(3)

    def setNotEnough(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(ValuePrice, self)._initialize()
        self._addStringProperty(b'value', b'0')
        self._addStringProperty(b'type', b'custom')
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'notEnough', False)
        return
