from comp7.gui.impl.gen.view_models.views.lobby.enums import Division, Rank, SeasonName, StatisticsMode
from frameworks.wulf import ViewModel

class RankIndicatorTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(RankIndicatorTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatisticsMode(self):
        return StatisticsMode(self._getNumber(0))

    def setStatisticsMode(self, value):
        self._setNumber(0, value.value)
        return

    def getSeasonName(self):
        return SeasonName(self._getString(1))

    def setSeasonName(self, value):
        self._setString(1, value.value)
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

    def getDiff(self):
        return self._getNumber(5)

    def setDiff(self, value):
        self._setNumber(5, value)
        return

    def getMaxAchievedRatingPoints(self):
        return self._getNumber(6)

    def setMaxAchievedRatingPoints(self, value):
        self._setNumber(6, value)
        return

    def getDayOfMaxRatingIndex(self):
        return self._getNumber(7)

    def setDayOfMaxRatingIndex(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(RankIndicatorTooltipModel, self)._initialize()
        self._addNumberProperty(b'statisticsMode')
        self._addStringProperty(b'seasonName')
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'division')
        self._addNumberProperty(b'ratingPoints', 0)
        self._addNumberProperty(b'diff', 0)
        self._addNumberProperty(b'maxAchievedRatingPoints', 0)
        self._addNumberProperty(b'dayOfMaxRatingIndex', 0)
        return
