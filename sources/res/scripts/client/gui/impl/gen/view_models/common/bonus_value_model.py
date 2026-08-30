from frameworks.wulf import ViewModel

class BonusValueModel(ViewModel):
    __slots__ = ()
    MUL_VALUE = b'mul'

    def __init__(self, properties=4, commands=0):
        super(BonusValueModel, self).__init__(properties=properties, commands=commands)
        return

    def getValueKey(self):
        return self._getString(0)

    def setValueKey(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)
        return

    def getValueType(self):
        return self._getString(2)

    def setValueType(self, value):
        self._setString(2, value)
        return

    def getIsDebuff(self):
        return self._getBool(3)

    def setIsDebuff(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(BonusValueModel, self)._initialize()
        self._addStringProperty(b'valueKey', b'')
        self._addRealProperty(b'value', 0.0)
        self._addStringProperty(b'valueType', b'mul')
        self._addBoolProperty(b'isDebuff', False)
        return
