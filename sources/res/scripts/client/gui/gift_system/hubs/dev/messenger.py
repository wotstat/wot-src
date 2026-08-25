import logging, typing
from gui.gift_system.hubs.base.messenger import GiftEventBaseMessenger
from gui.gift_system.hubs.dev import IDevMessagesPusher
from gui.shared.formatters import text_styles
if typing.TYPE_CHECKING:
    from gui.gift_system.wrappers import GiftsHistoryData, IncomeSysMessage, SendGiftResponse
_logger = logging.getLogger(__name__)

class GiftEventDevMessenger(GiftEventBaseMessenger, IDevMessagesPusher):
    __slots__ = ()

    def __repr__(self):
        return (b'GiftEventDevMessenger id={}').format(self._settings.eventID)

    @classmethod
    def _formatMessage(cls, message):
        return text_styles.statInfo(message)

    def _pushHistoryMessage(self, history):
        _logger.info(b'%s push history message %s', self, history)
        self._pushClientMessage((b'{}\npush history message').format(self))
        return

    def _pushIncomeMessage(self, incomeData):
        _logger.info(b'%s push income message %s', self, incomeData)
        self._pushClientMessage((b'{}\npush income message').format(self))
        return

    def _pushOutcomeMessage(self, outcomeData):
        _logger.info(b'%s push outcome message %s', self, outcomeData)
        self._pushClientMessage((b'{}\npush outcome message').format(self))
        return
