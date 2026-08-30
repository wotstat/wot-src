from gui import SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.ExchangeWindowMeta import ExchangeWindowMeta
from gui.shared.gui_items.processors.common import GoldToCreditsExchanger
from gui.shared.utils import decorators
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.game_control import IWalletController
from skeletons.gui.shared import IItemsCache

class ExchangeWindow(ExchangeWindowMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    wallet = dependency.descriptor(IWalletController)

    def __init__(self, ctx):
        super(ExchangeWindow, self).__init__()
        self.currencyValue = ctx.get(b'currencyValue', 0)
        return

    def _populate(self):
        super(ExchangeWindow, self)._populate()
        stats = self.itemsCache.items.stats
        self.as_setPrimaryCurrencyS(stats.actualGold)
        self.as_setSecondaryCurrencyS(stats.actualCredits)
        self.as_exchangeRateS({b'value': (self.itemsCache.items.shop.defaults.exchangeRate), 
           b'actionValue': (self.itemsCache.items.shop.exchangeRate), 
           b'actionMode': True})
        self.as_setWalletStatusS(self.wallet.componentsStatuses)
        self.as_setDefaultPrimaryCurrencyValueS(self.currencyValue)
        return

    @decorators.adisp_process(b'transferMoney')
    def exchange(self, gold):
        result = yield GoldToCreditsExchanger(gold).request()
        if result and result.userMsg:
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
            self.onWindowClose()
        return

    def _subscribe(self):
        g_clientUpdateManager.addCurrencyCallback(Currency.CREDITS, self.__setCreditsCallBack)
        g_clientUpdateManager.addCurrencyCallback(Currency.GOLD, self._setGoldCallBack)
        g_clientUpdateManager.addCallbacks({b'shop.exchangeRate': (self.__setExchangeRateCallBack)})
        self.wallet.onWalletStatusChanged += self.__setWalletCallback
        self.itemsCache.onSyncCompleted += self.__setExchangeRateCallBack
        return

    def __setExchangeRateCallBack(self, *args):
        self.as_exchangeRateS({b'value': (self.itemsCache.items.shop.defaults.exchangeRate), 
           b'actionValue': (self.itemsCache.items.shop.exchangeRate), 
           b'actionMode': True})
        return

    def __setCreditsCallBack(self, credit):
        self.as_setSecondaryCurrencyS(credit)
        return

    def __setWalletCallback(self, status):
        self.as_setPrimaryCurrencyS(self.itemsCache.items.stats.actualGold)
        self.as_setWalletStatusS(status)
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _dispose(self):
        self.itemsCache.onSyncCompleted -= self.__setExchangeRateCallBack
        self.wallet.onWalletStatusChanged -= self.__setWalletCallback
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(ExchangeWindow, self)._dispose()
        return
