from enum import IntEnum
from frameworks.wulf import ViewModel

class Complexity(IntEnum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class PortalBattleQueueViewModel(ViewModel):
    __slots__ = (b'onLeave',)

    def __init__(self, properties=1, commands=1):
        super(PortalBattleQueueViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getComplexity(self):
        return Complexity(self._getNumber(0))

    def setComplexity(self, value):
        self._setNumber(0, value.value)
        return

    def _initialize(self):
        super(PortalBattleQueueViewModel, self)._initialize()
        self._addNumberProperty(b'complexity')
        self.onLeave = self._addCommand(b'onLeave')
        return
