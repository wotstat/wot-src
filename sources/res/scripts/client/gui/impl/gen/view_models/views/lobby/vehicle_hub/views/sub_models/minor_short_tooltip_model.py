from frameworks.wulf import ViewModel
from gui.impl.gen import R

class MinorShortTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MinorShortTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getResource(0)

    def setIcon(self, value):
        self._setResource(0, value)
        return

    def getHeader(self):
        return self._getString(1)

    def setHeader(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(MinorShortTooltipModel, self)._initialize()
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'header', b'')
        self._addStringProperty(b'description', b'')
        return
