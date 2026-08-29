from frameworks.wulf import ViewModel

class InsufficientCreditsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(InsufficientCreditsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissingAmount(self):
        return self._getNumber(0)

    def setMissingAmount(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(InsufficientCreditsTooltipModel, self)._initialize()
        self._addNumberProperty(b'missingAmount', 0)
        return
