from battle_royale.gui.impl.gen.view_models.views.lobby.enums import CoinType, SubMode
from frameworks.wulf import ViewModel

class BattleRoyaleEventModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattleRoyaleEventModel, self).__init__(properties=properties, commands=commands)
        return

    def getSubMode(self):
        return SubMode(self._getString(0))

    def setSubMode(self, value):
        self._setString(0, value.value)
        return

    def getCoinType(self):
        return CoinType(self._getString(1))

    def setCoinType(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(BattleRoyaleEventModel, self)._initialize()
        self._addStringProperty(b'subMode')
        self._addStringProperty(b'coinType')
        return
