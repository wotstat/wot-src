import logging
from gui.shared.gui_items.processors.stall import PurchaseStallProductProcessor
from helpers import dependency
from skeletons.gui.game_control import ISummerSaleController
from skeletons.gui.shared import IItemsCache
from web.web_client_api import Field, W2CSchema, WebCommandException, w2c, w2capi
_logger = logging.getLogger(__name__)

def _amountValidator(amount, _=None):
    if amount and amount <= 0:
        raise WebCommandException(b'amount must be greater than 0')
    return True


class _ProductCodeSchema(W2CSchema):
    productCode = Field(required=True, type=basestring)


class _BuyProductSchema(W2CSchema):
    productCode = Field(required=True, type=basestring)
    amount = Field(required=False, type=int, validator=_amountValidator)


@w2capi(name=b'summersale', key=b'action')
class SummerSaleWebApi(W2CSchema):
    __summerSaleController = dependency.descriptor(ISummerSaleController)
    __itemsCache = dependency.descriptor(IItemsCache)

    @w2c(_BuyProductSchema, b'buy_product')
    def buyServerProductByCode(self, cmd):
        success, error = False, b''
        if self.__summerSaleController.isEnabled():
            response = yield PurchaseStallProductProcessor(cmd.productCode, cmd.amount).request()
            if response:
                success, error = response.success, response.userMsg
            else:
                error = b'Undefined server error'
        else:
            error = b'SummerSale event is not active'
        yield {b'success': success, 
           b'error': error}
        return

    @w2c(_ProductCodeSchema, b'get_product_lqo')
    def getLimitQuantity(self, cmd):
        yield {b'count': (self.__itemsCache.items.tokens.getTokenCount((b'{}_no_log').format(cmd.productCode)) or 0), 
           b'success': True}
        return
