from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    ACTIVE = b'active'
    LOCKED = b'locked'
    BATTLES_END = b'battlesEnd'


class EntryPointModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=4, commands=1):
        super(EntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getTimeLeft(self):
        return self._getNumber(1)

    def setTimeLeft(self, value):
        self._setNumber(1, value)
        return

    def getHunterLootBoxesCount(self):
        return self._getNumber(2)

    def setHunterLootBoxesCount(self, value):
        self._setNumber(2, value)
        return

    def getBossLootBoxesCount(self):
        return self._getNumber(3)

    def setBossLootBoxesCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(EntryPointModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'timeLeft', 0)
        self._addNumberProperty(b'hunterLootBoxesCount', 0)
        self._addNumberProperty(b'bossLootBoxesCount', 0)
        self.onClick = self._addCommand(b'onClick')
        return
