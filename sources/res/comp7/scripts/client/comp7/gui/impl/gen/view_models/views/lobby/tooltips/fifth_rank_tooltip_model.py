from frameworks.wulf import ViewModel

class FifthRankTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(FifthRankTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getFrom(self):
        return self._getNumber(0)

    def setFrom(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(FifthRankTooltipModel, self)._initialize()
        self._addNumberProperty(b'from', 2000)
        return
