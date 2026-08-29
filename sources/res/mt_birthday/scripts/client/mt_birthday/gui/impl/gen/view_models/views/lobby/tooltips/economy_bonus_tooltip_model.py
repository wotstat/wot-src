from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class EconomyBonusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(EconomyBonusTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getPercent(self):
        return self._getNumber(0)

    def setPercent(self, value):
        self._setNumber(0, value)
        return

    def getModes(self):
        return self._getArray(1)

    def setModes(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getModesType():
        return int

    def _initialize(self):
        super(EconomyBonusTooltipModel, self)._initialize()
        self._addNumberProperty(b'percent', 0)
        self._addArrayProperty(b'modes', Array())
        return
