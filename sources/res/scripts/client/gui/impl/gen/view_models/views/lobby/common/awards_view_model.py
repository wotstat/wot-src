from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel

class AwardsViewModel(ViewModel):
    __slots__ = (b'onCloseClick',)

    def __init__(self, properties=6, commands=1):
        super(AwardsViewModel, self).__init__(properties=properties, commands=commands)
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

    def getBackground(self):
        return self._getResource(2)

    def setBackground(self, value):
        self._setResource(2, value)
        return

    def getTitle(self):
        return self._getResource(3)

    def setTitle(self, value):
        self._setResource(3, value)
        return

    def getSubTitle(self):
        return self._getResource(4)

    def setSubTitle(self, value):
        self._setResource(4, value)
        return

    def getButtonTitle(self):
        return self._getResource(5)

    def setButtonTitle(self, value):
        self._setResource(5, value)
        return

    def _initialize(self):
        super(AwardsViewModel, self)._initialize()
        self._addViewModelProperty(b'mainRewards', UserListModel())
        self._addViewModelProperty(b'additionalRewards', UserListModel())
        self._addResourceProperty(b'background', R.invalid())
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'subTitle', R.invalid())
        self._addResourceProperty(b'buttonTitle', R.invalid())
        self.onCloseClick = self._addCommand(b'onCloseClick')
        return
