from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_personalInfo_model import NyPersonalinfoModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_player_model import NyPlayerModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_tabs_model import NyTabsModel

class State(Enum):
    INITIAL = b'initial'
    SUCCESS = b'success'
    ERROR = b'error'
    RECALC = b'Recalc'


class LastAction(Enum):
    PAGE = b'page'
    TOP = b'top'
    PLAYER = b'player'


class NyLeaderboardModel(ViewModel):
    __slots__ = (b'onClose', b'onTypeSelect', b'onInfoClick', b'onRewardsClick', b'onPersonalPositionClick', b'onRefresh', b'onPageClick', b'onTopClick')

    def __init__(self, properties=20, commands=8):
        super(NyLeaderboardModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def selfRank(self):
        return self._getViewModel(0)

    @staticmethod
    def getSelfRankType():
        return NyPlayerModel

    @property
    def personalInfoWeekly(self):
        return self._getViewModel(1)

    @staticmethod
    def getPersonalInfoWeeklyType():
        return NyPersonalinfoModel

    @property
    def personalInfoAll(self):
        return self._getViewModel(2)

    @staticmethod
    def getPersonalInfoAllType():
        return NyPersonalinfoModel

    def getCurrentTabIdx(self):
        return self._getNumber(3)

    def setCurrentTabIdx(self, value):
        self._setNumber(3, value)
        return

    def getState(self):
        return State(self._getString(4))

    def setState(self, value):
        self._setString(4, value.value)
        return

    def getLastAction(self):
        return LastAction(self._getString(5))

    def setLastAction(self, value):
        self._setString(5, value.value)
        return

    def getIsLoading(self):
        return self._getBool(6)

    def setIsLoading(self, value):
        self._setBool(6, value)
        return

    def getUpdatedTimestamp(self):
        return self._getNumber(7)

    def setUpdatedTimestamp(self, value):
        self._setNumber(7, value)
        return

    def getStage(self):
        return self._getNumber(8)

    def setStage(self, value):
        self._setNumber(8, value)
        return

    def getTop(self):
        return self._getNumber(9)

    def setTop(self, value):
        self._setNumber(9, value)
        return

    def getPointsToTop(self):
        return self._getNumber(10)

    def setPointsToTop(self, value):
        self._setNumber(10, value)
        return

    def getCurrentTab(self):
        return self._getNumber(11)

    def setCurrentTab(self, value):
        self._setNumber(11, value)
        return

    def getPagesCount(self):
        return self._getNumber(12)

    def setPagesCount(self, value):
        self._setNumber(12, value)
        return

    def getCurrentPage(self):
        return self._getNumber(13)

    def setCurrentPage(self, value):
        self._setNumber(13, value)
        return

    def getIsRewardsCheck(self):
        return self._getBool(14)

    def setIsRewardsCheck(self, value):
        self._setBool(14, value)
        return

    def getIsVehicleAvailable(self):
        return self._getBool(15)

    def setIsVehicleAvailable(self, value):
        self._setBool(15, value)
        return

    def getIsFinal(self):
        return self._getBool(16)

    def setIsFinal(self, value):
        self._setBool(16, value)
        return

    def getWasInLeaderboard(self):
        return self._getBool(17)

    def setWasInLeaderboard(self, value):
        self._setBool(17, value)
        return

    def getPlayers(self):
        return self._getArray(18)

    def setPlayers(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getPlayersType():
        return NyPlayerModel

    def getTabs(self):
        return self._getArray(19)

    def setTabs(self, value):
        self._setArray(19, value)
        return

    @staticmethod
    def getTabsType():
        return NyTabsModel

    def _initialize(self):
        super(NyLeaderboardModel, self)._initialize()
        self._addViewModelProperty(b'selfRank', NyPlayerModel())
        self._addViewModelProperty(b'personalInfoWeekly', NyPersonalinfoModel())
        self._addViewModelProperty(b'personalInfoAll', NyPersonalinfoModel())
        self._addNumberProperty(b'currentTabIdx', 0)
        self._addStringProperty(b'state')
        self._addStringProperty(b'lastAction')
        self._addBoolProperty(b'isLoading', False)
        self._addNumberProperty(b'updatedTimestamp', 0)
        self._addNumberProperty(b'stage', 0)
        self._addNumberProperty(b'top', 0)
        self._addNumberProperty(b'pointsToTop', 0)
        self._addNumberProperty(b'currentTab', 1)
        self._addNumberProperty(b'pagesCount', 0)
        self._addNumberProperty(b'currentPage', 0)
        self._addBoolProperty(b'isRewardsCheck', False)
        self._addBoolProperty(b'isVehicleAvailable', False)
        self._addBoolProperty(b'isFinal', False)
        self._addBoolProperty(b'wasInLeaderboard', True)
        self._addArrayProperty(b'players', Array())
        self._addArrayProperty(b'tabs', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onTypeSelect = self._addCommand(b'onTypeSelect')
        self.onInfoClick = self._addCommand(b'onInfoClick')
        self.onRewardsClick = self._addCommand(b'onRewardsClick')
        self.onPersonalPositionClick = self._addCommand(b'onPersonalPositionClick')
        self.onRefresh = self._addCommand(b'onRefresh')
        self.onPageClick = self._addCommand(b'onPageClick')
        self.onTopClick = self._addCommand(b'onTopClick')
        return
