from frameworks.wulf import ViewModel

class DynamicParamModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DynamicParamModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getValue1(self):
        return self._getString(1)

    def setValue1(self, value):
        self._setString(1, value)
        return

    def getValue2(self):
        return self._getString(2)

    def setValue2(self, value):
        self._setString(2, value)
        return

    def getValue3(self):
        return self._getString(3)

    def setValue3(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(DynamicParamModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'value1', b'')
        self._addStringProperty(b'value2', b'')
        self._addStringProperty(b'value3', b'')
        return
