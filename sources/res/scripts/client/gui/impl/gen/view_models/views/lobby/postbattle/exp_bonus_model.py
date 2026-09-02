from frameworks.wulf import ViewModel

class ExpBonusModel(ViewModel):
    __slots__ = ()
    IS_APPLIED = 1
    IS_NOT_VICTORY = 2
    DEPRECATED_RESULTS = 3
    NO_VEHICLE = 4
    NO_CREW = 5
    FASTER_EDUCATION_CREW_NOT_ACTIVE = 6
    FASTER_EDUCATION_CREW_ACTIVE = 7

    def __init__(self, properties=6, commands=0):
        super(ExpBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getMaxBonusCount(self):
        return self._getNumber(0)

    def setMaxBonusCount(self, value):
        self._setNumber(0, value)
        return

    def getUsedBonusCount(self):
        return self._getNumber(1)

    def setUsedBonusCount(self, value):
        self._setNumber(1, value)
        return

    def getNextBonusTime(self):
        return self._getReal(2)

    def setNextBonusTime(self, value):
        self._setReal(2, value)
        return

    def getBonusMultiplier(self):
        return self._getNumber(3)

    def setBonusMultiplier(self, value):
        self._setNumber(3, value)
        return

    def getRestriction(self):
        return self._getNumber(4)

    def setRestriction(self, value):
        self._setNumber(4, value)
        return

    def getIsEnabled(self):
        return self._getBool(5)

    def setIsEnabled(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(ExpBonusModel, self)._initialize()
        self._addNumberProperty(b'maxBonusCount', 0)
        self._addNumberProperty(b'usedBonusCount', 0)
        self._addRealProperty(b'nextBonusTime', 0.0)
        self._addNumberProperty(b'bonusMultiplier', 0)
        self._addNumberProperty(b'restriction', 0)
        self._addBoolProperty(b'isEnabled', False)
        return
