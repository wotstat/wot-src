from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class FunRandomProgressionCondition(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FunRandomProgressionCondition, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentPoints(self):
        return self._getNumber(0)

    def setCurrentPoints(self, value):
        self._setNumber(0, value)
        return

    def getMaximumPoints(self):
        return self._getNumber(1)

    def setMaximumPoints(self, value):
        self._setNumber(1, value)
        return

    def getText(self):
        return self._getString(2)

    def setText(self, value):
        self._setString(2, value)
        return

    def getConditions(self):
        return self._getArray(3)

    def setConditions(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getConditionsType():
        return unicode

    def _initialize(self):
        super(FunRandomProgressionCondition, self)._initialize()
        self._addNumberProperty(b'currentPoints', -1)
        self._addNumberProperty(b'maximumPoints', -1)
        self._addStringProperty(b'text', b'')
        self._addArrayProperty(b'conditions', Array())
        return
