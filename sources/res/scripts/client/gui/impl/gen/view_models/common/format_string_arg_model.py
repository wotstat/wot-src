from frameworks.wulf import ViewModel
from gui.impl.gen import R

class FormatStringArgModel(ViewModel):
    __slots__ = ()
    ALIGN_LEFT = b'left'
    ALIGN_RIGHT = b'right'
    ALIGN_CENTER = b'center'

    def __init__(self, properties=5, commands=0):
        super(FormatStringArgModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getStyle(self):
        return self._getResource(2)

    def setStyle(self, value):
        self._setResource(2, value)
        return

    def getAlign(self):
        return self._getString(3)

    def setAlign(self, value):
        self._setString(3, value)
        return

    def getHardSpace(self):
        return self._getBool(4)

    def setHardSpace(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(FormatStringArgModel, self)._initialize()
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'name', b'')
        self._addResourceProperty(b'style', R.invalid())
        self._addStringProperty(b'align', b'left')
        self._addBoolProperty(b'hardSpace', False)
        return
