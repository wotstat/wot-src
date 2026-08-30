from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class BattlePassBuyLevelViewModel(ViewModel):
    __slots__ = (b'onChangeSelectedLevels', b'onPurchase')

    def __init__(self, properties=6, commands=2):
        super(BattlePassBuyLevelViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getIsWalletAvailable(self):
        return self._getBool(1)

    def setIsWalletAvailable(self, value):
        self._setBool(1, value)
        return

    def getLevelsTotal(self):
        return self._getNumber(2)

    def setLevelsTotal(self, value):
        self._setNumber(2, value)
        return

    def getLevelsPassed(self):
        return self._getNumber(3)

    def setLevelsPassed(self, value):
        self._setNumber(3, value)
        return

    def getChapterID(self):
        return self._getNumber(4)

    def setChapterID(self, value):
        self._setNumber(4, value)
        return

    def getLevelPrice(self):
        return self._getNumber(5)

    def setLevelPrice(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(BattlePassBuyLevelViewModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addBoolProperty(b'isWalletAvailable', False)
        self._addNumberProperty(b'levelsTotal', 0)
        self._addNumberProperty(b'levelsPassed', 0)
        self._addNumberProperty(b'chapterID', 0)
        self._addNumberProperty(b'levelPrice', 0)
        self.onChangeSelectedLevels = self._addCommand(b'onChangeSelectedLevels')
        self.onPurchase = self._addCommand(b'onPurchase')
        return
