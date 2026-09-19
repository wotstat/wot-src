from enum import Enum
from frameworks.wulf import ViewModel

class AnomalyType(Enum):
    REGULAR = b'regular'
    EPIC = b'epic'
    INDIVIDUAL = b'individual'
    SECRET = b'secret'


class AnomalyState(Enum):
    UNKNOWN = b'unknown'
    KNOWN = b'known'
    AVAILABLE = b'available'
    ACQUIRED = b'acquired'
    NEW = b'new'


class AnomalyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(AnomalyModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return AnomalyType(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)
        return

    def getState(self):
        return AnomalyState(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(AnomalyModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'type')
        self._addStringProperty(b'state')
        return
