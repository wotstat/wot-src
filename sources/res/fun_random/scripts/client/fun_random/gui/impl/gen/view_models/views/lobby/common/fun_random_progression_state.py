from enum import Enum
from frameworks.wulf import ViewModel

class FunRandomProgressionStatus(Enum):
    DISABLED = b'disabled'
    ACTIVE_FINAL = b'activeFinal'
    ACTIVE_RESETTABLE = b'activeResettable'
    COMPLETED_FINAL = b'completedFinal'
    COMPLETED_RESETTABLE = b'completedResettable'


class FunRandomProgressionState(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FunRandomProgressionState, self).__init__(properties=properties, commands=commands)
        return

    def getStatus(self):
        return FunRandomProgressionStatus(self._getString(0))

    def setStatus(self, value):
        self._setString(0, value.value)
        return

    def getCurrentStage(self):
        return self._getNumber(1)

    def setCurrentStage(self, value):
        self._setNumber(1, value)
        return

    def getMaximumStage(self):
        return self._getNumber(2)

    def setMaximumStage(self, value):
        self._setNumber(2, value)
        return

    def getResetTimer(self):
        return self._getNumber(3)

    def setResetTimer(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(FunRandomProgressionState, self)._initialize()
        self._addStringProperty(b'status')
        self._addNumberProperty(b'currentStage', -1)
        self._addNumberProperty(b'maximumStage', -1)
        self._addNumberProperty(b'resetTimer', -1)
        return
