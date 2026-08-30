from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class BuyPackageViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BuyPackageViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def starterPackRewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getStarterPackRewardsType():
        return RewardItemModel

    def getPrice(self):
        return self._getNumber(1)

    def setPrice(self, value):
        self._setNumber(1, value)
        return

    def getPrevPrice(self):
        return self._getNumber(2)

    def setPrevPrice(self, value):
        self._setNumber(2, value)
        return

    def getChapterID(self):
        return self._getNumber(3)

    def setChapterID(self, value):
        self._setNumber(3, value)
        return

    def getIsActive(self):
        return self._getBool(4)

    def setIsActive(self, value):
        self._setBool(4, value)
        return

    def getIsPurchaseWithLevels(self):
        return self._getBool(5)

    def setIsPurchaseWithLevels(self, value):
        self._setBool(5, value)
        return

    def getRemainingLevelsCount(self):
        return self._getNumber(6)

    def setRemainingLevelsCount(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(BuyPackageViewModel, self)._initialize()
        self._addViewModelProperty(b'starterPackRewards', UserListModel())
        self._addNumberProperty(b'price', 0)
        self._addNumberProperty(b'prevPrice', 0)
        self._addNumberProperty(b'chapterID', 0)
        self._addBoolProperty(b'isActive', False)
        self._addBoolProperty(b'isPurchaseWithLevels', False)
        self._addNumberProperty(b'remainingLevelsCount', 0)
        return
