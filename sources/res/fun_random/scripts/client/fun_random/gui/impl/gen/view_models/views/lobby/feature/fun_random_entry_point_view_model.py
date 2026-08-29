from enum import IntEnum
from frameworks.wulf import ViewModel

class State(IntEnum):
    BEFORE = 0
    ACTIVE = 1
    NOTPRIMETIME = 2
    AFTER = 3


class FunRandomEntryPointViewModel(ViewModel):
    __slots__ = (b'onActionClick',)

    def __init__(self, properties=5, commands=1):
        super(FunRandomEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStartTime(self):
        return self._getNumber(0)

    def setStartTime(self, value):
        self._setNumber(0, value)
        return

    def getEndTime(self):
        return self._getNumber(1)

    def setEndTime(self, value):
        self._setNumber(1, value)
        return

    def getLeftTime(self):
        return self._getNumber(2)

    def setLeftTime(self, value):
        self._setNumber(2, value)
        return

    def getState(self):
        return State(self._getNumber(3))

    def setState(self, value):
        self._setNumber(3, value.value)
        return

    def getAssetsPointer(self):
        return self._getString(4)

    def setAssetsPointer(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(FunRandomEntryPointViewModel, self)._initialize()
        self._addNumberProperty(b'startTime', -1)
        self._addNumberProperty(b'endTime', -1)
        self._addNumberProperty(b'leftTime', -1)
        self._addNumberProperty(b'state')
        self._addStringProperty(b'assetsPointer', b'undefined')
        self.onActionClick = self._addCommand(b'onActionClick')
        return
