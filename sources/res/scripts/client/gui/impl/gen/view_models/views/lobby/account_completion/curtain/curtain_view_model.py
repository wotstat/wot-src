from enum import IntEnum
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class CurtainStateEnum(IntEnum):
    CLOSED = 0
    OPENING = 1
    OPENED = 2
    CLOSING = 3
    HIDING = 4
    HIDDEN = 5
    REVEALING = 6


class CurtainViewModel(ViewModel):
    __slots__ = (b'onMoveSpace', b'onStateTransitionComplete')

    def __init__(self, properties=4, commands=2):
        super(CurtainViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return CurtainStateEnum(self._getNumber(0))

    def setState(self, value):
        self._setNumber(0, value.value)
        return

    def getIsWaiting(self):
        return self._getBool(1)

    def setIsWaiting(self, value):
        self._setBool(1, value)
        return

    def getWaitingText(self):
        return self._getResource(2)

    def setWaitingText(self, value):
        self._setResource(2, value)
        return

    def getCurrentSubViewID(self):
        return self._getNumber(3)

    def setCurrentSubViewID(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(CurtainViewModel, self)._initialize()
        self._addNumberProperty(b'state')
        self._addBoolProperty(b'isWaiting', False)
        self._addResourceProperty(b'waitingText', R.invalid())
        self._addNumberProperty(b'currentSubViewID', 0)
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onStateTransitionComplete = self._addCommand(b'onStateTransitionComplete')
        return
