from frameworks.wulf import ViewModel

class RestBonusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RestBonusTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getMultiplier(self):
        return self._getNumber(0)

    def setMultiplier(self, value):
        self._setNumber(0, value)
        return

    def getResetTimestamp(self):
        return self._getNumber(1)

    def setResetTimestamp(self, value):
        self._setNumber(1, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(2)

    def setEndTimestamp(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(RestBonusTooltipModel, self)._initialize()
        self._addNumberProperty(b'multiplier', 0)
        self._addNumberProperty(b'resetTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        return
