from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class BattlePassBuyConfirmAnyNumberViewModel(ViewModel):
    __slots__ = (b'onCloseClick', b'onBuyClick', b'onShowRewardsClick', b'onChangeSelectedLevels')

    def __init__(self, properties=8, commands=4):
        super(BattlePassBuyConfirmAnyNumberViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getPrice(self):
        return self._getNumber(1)

    def setPrice(self, value):
        self._setNumber(1, value)
        return

    def getLevelsStart(self):
        return self._getNumber(2)

    def setLevelsStart(self, value):
        self._setNumber(2, value)
        return

    def getLevelsPassed(self):
        return self._getNumber(3)

    def setLevelsPassed(self, value):
        self._setNumber(3, value)
        return

    def getLevelsTotal(self):
        return self._getNumber(4)

    def setLevelsTotal(self, value):
        self._setNumber(4, value)
        return

    def getLevelsSelected(self):
        return self._getNumber(5)

    def setLevelsSelected(self, value):
        self._setNumber(5, value)
        return

    def getChapterID(self):
        return self._getNumber(6)

    def setChapterID(self, value):
        self._setNumber(6, value)
        return

    def getBackBtnText(self):
        return self._getString(7)

    def setBackBtnText(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(BattlePassBuyConfirmAnyNumberViewModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addNumberProperty(b'price', 0)
        self._addNumberProperty(b'levelsStart', 0)
        self._addNumberProperty(b'levelsPassed', 0)
        self._addNumberProperty(b'levelsTotal', 0)
        self._addNumberProperty(b'levelsSelected', 0)
        self._addNumberProperty(b'chapterID', 0)
        self._addStringProperty(b'backBtnText', b'')
        self.onCloseClick = self._addCommand(b'onCloseClick')
        self.onBuyClick = self._addCommand(b'onBuyClick')
        self.onShowRewardsClick = self._addCommand(b'onShowRewardsClick')
        self.onChangeSelectedLevels = self._addCommand(b'onChangeSelectedLevels')
        return
