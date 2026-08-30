from gui.Scaleform.daapi.view.lobby.exchange.BaseExchangeWindow import BaseExchangeWindow

class ExchangeWindowMeta(BaseExchangeWindow):

    def as_setSecondaryCurrencyS(self, credits):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryCurrency(credits)
        return

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)
        return

    def as_setDefaultPrimaryCurrencyValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultPrimaryCurrencyValue(value)
        return
