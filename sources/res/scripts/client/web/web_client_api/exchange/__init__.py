from exchange.personal_discounts_constants import ExchangeDiscountType, EXCHANGE_RATE_GOLD_NAME, EXCHANGE_RATE_FREE_XP_NAME
from gui.impl.lobby.exchange.exchange_rates_helper import convertToGuiLimit, getShowFormatRate
from helpers import dependency
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider
from web.web_client_api import w2capi, w2c, W2CSchema, Field
_selectedAmountValidator = lambda value, data: value >= 0

class _GoldSchema(W2CSchema):
    gold_amount = Field(required=True, type=int, validator=_selectedAmountValidator)


class _CreditsSchema(W2CSchema):
    credits_amount = Field(required=True, type=int, validator=_selectedAmountValidator)


@w2capi(name=b'personal_exchange_rates_discounts', key=b'action')
class PersonalExchangeRatesDiscountsWebApi(object):
    __exchangeRatesProvider = dependency.descriptor(IExchangeRatesWithDiscountsProvider)
    EXCHNAGE_RATES_MAPPING = {b'goldToCredits': EXCHANGE_RATE_GOLD_NAME, b'xpTranslation': EXCHANGE_RATE_FREE_XP_NAME}

    @w2c(_GoldSchema, b'get_credits_after_gold_to_credits_exchange')
    def calculateGoldToCreditsExchange(self, cmd):
        return {b'creditsAmount': (self.__exchangeRatesProvider.goldToCredits.calculateExchange(cmd.gold_amount))}

    @w2c(_CreditsSchema, b'get_gold_after_gold_to_credits_exchange')
    def calculateCreditsToGoldExchange(self, cmd):
        goldAmount, creditsAmount = self.__exchangeRatesProvider.goldToCredits.calculateResourceToExchange(cmd.credits_amount)
        return {b'goldAmount': goldAmount, b'creditsAmount': creditsAmount}

    @w2c(W2CSchema, b'get_personal_discounts')
    def getPersonalDiscounts(self, _):
        response = {}
        for personalDiscountName, exchangeRate in self.EXCHNAGE_RATES_MAPPING.items():
            discountInfo = None
            exchangeRate = self.__exchangeRatesProvider.get(exchangeRate)
            bestPersonalDiscount = exchangeRate.bestPersonalDiscount
            if bestPersonalDiscount is not None:
                discountInfo = self.__serializePersonalDiscountToDict(bestPersonalDiscount)
            response[personalDiscountName] = discountInfo

        return response

    @staticmethod
    def __serializePersonalDiscountToDict(discount):
        valueFrom, valueTo = getShowFormatRate(discount)
        return {b'showFormat': (discount.showFormat.value), 
           b'isLimited': (discount.discountType == ExchangeDiscountType.LIMITED), 
           b'limitAmount': (convertToGuiLimit(discount, discount.amountOfDiscount)), 
           b'lifetime': (discount.discountLifetime), 
           b'valueFrom': valueFrom, 
           b'valueTo': valueTo}
