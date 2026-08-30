from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class StageRewardViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=4, commands=1):
        super(StageRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getArtefactNumber(self):
        return self._getNumber(0)

    def setArtefactNumber(self, value):
        self._setNumber(0, value)
        return

    def getIsLastArtefact(self):
        return self._getBool(1)

    def setIsLastArtefact(self, value):
        self._setBool(1, value)
        return

    def getIsQuestReward(self):
        return self._getBool(2)

    def setIsQuestReward(self, value):
        self._setBool(2, value)
        return

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(StageRewardViewModel, self)._initialize()
        self._addNumberProperty(b'artefactNumber', 0)
        self._addBoolProperty(b'isLastArtefact', False)
        self._addBoolProperty(b'isQuestReward', False)
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        return
