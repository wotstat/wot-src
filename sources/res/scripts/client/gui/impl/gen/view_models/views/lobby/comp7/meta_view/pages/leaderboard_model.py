from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.comp7.leaderboard_navigation_division_info import LeaderboardNavigationDivisionInfo
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.progression_item_model import ProgressionItemModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.table_record_model import TableRecordModel

class State(IntEnum):
    INITIAL = 0
    SUCCESS = 1
    ERROR = 2


class LeaderboardModel(ViewModel):
    __slots__ = (b'onRefresh', b'getTableRecords')
    DEFAULT_POSITION = -1
    PAGE_SIZE = 50

    def __init__(self, properties=14, commands=2):
        super(LeaderboardModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def ranks(self):
        return self._getViewModel(0)

    @staticmethod
    def getRanksType():
        return ProgressionItemModel

    def getState(self):
        return State(self._getNumber(1))

    def setState(self, value):
        self._setNumber(1, value.value)
        return

    def getIsLoading(self):
        return self._getBool(2)

    def setIsLoading(self, value):
        self._setBool(2, value)
        return

    def getPersonalPosition(self):
        return self._getNumber(3)

    def setPersonalPosition(self, value):
        self._setNumber(3, value)
        return

    def getPersonalScore(self):
        return self._getNumber(4)

    def setPersonalScore(self, value):
        self._setNumber(4, value)
        return

    def getPersonalBattlesCount(self):
        return self._getNumber(5)

    def setPersonalBattlesCount(self, value):
        self._setNumber(5, value)
        return

    def getLastBestUserPosition(self):
        return self._getNumber(6)

    def setLastBestUserPosition(self, value):
        self._setNumber(6, value)
        return

    def getLeaderboardUpdateTimestamp(self):
        return self._getNumber(7)

    def setLeaderboardUpdateTimestamp(self, value):
        self._setNumber(7, value)
        return

    def getFrom(self):
        return self._getNumber(8)

    def setFrom(self, value):
        self._setNumber(8, value)
        return

    def getTopPercentage(self):
        return self._getNumber(9)

    def setTopPercentage(self, value):
        self._setNumber(9, value)
        return

    def getRecordsCount(self):
        return self._getNumber(10)

    def setRecordsCount(self, value):
        self._setNumber(10, value)
        return

    def getOwnSpaID(self):
        return self._getNumber(11)

    def setOwnSpaID(self, value):
        self._setNumber(11, value)
        return

    def getItems(self):
        return self._getArray(12)

    def setItems(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getItemsType():
        return TableRecordModel

    def getDivisions(self):
        return self._getArray(13)

    def setDivisions(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getDivisionsType():
        return LeaderboardNavigationDivisionInfo

    def _initialize(self):
        super(LeaderboardModel, self)._initialize()
        self._addViewModelProperty(b'ranks', UserListModel())
        self._addNumberProperty(b'state')
        self._addBoolProperty(b'isLoading', False)
        self._addNumberProperty(b'personalPosition', -1)
        self._addNumberProperty(b'personalScore', 0)
        self._addNumberProperty(b'personalBattlesCount', 0)
        self._addNumberProperty(b'lastBestUserPosition', -1)
        self._addNumberProperty(b'leaderboardUpdateTimestamp', 0)
        self._addNumberProperty(b'from', 2000)
        self._addNumberProperty(b'topPercentage', 10)
        self._addNumberProperty(b'recordsCount', 0)
        self._addNumberProperty(b'ownSpaID', 0)
        self._addArrayProperty(b'items', Array())
        self._addArrayProperty(b'divisions', Array())
        self.onRefresh = self._addCommand(b'onRefresh')
        self.getTableRecords = self._addCommand(b'getTableRecords')
        return
