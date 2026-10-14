from enum import Enum
from frameworks.wulf import ViewModel

class ClipState(Enum):
    NONE = b'none'
    NORMAL = b'normal'
    CRITICAL = b'critical'


class ExtraShotClipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ExtraShotClipModel, self).__init__(properties=properties, commands=commands)
        return

    def getClipCapacity(self):
        return self._getNumber(0)

    def setClipCapacity(self, value):
        self._setNumber(0, value)
        return

    def getQuantityInClip(self):
        return self._getNumber(1)

    def setQuantityInClip(self, value):
        self._setNumber(1, value)
        return

    def getClipState(self):
        return ClipState(self._getString(2))

    def setClipState(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(ExtraShotClipModel, self)._initialize()
        self._addNumberProperty(b'clipCapacity', -1)
        self._addNumberProperty(b'quantityInClip', -1)
        self._addStringProperty(b'clipState', ClipState.NONE.value)
        return
