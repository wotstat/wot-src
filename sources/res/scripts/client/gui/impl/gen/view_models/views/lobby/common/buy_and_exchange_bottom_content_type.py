from frameworks.wulf import ViewModel

class BuyAndExchangeBottomContentType(ViewModel):
    __slots__ = ()
    DEAL_PANEL = b'dealPanel'
    EXCHANGE_PANEL = b'exchangePanel'

    def __init__(self, properties=0, commands=0):
        super(BuyAndExchangeBottomContentType, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(BuyAndExchangeBottomContentType, self)._initialize()
        return
