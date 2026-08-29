from enum import IntEnum
from frameworks.wulf import ViewModel

class State(IntEnum):
    NOTSTARTED = 0
    PRIMETIMENOW = 1
    PRIMETIMETODAY = 2
    PRIMETIMETOMORROW = 3
    PRIMETIMENOTCHOSEN = 4
    STARTED = 5
    ENDED = 6
    DATAERROR = 7


class StrongholdEntryPointViewModel(ViewModel):
    __slots__ = (b'onOpen',)

    def __init__(self, properties=6, commands=1):
        super(StrongholdEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getNumber(0))

    def setState(self, value):
        self._setNumber(0, value.value)
        return

    def getIsSingle(self):
        return self._getBool(1)

    def setIsSingle(self, value):
        self._setBool(1, value)
        return

    def getStartTimestamp(self):
        return self._getNumber(2)

    def setStartTimestamp(self, value):
        self._setNumber(2, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(3)

    def setEndTimestamp(self, value):
        self._setNumber(3, value)
        return

    def getSprintType(self):
        return self._getString(4)

    def setSprintType(self, value):
        self._setString(4, value)
        return

    def getSprintStage(self):
        return self._getString(5)

    def setSprintStage(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(StrongholdEntryPointViewModel, self)._initialize()
        self._addNumberProperty(b'state')
        self._addBoolProperty(b'isSingle', True)
        self._addNumberProperty(b'startTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addStringProperty(b'sprintType', b'')
        self._addStringProperty(b'sprintStage', b'')
        self.onOpen = self._addCommand(b'onOpen')
        return
