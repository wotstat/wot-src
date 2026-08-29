from uilogging.base.logger import MetricsLogger
from wotdecorators import noexcept

class TicketExchangeLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(TicketExchangeLogger, self).__init__(b'exchange_tickets')
        return

    @noexcept
    def logEnter(self):
        self.log(action=b'EnterMainScreen', item=b'MainScreen')
        return

    @noexcept
    def logExit(self):
        self.log(action=b'ExitMainScreen', item=b'MainScreen')
        return
