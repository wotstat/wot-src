from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class RewardPathArtefactViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(RewardPathArtefactViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIndex(self):
        return self._getNumber(1)

    def setIndex(self, value):
        self._setNumber(1, value)
        return

    def getCost(self):
        return self._getNumber(2)

    def setCost(self, value):
        self._setNumber(2, value)
        return

    def getIsCompleted(self):
        return self._getBool(3)

    def setIsCompleted(self, value):
        self._setBool(3, value)
        return

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(RewardPathArtefactViewModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'index', 0)
        self._addNumberProperty(b'cost', 0)
        self._addBoolProperty(b'isCompleted', False)
        self._addArrayProperty(b'rewards', Array())
        return
