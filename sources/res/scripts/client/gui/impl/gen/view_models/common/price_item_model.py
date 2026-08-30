from frameworks.wulf import ViewModel

class PriceItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PriceItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)
        return

    def getIsEnough(self):
        return self._getBool(2)

    def setIsEnough(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(PriceItemModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addRealProperty(b'value', 0.0)
        self._addBoolProperty(b'isEnough', True)
        return
