from comp7.gui.impl.gen.view_models.views.lobby.enums import Division, Rank, SeasonName
from frameworks.wulf import ViewModel

class DayTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(DayTooltipModel, self).__init__(properties=properties, commands=commands)
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

    def getSeasonName(self):
        return SeasonName(self._getString(2))

    def setSeasonName(self, value):
        self._setString(2, value.value)
        return

    def getDiff(self):
        return self._getNumber(3)

    def setDiff(self, value):
        self._setNumber(3, value)
        return

    def getRank(self):
        return Rank(self._getNumber(4))

    def setRank(self, value):
        self._setNumber(4, value.value)
        return

    def getDivision(self):
        return Division(self._getNumber(5))

    def setDivision(self, value):
        self._setNumber(5, value.value)
        return

    def getHasBattles(self):
        return self._getBool(6)

    def setHasBattles(self, value):
        self._setBool(6, value)
        return

    def getRatingPoints(self):
        return self._getNumber(7)

    def setRatingPoints(self, value):
        self._setNumber(7, value)
        return

    def getRankInactivityPenalty(self):
        return self._getNumber(8)

    def setRankInactivityPenalty(self, value):
        self._setNumber(8, value)
        return

    def getCurrentDayIndex(self):
        return self._getNumber(9)

    def setCurrentDayIndex(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(DayTooltipModel, self)._initialize()
        self._addNumberProperty(b'index', 0)
        self._addBoolProperty(b'isQualification', False)
        self._addStringProperty(b'seasonName')
        self._addNumberProperty(b'diff', 0)
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'division')
        self._addBoolProperty(b'hasBattles', False)
        self._addNumberProperty(b'ratingPoints', 0)
        self._addNumberProperty(b'rankInactivityPenalty', 0)
        self._addNumberProperty(b'currentDayIndex', 0)
        return
