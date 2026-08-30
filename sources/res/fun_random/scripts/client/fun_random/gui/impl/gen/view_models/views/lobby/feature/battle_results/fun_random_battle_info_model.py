from gui.impl.gen.view_models.views.lobby.battle_results.battle_info_model import BattleInfoModel

class FunRandomBattleInfoModel(BattleInfoModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(FunRandomBattleInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getAssetsPointer(self):
        return self._getString(7)

    def setAssetsPointer(self, value):
        self._setString(7, value)
        return

    def getSubModeAssetsPointer(self):
        return self._getString(8)

    def setSubModeAssetsPointer(self, value):
        self._setString(8, value)
        return

    def getBattleType(self):
        return self._getString(9)

    def setBattleType(self, value):
        self._setString(9, value)
        return

    def _initialize(self):
        super(FunRandomBattleInfoModel, self)._initialize()
        self._addStringProperty(b'assetsPointer', b'undefined')
        self._addStringProperty(b'subModeAssetsPointer', b'undefined')
        self._addStringProperty(b'battleType', b'standard')
        return
