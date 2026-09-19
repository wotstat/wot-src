from enum import Enum
from frameworks.wulf import ViewModel

class ClipState(Enum):
    NONE = b'none'
    NORMAL = b'normal'
    CRITICAL = b'critical'


class ShellCalibrationClipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ShellCalibrationClipModel, self).__init__(properties=properties, commands=commands)
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

    def getTotalAmmo(self):
        return self._getNumber(2)

    def setTotalAmmo(self, value):
        self._setNumber(2, value)
        return

    def getClipState(self):
        return ClipState(self._getString(3))

    def setClipState(self, value):
        self._setString(3, value.value)
        return

    def getCalibrationState(self):
        return self._getNumber(4)

    def setCalibrationState(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(ShellCalibrationClipModel, self)._initialize()
        self._addNumberProperty(b'clipCapacity', -1)
        self._addNumberProperty(b'quantityInClip', -1)
        self._addNumberProperty(b'totalAmmo', -1)
        self._addStringProperty(b'clipState', ClipState.NONE.value)
        self._addNumberProperty(b'calibrationState', 0)
        return
