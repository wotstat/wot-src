from enum import Enum
from frameworks.wulf import ViewModel

class TipType(Enum):
    INFO = b'info'
    ERROR = b'error'


class InfoTipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(InfoTipModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getText(self):
        return self._getString(1)

    def setText(self, value):
        self._setString(1, value)
        return

    def getType(self):
        return TipType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(InfoTipModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'text', b'')
        self._addStringProperty(b'type')
        return
