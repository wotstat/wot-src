from enum import Enum
from frameworks.wulf import Array
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_player_model import Comp7PlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import TeamStatsModel

class Comp7ColumnType(Enum):
    SQUAD = b'squad'
    RANK = b'rank'
    PLAYER = b'player'
    DAMAGE = b'damage'
    FRAG = b'frag'
    XP = b'xp'
    VEHICLE = b'tank'
    MEDAL = b'medal'
    PRESTIGEPOINTS = b'prestigePoints'


class Comp7TeamStatsModel(TeamStatsModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(Comp7TeamStatsModel, self).__init__(properties=properties, commands=commands)
        return

    def getAllies(self):
        return self._getArray(5)

    def setAllies(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getAlliesType():
        return Comp7PlayerModel

    def getEnemies(self):
        return self._getArray(6)

    def setEnemies(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getEnemiesType():
        return Comp7PlayerModel

    def getSortingColumn(self):
        return Comp7ColumnType(self._getString(7))

    def setSortingColumn(self, value):
        self._setString(7, value.value)
        return

    def _initialize(self):
        super(Comp7TeamStatsModel, self)._initialize()
        self._addArrayProperty(b'allies', Array())
        self._addArrayProperty(b'enemies', Array())
        self._addStringProperty(b'sortingColumn', Comp7ColumnType.PLAYER.value)
        return
