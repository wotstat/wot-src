from enum import IntEnum
from frameworks.wulf import ViewModel

class CrosshairType(IntEnum):
    UNDEFINED = 0
    ARCADE = 1
    SNIPER = 2
    STRATEGIC = 3
    POSTMORTEM = 4


class CrosshairStateModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CrosshairStateModel, self).__init__(properties=properties, commands=commands)
        return

    def getCrosshairType(self):
        return CrosshairType(self._getNumber(0))

    def setCrosshairType(self, value):
        self._setNumber(0, value.value)
        return

    def getZoomFactor(self):
        return self._getNumber(1)

    def setZoomFactor(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(CrosshairStateModel, self)._initialize()
        self._addNumberProperty(b'crosshairType')
        self._addNumberProperty(b'zoomFactor', 1)
        return
