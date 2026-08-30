from frameworks.wulf import ViewModel

class SimpleEfficiencyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SimpleEfficiencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getParamName(self):
        return self._getString(0)

    def setParamName(self, value):
        self._setString(0, value)
        return

    def getRank(self):
        return self._getNumber(1)

    def setRank(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(SimpleEfficiencyModel, self)._initialize()
        self._addStringProperty(b'paramName', b'')
        self._addNumberProperty(b'rank', 0)
        return
