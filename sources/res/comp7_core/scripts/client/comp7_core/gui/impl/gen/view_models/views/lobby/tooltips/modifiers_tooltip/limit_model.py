from enum import Enum
from frameworks.wulf import ViewModel

class LimitType(Enum):
    MIN = b'min'
    MAX = b'max'


class LimitModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LimitModel, self).__init__(properties=properties, commands=commands)
        return

    def getLimitType(self):
        return LimitType(self._getString(0))

    def setLimitType(self, value):
        self._setString(0, value.value)
        return

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)
        return

    def _initialize(self):
        super(LimitModel, self)._initialize()
        self._addStringProperty(b'limitType')
        self._addRealProperty(b'value', 0.0)
        return
