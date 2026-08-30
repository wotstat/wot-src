from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class ArmoryYardPurchaseStageBuyViewModel(ViewModel):
    __slots__ = (b'onBuy', b'onCancel', b'onBack')
    ARG_TOKENS = b'tokens'
    ARG_CURRENCY_TYPE = b'currencyType'

    def __init__(self, properties=8, commands=3):
        super(ArmoryYardPurchaseStageBuyViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceModel

    @property
    def crystalPrice(self):
        return self._getViewModel(1)

    @staticmethod
    def getCrystalPriceType():
        return PriceModel

    def getTokensCount(self):
        return self._getNumber(2)

    def setTokensCount(self, value):
        self._setNumber(2, value)
        return

    def getPayedTokensLimit(self):
        return self._getNumber(3)

    def setPayedTokensLimit(self, value):
        self._setNumber(3, value)
        return

    def getIsWalletAvailable(self):
        return self._getBool(4)

    def setIsWalletAvailable(self, value):
        self._setBool(4, value)
        return

    def getIsBlurEnabled(self):
        return self._getBool(5)

    def setIsBlurEnabled(self, value):
        self._setBool(5, value)
        return

    def getUserGold(self):
        return self._getNumber(6)

    def setUserGold(self, value):
        self._setNumber(6, value)
        return

    def getUserCrystal(self):
        return self._getNumber(7)

    def setUserCrystal(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(ArmoryYardPurchaseStageBuyViewModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addViewModelProperty(b'crystalPrice', PriceModel())
        self._addNumberProperty(b'tokensCount', 0)
        self._addNumberProperty(b'payedTokensLimit', 0)
        self._addBoolProperty(b'isWalletAvailable', True)
        self._addBoolProperty(b'isBlurEnabled', False)
        self._addNumberProperty(b'userGold', 0)
        self._addNumberProperty(b'userCrystal', 0)
        self.onBuy = self._addCommand(b'onBuy')
        self.onCancel = self._addCommand(b'onCancel')
        self.onBack = self._addCommand(b'onBack')
        return
