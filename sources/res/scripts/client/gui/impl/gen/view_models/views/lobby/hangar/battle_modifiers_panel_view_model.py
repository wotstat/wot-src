from enum import IntEnum
from frameworks.wulf import ViewModel

class Queue(IntEnum):
    STRONGHOLD = 0
    GLOBALMAP = 1


class BattleModifiersPanelViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(BattleModifiersPanelViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getQueue(self):
        return Queue(self._getNumber(0))

    def setQueue(self, value):
        self._setNumber(0, value.value)
        return

    def _initialize(self):
        super(BattleModifiersPanelViewModel, self)._initialize()
        self._addNumberProperty(b'queue')
        return
