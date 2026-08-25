from comp7.gui.impl.gen.view_models.views.lobby.enums import Division
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.statistics_model import StatisticsModel

class DayStatisticsModel(StatisticsModel):
    __slots__ = ()

    def __init__(self, properties=20, commands=0):
        super(DayStatisticsModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsQualification(self):
        return self._getBool(14)

    def setIsQualification(self, value):
        self._setBool(14, value)
        return

    def getHasBattles(self):
        return self._getBool(15)

    def setHasBattles(self, value):
        self._setBool(15, value)
        return

    def getRatingPoints(self):
        return self._getNumber(16)

    def setRatingPoints(self, value):
        self._setNumber(16, value)
        return

    def getDiff(self):
        return self._getNumber(17)

    def setDiff(self, value):
        self._setNumber(17, value)
        return

    def getRankInactivityPenalty(self):
        return self._getNumber(18)

    def setRankInactivityPenalty(self, value):
        self._setNumber(18, value)
        return

    def getDivision(self):
        return Division(self._getNumber(19))

    def setDivision(self, value):
        self._setNumber(19, value.value)
        return

    def _initialize(self):
        super(DayStatisticsModel, self)._initialize()
        self._addBoolProperty(b'isQualification', False)
        self._addBoolProperty(b'hasBattles', False)
        self._addNumberProperty(b'ratingPoints', 0)
        self._addNumberProperty(b'diff', 0)
        self._addNumberProperty(b'rankInactivityPenalty', 0)
        self._addNumberProperty(b'division')
        return
