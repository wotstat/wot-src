from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.rank_model import RankModel

class WtrMainTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(WtrMainTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getRequiredNumberOfBattles(self):
        return self._getNumber(0)

    def setRequiredNumberOfBattles(self, value):
        self._setNumber(0, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(1)

    def setCurrentPoints(self, value):
        self._setNumber(1, value)
        return

    def getRank(self):
        return self._getNumber(2)

    def setRank(self, value):
        self._setNumber(2, value)
        return

    def getSubRank(self):
        return self._getNumber(3)

    def setSubRank(self, value):
        self._setNumber(3, value)
        return

    def getRanks(self):
        return self._getArray(4)

    def setRanks(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRanksType():
        return RankModel

    def _initialize(self):
        super(WtrMainTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'requiredNumberOfBattles', 0)
        self._addNumberProperty(b'currentPoints', 0)
        self._addNumberProperty(b'rank', 0)
        self._addNumberProperty(b'subRank', 0)
        self._addArrayProperty(b'ranks', Array())
        return
