from gui.impl.gen.view_models.views.lobby.battle_results.battle_info_model import BattleInfoModel

class RandomBattleInfoModel(BattleInfoModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(RandomBattleInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getFinishReason(self):
        return self._getNumber(7)

    def setFinishReason(self, value):
        self._setNumber(7, value)
        return

    def getFinishReasonClarification(self):
        return self._getString(8)

    def setFinishReasonClarification(self, value):
        self._setString(8, value)
        return

    def getCommendationsReceived(self):
        return self._getNumber(9)

    def setCommendationsReceived(self, value):
        self._setNumber(9, value)
        return

    def getArenaGuiType(self):
        return self._getNumber(10)

    def setArenaGuiType(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(RandomBattleInfoModel, self)._initialize()
        self._addNumberProperty(b'finishReason', 0)
        self._addStringProperty(b'finishReasonClarification', b'')
        self._addNumberProperty(b'commendationsReceived', 0)
        self._addNumberProperty(b'arenaGuiType', 0)
        return
