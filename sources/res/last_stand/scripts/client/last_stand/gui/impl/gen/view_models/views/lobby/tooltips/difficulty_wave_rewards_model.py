from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class DifficultyWaveRewardsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DifficultyWaveRewardsModel, self).__init__(properties=properties, commands=commands)
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

    def getIsReceived(self):
        return self._getBool(2)

    def setIsReceived(self, value):
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
        super(DifficultyWaveRewardsModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'index', 0)
        self._addBoolProperty(b'isReceived', False)
        self._addArrayProperty(b'rewards', Array())
        return
