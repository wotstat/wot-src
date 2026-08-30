from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel

class AwardsViewModel(ViewModel):
    __slots__ = (b'onAnimationEnded', b'onRedirect', b'onClose')
    CLOSE_REASON_CANCEL = b'cancel'
    CLOSE_REASON_CONFIRM = b'confirm'

    def __init__(self, properties=9, commands=3):
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

    def getUnderTitle(self):
        return self._getResource(5)

    def setUnderTitle(self, value):
        self._setResource(5, value)
        return

    def getBottomNote(self):
        return self._getResource(6)

    def setBottomNote(self, value):
        self._setResource(6, value)
        return

    def getDefaultButtonTitle(self):
        return self._getResource(7)

    def setDefaultButtonTitle(self, value):
        self._setResource(7, value)
        return

    def getRedirectButtonTitle(self):
        return self._getResource(8)

    def setRedirectButtonTitle(self, value):
        self._setResource(8, value)
        return

    def _initialize(self):
        super(AwardsViewModel, self)._initialize()
        self._addViewModelProperty(b'mainRewards', UserListModel())
        self._addViewModelProperty(b'additionalRewards', UserListModel())
        self._addResourceProperty(b'background', R.invalid())
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'subTitle', R.invalid())
        self._addResourceProperty(b'underTitle', R.invalid())
        self._addResourceProperty(b'bottomNote', R.invalid())
        self._addResourceProperty(b'defaultButtonTitle', R.invalid())
        self._addResourceProperty(b'redirectButtonTitle', R.invalid())
        self.onAnimationEnded = self._addCommand(b'onAnimationEnded')
        self.onRedirect = self._addCommand(b'onRedirect')
        self.onClose = self._addCommand(b'onClose')
        return
