from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel

class NyLeaderboardRewardViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=6, commands=1):
        super(NyLeaderboardRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getIsPreorder(self):
        return self._getBool(1)

    def setIsPreorder(self, value):
        self._setBool(1, value)
        return

    def getIsFinal(self):
        return self._getBool(2)

    def setIsFinal(self, value):
        self._setBool(2, value)
        return

    def getPosition(self):
        return self._getNumber(3)

    def setPosition(self, value):
        self._setNumber(3, value)
        return

    def getTop(self):
        return self._getNumber(4)

    def setTop(self, value):
        self._setNumber(4, value)
        return

    def getStage(self):
        return self._getNumber(5)

    def setStage(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(NyLeaderboardRewardViewModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addBoolProperty(b'isPreorder', False)
        self._addBoolProperty(b'isFinal', False)
        self._addNumberProperty(b'position', 0)
        self._addNumberProperty(b'top', 0)
        self._addNumberProperty(b'stage', 0)
        self.onClose = self._addCommand(b'onClose')
        return
