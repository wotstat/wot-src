from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.page.header.premium_account_subscription_model import PremiumAccountSubscriptionModel
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusSubscriptionModel

class SubscriptionsModel(ViewModel):
    __slots__ = (b'onOpenPremium', b'onOpenWotPlus')

    def __init__(self, properties=4, commands=2):
        super(SubscriptionsModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def wotPlus(self):
        return self._getViewModel(0)

    @staticmethod
    def getWotPlusType():
        return WotPlusSubscriptionModel

    @property
    def premiumAccount(self):
        return self._getViewModel(1)

    @staticmethod
    def getPremiumAccountType():
        return PremiumAccountSubscriptionModel

    def getIsSteamPlatform(self):
        return self._getBool(2)

    def setIsSteamPlatform(self, value):
        self._setBool(2, value)
        return

    def getIsCnRealm(self):
        return self._getBool(3)

    def setIsCnRealm(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(SubscriptionsModel, self)._initialize()
        self._addViewModelProperty(b'wotPlus', WotPlusSubscriptionModel())
        self._addViewModelProperty(b'premiumAccount', PremiumAccountSubscriptionModel())
        self._addBoolProperty(b'isSteamPlatform', False)
        self._addBoolProperty(b'isCnRealm', False)
        self.onOpenPremium = self._addCommand(b'onOpenPremium')
        self.onOpenWotPlus = self._addCommand(b'onOpenWotPlus')
        return
