from frameworks.wulf import Array, ViewModel

class EarningsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(EarningsModel, self).__init__(properties=properties, commands=commands)
        return

    def getXp(self):
        return self._getNumber(0)

    def setXp(self, value):
        self._setNumber(0, value)
        return

    def getBonusMultiplier(self):
        return self._getNumber(1)

    def setBonusMultiplier(self, value):
        self._setNumber(1, value)
        return

    def getCrystalEarning(self):
        return self._getBool(2)

    def setCrystalEarning(self, value):
        self._setBool(2, value)
        return

    def getCrystalTimeout(self):
        return self._getNumber(3)

    def setCrystalTimeout(self, value):
        self._setNumber(3, value)
        return

    def getWotPlus(self):
        return self._getBool(4)

    def setWotPlus(self, value):
        self._setBool(4, value)
        return

    def getTelecomRent(self):
        return self._getBool(5)

    def setTelecomRent(self, value):
        self._setBool(5, value)
        return

    def getTradeIn(self):
        return self._getBool(6)

    def setTradeIn(self, value):
        self._setBool(6, value)
        return

    def getNumberOfCrystalEarned(self):
        return self._getArray(7)

    def setNumberOfCrystalEarned(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getNumberOfCrystalEarnedType():
        return int

    def getCurrentBpScore(self):
        return self._getNumber(8)

    def setCurrentBpScore(self, value):
        self._setNumber(8, value)
        return

    def getWotPlusExpiryTime(self):
        return self._getNumber(9)

    def setWotPlusExpiryTime(self, value):
        self._setNumber(9, value)
        return

    def getWotPlusState(self):
        return self._getString(10)

    def setWotPlusState(self, value):
        self._setString(10, value)
        return

    def getMaxBpScore(self):
        return self._getNumber(11)

    def setMaxBpScore(self, value):
        self._setNumber(11, value)
        return

    def getBpReward(self):
        return self._getNumber(12)

    def setBpReward(self, value):
        self._setNumber(12, value)
        return

    def getBpActive(self):
        return self._getBool(13)

    def setBpActive(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(EarningsModel, self)._initialize()
        self._addNumberProperty(b'xp', 0)
        self._addNumberProperty(b'bonusMultiplier', -1)
        self._addBoolProperty(b'crystalEarning', False)
        self._addNumberProperty(b'crystalTimeout', 0)
        self._addBoolProperty(b'wotPlus', False)
        self._addBoolProperty(b'telecomRent', False)
        self._addBoolProperty(b'tradeIn', False)
        self._addArrayProperty(b'numberOfCrystalEarned', Array())
        self._addNumberProperty(b'currentBpScore', -1)
        self._addNumberProperty(b'wotPlusExpiryTime', 0)
        self._addStringProperty(b'wotPlusState', b'')
        self._addNumberProperty(b'maxBpScore', -1)
        self._addNumberProperty(b'bpReward', 0)
        self._addBoolProperty(b'bpActive', False)
        return
