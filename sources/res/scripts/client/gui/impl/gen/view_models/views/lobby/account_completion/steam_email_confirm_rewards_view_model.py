from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class SteamEmailConfirmRewardsViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=1, commands=1):
        super(SteamEmailConfirmRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBonuses(self):
        return self._getArray(0)

    def setBonuses(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getBonusesType():
        return ItemBonusModel

    def _initialize(self):
        super(SteamEmailConfirmRewardsViewModel, self)._initialize()
        self._addArrayProperty(b'bonuses', Array())
        self.onClose = self._addCommand(b'onClose')
        return
