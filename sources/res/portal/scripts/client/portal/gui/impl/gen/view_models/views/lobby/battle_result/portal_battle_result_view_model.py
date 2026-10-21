from enum import Enum
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.battle_result.leader_board.leaderboard_model import LeaderboardModel
from portal.gui.impl.gen.view_models.views.lobby.battle_result.player_results.personal_results_model import PersonalResultsModel

class FinishResultType(Enum):
    DEFAULT_WIN = b'default_win'
    SUPER_BOSS_WIN = b'super_boss_win'
    TIME_OUT_DEFEAT = b'timeout_defeat'
    PLAYER_BASE_CAPTURED_DEFEAT = b'player_base_captured_defeat'
    TECHNICAL_DEFEAT = b'technical_defeat'


class PortalBattleResultViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=11, commands=1):
        super(PortalBattleResultViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def playerResultsModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getPlayerResultsModelType():
        return PersonalResultsModel

    @property
    def leaderboardModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getLeaderboardModelType():
        return LeaderboardModel

    def getFinishResultTitle(self):
        return self._getResource(2)

    def setFinishResultTitle(self, value):
        self._setResource(2, value)
        return

    def getFinishResultType(self):
        return FinishResultType(self._getString(3))

    def setFinishResultType(self, value):
        self._setString(3, value.value)
        return

    def getFinishResultDescr(self):
        return self._getString(4)

    def setFinishResultDescr(self, value):
        self._setString(4, value)
        return

    def getBattleDifficulty(self):
        return self._getNumber(5)

    def setBattleDifficulty(self, value):
        self._setNumber(5, value)
        return

    def getPlayerName(self):
        return self._getString(6)

    def setPlayerName(self, value):
        self._setString(6, value)
        return

    def getClanAbbrev(self):
        return self._getString(7)

    def setClanAbbrev(self, value):
        self._setString(7, value)
        return

    def getBattleDuration(self):
        return self._getString(8)

    def setBattleDuration(self, value):
        self._setString(8, value)
        return

    def getArenaStartDateTime(self):
        return self._getString(9)

    def setArenaStartDateTime(self, value):
        self._setString(9, value)
        return

    def getPlayerVehicleName(self):
        return self._getString(10)

    def setPlayerVehicleName(self, value):
        self._setString(10, value)
        return

    def _initialize(self):
        super(PortalBattleResultViewModel, self)._initialize()
        self._addViewModelProperty(b'playerResultsModel', PersonalResultsModel())
        self._addViewModelProperty(b'leaderboardModel', LeaderboardModel())
        self._addResourceProperty(b'finishResultTitle', R.invalid())
        self._addStringProperty(b'finishResultType')
        self._addStringProperty(b'finishResultDescr', b'')
        self._addNumberProperty(b'battleDifficulty', 0)
        self._addStringProperty(b'playerName', b'')
        self._addStringProperty(b'clanAbbrev', b'')
        self._addStringProperty(b'battleDuration', b'')
        self._addStringProperty(b'arenaStartDateTime', b'')
        self._addStringProperty(b'playerVehicleName', b'')
        self.onClose = self._addCommand(b'onClose')
        return
