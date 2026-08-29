from gui.impl.gen import R
from frameworks.wulf import ViewModel

class CommanderCmpPerkModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CommanderCmpPerkModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getResource(0)

    def setIcon(self, value):
        self._setResource(0, value)
        return

    def getTooltipID(self):
        return self._getString(1)

    def setTooltipID(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(CommanderCmpPerkModel, self)._initialize()
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'tooltipID', b'')
        return
