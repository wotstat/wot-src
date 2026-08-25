from enum import Enum
from frameworks.wulf import Array
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.player_model import PlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import TeamStatsModel

class FrontlineColumnType(Enum):
    SQUAD = b'squad'
    PLAYER = b'player'
    RANK = b'rank'
    DAMAGE = b'damage'
    FRAG = b'frag'
    XP = b'xp'
    RESPAWNS = b'respawns'
    MEDAL = b'medal'


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
        return FrontlineColumnType(self._getString(7))

    def setSortingColumn(self, value):
        self._setString(7, value.value)
        return

    def _initialize(self):
        super(BattleTeamStatsModel, self)._initialize()
        self._addArrayProperty(b'allies', Array())
        self._addArrayProperty(b'enemies', Array())
        self._addStringProperty(b'sortingColumn', FrontlineColumnType.PLAYER.value)
        return
