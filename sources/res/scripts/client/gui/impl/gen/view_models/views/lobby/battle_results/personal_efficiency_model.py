from enum import IntEnum
from frameworks.wulf import ViewModel

class ValueType(IntEnum):
    INTEGER = 0
    TIME = 1
    NON_NEGATIVE_INTEGER = 2


class PersonalEfficiencyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PersonalEfficiencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getParamType(self):
        return self._getString(0)

    def setParamType(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)
        return

    def getValueType(self):
        return ValueType(self._getNumber(2))

    def setValueType(self, value):
        self._setNumber(2, value.value)
        return

    def _initialize(self):
        super(PersonalEfficiencyModel, self)._initialize()
        self._addStringProperty(b'paramType', b'')
        self._addRealProperty(b'value', 0.0)
        self._addNumberProperty(b'valueType', ValueType.INTEGER.value)
        return
