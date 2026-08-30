from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.postbattle.player_model import PlayerModel

class TeamStatsModel(ViewModel):
    __slots__ = ()
    ALLIES_TEAM_ALIAS = b'allies'
    ENEMIES_TEAM_ALIAS = b'enemies'

    def __init__(self, properties=2, commands=0):
        super(TeamStatsModel, self).__init__(properties=properties, commands=commands)
        return

    def getEnemies(self):
        return self._getArray(0)

    def setEnemies(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getEnemiesType():
        return PlayerModel

    def getAllies(self):
        return self._getArray(1)

    def setAllies(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getAlliesType():
        return PlayerModel

    def _initialize(self):
        super(TeamStatsModel, self)._initialize()
        self._addArrayProperty(b'enemies', Array())
        self._addArrayProperty(b'allies', Array())
        return
