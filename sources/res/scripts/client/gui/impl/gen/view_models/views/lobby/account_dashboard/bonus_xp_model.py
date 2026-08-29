from frameworks.wulf import ViewModel

class BonusXpModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=4, commands=1):
        super(BonusXpModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getMultiplier(self):
        return self._getNumber(1)

    def setMultiplier(self, value):
        self._setNumber(1, value)
        return

    def getTotalUses(self):
        return self._getNumber(2)

    def setTotalUses(self, value):
        self._setNumber(2, value)
        return

    def getUsesLeft(self):
        return self._getNumber(3)

    def setUsesLeft(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(BonusXpModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', True)
        self._addNumberProperty(b'multiplier', 1)
        self._addNumberProperty(b'totalUses', 0)
        self._addNumberProperty(b'usesLeft', 0)
        self.onClick = self._addCommand(b'onClick')
        return
