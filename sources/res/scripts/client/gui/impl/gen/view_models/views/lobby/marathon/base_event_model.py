from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BaseEventModel(ViewModel):
    __slots__ = (b'onAction',)

    def __init__(self, properties=2, commands=1):
        super(BaseEventModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)
        return

    def _initialize(self):
        super(BaseEventModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addResourceProperty(b'title', R.invalid())
        self.onAction = self._addCommand(b'onAction')
        return
