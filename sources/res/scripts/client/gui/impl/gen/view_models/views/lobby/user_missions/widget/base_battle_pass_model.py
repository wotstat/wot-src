from frameworks.wulf import ViewModel

class BaseBattlePassModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BaseBattlePassModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewardsHash(self):
        return self._getNumber(0)

    def setRewardsHash(self, value):
        self._setNumber(0, value)
        return

    def getPointsEarned(self):
        return self._getNumber(1)

    def setPointsEarned(self, value):
        self._setNumber(1, value)
        return

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(BaseBattlePassModel, self)._initialize()
        self._addNumberProperty(b'rewardsHash', 0)
        self._addNumberProperty(b'pointsEarned', 0)
        self._addNumberProperty(b'level', 0)
        return
