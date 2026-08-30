from frameworks.wulf import ViewModel

class BattleRoyaleShellModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleRoyaleShellModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconName(self):
        return self._getString(0)

    def setIconName(self, value):
        self._setString(0, value)
        return

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)
        return

    def getQuantity(self):
        return self._getNumber(2)

    def setQuantity(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(BattleRoyaleShellModel, self)._initialize()
        self._addStringProperty(b'iconName', b'')
        self._addNumberProperty(b'intCD', 0)
        self._addNumberProperty(b'quantity', 0)
        return
