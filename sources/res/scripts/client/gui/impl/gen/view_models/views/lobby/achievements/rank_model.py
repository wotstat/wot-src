from frameworks.wulf import ViewModel

class RankModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RankModel, self).__init__(properties=properties, commands=commands)
        return

    def getRank(self):
        return self._getNumber(0)

    def setRank(self, value):
        self._setNumber(0, value)
        return

    def getSubRank(self):
        return self._getNumber(1)

    def setSubRank(self, value):
        self._setNumber(1, value)
        return

    def getCountOfPoints(self):
        return self._getNumber(2)

    def setCountOfPoints(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(RankModel, self)._initialize()
        self._addNumberProperty(b'rank', 0)
        self._addNumberProperty(b'subRank', 0)
        self._addNumberProperty(b'countOfPoints', 0)
        return
