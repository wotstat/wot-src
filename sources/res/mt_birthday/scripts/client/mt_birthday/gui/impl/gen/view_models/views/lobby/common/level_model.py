from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class LevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(LevelModel, self).__init__(properties=properties, commands=commands)
        return

    def getNumber(self):
        return self._getNumber(0)

    def setNumber(self, value):
        self._setNumber(0, value)
        return

    def getIsCompleted(self):
        return self._getBool(1)

    def setIsCompleted(self, value):
        self._setBool(1, value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(LevelModel, self)._initialize()
        self._addNumberProperty(b'number', 1)
        self._addBoolProperty(b'isCompleted', False)
        self._addArrayProperty(b'rewards', Array())
        return
