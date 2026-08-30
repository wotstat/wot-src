from frameworks.wulf import ViewModel
from gui.impl.gen import R

class TabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TabModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)
        return

    def _initialize(self):
        super(TabModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addResourceProperty(b'title', R.invalid())
        return
