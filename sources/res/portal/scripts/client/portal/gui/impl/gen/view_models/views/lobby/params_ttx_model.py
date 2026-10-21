from enum import Enum
from frameworks.wulf import ViewModel

class TtxComparisonStatus(Enum):
    INCREASE = b'increase'
    DECREASE = b'decrease'
    DEFAULT = b'default'


class ParamsTtxModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ParamsTtxModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getStatus(self):
        return TtxComparisonStatus(self._getString(1))

    def setStatus(self, value):
        self._setString(1, value.value)
        return

    def getValue(self):
        return self._getReal(2)

    def setValue(self, value):
        self._setReal(2, value)
        return

    def _initialize(self):
        super(ParamsTtxModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'status')
        self._addRealProperty(b'value', 0.0)
        return
