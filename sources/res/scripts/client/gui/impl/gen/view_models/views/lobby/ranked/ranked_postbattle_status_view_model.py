from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel
from gui.impl.gen.view_models.views.lobby.ranked.ranked_state_model import RankedStateModel

class RankedPostbattleStatusViewModel(ViewModel):
    __slots__ = (b'onClose', b'onSwitchAnimation', b'onSelectReward')

    def __init__(self, properties=9, commands=3):
        super(RankedPostbattleStatusViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def oldState(self):
        return self._getViewModel(0)

    @staticmethod
    def getOldStateType():
        return RankedStateModel

    @property
    def newState(self):
        return self._getViewModel(1)

    @staticmethod
    def getNewStateType():
        return RankedStateModel

    @property
    def rewards(self):
        return self._getViewModel(2)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getMaxRank(self):
        return self._getNumber(3)

    def setMaxRank(self, value):
        self._setNumber(3, value)
        return

    def getShowAnimation(self):
        return self._getBool(4)

    def setShowAnimation(self, value):
        self._setBool(4, value)
        return

    def getCanTakeReward(self):
        return self._getBool(5)

    def setCanTakeReward(self, value):
        self._setBool(5, value)
        return

    def getIsFinal(self):
        return self._getBool(6)

    def setIsFinal(self, value):
        self._setBool(6, value)
        return

    def getTotalSteps(self):
        return self._getNumber(7)

    def setTotalSteps(self, value):
        self._setNumber(7, value)
        return

    def getUnburnableRanks(self):
        return self._getArray(8)

    def setUnburnableRanks(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getUnburnableRanksType():
        return int

    def _initialize(self):
        super(RankedPostbattleStatusViewModel, self)._initialize()
        self._addViewModelProperty(b'oldState', RankedStateModel())
        self._addViewModelProperty(b'newState', RankedStateModel())
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addNumberProperty(b'maxRank', 0)
        self._addBoolProperty(b'showAnimation', False)
        self._addBoolProperty(b'canTakeReward', False)
        self._addBoolProperty(b'isFinal', False)
        self._addNumberProperty(b'totalSteps', 0)
        self._addArrayProperty(b'unburnableRanks', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onSwitchAnimation = self._addCommand(b'onSwitchAnimation')
        self.onSelectReward = self._addCommand(b'onSelectReward')
        return
