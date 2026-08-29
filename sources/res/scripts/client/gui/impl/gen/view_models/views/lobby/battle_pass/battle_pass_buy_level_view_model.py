from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_buy_confirm_any_number_view_model import BattlePassBuyConfirmAnyNumberViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_buy_rewards_view_model import BattlePassBuyRewardsViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.package_item import PackageItem

class BattlePassBuyLevelViewModel(ViewModel):
    __slots__ = (b'onBackClick', b'showConfirm', b'showConfirmAny', b'showRewards')
    CONFIRM_ANY_NUMBER_STATE = b'confirmAnyNumberState'
    REWARDS_STATE = b'rewardsState'

    def __init__(self, properties=5, commands=4):
        super(BattlePassBuyLevelViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def packages(self):
        return self._getViewModel(0)

    @staticmethod
    def getPackagesType():
        return PackageItem

    @property
    def confirmAnyNumber(self):
        return self._getViewModel(1)

    @staticmethod
    def getConfirmAnyNumberType():
        return BattlePassBuyConfirmAnyNumberViewModel

    @property
    def rewards(self):
        return self._getViewModel(2)

    @staticmethod
    def getRewardsType():
        return BattlePassBuyRewardsViewModel

    def getState(self):
        return self._getString(3)

    def setState(self, value):
        self._setString(3, value)
        return

    def getIsWalletAvailable(self):
        return self._getBool(4)

    def setIsWalletAvailable(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(BattlePassBuyLevelViewModel, self)._initialize()
        self._addViewModelProperty(b'packages', UserListModel())
        self._addViewModelProperty(b'confirmAnyNumber', BattlePassBuyConfirmAnyNumberViewModel())
        self._addViewModelProperty(b'rewards', BattlePassBuyRewardsViewModel())
        self._addStringProperty(b'state', b'confirmAnyNumberState')
        self._addBoolProperty(b'isWalletAvailable', False)
        self.onBackClick = self._addCommand(b'onBackClick')
        self.showConfirm = self._addCommand(b'showConfirm')
        self.showConfirmAny = self._addCommand(b'showConfirmAny')
        self.showRewards = self._addCommand(b'showRewards')
        return
