from comp7.gui.impl.gen.view_models.views.lobby.enums import Division, Rank, SeasonName
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.summary_statistics_model import SummaryStatisticsModel
from comp7.gui.impl.gen.view_models.views.lobby.vehicle_statistics_model import VehicleStatisticsModel

class SeasonStatisticsModel(ViewModel):
    __slots__ = (b'onClose',)
    DEFAULT_POSITION = -1

    def __init__(self, properties=12, commands=1):
        super(SeasonStatisticsModel, self).__init__(properties=properties, commands=commands)
        return

    def getSeason(self):
        return SeasonName(self._getString(0))

    def setSeason(self, value):
        self._setString(0, value.value)
        return

    def getUserName(self):
        return self._getString(1)

    def setUserName(self, value):
        self._setString(1, value)
        return

    def getClanTag(self):
        return self._getString(2)

    def setClanTag(self, value):
        self._setString(2, value)
        return

    def getClanTagColor(self):
        return self._getString(3)

    def setClanTagColor(self, value):
        self._setString(3, value)
        return

    def getScore(self):
        return self._getNumber(4)

    def setScore(self, value):
        self._setNumber(4, value)
        return

    def getRank(self):
        return Rank(self._getNumber(5))

    def setRank(self, value):
        self._setNumber(5, value.value)
        return

    def getDivision(self):
        return Division(self._getNumber(6))

    def setDivision(self, value):
        self._setNumber(6, value.value)
        return

    def getLeaderboardPosition(self):
        return self._getNumber(7)

    def setLeaderboardPosition(self, value):
        self._setNumber(7, value)
        return

    def getAchievedSeasonPoints(self):
        return self._getNumber(8)

    def setAchievedSeasonPoints(self, value):
        self._setNumber(8, value)
        return

    def getSeasonPointsLimit(self):
        return self._getNumber(9)

    def setSeasonPointsLimit(self, value):
        self._setNumber(9, value)
        return

    def getSummaryStatistics(self):
        return self._getArray(10)

    def setSummaryStatistics(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getSummaryStatisticsType():
        return SummaryStatisticsModel

    def getVehicleStatistics(self):
        return self._getArray(11)

    def setVehicleStatistics(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getVehicleStatisticsType():
        return VehicleStatisticsModel

    def _initialize(self):
        super(SeasonStatisticsModel, self)._initialize()
        self._addStringProperty(b'season')
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'clanTag', b'')
        self._addStringProperty(b'clanTagColor', b'')
        self._addNumberProperty(b'score', 0)
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'division')
        self._addNumberProperty(b'leaderboardPosition', -1)
        self._addNumberProperty(b'achievedSeasonPoints', 0)
        self._addNumberProperty(b'seasonPointsLimit', 0)
        self._addArrayProperty(b'summaryStatistics', Array())
        self._addArrayProperty(b'vehicleStatistics', Array())
        self.onClose = self._addCommand(b'onClose')
        return
