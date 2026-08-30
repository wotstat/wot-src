from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.play_streak.rewards_calendar_item import RewardsCalendarItem

class PeriodicRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PeriodicRewardsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getStreakLength(self):
        return self._getNumber(0)

    def setStreakLength(self, value):
        self._setNumber(0, value)
        return

    def getDailyWin(self):
        return self._getBool(1)

    def setDailyWin(self, value):
        self._setBool(1, value)
        return

    def getRewardsCalendar(self):
        return self._getArray(2)

    def setRewardsCalendar(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsCalendarType():
        return RewardsCalendarItem

    def _initialize(self):
        super(PeriodicRewardsTooltipModel, self)._initialize()
        self._addNumberProperty(b'streakLength', 0)
        self._addBoolProperty(b'dailyWin', False)
        self._addArrayProperty(b'rewardsCalendar', Array())
        return
