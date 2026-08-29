from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.views.lobby.play_streak.rewards_calendar_item import RewardsCalendarItem

class PlayStreakViewModel(ViewModel):
    __slots__ = (b'onVehiclePreviewClick', b'onShowVehicle', b'onStylePreviewClick')

    def __init__(self, properties=15, commands=3):
        super(PlayStreakViewModel, self).__init__(properties=properties, commands=commands)
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

    def getDailyWin(self):
        return self._getBool(2)

    def setDailyWin(self, value):
        self._setBool(2, value)
        return

    def getIsBlocked(self):
        return self._getBool(3)

    def setIsBlocked(self, value):
        self._setBool(3, value)
        return

    def getIsPaused(self):
        return self._getBool(4)

    def setIsPaused(self, value):
        self._setBool(4, value)
        return

    def getIsFirstAppearance(self):
        return self._getBool(5)

    def setIsFirstAppearance(self, value):
        self._setBool(5, value)
        return

    def getIsFirstAppearanceRedemptionDay(self):
        return self._getBool(6)

    def setIsFirstAppearanceRedemptionDay(self, value):
        self._setBool(6, value)
        return

    def getIsLastDayRedemption(self):
        return self._getBool(7)

    def setIsLastDayRedemption(self, value):
        self._setBool(7, value)
        return

    def getRedemptionDayCount(self):
        return self._getNumber(8)

    def setRedemptionDayCount(self, value):
        self._setNumber(8, value)
        return

    def getRedemptionMaxDayCount(self):
        return self._getNumber(9)

    def setRedemptionMaxDayCount(self, value):
        self._setNumber(9, value)
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

    def getRewardsCalendar(self):
        return self._getArray(12)

    def setRewardsCalendar(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getRewardsCalendarType():
        return RewardsCalendarItem

    def getTopRewards(self):
        return self._getArray(13)

    def setTopRewards(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getTopRewardsType():
        return RewardsCalendarItem

    def getPeriodicRewards(self):
        return self._getArray(14)

    def setPeriodicRewards(self, value):
        self._setArray(14, value)
        return

    @staticmethod
    def getPeriodicRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(PlayStreakViewModel, self)._initialize()
        self._addNumberProperty(b'streakLength', 0)
        self._addNumberProperty(b'skipDayCount', 0)
        self._addBoolProperty(b'dailyWin', False)
        self._addBoolProperty(b'isBlocked', False)
        self._addBoolProperty(b'isPaused', False)
        self._addBoolProperty(b'isFirstAppearance', False)
        self._addBoolProperty(b'isFirstAppearanceRedemptionDay', False)
        self._addBoolProperty(b'isLastDayRedemption', False)
        self._addNumberProperty(b'redemptionDayCount', 0)
        self._addNumberProperty(b'redemptionMaxDayCount', 0)
        self._addBoolProperty(b'isEnabled', False)
        self._addArrayProperty(b'battleTypes', Array())
        self._addArrayProperty(b'rewardsCalendar', Array())
        self._addArrayProperty(b'topRewards', Array())
        self._addArrayProperty(b'periodicRewards', Array())
        self.onVehiclePreviewClick = self._addCommand(b'onVehiclePreviewClick')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        self.onStylePreviewClick = self._addCommand(b'onStylePreviewClick')
        return
