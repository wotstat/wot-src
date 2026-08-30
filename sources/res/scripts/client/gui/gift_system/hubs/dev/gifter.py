import logging
from adisp import adisp_process
from gui.gift_system.constants import GifterResponseState
from gui.gift_system.hubs.base.gifter import GiftEventBaseGifter
from gui.gift_system.hubs.dev import IDevMessagesPusher
from gui.shared.formatters import text_styles
_logger = logging.getLogger(__name__)

class GiftEventDevGifter(GiftEventBaseGifter, IDevMessagesPusher):
    __slots__ = ()

    def __repr__(self):
        return (b'GiftEventDevGifter id={}').format(self._settings.eventID)

    @adisp_process
    def sendGift(self, entitlementCode, receiverID, metaInfo, callback=None):
        result = yield super(GiftEventDevGifter, self).sendGift(entitlementCode, receiverID, metaInfo)
        if result.state not in (GifterResponseState.WEB_SUCCESS, GifterResponseState.WEB_FAILURE):
            _logger.info(b'%s send gift rejected by reason=%s', self, result.state.value)
            self._pushClientMessage((b'{}\nsend gift rejected').format(self))
        return

    @adisp_process
    def sendGiftMultiple(self, entitlementCode, receiverIDs, metaInfo, callback=None):
        result = yield super(GiftEventDevGifter, self).sendGift(entitlementCode, receiverIDs, metaInfo)
        if result.state not in (GifterResponseState.WEB_SUCCESS, GifterResponseState.WEB_FAILURE):
            _logger.info(b'%s send gift rejected by reason=%s', self, result.state.value)
            self._pushClientMessage((b'{}\nsend gift rejected').format(self))
        return

    @classmethod
    def _formatMessage(cls, message):
        return text_styles.statusAlert(message)
