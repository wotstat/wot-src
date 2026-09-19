from enum import Enum
from frameworks.wulf import Array
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.player_model import PlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import TeamStatsModel

class FortRushColumnType(Enum):
    SQUAD = b'squad'
    PLAYER = b'player'
    DAMAGE = b'damage'
    FRAG = b'frag'
    RESPAWNS = b'respawns'
    FORTRUSHSCORE = b'fortRushScore'


class BattleTeamStatsModel(TeamStatsModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(BattleTeamStatsModel, self).__init__(properties=properties, commands=commands)
        return

    def getAllies(self):
        return self._getArray(5)

    def setAllies(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getAlliesType():
        return PlayerModel

    def getEnemies(self):
        return self._getArray(6)

    def setEnemies(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getEnemiesType():
        return PlayerModel

    def getSortingColumn(self):
        return FortRushColumnType(self._getString(7))

    def setSortingColumn(self, value):
        self._setString(7, value.value)
        return

    def _initialize(self):
        super(BattleTeamStatsModel, self)._initialize()
        self._addArrayProperty(b'allies', Array())
        self._addArrayProperty(b'enemies', Array())
        self._addStringProperty(b'sortingColumn', FortRushColumnType.PLAYER.value)
        return
