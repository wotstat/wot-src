from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class PlayStreakTabViewModel(ViewModel):
    __slots__ = (b'onShowInfo', b'onFinishAnimation')

    def __init__(self, properties=12, commands=2):
        super(PlayStreakTabViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStreakLength(self):
        return self._getNumber(0)

    def setStreakLength(self, value):
        self._setNumber(0, value)
        return

    def getSkipDayCount(self):
        return self._getNumber(1)

    def setSkipDayCount(self, value):
        self._setNumber(1, value)
        return

    def getRedemptionDayCount(self):
        return self._getNumber(2)

    def setRedemptionDayCount(self, value):
        self._setNumber(2, value)
        return

    def getRedemptionMaxDayCount(self):
        return self._getNumber(3)

    def setRedemptionMaxDayCount(self, value):
        self._setNumber(3, value)
        return

    def getDailyWin(self):
        return self._getBool(4)

    def setDailyWin(self, value):
        self._setBool(4, value)
        return

    def getIsBlocked(self):
        return self._getBool(5)

    def setIsBlocked(self, value):
        self._setBool(5, value)
        return

    def getIsFirstAppearance(self):
        return self._getBool(6)

    def setIsFirstAppearance(self, value):
        self._setBool(6, value)
        return

    def getIsFirstAppearanceRedemptionDay(self):
        return self._getBool(7)

    def setIsFirstAppearanceRedemptionDay(self, value):
        self._setBool(7, value)
        return

    def getIsLastDayRedemption(self):
        return self._getBool(8)

    def setIsLastDayRedemption(self, value):
        self._setBool(8, value)
        return

    def getIsPaused(self):
        return self._getBool(9)

    def setIsPaused(self, value):
        self._setBool(9, value)
        return

    def getIsEnabled(self):
        return self._getBool(10)

    def setIsEnabled(self, value):
        self._setBool(10, value)
        return

    def getBattleTypes(self):
        return self._getArray(11)

    def setBattleTypes(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getBattleTypesType():
        return int

    def _initialize(self):
        super(PlayStreakTabViewModel, self)._initialize()
        self._addNumberProperty(b'streakLength', 0)
        self._addNumberProperty(b'skipDayCount', 0)
        self._addNumberProperty(b'redemptionDayCount', 0)
        self._addNumberProperty(b'redemptionMaxDayCount', 0)
        self._addBoolProperty(b'dailyWin', False)
        self._addBoolProperty(b'isBlocked', False)
        self._addBoolProperty(b'isFirstAppearance', False)
        self._addBoolProperty(b'isFirstAppearanceRedemptionDay', False)
        self._addBoolProperty(b'isLastDayRedemption', False)
        self._addBoolProperty(b'isPaused', False)
        self._addBoolProperty(b'isEnabled', False)
        self._addArrayProperty(b'battleTypes', Array())
        self.onShowInfo = self._addCommand(b'onShowInfo')
        self.onFinishAnimation = self._addCommand(b'onFinishAnimation')
        return
