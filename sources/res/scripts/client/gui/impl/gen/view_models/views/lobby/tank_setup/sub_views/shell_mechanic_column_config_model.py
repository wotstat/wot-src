from frameworks.wulf import ViewModel

class ShellMechanicColumnConfigModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ShellMechanicColumnConfigModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)
        return

    def getSubtype(self):
        return self._getString(1)

    def setSubtype(self, value):
        self._setString(1, value)
        return

    def getWithTextLabel(self):
        return self._getBool(2)

    def setWithTextLabel(self, value):
        self._setBool(2, value)
        return

    def getWithRichTooltip(self):
        return self._getBool(3)

    def setWithRichTooltip(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(ShellMechanicColumnConfigModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        self._addStringProperty(b'subtype', b'')
        self._addBoolProperty(b'withTextLabel', False)
        self._addBoolProperty(b'withRichTooltip', True)
        return
