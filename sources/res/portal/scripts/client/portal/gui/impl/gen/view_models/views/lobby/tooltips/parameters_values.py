from frameworks.wulf import ViewModel

class ParametersValues(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ParametersValues, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getIsWorst(self):
        return self._getBool(1)

    def setIsWorst(self, value):
        self._setBool(1, value)
        return

    def getIsBetter(self):
        return self._getBool(2)

    def setIsBetter(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(ParametersValues, self)._initialize()
        self._addStringProperty(b'value', b'')
        self._addBoolProperty(b'isWorst', False)
        self._addBoolProperty(b'isBetter', False)
        return
