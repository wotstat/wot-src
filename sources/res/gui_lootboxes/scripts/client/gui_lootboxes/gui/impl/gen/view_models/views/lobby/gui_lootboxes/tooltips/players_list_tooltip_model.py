from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.tooltips.player_info_model import PlayerInfoModel

class PlayersListTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PlayersListTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAllNamesLoaded(self):
        return self._getBool(0)

    def setIsAllNamesLoaded(self, value):
        self._setBool(0, value)
        return

    def getPlayersCount(self):
        return self._getNumber(1)

    def setPlayersCount(self, value):
        self._setNumber(1, value)
        return

    def getPlayers(self):
        return self._getArray(2)

    def setPlayers(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getPlayersType():
        return PlayerInfoModel

    def _initialize(self):
        super(PlayersListTooltipModel, self)._initialize()
        self._addBoolProperty(b'isAllNamesLoaded', True)
        self._addNumberProperty(b'playersCount', 0)
        self._addArrayProperty(b'players', Array())
        return
