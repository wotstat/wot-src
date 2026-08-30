from frameworks.wulf import ViewModel

class RankedPlatoonRankData(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RankedPlatoonRankData, self).__init__(properties=properties, commands=commands)
        return

    def getRank(self):
        return self._getNumber(0)

    def setRank(self, value):
        self._setNumber(0, value)
        return

    def getDivision(self):
        return self._getNumber(1)

    def setDivision(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(RankedPlatoonRankData, self)._initialize()
        self._addNumberProperty(b'rank', 0)
        self._addNumberProperty(b'division', 0)
        return
