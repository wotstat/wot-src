from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_buy_rewards_view_model import BattlePassBuyRewardsViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.buy_chapter_model import BuyChapterModel
from gui.impl.gen.view_models.views.lobby.battle_pass.buy_package_view_model import BuyPackageViewModel

class BattlePassBuyViewModel(ViewModel):
    __slots__ = (b'onShopOfferClick', b'onCloseClick', b'onBuyClick', b'onShowRewardsClick', b'onChangePurchaseWithLevels')
    BUY_STATE = b'buyState'
    REWARDS_STATE = b'rewardsState'

    def __init__(self, properties=8, commands=5):
        super(BattlePassBuyViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def package(self):
        return self._getViewModel(0)

    @staticmethod
    def getPackageType():
        return BuyPackageViewModel

    @property
    def rewards(self):
        return self._getViewModel(1)

    @staticmethod
    def getRewardsType():
        return BattlePassBuyRewardsViewModel

    def getState(self):
        return self._getString(2)

    def setState(self, value):
        self._setString(2, value)
        return

    def getIsWalletAvailable(self):
        return self._getBool(3)

    def setIsWalletAvailable(self, value):
        self._setBool(3, value)
        return

    def getIsShopOfferAvailable(self):
        return self._getBool(4)

    def setIsShopOfferAvailable(self, value):
        self._setBool(4, value)
        return

    def getShopOfferDiscount(self):
        return self._getNumber(5)

    def setShopOfferDiscount(self, value):
        self._setNumber(5, value)
        return

    def getIsLogoBg(self):
        return self._getBool(6)

    def setIsLogoBg(self, value):
        self._setBool(6, value)
        return

    def getChapters(self):
        return self._getArray(7)

    def setChapters(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getChaptersType():
        return BuyChapterModel

    def _initialize(self):
        super(BattlePassBuyViewModel, self)._initialize()
        self._addViewModelProperty(b'package', BuyPackageViewModel())
        self._addViewModelProperty(b'rewards', BattlePassBuyRewardsViewModel())
        self._addStringProperty(b'state', b'buyState')
        self._addBoolProperty(b'isWalletAvailable', False)
        self._addBoolProperty(b'isShopOfferAvailable', False)
        self._addNumberProperty(b'shopOfferDiscount', 0)
        self._addBoolProperty(b'isLogoBg', False)
        self._addArrayProperty(b'chapters', Array())
        self.onShopOfferClick = self._addCommand(b'onShopOfferClick')
        self.onCloseClick = self._addCommand(b'onCloseClick')
        self.onBuyClick = self._addCommand(b'onBuyClick')
        self.onShowRewardsClick = self._addCommand(b'onShowRewardsClick')
        self.onChangePurchaseWithLevels = self._addCommand(b'onChangePurchaseWithLevels')
        return
