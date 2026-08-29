from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class DescriptionRulesTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(DescriptionRulesTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getMinLevel(self):
        return self._getNumber(0)

    def setMinLevel(self, value):
        self._setNumber(0, value)
        return

    def getMaxLevel(self):
        return self._getNumber(1)

    def setMaxLevel(self, value):
        self._setNumber(1, value)
        return

    def getBattleTypes(self):
        return self._getArray(2)

    def setBattleTypes(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBattleTypesType():
        return int

    def _initialize(self):
        super(DescriptionRulesTooltipModel, self)._initialize()
        self._addNumberProperty(b'minLevel', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addArrayProperty(b'battleTypes', Array())
        return
