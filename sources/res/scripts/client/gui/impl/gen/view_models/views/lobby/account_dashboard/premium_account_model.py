from frameworks.wulf import ViewModel

class PremiumAccountModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=10, commands=1):
        super(PremiumAccountModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getWotPremiumSecondsLeft(self):
        return self._getNumber(1)

    def setWotPremiumSecondsLeft(self, value):
        self._setNumber(1, value)
        return

    def getWgPremiumSecondsLeft(self):
        return self._getNumber(2)

    def setWgPremiumSecondsLeft(self, value):
        self._setNumber(2, value)
        return

    def getXpBonus(self):
        return self._getNumber(3)

    def setXpBonus(self, value):
        self._setNumber(3, value)
        return

    def getCreditBonus(self):
        return self._getNumber(4)

    def setCreditBonus(self, value):
        self._setNumber(4, value)
        return

    def getPlatoonBonus(self):
        return self._getNumber(5)

    def setPlatoonBonus(self, value):
        self._setNumber(5, value)
        return

    def getStandardAccountCredits(self):
        return self._getNumber(6)

    def setStandardAccountCredits(self, value):
        self._setNumber(6, value)
        return

    def getStandardAccountXp(self):
        return self._getNumber(7)

    def setStandardAccountXp(self, value):
        self._setNumber(7, value)
        return

    def getPremiumAccountCredits(self):
        return self._getNumber(8)

    def setPremiumAccountCredits(self, value):
        self._setNumber(8, value)
        return

    def getPremiumAccountXp(self):
        return self._getNumber(9)

    def setPremiumAccountXp(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(PremiumAccountModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', True)
        self._addNumberProperty(b'wotPremiumSecondsLeft', 0)
        self._addNumberProperty(b'wgPremiumSecondsLeft', 0)
        self._addNumberProperty(b'xpBonus', 50)
        self._addNumberProperty(b'creditBonus', 50)
        self._addNumberProperty(b'platoonBonus', 15)
        self._addNumberProperty(b'standardAccountCredits', 0)
        self._addNumberProperty(b'standardAccountXp', 0)
        self._addNumberProperty(b'premiumAccountCredits', 0)
        self._addNumberProperty(b'premiumAccountXp', 0)
        self.onClick = self._addCommand(b'onClick')
        return
