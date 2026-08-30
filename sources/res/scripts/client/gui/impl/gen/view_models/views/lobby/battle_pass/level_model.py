from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class LevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(LevelModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getLevelPoints(self):
        return self._getNumber(1)

    def setLevelPoints(self, value):
        self._setNumber(1, value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def _initialize(self):
        super(LevelModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'levelPoints', 0)
        self._addArrayProperty(b'rewards', Array())
        return
