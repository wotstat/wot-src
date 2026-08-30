from enum import Enum
from frameworks.wulf import ViewModel

class HeaderType(Enum):
    NORMAL = b'normal'
    ATTENTION = b'attention'
    ALERT = b'alert'
    BLOCKER = b'blocker'


class SimpleIconTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SimpleIconTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)
        return

    def getHeader(self):
        return self._getString(1)

    def setHeader(self, value):
        self._setString(1, value)
        return

    def getBody(self):
        return self._getString(2)

    def setBody(self, value):
        self._setString(2, value)
        return

    def getHeaderType(self):
        return HeaderType(self._getString(3))

    def setHeaderType(self, value):
        self._setString(3, value.value)
        return

    def _initialize(self):
        super(SimpleIconTooltipModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'header', b'')
        self._addStringProperty(b'body', b'')
        self._addStringProperty(b'headerType')
        return
