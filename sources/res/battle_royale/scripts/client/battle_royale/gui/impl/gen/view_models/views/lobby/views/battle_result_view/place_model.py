from frameworks.wulf import Array, ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.row_model import RowModel

class PlaceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PlaceModel, self).__init__(properties=properties, commands=commands)
        return

    def getPlace(self):
        return self._getString(0)

    def setPlace(self, value):
        self._setString(0, value)
        return

    def getIsSquadMode(self):
        return self._getBool(1)

    def setIsSquadMode(self, value):
        self._setBool(1, value)
        return

    def getPlayersList(self):
        return self._getArray(2)

    def setPlayersList(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getPlayersListType():
        return RowModel

    def _initialize(self):
        super(PlaceModel, self)._initialize()
        self._addStringProperty(b'place', b'')
        self._addBoolProperty(b'isSquadMode', False)
        self._addArrayProperty(b'playersList', Array())
        return
