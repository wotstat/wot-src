from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BaseExchangeWindowMeta(AbstractWindowView):

    def exchange(self, data):
        self._printOverrideError(b'exchange')
        return

    def as_setPrimaryCurrencyS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrimaryCurrency(value)
        return

    def as_exchangeRateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_exchangeRate(data)
        return
