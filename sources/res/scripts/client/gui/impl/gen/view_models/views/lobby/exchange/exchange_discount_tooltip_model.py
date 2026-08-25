from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_model import ExchangeRateModel

class CurrencyType(Enum):
    CREDITS = b'credits'
    GOLD = b'gold'
    FREEXP = b'freeXP'


class ExchangeDiscountTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ExchangeDiscountTooltipModel, self).__init__(properties=properties, commands=commands)
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

    @property
    def personalExchangeRate(self):
        return self._getViewModel(2)

    @staticmethod
    def getPersonalExchangeRateType():
        return ExchangeRateModel

    def getIsTemporary(self):
        return self._getBool(3)

    def setIsTemporary(self, value):
        self._setBool(3, value)
        return

    def getCurrencyTypeFrom(self):
        return CurrencyType(self._getString(4))

    def setCurrencyTypeFrom(self, value):
        self._setString(4, value.value)
        return

    def getCurrencyTypeTo(self):
        return CurrencyType(self._getString(5))

    def setCurrencyTypeTo(self, value):
        self._setString(5, value.value)
        return

    def _initialize(self):
        super(ExchangeDiscountTooltipModel, self)._initialize()
        self._addViewModelProperty(b'defaultExchangeRate', ExchangeRateModel())
        self._addViewModelProperty(b'commonExchangeRate', ExchangeRateModel())
        self._addViewModelProperty(b'personalExchangeRate', ExchangeRateModel())
        self._addBoolProperty(b'isTemporary', False)
        self._addStringProperty(b'currencyTypeFrom', CurrencyType.GOLD.value)
        self._addStringProperty(b'currencyTypeTo', CurrencyType.CREDITS.value)
        return
