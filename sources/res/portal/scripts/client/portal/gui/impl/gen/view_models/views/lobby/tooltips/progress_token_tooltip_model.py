from frameworks.wulf import ViewModel

class ProgressTokenTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ProgressTokenTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsTokenTooltip(self):
        return self._getBool(0)

    def setIsTokenTooltip(self, value):
        self._setBool(0, value)
        return

    def getIsCompleted(self):
        return self._getBool(1)

    def setIsCompleted(self, value):
        self._setBool(1, value)
        return

    def getInProgress(self):
        return self._getBool(2)

    def setInProgress(self, value):
        self._setBool(2, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(3)

    def setCurrentPoints(self, value):
        self._setNumber(3, value)
        return

    def getNextLevelPoints(self):
        return self._getNumber(4)

    def setNextLevelPoints(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(ProgressTokenTooltipModel, self)._initialize()
        self._addBoolProperty(b'isTokenTooltip', False)
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'inProgress', False)
        self._addNumberProperty(b'currentPoints', 0)
        self._addNumberProperty(b'nextLevelPoints', 0)
        return
