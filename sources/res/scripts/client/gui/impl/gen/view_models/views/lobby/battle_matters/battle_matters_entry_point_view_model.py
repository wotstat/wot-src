from enum import IntEnum
from frameworks.wulf import ViewModel

class State(IntEnum):
    NORMAL = 0
    HASTOKEN = 1
    ERROR = 2


class BattleMattersEntryPointViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=5, commands=1):
        super(BattleMattersEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentProgress(self):
        return self._getNumber(0)

    def setCurrentProgress(self, value):
        self._setNumber(0, value)
        return

    def getMaxProgress(self):
        return self._getNumber(1)

    def setMaxProgress(self, value):
        self._setNumber(1, value)
        return

    def getQuestNumber(self):
        return self._getNumber(2)

    def setQuestNumber(self, value):
        self._setNumber(2, value)
        return

    def getIsCompleted(self):
        return self._getBool(3)

    def setIsCompleted(self, value):
        self._setBool(3, value)
        return

    def getState(self):
        return State(self._getNumber(4))

    def setState(self, value):
        self._setNumber(4, value.value)
        return

    def _initialize(self):
        super(BattleMattersEntryPointViewModel, self)._initialize()
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'maxProgress', 0)
        self._addNumberProperty(b'questNumber', 0)
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'state')
        self.onClick = self._addCommand(b'onClick')
        return
