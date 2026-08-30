from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from battle_royale.gui.impl.gen.view_models.views.lobby.views.team_model import TeamModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.user_extended_model import UserExtendedModel
from gui.impl.gen.view_models.ui_kit.gf_drop_down_item import GfDropDownItem

class PreBattleViewModel(ViewModel):
    __slots__ = (b'onBattleClick', b'onClose')

    def __init__(self, properties=5, commands=2):
        super(PreBattleViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getIsSpectator(self):
        return self._getBool(1)

    def setIsSpectator(self, value):
        self._setBool(1, value)
        return

    def getTeams(self):
        return self._getArray(2)

    def setTeams(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getTeamsType():
        return TeamModel

    def getCurrentTeam(self):
        return self._getArray(3)

    def setCurrentTeam(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getCurrentTeamType():
        return UserExtendedModel

    def getMaps(self):
        return self._getArray(4)

    def setMaps(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getMapsType():
        return GfDropDownItem

    def _initialize(self):
        super(PreBattleViewModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addBoolProperty(b'isSpectator', False)
        self._addArrayProperty(b'teams', Array())
        self._addArrayProperty(b'currentTeam', Array())
        self._addArrayProperty(b'maps', Array())
        self.onBattleClick = self._addCommand(b'onBattleClick')
        self.onClose = self._addCommand(b'onClose')
        return
