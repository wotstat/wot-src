from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_buy_confirm_view_model import BattlePassBuyConfirmViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_buy_rewards_view_model import BattlePassBuyRewardsViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.package_item import PackageItem

class BattlePassBuyViewModel(ViewModel):
    __slots__ = (b'onBackClick', b'choosePackage', b'showConfirm', b'showRewards', b'onShopOfferClick')
    BUY_STATE = b'buyState'
    CONFIRM_STATE = b'confirmState'
    REWARDS_STATE = b'rewardsState'

    def __init__(self, properties=9, commands=5):
        super(BattlePassBuyViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def packages(self):
        return self._getViewModel(0)

    @staticmethod
    def getPackagesType():
        return PackageItem

    @property
    def confirm(self):
        return self._getViewModel(1)

    @staticmethod
    def getConfirmType():
        return BattlePassBuyConfirmViewModel

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

    def getIsShopOfferAvailable(self):
        return self._getBool(5)

    def setIsShopOfferAvailable(self, value):
        self._setBool(5, value)
        return

    def getShopOfferDiscount(self):
        return self._getNumber(6)

    def setShopOfferDiscount(self, value):
        self._setNumber(6, value)
        return

    def getShopOfferTimeLeft(self):
        return self._getNumber(7)

    def setShopOfferTimeLeft(self, value):
        self._setNumber(7, value)
        return

    def getIsSingleChapter(self):
        return self._getBool(8)

    def setIsSingleChapter(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(BattlePassBuyViewModel, self)._initialize()
        self._addViewModelProperty(b'packages', UserListModel())
        self._addViewModelProperty(b'confirm', BattlePassBuyConfirmViewModel())
        self._addViewModelProperty(b'rewards', BattlePassBuyRewardsViewModel())
        self._addStringProperty(b'state', b'buyState')
        self._addBoolProperty(b'isWalletAvailable', False)
        self._addBoolProperty(b'isShopOfferAvailable', False)
        self._addNumberProperty(b'shopOfferDiscount', 0)
        self._addNumberProperty(b'shopOfferTimeLeft', 0)
        self._addBoolProperty(b'isSingleChapter', False)
        self.onBackClick = self._addCommand(b'onBackClick')
        self.choosePackage = self._addCommand(b'choosePackage')
        self.showConfirm = self._addCommand(b'showConfirm')
        self.showRewards = self._addCommand(b'showRewards')
        self.onShopOfferClick = self._addCommand(b'onShopOfferClick')
        return
