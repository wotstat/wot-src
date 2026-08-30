from frameworks.wulf import ViewModel

class DailyExperienceBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DailyExperienceBaseModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsTankPremiumActive(self):
        return self._getBool(0)

    def setIsTankPremiumActive(self, value):
        self._setBool(0, value)
        return

    def getMultiplier(self):
        return self._getNumber(1)

    def setMultiplier(self, value):
        self._setNumber(1, value)
        return

    def getLeftBonusCount(self):
        return self._getNumber(2)

    def setLeftBonusCount(self, value):
        self._setNumber(2, value)
        return

    def getTotalBonusCount(self):
        return self._getNumber(3)

    def setTotalBonusCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(DailyExperienceBaseModel, self)._initialize()
        self._addBoolProperty(b'isTankPremiumActive', False)
        self._addNumberProperty(b'multiplier', 1)
        self._addNumberProperty(b'leftBonusCount', 0)
        self._addNumberProperty(b'totalBonusCount', 5)
        return
