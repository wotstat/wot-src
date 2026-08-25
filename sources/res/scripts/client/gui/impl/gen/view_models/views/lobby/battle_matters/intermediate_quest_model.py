from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class IntermediateQuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(IntermediateQuestModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuestIdx(self):
        return self._getNumber(0)

    def setQuestIdx(self, value):
        self._setNumber(0, value)
        return

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(IntermediateQuestModel, self)._initialize()
        self._addNumberProperty(b'questIdx', 0)
        self._addArrayProperty(b'rewards', Array())
        return
