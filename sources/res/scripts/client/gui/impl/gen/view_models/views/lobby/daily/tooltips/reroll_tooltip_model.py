from frameworks.wulf import ViewModel

class RerollTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(RerollTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCanReroll(self):
        return self._getBool(0)

    def setCanReroll(self, value):
        self._setBool(0, value)
        return

    def getIsCompleted(self):
        return self._getBool(1)

    def setIsCompleted(self, value):
        self._setBool(1, value)
        return

    def getIsBonusCompleted(self):
        return self._getBool(2)

    def setIsBonusCompleted(self, value):
        self._setBool(2, value)
        return

    def getIsPremium(self):
        return self._getBool(3)

    def setIsPremium(self, value):
        self._setBool(3, value)
        return

    def getIsPremiumActive(self):
        return self._getBool(4)

    def setIsPremiumActive(self, value):
        self._setBool(4, value)
        return

    def getTimeToUpdate(self):
        return self._getNumber(5)

    def setTimeToUpdate(self, value):
        self._setNumber(5, value)
        return

    def getRerollCooldown(self):
        return self._getNumber(6)

    def setRerollCooldown(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(RerollTooltipModel, self)._initialize()
        self._addBoolProperty(b'canReroll', False)
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isBonusCompleted', False)
        self._addBoolProperty(b'isPremium', False)
        self._addBoolProperty(b'isPremiumActive', False)
        self._addNumberProperty(b'timeToUpdate', 0)
        self._addNumberProperty(b'rerollCooldown', 0)
        return
