from frameworks.wulf import ViewModel

class WtRerollModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(WtRerollModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAffordable(self):
        return self._getBool(0)

    def setIsAffordable(self, value):
        self._setBool(0, value)
        return

    def getCurrency(self):
        return self._getString(1)

    def setCurrency(self, value):
        self._setString(1, value)
        return

    def getPrice(self):
        return self._getNumber(2)

    def setPrice(self, value):
        self._setNumber(2, value)
        return

    def getCount(self):
        return self._getNumber(3)

    def setCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(WtRerollModel, self)._initialize()
        self._addBoolProperty(b'isAffordable', False)
        self._addStringProperty(b'currency', b'gold')
        self._addNumberProperty(b'price', 400)
        self._addNumberProperty(b'count', 2)
        return
