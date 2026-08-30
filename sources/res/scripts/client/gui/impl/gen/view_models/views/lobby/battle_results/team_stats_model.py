from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.player_model import PlayerModel

class SortingOrder(Enum):
    ASC = b'ascending'
    DESC = b'descending'


class TeamStatsModel(ViewModel):
    __slots__ = (b'onStatsSorted',)

    def __init__(self, properties=5, commands=1):
        super(TeamStatsModel, self).__init__(properties=properties, commands=commands)
        return

    def getAllies(self):
        return self._getArray(0)

    def setAllies(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getAlliesType():
        return PlayerModel

    def getEnemies(self):
        return self._getArray(1)

    def setEnemies(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getEnemiesType():
        return PlayerModel

    def getShownValueColumns(self):
        return self._getArray(2)

    def setShownValueColumns(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getShownValueColumnsType():
        return unicode

    def getSortingColumn(self):
        return self._getString(3)

    def setSortingColumn(self, value):
        self._setString(3, value)
        return

    def getSortingOrder(self):
        return SortingOrder(self._getString(4))

    def setSortingOrder(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(TeamStatsModel, self)._initialize()
        self._addArrayProperty(b'allies', Array())
        self._addArrayProperty(b'enemies', Array())
        self._addArrayProperty(b'shownValueColumns', Array())
        self._addStringProperty(b'sortingColumn', b'xp')
        self._addStringProperty(b'sortingOrder', SortingOrder.DESC.value)
        self.onStatsSorted = self._addCommand(b'onStatsSorted')
        return
