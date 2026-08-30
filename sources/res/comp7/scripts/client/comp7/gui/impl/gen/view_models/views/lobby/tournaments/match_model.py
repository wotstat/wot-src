from enum import Enum
from frameworks.wulf import ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.team_model import TeamModel

class MatchState(Enum):
    NOTSTARTED = b'notStarted'
    COMPLETED = b'completed'
    LIVE = b'live'


class MatchStage(Enum):
    ROUNDROBIN = b'roundRobin'
    UBSEMIFINALS = b'UBSemifinals'
    UBFINALS = b'UBFinals'
    LBROUND1 = b'LBRound1'
    LBROUND2 = b'LBRound2'
    LBSEMIFINALS = b'LBSemifinals'
    LBFINALS = b'LBFinals'
    GRANDFINALS = b'grandFinals'


class MatchModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MatchModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def team1(self):
        return self._getViewModel(0)

    @staticmethod
    def getTeam1Type():
        return TeamModel

    @property
    def team2(self):
        return self._getViewModel(1)

    @staticmethod
    def getTeam2Type():
        return TeamModel

    def getStartOfMatchTimestamp(self):
        return self._getNumber(2)

    def setStartOfMatchTimestamp(self, value):
        self._setNumber(2, value)
        return

    def getMatchStage(self):
        return MatchStage(self._getString(3))

    def setMatchStage(self, value):
        self._setString(3, value.value)
        return

    def getBestOf(self):
        return self._getNumber(4)

    def setBestOf(self, value):
        self._setNumber(4, value)
        return

    def getPhase(self):
        return self._getNumber(5)

    def setPhase(self, value):
        self._setNumber(5, value)
        return

    def getRound(self):
        return self._getNumber(6)

    def setRound(self, value):
        self._setNumber(6, value)
        return

    def getMatchState(self):
        return MatchState(self._getString(7))

    def setMatchState(self, value):
        self._setString(7, value.value)
        return

    def _initialize(self):
        super(MatchModel, self)._initialize()
        self._addViewModelProperty(b'team1', TeamModel())
        self._addViewModelProperty(b'team2', TeamModel())
        self._addNumberProperty(b'startOfMatchTimestamp', 0)
        self._addStringProperty(b'matchStage')
        self._addNumberProperty(b'bestOf', 0)
        self._addNumberProperty(b'phase', 0)
        self._addNumberProperty(b'round', 0)
        self._addStringProperty(b'matchState')
        return
