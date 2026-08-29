from enum import IntEnum
from frameworks.wulf import ViewModel

class Division(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5


class DivisionInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(DivisionInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return Division(self._getNumber(0))

    def setName(self, value):
        self._setNumber(0, value.value)
        return

    def getFrom(self):
        return self._getNumber(1)

    def setFrom(self, value):
        self._setNumber(1, value)
        return

    def getTo(self):
        return self._getNumber(2)

    def setTo(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(DivisionInfoModel, self)._initialize()
        self._addNumberProperty(b'name')
        self._addNumberProperty(b'from', 0)
        self._addNumberProperty(b'to', 0)
        return
