from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    ACTIVE = b'active'
    DISABLED = b'disabled'
    ANNOUNCE = b'announce'


class BattleRoyaleEntryPointModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=3, commands=1):
        super(BattleRoyaleEntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getTimestamp(self):
        return self._getNumber(1)

    def setTimestamp(self, value):
        self._setNumber(1, value)
        return

    def getIsSingle(self):
        return self._getBool(2)

    def setIsSingle(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(BattleRoyaleEntryPointModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'timestamp', 0)
        self._addBoolProperty(b'isSingle', True)
        self.onClick = self._addCommand(b'onClick')
        return
