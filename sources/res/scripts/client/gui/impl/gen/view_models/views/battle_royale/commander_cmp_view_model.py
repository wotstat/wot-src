from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle_royale.commander_cmp_perk_model import CommanderCmpPerkModel

class CommanderCmpViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CommanderCmpViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getNation(self):
        return self._getString(0)

    def setNation(self, value):
        self._setString(0, value)
        return

    def getIconPostfix(self):
        return self._getString(1)

    def setIconPostfix(self, value):
        self._setString(1, value)
        return

    def getPerkList(self):
        return self._getArray(2)

    def setPerkList(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getPerkListType():
        return CommanderCmpPerkModel

    def _initialize(self):
        super(CommanderCmpViewModel, self)._initialize()
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'iconPostfix', b'')
        self._addArrayProperty(b'perkList', Array())
        return
