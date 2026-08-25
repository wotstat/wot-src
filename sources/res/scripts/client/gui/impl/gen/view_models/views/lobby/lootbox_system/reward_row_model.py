from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.bonus_model import BonusModel

class RewardRowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RewardRowModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return BonusModel

    def getLabel(self):
        return self._getString(1)

    def setLabel(self, value):
        self._setString(1, value)
        return

    def getRewardsCount(self):
        return self._getNumber(2)

    def setRewardsCount(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(RewardRowModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addStringProperty(b'label', b'')
        self._addNumberProperty(b'rewardsCount', 0)
        return
