from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_rows_model import GameModeRowsModel

class BattleRoyaleConditionsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattleRoyaleConditionsModel, self).__init__(properties=properties, commands=commands)
        return

    def getSolo(self):
        return self._getArray(0)

    def setSolo(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getSoloType():
        return GameModeRowsModel

    def getSquad(self):
        return self._getArray(1)

    def setSquad(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSquadType():
        return GameModeRowsModel

    def _initialize(self):
        super(BattleRoyaleConditionsModel, self)._initialize()
        self._addArrayProperty(b'solo', Array())
        self._addArrayProperty(b'squad', Array())
        return
