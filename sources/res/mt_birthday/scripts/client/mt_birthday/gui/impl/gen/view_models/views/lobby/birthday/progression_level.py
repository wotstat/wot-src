from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel

class ProgressionLevel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ProgressionLevel, self).__init__(properties=properties, commands=commands)
        return

    def getNumber(self):
        return self._getNumber(0)

    def setNumber(self, value):
        self._setNumber(0, value)
        return

    def getMaxPoints(self):
        return self._getNumber(1)

    def setMaxPoints(self, value):
        self._setNumber(1, value)
        return

    def getSubstagesCount(self):
        return self._getNumber(2)

    def setSubstagesCount(self, value):
        self._setNumber(2, value)
        return

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return TokenBonusModel

    def _initialize(self):
        super(ProgressionLevel, self)._initialize()
        self._addNumberProperty(b'number', 1)
        self._addNumberProperty(b'maxPoints', 0)
        self._addNumberProperty(b'substagesCount', 0)
        self._addArrayProperty(b'rewards', Array())
        return
