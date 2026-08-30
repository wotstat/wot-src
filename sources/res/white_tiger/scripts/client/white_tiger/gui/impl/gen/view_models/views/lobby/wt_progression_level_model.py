from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class WtProgressionLevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(WtProgressionLevelModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(WtProgressionLevelModel, self)._initialize()
        self._addArrayProperty(b'rewards', Array())
        return
