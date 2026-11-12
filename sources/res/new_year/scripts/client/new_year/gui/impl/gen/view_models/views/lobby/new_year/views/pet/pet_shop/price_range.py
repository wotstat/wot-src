from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class PriceRange(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PriceRange, self).__init__(properties=properties, commands=commands)
        return

    def getRange(self):
        return self._getArray(0)

    def setRange(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getRangeType():
        return int

    def getPrice(self):
        return self._getNumber(1)

    def setPrice(self, value):
        self._setNumber(1, value)
        return

    def getIsDynamic(self):
        return self._getBool(2)

    def setIsDynamic(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(PriceRange, self)._initialize()
        self._addArrayProperty(b'range', Array())
        self._addNumberProperty(b'price', 0)
        self._addBoolProperty(b'isDynamic', False)
        return
