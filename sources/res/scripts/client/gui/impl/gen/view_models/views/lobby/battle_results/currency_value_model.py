from enum import Enum
from frameworks.wulf import Array, ViewModel

class ValueModifiers(Enum):
    UNDEFINED = b'undefined'
    MUL = b'mul'
    ADD = b'add'
    SUB = b'sub'
    PROCENT = b'procent'
    SHOW_NEGATIVE_IMPACT = b'showNegativeImpact'


class CurrencyValueModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(CurrencyValueModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrencyType(self):
        return self._getString(0)

    def setCurrencyType(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)
        return

    def getIsShown(self):
        return self._getBool(2)

    def setIsShown(self, value):
        self._setBool(2, value)
        return

    def getModifiers(self):
        return self._getArray(3)

    def setModifiers(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getModifiersType():
        return ValueModifiers

    def _initialize(self):
        super(CurrencyValueModel, self)._initialize()
        self._addStringProperty(b'currencyType', b'')
        self._addRealProperty(b'value', 0.0)
        self._addBoolProperty(b'isShown', False)
        self._addArrayProperty(b'modifiers', Array())
        return
