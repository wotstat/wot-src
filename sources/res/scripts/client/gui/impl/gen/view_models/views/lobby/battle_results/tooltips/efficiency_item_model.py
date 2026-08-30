from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class Unit(Enum):
    SEC = b'sec'
    COUNT = b'count'


class EfficiencyItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(EfficiencyItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabel(self):
        return self._getResource(0)

    def setLabel(self, value):
        self._setResource(0, value)
        return

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)
        return

    def getValueType(self):
        return self._getResource(2)

    def setValueType(self, value):
        self._setResource(2, value)
        return

    def _initialize(self):
        super(EfficiencyItemModel, self)._initialize()
        self._addResourceProperty(b'label', R.invalid())
        self._addRealProperty(b'value', 0.0)
        self._addResourceProperty(b'valueType', R.invalid())
        return
