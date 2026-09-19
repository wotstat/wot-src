from enum import Enum
from frameworks.wulf import ViewModel

class FortRushBaseCaptureTeam(Enum):
    NEUTRAL = b'neutral'
    ALLY = b'ally'
    ENEMY = b'enemy'


class FortRushBaseCaptureState(Enum):
    IDLE = b'Idle'
    CAPTURING = b'Capturing'
    CONTESTED = b'Contested'
    DECAPPING = b'Decapping'


class FortRushHudBaseCaptureIndicatorModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FortRushHudBaseCaptureIndicatorModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabel(self):
        return self._getString(0)

    def setLabel(self, value):
        self._setString(0, value)
        return

    def getOwnerTeam(self):
        return FortRushBaseCaptureTeam(self._getString(1))

    def setOwnerTeam(self, value):
        self._setString(1, value.value)
        return

    def getCapturingTeam(self):
        return FortRushBaseCaptureTeam(self._getString(2))

    def setCapturingTeam(self, value):
        self._setString(2, value.value)
        return

    def getState(self):
        return FortRushBaseCaptureState(self._getString(3))

    def setState(self, value):
        self._setString(3, value.value)
        return

    def getCaptureProgress(self):
        return self._getReal(4)

    def setCaptureProgress(self, value):
        self._setReal(4, value)
        return

    def getUid(self):
        return self._getNumber(5)

    def setUid(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(FortRushHudBaseCaptureIndicatorModel, self)._initialize()
        self._addStringProperty(b'label', b'')
        self._addStringProperty(b'ownerTeam', FortRushBaseCaptureTeam.NEUTRAL.value)
        self._addStringProperty(b'capturingTeam', FortRushBaseCaptureTeam.NEUTRAL.value)
        self._addStringProperty(b'state', FortRushBaseCaptureState.IDLE.value)
        self._addRealProperty(b'captureProgress', 0.0)
        self._addNumberProperty(b'uid', -1)
        return
