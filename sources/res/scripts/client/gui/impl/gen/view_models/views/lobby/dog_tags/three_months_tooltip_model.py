from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ThreeMonthsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ThreeMonthsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getHighlightedIndex(self):
        return self._getNumber(0)

    def setHighlightedIndex(self, value):
        self._setNumber(0, value)
        return

    def getMonthlyValues(self):
        return self._getArray(1)

    def setMonthlyValues(self, value):
        self._setArray(1, value)
        return

    def getMonthNames(self):
        return self._getArray(2)

    def setMonthNames(self, value):
        self._setArray(2, value)
        return

    def getCurrentMonth(self):
        return self._getResource(3)

    def setCurrentMonth(self, value):
        self._setResource(3, value)
        return

    def getProgressNumberType(self):
        return self._getString(4)

    def setProgressNumberType(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(ThreeMonthsTooltipModel, self)._initialize()
        self._addNumberProperty(b'highlightedIndex', 0)
        self._addArrayProperty(b'monthlyValues', Array())
        self._addArrayProperty(b'monthNames', Array())
        self._addResourceProperty(b'currentMonth', R.invalid())
        self._addStringProperty(b'progressNumberType', b'')
        return
