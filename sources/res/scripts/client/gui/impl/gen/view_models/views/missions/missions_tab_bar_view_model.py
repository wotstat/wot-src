from frameworks.wulf import Array, ViewModel

class MissionsTabBarViewModel(ViewModel):
    __slots__ = (b'onTabSelectionChanged',)

    def __init__(self, properties=3, commands=1):
        super(MissionsTabBarViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getViews(self):
        return self._getArray(0)

    def setViews(self, value):
        self._setArray(0, value)
        return

    def getCurrentView(self):
        return self._getString(1)

    def setCurrentView(self, value):
        self._setString(1, value)
        return

    def getStartIndex(self):
        return self._getNumber(2)

    def setStartIndex(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(MissionsTabBarViewModel, self)._initialize()
        self._addArrayProperty(b'views', Array())
        self._addStringProperty(b'currentView', b'')
        self._addNumberProperty(b'startIndex', 0)
        self.onTabSelectionChanged = self._addCommand(b'onTabSelectionChanged')
        return
