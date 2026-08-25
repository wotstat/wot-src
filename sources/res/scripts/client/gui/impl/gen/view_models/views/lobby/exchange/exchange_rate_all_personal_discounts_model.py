from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.exchange.discount_presentation import DiscountPresentation
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_model import ExchangeRateModel

class CurrencyType(Enum):
    CREDITS = b'credits'
    GOLD = b'gold'
    FREEXP = b'freeXP'


class ExchangeRateAllPersonalDiscountsModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=6, commands=1):
        super(ExchangeRateAllPersonalDiscountsModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def defaultExchangeRate(self):
        return self._getViewModel(0)

    @staticmethod
    def getDefaultExchangeRateType():
        return ExchangeRateModel

    @property
    def commonExchangeRate(self):
        return self._getViewModel(1)

    @staticmethod
    def getCommonExchangeRateType():
        return ExchangeRateModel

    def getCurrencyTypeFrom(self):
        return CurrencyType(self._getString(2))

    def setCurrencyTypeFrom(self, value):
        self._setString(2, value.value)
        return

    def getCurrencyTypeTo(self):
        return CurrencyType(self._getString(3))

    def setCurrencyTypeTo(self, value):
        self._setString(3, value.value)
        return

    def getAllDiscountsLimitsAmount(self):
        return self._getNumber(4)

    def setAllDiscountsLimitsAmount(self, value):
        self._setNumber(4, value)
        return

    def getDiscounts(self):
        return self._getArray(5)

    def setDiscounts(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getDiscountsType():
        return DiscountPresentation

    def _initialize(self):
        super(ExchangeRateAllPersonalDiscountsModel, self)._initialize()
        self._addViewModelProperty(b'defaultExchangeRate', ExchangeRateModel())
        self._addViewModelProperty(b'commonExchangeRate', ExchangeRateModel())
        self._addStringProperty(b'currencyTypeFrom', CurrencyType.GOLD.value)
        self._addStringProperty(b'currencyTypeTo', CurrencyType.CREDITS.value)
        self._addNumberProperty(b'allDiscountsLimitsAmount', 0)
        self._addArrayProperty(b'discounts', Array())
        self.onClose = self._addCommand(b'onClose')
        return
