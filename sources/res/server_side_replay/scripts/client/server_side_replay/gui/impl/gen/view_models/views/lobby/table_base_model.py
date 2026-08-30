from enum import Enum, IntEnum
from frameworks.wulf import Array, ViewModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.replay_model import ReplayModel

class StatParams(Enum):
    EARNEDXP = b'earnedXp'
    DAMAGEDEALT = b'damageDealt'
    DAMAGEASSISTED = b'damageAssisted'
    DAMAGEBLOCKEDBYARMOR = b'damageBlockedByArmor'
    KILLS = b'kills'
    MARKSOFMASTERY = b'marksOfMastery'
    DATE = b'date'


class State(IntEnum):
    INITIAL = 0
    SUCCESS = 1
    ERROR = 2


class TableBaseModel(ViewModel):
    __slots__ = (b'onResetFilter', b'onSort', b'onRefresh', b'onWatch')
    DEFAULT_REPLAY_INDEX = -1

    def __init__(self, properties=7, commands=4):
        super(TableBaseModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getNumber(0))

    def setState(self, value):
        self._setNumber(0, value.value)
        return

    def getIsLoading(self):
        return self._getBool(1)

    def setIsLoading(self, value):
        self._setBool(1, value)
        return

    def getIsPopoverEnabled(self):
        return self._getBool(2)

    def setIsPopoverEnabled(self, value):
        self._setBool(2, value)
        return

    def getIsPopoverHighlighted(self):
        return self._getBool(3)

    def setIsPopoverHighlighted(self, value):
        self._setBool(3, value)
        return

    def getSelectedSorting(self):
        return StatParams(self._getString(4))

    def setSelectedSorting(self, value):
        self._setString(4, value.value)
        return

    def getItems(self):
        return self._getArray(5)

    def setItems(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getItemsType():
        return ReplayModel

    def getInitialReplayIndex(self):
        return self._getNumber(6)

    def setInitialReplayIndex(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(TableBaseModel, self)._initialize()
        self._addNumberProperty(b'state')
        self._addBoolProperty(b'isLoading', False)
        self._addBoolProperty(b'isPopoverEnabled', True)
        self._addBoolProperty(b'isPopoverHighlighted', False)
        self._addStringProperty(b'selectedSorting', StatParams.EARNEDXP.value)
        self._addArrayProperty(b'items', Array())
        self._addNumberProperty(b'initialReplayIndex', -1)
        self.onResetFilter = self._addCommand(b'onResetFilter')
        self.onSort = self._addCommand(b'onSort')
        self.onRefresh = self._addCommand(b'onRefresh')
        self.onWatch = self._addCommand(b'onWatch')
        return
