from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.comp7.comp7_bonus_model import Comp7BonusModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.progression_item_base_model import ProgressionItemBaseModel

class RankRewardsItemModel(ProgressionItemBaseModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RankRewardsItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasRewardsReceived(self):
        return self._getBool(4)

    def setHasRewardsReceived(self, value):
        self._setBool(4, value)
        return

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRewardsType():
        return Comp7BonusModel

    def _initialize(self):
        super(RankRewardsItemModel, self)._initialize()
        self._addBoolProperty(b'hasRewardsReceived', False)
        self._addArrayProperty(b'rewards', Array())
        return
