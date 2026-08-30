from frameworks.wulf import ViewModel

class UniversalFlagBackground(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(UniversalFlagBackground, self).__init__(properties=properties, commands=commands)
        return

    def getActive(self):
        return self._getString(0)

    def setActive(self, value):
        self._setString(0, value)
        return

    def getActiveHover(self):
        return self._getString(1)

    def setActiveHover(self, value):
        self._setString(1, value)
        return

    def getDisabled(self):
        return self._getString(2)

    def setDisabled(self, value):
        self._setString(2, value)
        return

    def getDisabledHover(self):
        return self._getString(3)

    def setDisabledHover(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(UniversalFlagBackground, self)._initialize()
        self._addStringProperty(b'active', b'')
        self._addStringProperty(b'activeHover', b'')
        self._addStringProperty(b'disabled', b'')
        self._addStringProperty(b'disabledHover', b'')
        return
