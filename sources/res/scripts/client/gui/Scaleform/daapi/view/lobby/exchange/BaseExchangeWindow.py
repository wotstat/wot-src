from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.BaseExchangeWindowMeta import BaseExchangeWindowMeta

class BaseExchangeWindow(BaseExchangeWindowMeta):

    def __init__(self, ctx=None):
        super(BaseExchangeWindow, self).__init__(self)
        return

    def _populate(self):
        super(BaseExchangeWindow, self)._populate()
        self._subscribe()
        return

    def _subscribe(self):
        return

    def _setGoldCallBack(self, gold):
        self.as_setPrimaryCurrencyS(gold)
        return

    def _dispose(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(BaseExchangeWindow, self)._dispose()
        return
