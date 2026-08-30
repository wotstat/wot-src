import logging, typing
from gui.gift_system.hubs.base.hub_core import GiftEventBaseHub
from gui.gift_system.hubs.dev import IDevMessagesPusher
from gui.gift_system.hubs.dev.stamper import GiftEventDevStamper
from gui.gift_system.hubs.dev.gifter import GiftEventDevGifter
from gui.gift_system.hubs.dev.messenger import GiftEventDevMessenger
from gui.gift_system.hubs.dev.relations_keeper import GiftEventDevKeeper
if typing.TYPE_CHECKING:
    from gui.gift_system.hubs.base.stamper import IGiftEventStamper
    from gui.gift_system.hubs.base.gifter import IGiftEventGifter
    from gui.gift_system.hubs.base.messenger import IGiftEventMessenger
    from gui.gift_system.hubs.base.relations_keeper import IGiftEventKeeper
    from gui.gift_system.wrappers import SendGiftResponse
    from helpers.server_settings import GiftEventConfig
_logger = logging.getLogger(__name__)

class GiftEventDevHub(GiftEventBaseHub, IDevMessagesPusher):
    __slots__ = ()

    def __init__(self, eventSettings, isMessagesAllowed):
        super(GiftEventDevHub, self).__init__(eventSettings, isMessagesAllowed)
        _logger.info(b'%s is created with settings %s', self, self._settings)
        self._pushClientMessage((b'{}\nis created').format(self))
        return

    def __repr__(self):
        return (b'GiftEventDevHub id={}, state={}').format(self._settings.eventID, self._settings.giftEventState)

    def destroy(self):
        _logger.info(b'%s is destroyed', self)
        self._pushClientMessage((b'{}\nis destroyed').format(self))
        super(GiftEventDevHub, self).destroy()
        return

    def reset(self):
        _logger.info(b'%s is reset', self)
        self._pushClientMessage((b'{}\nis reset').format(self))
        super(GiftEventDevHub, self).reset()
        return

    def _createGifter(self, eventSettings):
        return GiftEventDevGifter(eventSettings, self._onGifterResponse)

    def _createKeeper(self, eventSettings):
        return GiftEventDevKeeper(eventSettings, self._onKeeperCleared)

    def _createMessenger(self, eventSetting, isMessagesAllowed):
        return GiftEventDevMessenger(eventSetting, isMessagesAllowed)

    def _createStamper(self, eventSettings):
        return GiftEventDevStamper(eventSettings, self._onStamperUpdate)

    def _onGifterResponse(self, responseData):
        _logger.info(b'%s received gifter response %s', self, responseData)
        self._pushClientMessage((b'{}\nreceived gifter response').format(self))
        super(GiftEventDevHub, self)._onGifterResponse(responseData)
        return

    def _onKeeperCleared(self):
        _logger.info(b'%s received keeper clearing', self)
        self._pushClientMessage((b'{}\nreceived keeper clearing').format(self))
        super(GiftEventDevHub, self)._onKeeperCleared()
        return

    def _onStamperUpdate(self):
        _logger.info(b'%s received stamper update', self)
        self._pushClientMessage((b'{}\nreceived stamper update').format(self))
        super(GiftEventDevHub, self)._onStamperUpdate()
        return

    def _updateSettings(self, eventSettings):
        _logger.info(b'%s received new settings %s', self, eventSettings)
        self._pushClientMessage((b'{}\nreceived new server settings').format(self))
        super(GiftEventDevHub, self)._updateSettings(eventSettings)
        return
