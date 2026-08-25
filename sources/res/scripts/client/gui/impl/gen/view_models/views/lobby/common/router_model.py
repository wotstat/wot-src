from frameworks.wulf import ViewModel

class RouterModel(ViewModel):
    __slots__ = (b'navigateTo', b'navigateBack')

    def __init__(self, properties=2, commands=2):
        super(RouterModel, self).__init__(properties=properties, commands=commands)
        return

    def getRoute(self):
        return self._getString(0)

    def setRoute(self, value):
        self._setString(0, value)
        return

    def getParams(self):
        return self._getString(1)

    def setParams(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(RouterModel, self)._initialize()
        self._addStringProperty(b'route', b'')
        self._addStringProperty(b'params', b'')
        self.navigateTo = self._addCommand(b'navigateTo')
        self.navigateBack = self._addCommand(b'navigateBack')
        return
