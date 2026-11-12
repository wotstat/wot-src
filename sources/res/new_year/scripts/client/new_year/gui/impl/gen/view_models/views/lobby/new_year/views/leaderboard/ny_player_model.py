from enum import Enum
from frameworks.wulf import ViewModel

class PositionType(Enum):
    NOCHANGES = b'noChanges'
    UP = b'up'
    DOWN = b'down'


class NyPlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(NyPlayerModel, self).__init__(properties=properties, commands=commands)
        return

    def getPositionType(self):
        return PositionType(self._getString(0))

    def setPositionType(self, value):
        self._setString(0, value.value)
        return

    def getUserName(self):
        return self._getString(1)

    def setUserName(self, value):
        self._setString(1, value)
        return

    def getPosition(self):
        return self._getNumber(2)

    def setPosition(self, value):
        self._setNumber(2, value)
        return

    def getScore(self):
        return self._getNumber(3)

    def setScore(self, value):
        self._setNumber(3, value)
        return

    def getTop(self):
        return self._getNumber(4)

    def setTop(self, value):
        self._setNumber(4, value)
        return

    def getStartPos(self):
        return self._getNumber(5)

    def setStartPos(self, value):
        self._setNumber(5, value)
        return

    def getEndPos(self):
        return self._getNumber(6)

    def setEndPos(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(NyPlayerModel, self)._initialize()
        self._addStringProperty(b'positionType')
        self._addStringProperty(b'userName', b'')
        self._addNumberProperty(b'position', 0)
        self._addNumberProperty(b'score', 0)
        self._addNumberProperty(b'top', 0)
        self._addNumberProperty(b'startPos', 0)
        self._addNumberProperty(b'endPos', 0)
        return
