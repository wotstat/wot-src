from enum import IntEnum
from frameworks.wulf import ViewModel

class Division(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5


class State(IntEnum):
    ACHIEVED = 0
    CURRENT = 1
    INACTIVE = 2


class DivisionInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(DivisionInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getNumber(0)

    def setType(self, value):
        self._setNumber(0, value)
        return

    def getElitePercent(self):
        return self._getNumber(1)

    def setElitePercent(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return Division(self._getNumber(2))

    def setName(self, value):
        self._setNumber(2, value.value)
        return

    def getFrom(self):
        return self._getNumber(3)

    def setFrom(self, value):
        self._setNumber(3, value)
        return

    def getTo(self):
        return self._getNumber(4)

    def setTo(self, value):
        self._setNumber(4, value)
        return

    def getState(self):
        return State(self._getNumber(5))

    def setState(self, value):
        self._setNumber(5, value.value)
        return

    def _initialize(self):
        super(DivisionInfoModel, self)._initialize()
        self._addNumberProperty(b'type', 0)
        self._addNumberProperty(b'elitePercent', 0)
        self._addNumberProperty(b'name')
        self._addNumberProperty(b'from', 0)
        self._addNumberProperty(b'to', 0)
        self._addNumberProperty(b'state', State.INACTIVE.value)
        return
