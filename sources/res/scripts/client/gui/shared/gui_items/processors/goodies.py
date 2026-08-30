import logging, typing, BigWorld, AccountCommands
from gui.SystemMessages import SM_TYPE, CURRENCY_TO_SM_TYPE
from gui.impl import backport
from gui.shared.formatters import formatPrice
from gui.shared.gui_items.processors import Processor, makeI18nError, makeI18nSuccess, plugins as proc_plugs
from gui.shared.gui_items.gui_item_economics import ItemPrice
from gui.shared.money import Currency
from gui.shared.utils import code2str
if typing.TYPE_CHECKING:
    from gui.SystemMessages import ResultMsg
_logger = logging.getLogger(__name__)

class BoosterProcessor(Processor):

    def __init__(self, booster, opType, plugins=None):
        super(BoosterProcessor, self).__init__(plugins or [])
        self.booster = booster
        self.opType = opType
        return

    def _response(self, code, callback, ctx=None, errStr=b''):
        if code < 0:
            _logger.error(b"Server responses an error [%s] while process %s '%s'", code2str(code), self.booster.boosterGuiType, str(self.booster))
            return callback(self._errorHandler(code, ctx=ctx, errStr=errStr))
        return callback(self._successHandler(code, ctx=ctx))

    def _getMsgCtx(self):
        raise NotImplementedError
        return

    def _formMessage(self, msg):
        _logger.debug(b'Generating response for BoosterProcessor: %s %s', self.opType, msg)
        return (b'booster_{opType}/{msg}').format(opType=self.opType, msg=msg)

    def _errorHandler(self, code, errStr=b'', ctx=None):
        if not errStr:
            errStr = b'server_error' if code != AccountCommands.RES_CENTER_DISCONNECTED else b'server_error_centerDown'
        return makeI18nError(self._formMessage(errStr), defaultSysMsgKey=self._formMessage(b'server_error'), auxData={b'errStr': errStr}, **self._getMsgCtx())


class BoosterActivator(BoosterProcessor):

    def __init__(self, booster):
        super(BoosterActivator, self).__init__(booster, b'activate', [proc_plugs.BoosterActivateValidator(booster)])
        return

    def _getMsgCtx(self):
        return {b'boosterName': (self.booster.userName), 
           b'time': (self.booster.getEffectTimeStr())}

    def _successHandler(self, code, ctx=None):
        return makeI18nSuccess(self._formMessage(b'success'), type=SM_TYPE.Information, **self._getMsgCtx())

    def _request(self, callback):
        _logger.debug(b'Make server request to activate booster, %s, %s', self.booster.boosterID, self.booster.userName)
        BigWorld.player().activateGoodie(self.booster.boosterID, (lambda code, errStr: self._response(code, callback, errStr=errStr)))
        return


class BoosterTradeProcessor(BoosterProcessor):

    def __init__(self, booster, count, opType, plugs=None):
        super(BoosterTradeProcessor, self).__init__(booster, opType, plugs or [])
        self.count = count
        return

    def _getMsgCtx(self):
        return {b'boosterName': (self.booster.userName), 
           b'count': (backport.getIntegralFormat(int(self.count))), 
           b'money': (formatPrice(self._getOpPrice().price))}

    def _getOpPrice(self):
        raise NotImplementedError
        return


class BoosterBuyer(BoosterTradeProcessor):

    def __init__(self, booster, count, currency):
        super(BoosterBuyer, self).__init__(booster, count, b'buy')
        self.buyCurrency = currency
        self.addPlugins((
         proc_plugs.MoneyValidator(self._getOpPrice().price),))
        return

    def _getOpPrice(self):
        minItemPrice = self.booster.buyPrices.getMinItemPriceByCurrency(self.buyCurrency)
        if minItemPrice is None:
            _logger.error(b'Attempt to buy booster %s for the invalid currency %s.', self.booster, self.buyCurrency)
            minItemPrice = self.booster.buyPrices.itemPrice
        return minItemPrice * self.count

    def _successHandler(self, code, ctx=None):
        sysMsgType = CURRENCY_TO_SM_TYPE.get(self.buyCurrency, SM_TYPE.PurchaseForCredits)
        return makeI18nSuccess(sysMsgKey=self._formMessage(b'success'), type=sysMsgType, **self._getMsgCtx())

    def _request(self, callback):
        _logger.debug(b'Make server request to buy booster: %s, %s, %s, %s', self.booster.boosterID, self.booster.buyPrices, self.count, self.buyCurrency)
        BigWorld.player().shop.buyGoodie(self.booster.boosterID, self.count, self.buyCurrency == Currency.GOLD, (lambda code: self._response(code, callback)))
        return


class BoosterSeller(BoosterTradeProcessor):

    def __init__(self, booster, count):
        super(BoosterSeller, self).__init__(booster, count, b'sell')
        return

    def _getOpPrice(self):
        sellPrice = self.booster.sellPrices.itemPrice
        if not sellPrice:
            _logger.error(b'Attempt to sell booster %s that is not sold.', self.booster)
        return sellPrice * self.count

    def _successHandler(self, code, ctx=None):
        return makeI18nSuccess(sysMsgKey=self._formMessage(b'success'), type=SM_TYPE.Selling, **self._getMsgCtx())

    def _request(self, callback):
        _logger.debug(b'Make server request to sell booster: %s, %s', self.booster, self.count)
        BigWorld.player().inventory.sellGoodie(self.booster.boosterID, self.count, (lambda code: self._response(code, callback)))
        return
