from frameworks.wulf import ViewModel

class CurrencyItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(CurrencyItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getCurrency(self):
        return self._getString(1)

    def setCurrency(self, value):
        self._setString(1, value)
        return

    def getIsEnough(self):
        return self._getBool(2)

    def setIsEnough(self, value):
        self._setBool(2, value)
        return

    def getSpecialTooltip(self):
        return self._getString(3)

    def setSpecialTooltip(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(CurrencyItemModel, self)._initialize()
        self._addStringProperty(b'value', b'--')
        self._addStringProperty(b'currency', b'')
        self._addBoolProperty(b'isEnough', True)
        self._addStringProperty(b'specialTooltip', b'')
        return
