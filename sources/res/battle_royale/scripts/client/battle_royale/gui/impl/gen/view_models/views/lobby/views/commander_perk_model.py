from frameworks.wulf import ViewModel

class CommanderPerkModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CommanderPerkModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getTooltipID(self):
        return self._getString(1)

    def setTooltipID(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(CommanderPerkModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'tooltipID', b'')
        return
