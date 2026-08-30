from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class RankedSelectedRewardViewModel(ViewModel):
    __slots__ = (b'onClosed',)

    def __init__(self, properties=3, commands=1):
        super(RankedSelectedRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def mainRewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getMainRewardsType():
        return RewardItemModel

    @property
    def additionalRewards(self):
        return self._getViewModel(1)

    @staticmethod
    def getAdditionalRewardsType():
        return RewardItemModel

    def getTitle(self):
        return self._getString(2)

    def setTitle(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(RankedSelectedRewardViewModel, self)._initialize()
        self._addViewModelProperty(b'mainRewards', UserListModel())
        self._addViewModelProperty(b'additionalRewards', UserListModel())
        self._addStringProperty(b'title', b'')
        self.onClosed = self._addCommand(b'onClosed')
        return
