from frameworks.wulf import ViewModel
from gui.impl.gen import R

class FormatResourceArgModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FormatResourceArgModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getResource(0)

    def setValue(self, value):
        self._setResource(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(FormatResourceArgModel, self)._initialize()
        self._addResourceProperty(b'value', R.invalid())
        self._addStringProperty(b'name', b'')
        return
