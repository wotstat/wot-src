from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ProgressLevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ProgressLevelModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getResource(2)

    def setName(self, value):
        self._setResource(2, value)
        return

    def _initialize(self):
        super(ProgressLevelModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'value', 0)
        self._addResourceProperty(b'name', R.invalid())
        return
