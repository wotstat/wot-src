from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_model import ExchangeRateModel

class DiscountType(Enum):
    LIMITED = b'limited'
    UNLIMITED = b'unlimited'


class ShowFormat(Enum):
    COEFFICIENT = b'coefficient'
    INTEGER = b'integer'
    TEMPORARY = b'temporary'
    LIMITED = b'limited'


class ExchangeRateDiscountModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ExchangeRateDiscountModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def exchangeRate(self):
        return self._getViewModel(0)

    @staticmethod
    def getExchangeRateType():
        return ExchangeRateModel

    def getIsDiscountAvailable(self):
        return self._getBool(1)

    def setIsDiscountAvailable(self, value):
        self._setBool(1, value)
        return

    def getDiscountType(self):
        return DiscountType(self._getString(2))

    def setDiscountType(self, value):
        self._setString(2, value.value)
        return

    def getShowFormat(self):
        return ShowFormat(self._getString(3))

    def setShowFormat(self, value):
        self._setString(3, value.value)
        return

    def getAmountOfDiscount(self):
        return self._getNumber(4)

    def setAmountOfDiscount(self, value):
        self._setNumber(4, value)
        return

    def getDiscountLifetime(self):
        return self._getNumber(5)

    def setDiscountLifetime(self, value):
        self._setNumber(5, value)
        return

    def getDiscountPercent(self):
        return self._getNumber(6)

    def setDiscountPercent(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(ExchangeRateDiscountModel, self)._initialize()
        self._addViewModelProperty(b'exchangeRate', ExchangeRateModel())
        self._addBoolProperty(b'isDiscountAvailable', False)
        self._addStringProperty(b'discountType', DiscountType.LIMITED.value)
        self._addStringProperty(b'showFormat', ShowFormat.COEFFICIENT.value)
        self._addNumberProperty(b'amountOfDiscount', 0)
        self._addNumberProperty(b'discountLifetime', 0)
        self._addNumberProperty(b'discountPercent', 0)
        return
