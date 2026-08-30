from comp7.gui.impl.gen.view_models.views.lobby.enums import Division, Rank
from frameworks.wulf import ViewModel

class PlatoonRankData(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PlatoonRankData, self).__init__(properties=properties, commands=commands)
        return

    def getRank(self):
        return Rank(self._getNumber(0))

    def setRank(self, value):
        self._setNumber(0, value.value)
        return

    def getDivision(self):
        return Division(self._getNumber(1))

    def setDivision(self, value):
        self._setNumber(1, value.value)
        return

    def getScore(self):
        return self._getNumber(2)

    def setScore(self, value):
        self._setNumber(2, value)
        return

    def getFrom(self):
        return self._getNumber(3)

    def setFrom(self, value):
        self._setNumber(3, value)
        return

    def getTo(self):
        return self._getNumber(4)

    def setTo(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(PlatoonRankData, self)._initialize()
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'division')
        self._addNumberProperty(b'score', 0)
        self._addNumberProperty(b'from', 0)
        self._addNumberProperty(b'to', 0)
        return
