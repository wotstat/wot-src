from comp7.gui.impl.gen.view_models.views.lobby.enums import Division, Rank
from frameworks.wulf import ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.season_model import SeasonModel

class YearlyStatisticsSeasonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(YearlyStatisticsSeasonModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def season(self):
        return self._getViewModel(0)

    @staticmethod
    def getSeasonType():
        return SeasonModel

    def getRating(self):
        return self._getNumber(1)

    def setRating(self, value):
        self._setNumber(1, value)
        return

    def getSingleBattlesCount(self):
        return self._getNumber(2)

    def setSingleBattlesCount(self, value):
        self._setNumber(2, value)
        return

    def getSingleBattlesWinRate(self):
        return self._getReal(3)

    def setSingleBattlesWinRate(self, value):
        self._setReal(3, value)
        return

    def getSuperPlatoonBattlesCount(self):
        return self._getNumber(4)

    def setSuperPlatoonBattlesCount(self, value):
        self._setNumber(4, value)
        return

    def getSuperPlatoonBattlesWinRate(self):
        return self._getReal(5)

    def setSuperPlatoonBattlesWinRate(self, value):
        self._setReal(5, value)
        return

    def getHasRankReceived(self):
        return self._getBool(6)

    def setHasRankReceived(self, value):
        self._setBool(6, value)
        return

    def getHasStatisticsCalculated(self):
        return self._getBool(7)

    def setHasStatisticsCalculated(self, value):
        self._setBool(7, value)
        return

    def getRank(self):
        return Rank(self._getNumber(8))

    def setRank(self, value):
        self._setNumber(8, value.value)
        return

    def getDivision(self):
        return Division(self._getNumber(9))

    def setDivision(self, value):
        self._setNumber(9, value.value)
        return

    def _initialize(self):
        super(YearlyStatisticsSeasonModel, self)._initialize()
        self._addViewModelProperty(b'season', SeasonModel())
        self._addNumberProperty(b'rating', 0)
        self._addNumberProperty(b'singleBattlesCount', 0)
        self._addRealProperty(b'singleBattlesWinRate', 0.0)
        self._addNumberProperty(b'superPlatoonBattlesCount', 0)
        self._addRealProperty(b'superPlatoonBattlesWinRate', 0.0)
        self._addBoolProperty(b'hasRankReceived', False)
        self._addBoolProperty(b'hasStatisticsCalculated', False)
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'division')
        return
