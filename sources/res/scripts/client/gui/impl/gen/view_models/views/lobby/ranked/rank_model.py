from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class RankModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RankModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getRankID(self):
        return self._getNumber(1)

    def setRankID(self, value):
        self._setNumber(1, value)
        return

    def getStepsToRank(self):
        return self._getNumber(2)

    def setStepsToRank(self, value):
        self._setNumber(2, value)
        return

    def getIsUnburnable(self):
        return self._getBool(3)

    def setIsUnburnable(self, value):
        self._setBool(3, value)
        return

    def getNeedTakeReward(self):
        return self._getBool(4)

    def setNeedTakeReward(self, value):
        self._setBool(4, value)
        return

    def getCanTakeReward(self):
        return self._getBool(5)

    def setCanTakeReward(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(RankModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addNumberProperty(b'rankID', 0)
        self._addNumberProperty(b'stepsToRank', 0)
        self._addBoolProperty(b'isUnburnable', False)
        self._addBoolProperty(b'needTakeReward', False)
        self._addBoolProperty(b'canTakeReward', False)
        return
