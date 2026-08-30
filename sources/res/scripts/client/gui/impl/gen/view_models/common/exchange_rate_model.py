from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_discount_model import ExchangeRateDiscountModel

class ExchangeRateModel(ViewModel):
    __slots__ = (b'onOpenAllDiscountsWindow', b'onSelectedValueUpdated')

    def __init__(self, properties=5, commands=2):
        super(ExchangeRateModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def discount(self):
        return self._getViewModel(0)

    @staticmethod
    def getDiscountType():
        return ExchangeRateDiscountModel

    def getDefault(self):
        return self._getReal(1)

    def setDefault(self, value):
        self._setReal(1, value)
        return

    def getMaxResourceAmountForExchange(self):
        return self._getNumber(2)

    def setMaxResourceAmountForExchange(self, value):
        self._setNumber(2, value)
        return

    def getMaxGoldAmountForExchange(self):
        return self._getNumber(3)

    def setMaxGoldAmountForExchange(self, value):
        self._setNumber(3, value)
        return

    def getAmountOfPersonalDiscounts(self):
        return self._getNumber(4)

    def setAmountOfPersonalDiscounts(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(ExchangeRateModel, self)._initialize()
        self._addViewModelProperty(b'discount', ExchangeRateDiscountModel())
        self._addRealProperty(b'default', 0.0)
        self._addNumberProperty(b'maxResourceAmountForExchange', 0)
        self._addNumberProperty(b'maxGoldAmountForExchange', 1)
        self._addNumberProperty(b'amountOfPersonalDiscounts', 0)
        self.onOpenAllDiscountsWindow = self._addCommand(b'onOpenAllDiscountsWindow')
        self.onSelectedValueUpdated = self._addCommand(b'onSelectedValueUpdated')
        return
