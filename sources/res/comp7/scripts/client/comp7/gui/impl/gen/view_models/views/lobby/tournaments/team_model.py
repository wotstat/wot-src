from frameworks.wulf import ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.team_logos_model import TeamLogosModel

class TeamModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(TeamModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def logos(self):
        return self._getViewModel(0)

    @staticmethod
    def getLogosType():
        return TeamLogosModel

    def getTeamName(self):
        return self._getString(1)

    def setTeamName(self, value):
        self._setString(1, value)
        return

    def getScore(self):
        return self._getNumber(2)

    def setScore(self, value):
        self._setNumber(2, value)
        return

    def getPrize(self):
        return self._getNumber(3)

    def setPrize(self, value):
        self._setNumber(3, value)
        return

    def getSharedPositionFrom(self):
        return self._getNumber(4)

    def setSharedPositionFrom(self, value):
        self._setNumber(4, value)
        return

    def getSharedPositionTo(self):
        return self._getNumber(5)

    def setSharedPositionTo(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(TeamModel, self)._initialize()
        self._addViewModelProperty(b'logos', TeamLogosModel())
        self._addStringProperty(b'teamName', b'')
        self._addNumberProperty(b'score', 0)
        self._addNumberProperty(b'prize', 0)
        self._addNumberProperty(b'sharedPositionFrom', 0)
        self._addNumberProperty(b'sharedPositionTo', 0)
        return
