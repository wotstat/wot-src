from comp7.gui.impl.gen.view_models.views.lobby.enums import Division, Rank
from frameworks.wulf import ViewModel

class DayTooltip(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(DayTooltip, self).__init__(properties=properties, commands=commands)
        return

    def getIndex(self):
        return self._getNumber(0)

    def setIndex(self, value):
        self._setNumber(0, value)
        return

    def getIsQualification(self):
        return self._getBool(1)

    def setIsQualification(self, value):
        self._setBool(1, value)
        return

    def getRank(self):
        return Rank(self._getNumber(2))

    def setRank(self, value):
        self._setNumber(2, value.value)
        return

    def getDivision(self):
        return Division(self._getNumber(3))

    def setDivision(self, value):
        self._setNumber(3, value.value)
        return

    def getRatingPoints(self):
        return self._getNumber(4)

    def setRatingPoints(self, value):
        self._setNumber(4, value)
        return

    def getRankInactivityPenalty(self):
        return self._getNumber(5)

    def setRankInactivityPenalty(self, value):
        self._setNumber(5, value)
        return

    def getMaxAchievedRank(self):
        return Rank(self._getNumber(6))

    def setMaxAchievedRank(self, value):
        self._setNumber(6, value.value)
        return

    def getCurrentDayIndex(self):
        return self._getNumber(7)

    def setCurrentDayIndex(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(DayTooltip, self)._initialize()
        self._addNumberProperty(b'index', 0)
        self._addBoolProperty(b'isQualification', False)
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'division')
        self._addNumberProperty(b'ratingPoints', 0)
        self._addNumberProperty(b'rankInactivityPenalty', 0)
        self._addNumberProperty(b'maxAchievedRank')
        self._addNumberProperty(b'currentDayIndex', 0)
        return
