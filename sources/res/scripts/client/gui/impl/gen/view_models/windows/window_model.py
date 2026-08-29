from gui.impl.gen import R
from frameworks.wulf import ViewModel

class WindowModel(ViewModel):
    __slots__ = (b'onClosed', b'onMinimized')

    def __init__(self, properties=3, commands=2):
        super(WindowModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getRawTitle(self):
        return self._getString(1)

    def setRawTitle(self, value):
        self._setString(1, value)
        return

    def getCanMinimize(self):
        return self._getBool(2)

    def setCanMinimize(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(WindowModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addStringProperty(b'rawTitle', b'')
        self._addBoolProperty(b'canMinimize', False)
        self.onClosed = self._addCommand(b'onClosed')
        self.onMinimized = self._addCommand(b'onMinimized')
        return
