from enum import IntEnum
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class PackageType(IntEnum):
    BATTLEPASS = 0
    ANYLEVELS = 1
    SHOPOFFER = 2


class BattlePassBuyRewardsViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(BattlePassBuyRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def nowRewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getNowRewardsType():
        return RewardItemModel

    @property
    def futureRewards(self):
        return self._getViewModel(1)

    @staticmethod
    def getFutureRewardsType():
        return RewardItemModel

    @property
    def topPriorityRewards(self):
        return self._getViewModel(2)

    @staticmethod
    def getTopPriorityRewardsType():
        return RewardItemModel

    @property
    def prevTopPriorityRewards(self):
        return self._getViewModel(3)

    @staticmethod
    def getPrevTopPriorityRewardsType():
        return RewardItemModel

    def getFromLevel(self):
        return self._getNumber(4)

    def setFromLevel(self, value):
        self._setNumber(4, value)
        return

    def getToLevel(self):
        return self._getNumber(5)

    def setToLevel(self, value):
        self._setNumber(5, value)
        return

    def getPackageState(self):
        return PackageType(self._getNumber(6))

    def setPackageState(self, value):
        self._setNumber(6, value.value)
        return

    def getChapterID(self):
        return self._getNumber(7)

    def setChapterID(self, value):
        self._setNumber(7, value)
        return

    def getIsPurchaseWithLevels(self):
        return self._getBool(8)

    def setIsPurchaseWithLevels(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(BattlePassBuyRewardsViewModel, self)._initialize()
        self._addViewModelProperty(b'nowRewards', UserListModel())
        self._addViewModelProperty(b'futureRewards', UserListModel())
        self._addViewModelProperty(b'topPriorityRewards', UserListModel())
        self._addViewModelProperty(b'prevTopPriorityRewards', UserListModel())
        self._addNumberProperty(b'fromLevel', 0)
        self._addNumberProperty(b'toLevel', 0)
        self._addNumberProperty(b'packageState')
        self._addNumberProperty(b'chapterID', 0)
        self._addBoolProperty(b'isPurchaseWithLevels', False)
        return
