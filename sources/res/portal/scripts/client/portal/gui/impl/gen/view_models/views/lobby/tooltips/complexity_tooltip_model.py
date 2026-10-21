from frameworks.wulf import ViewModel

class ComplexityTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ComplexityTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getIsLock(self):
        return self._getBool(1)

    def setIsLock(self, value):
        self._setBool(1, value)
        return

    def getRecommendedMin(self):
        return self._getNumber(2)

    def setRecommendedMin(self, value):
        self._setNumber(2, value)
        return

    def getRecommendedMax(self):
        return self._getNumber(3)

    def setRecommendedMax(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(ComplexityTooltipModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isLock', False)
        self._addNumberProperty(b'recommendedMin', 0)
        self._addNumberProperty(b'recommendedMax', 0)
        return
