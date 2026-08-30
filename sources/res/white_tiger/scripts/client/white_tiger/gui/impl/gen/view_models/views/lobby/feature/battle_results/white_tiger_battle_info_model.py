from gui.impl.gen.view_models.views.lobby.battle_results.battle_info_model import BattleInfoModel

class WhiteTigerBattleInfoModel(BattleInfoModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(WhiteTigerBattleInfoModel, self).__init__(properties=properties, commands=commands)
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

    def _initialize(self):
        super(WhiteTigerBattleInfoModel, self)._initialize()
        self._addStringProperty(b'assetsPointer', b'undefined')
        self._addStringProperty(b'subModeAssetsPointer', b'undefined')
        return
