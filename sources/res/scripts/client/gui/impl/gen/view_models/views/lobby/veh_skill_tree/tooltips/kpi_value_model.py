from frameworks.wulf import ViewModel

class KpiValueModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(KpiValueModel, self).__init__(properties=properties, commands=commands)
        return

    def getBaseValue(self):
        return self._getReal(0)

    def setBaseValue(self, value):
        self._setReal(0, value)
        return

    def getValueKey(self):
        return self._getString(1)

    def setValueKey(self, value):
        self._setString(1, value)
        return

    def getValue(self):
        return self._getReal(2)

    def setValue(self, value):
        self._setReal(2, value)
        return

    def getValueType(self):
        return self._getString(3)

    def setValueType(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(KpiValueModel, self)._initialize()
        self._addRealProperty(b'baseValue', 0.0)
        self._addStringProperty(b'valueKey', b'')
        self._addRealProperty(b'value', 0.0)
        self._addStringProperty(b'valueType', b'mul')
        return
