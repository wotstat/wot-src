from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.exchange.currency_tab_model import CurrencyTabModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_discount_model import ExchangeRateDiscountModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_model import ExchangeRateModel

class ExchangeRateBaseModel(ViewModel):
    __slots__ = (b'onClose', b'onExchange', b'onOpenAllDiscountsWindow', b'onSelectedValueUpdated')

    def __init__(self, properties=9, commands=4):
        super(ExchangeRateBaseModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def exchangeRate(self):
        return self._getViewModel(0)

    @staticmethod
    def getExchangeRateType():
        return ExchangeRateModel

    @property
    def discount(self):
        return self._getViewModel(1)

    @staticmethod
    def getDiscountType():
        return ExchangeRateDiscountModel

    @property
    def balance(self):
        return self._getViewModel(2)

    @staticmethod
    def getBalanceType():
        return CurrencyTabModel

    def getGoldAmountForExchange(self):
        return self._getNumber(3)

    def setGoldAmountForExchange(self, value):
        self._setNumber(3, value)
        return

    def getResourceAmountForExchange(self):
        return self._getNumber(4)

    def setResourceAmountForExchange(self, value):
        self._setNumber(4, value)
        return

    def getMaxResourceAmountForExchange(self):
        return self._getNumber(5)

    def setMaxResourceAmountForExchange(self, value):
        self._setNumber(5, value)
        return

    def getMaxGoldAmountForExchange(self):
        return self._getNumber(6)

    def setMaxGoldAmountForExchange(self, value):
        self._setNumber(6, value)
        return

    def getBackground(self):
        return self._getResource(7)

    def setBackground(self, value):
        self._setResource(7, value)
        return

    def getAmountOfPersonalDiscounts(self):
        return self._getNumber(8)

    def setAmountOfPersonalDiscounts(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(ExchangeRateBaseModel, self)._initialize()
        self._addViewModelProperty(b'exchangeRate', ExchangeRateModel())
        self._addViewModelProperty(b'discount', ExchangeRateDiscountModel())
        self._addViewModelProperty(b'balance', CurrencyTabModel())
        self._addNumberProperty(b'goldAmountForExchange', 0)
        self._addNumberProperty(b'resourceAmountForExchange', 0)
        self._addNumberProperty(b'maxResourceAmountForExchange', 0)
        self._addNumberProperty(b'maxGoldAmountForExchange', 0)
        self._addResourceProperty(b'background', R.invalid())
        self._addNumberProperty(b'amountOfPersonalDiscounts', 0)
        self.onClose = self._addCommand(b'onClose')
        self.onExchange = self._addCommand(b'onExchange')
        self.onOpenAllDiscountsWindow = self._addCommand(b'onOpenAllDiscountsWindow')
        self.onSelectedValueUpdated = self._addCommand(b'onSelectedValueUpdated')
        return
