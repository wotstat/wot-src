from enum import Enum
from frameworks.wulf import ViewModel

class ComplexityLevelStatus(Enum):
    SELECTED = b'selected'
    DEFAULT = b'default'
    LOCKED = b'locked'
    LOCKED_BY_SQUAD = b'lockedBySquad'


class PortalComplexityLevel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PortalComplexityLevel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getStatus(self):
        return ComplexityLevelStatus(self._getString(1))

    def setStatus(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(PortalComplexityLevel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'status')
        return
