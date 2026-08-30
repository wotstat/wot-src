from enum import Enum
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.match_model import MatchModel
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.team_model import TeamModel

class OverviewState(Enum):
    SCHEDULE = b'schedule'
    LIVE = b'live'
    FINALRESULT = b'finalResult'
    ERROR = b'error'


class Streaming(Enum):
    TWITCH = b'twitch'
    HUYA = b'huya'
    YOUTUBE = b'youtube'
    DOUYIN = b'douyin'


class PageState(Enum):
    LOADING = b'loading'
    CONTENT = b'content'


class TournamentViewModel(ViewModel):
    __slots__ = (b'onWatchStreamingOne', b'onWatchStreamingTwo', b'onGoToShop', b'onGoToTokenStore', b'onRefresh', b'onClose', b'pollServerTime')

    def __init__(self, properties=12, commands=7):
        super(TournamentViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getOverviewState(self):
        return OverviewState(self._getString(0))

    def setOverviewState(self, value):
        self._setString(0, value.value)
        return

    def getPageState(self):
        return PageState(self._getString(1))

    def setPageState(self, value):
        self._setString(1, value.value)
        return

    def getPrizeFund(self):
        return self._getNumber(2)

    def setPrizeFund(self, value):
        self._setNumber(2, value)
        return

    def getIsDynamicPrizePool(self):
        return self._getBool(3)

    def setIsDynamicPrizePool(self, value):
        self._setBool(3, value)
        return

    def getLastPrizePoolUpdate(self):
        return self._getNumber(4)

    def setLastPrizePoolUpdate(self, value):
        self._setNumber(4, value)
        return

    def getIsRefreshing(self):
        return self._getBool(5)

    def setIsRefreshing(self, value):
        self._setBool(5, value)
        return

    def getTokenStoreAvailabilityTimestamp(self):
        return self._getNumber(6)

    def setTokenStoreAvailabilityTimestamp(self, value):
        self._setNumber(6, value)
        return

    def getServerTimestamp(self):
        return self._getNumber(7)

    def setServerTimestamp(self, value):
        self._setNumber(7, value)
        return

    def getSchedule(self):
        return self._getArray(8)

    def setSchedule(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getScheduleType():
        return MatchModel

    def getFundDistribution(self):
        return self._getArray(9)

    def setFundDistribution(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getFundDistributionType():
        return TeamModel

    def getStreamingWithDrops(self):
        return Streaming(self._getString(10))

    def setStreamingWithDrops(self, value):
        self._setString(10, value.value)
        return

    def getStreamingWithoutDrops(self):
        return Streaming(self._getString(11))

    def setStreamingWithoutDrops(self, value):
        self._setString(11, value.value)
        return

    def _initialize(self):
        super(TournamentViewModel, self)._initialize()
        self._addStringProperty(b'overviewState')
        self._addStringProperty(b'pageState')
        self._addNumberProperty(b'prizeFund', 0)
        self._addBoolProperty(b'isDynamicPrizePool', False)
        self._addNumberProperty(b'lastPrizePoolUpdate', 0)
        self._addBoolProperty(b'isRefreshing', False)
        self._addNumberProperty(b'tokenStoreAvailabilityTimestamp', 0)
        self._addNumberProperty(b'serverTimestamp', 0)
        self._addArrayProperty(b'schedule', Array())
        self._addArrayProperty(b'fundDistribution', Array())
        self._addStringProperty(b'streamingWithDrops')
        self._addStringProperty(b'streamingWithoutDrops')
        self.onWatchStreamingOne = self._addCommand(b'onWatchStreamingOne')
        self.onWatchStreamingTwo = self._addCommand(b'onWatchStreamingTwo')
        self.onGoToShop = self._addCommand(b'onGoToShop')
        self.onGoToTokenStore = self._addCommand(b'onGoToTokenStore')
        self.onRefresh = self._addCommand(b'onRefresh')
        self.onClose = self._addCommand(b'onClose')
        self.pollServerTime = self._addCommand(b'pollServerTime')
        return
