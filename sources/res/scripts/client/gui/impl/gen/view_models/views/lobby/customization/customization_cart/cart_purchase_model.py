from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_compound_price_model import UserCompoundPriceModel

class CartPurchaseModel(ViewModel):
    __slots__ = (b'onBuyAction',)

    def __init__(self, properties=4, commands=1):
        super(CartPurchaseModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def totalPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getTotalPriceType():
        return UserCompoundPriceModel

    def getPurchasedCount(self):
        return self._getNumber(1)

    def setPurchasedCount(self, value):
        self._setNumber(1, value)
        return

    def getIsEnoughMoney(self):
        return self._getBool(2)

    def setIsEnoughMoney(self, value):
        self._setBool(2, value)
        return

    def getIsGoldPrice(self):
        return self._getBool(3)

    def setIsGoldPrice(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(CartPurchaseModel, self)._initialize()
        self._addViewModelProperty(b'totalPrice', UserCompoundPriceModel())
        self._addNumberProperty(b'purchasedCount', 0)
        self._addBoolProperty(b'isEnoughMoney', False)
        self._addBoolProperty(b'isGoldPrice', False)
        self.onBuyAction = self._addCommand(b'onBuyAction')
        return
