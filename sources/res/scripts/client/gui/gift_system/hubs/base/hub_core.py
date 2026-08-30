import typing
from Event import Event, EventManager
from gui.gift_system.constants import HubUpdateReason
from gui.gift_system.hubs.base.stamper import GiftEventBaseStamper
from gui.gift_system.hubs.base.gifter import GiftEventBaseGifter
from gui.gift_system.hubs.base.messenger import GiftEventBaseMessenger
from gui.gift_system.hubs.base.relations_keeper import GiftEventBaseKeeper
if typing.TYPE_CHECKING:
    from gifts.gifts_common import ClientReqStrategy
    from gui.gift_system.hubs.base.stamper import IGiftEventStamper
    from gui.gift_system.hubs.base.gifter import IGiftEventGifter
    from gui.gift_system.hubs.base.messenger import IGiftEventMessenger
    from gui.gift_system.hubs.base.relations_keeper import IGiftEventKeeper
    from gui.gift_system.wrappers import GiftsHistoryData, GiftsWebState, IncomeSysMessage, SendGiftResponse
    from helpers.server_settings import GiftEventConfig

class IGiftEventHub(object):
    onHubUpdated = None

    def destroy(self):
        return

    def isHistoryReceived(self):
        raise NotImplementedError
        return

    def isHistoryRequired(self):
        raise NotImplementedError
        return

    def isWebStateReceived(self):
        raise NotImplementedError
        return

    def isWebStateRequired(self, strategy=None):
        raise NotImplementedError
        return

    def getGifter(self):
        raise NotImplementedError
        return

    def getKeeper(self):
        raise NotImplementedError
        return

    def getMessenger(self):
        raise NotImplementedError
        return

    def getStamper(self):
        raise NotImplementedError
        return

    def getSettings(self):
        raise NotImplementedError
        return

    def processHistory(self, history):
        raise NotImplementedError
        return

    def processMessage(self, incomeData):
        raise NotImplementedError
        return

    def processWebState(self, webState):
        raise NotImplementedError
        return

    def reset(self):
        return

    def updateSettings(self, eventSettings):
        raise NotImplementedError
        return


class GiftEventBaseHub(IGiftEventHub):
    __slots__ = (b'onHubUpdated', b'_eventManager', b'_settings', b'_isHistoryReceived', b'_isWebStateReceived', b'_gifter', b'_keeper', b'_messenger', b'_stamper')

    def __init__(self, eventSettings, isMessagesAllowed):
        self._eventManager = EventManager()
        self.onHubUpdated = Event(self._eventManager)
        self._isHistoryReceived = False
        self._isWebStateReceived = False
        self._settings = eventSettings
        self._gifter = self._createGifter(eventSettings)
        self._keeper = self._createKeeper(eventSettings)
        self._messenger = self._createMessenger(eventSettings, isMessagesAllowed)
        self._stamper = self._createStamper(eventSettings)
        return

    def destroy(self):
        self._gifter.destroy()
        self._keeper.destroy()
        self._messenger.destroy()
        self._stamper.destroy()
        self._eventManager.clear()
        return

    def isHistoryReceived(self):
        return self._isHistoryReceived

    def isHistoryRequired(self):
        return not self._isHistoryReceived and self._isHistoryEnabled()

    def isWebStateReceived(self):
        return self._isWebStateReceived

    def isWebStateRequired(self, strategy=None):
        strategy = strategy or self._settings.clientReqStrategy
        if not self._isHistoryReceived or strategy != self._settings.clientReqStrategy:
            return False
        return not self._isWebStateReceived and self._isWebStateEnabled()

    def getGifter(self):
        return self._gifter

    def getKeeper(self):
        return self._keeper

    def getMessenger(self):
        return self._messenger

    def getStamper(self):
        return self._stamper

    def getSettings(self):
        return self._settings

    def processMessage(self, incomeData):
        self._messenger.pushIncomeMessage(incomeData)
        self._keeper.processIncomeMessage(incomeData)
        self.onHubUpdated(HubUpdateReason.INCOME_GIFT, incomeData)
        return

    def processHistory(self, history):
        if not self.isHistoryRequired() or history is None:
            return
        self._messenger.pushHistoryMessage(history)
        self._isHistoryReceived = True
        self.onHubUpdated(HubUpdateReason.HISTORY, history)
        return

    def processWebState(self, webState):
        if not self.isWebStateRequired() or webState is None:
            return
        self._keeper.processWebState(webState)
        self._isWebStateReceived = True
        self.onHubUpdated(HubUpdateReason.WEB_STATE, webState)
        return

    def reset(self):
        self._isHistoryReceived = False
        self._isWebStateReceived = False
        self._gifter.reset()
        self._keeper.reset()
        self._messenger.reset()
        self._stamper.reset()
        return

    def updateSettings(self, eventSettings):
        if self._settings == eventSettings:
            return
        self._updateSettings(eventSettings)
        self._settings = eventSettings
        self.onHubUpdated(HubUpdateReason.SETTINGS, eventSettings)
        return

    def _isHistoryEnabled(self, eventSettings=None):
        settings = eventSettings or self._settings
        return settings.isEnabled

    def _isWebStateEnabled(self, eventSettings=None):
        settings = eventSettings or self._settings
        return settings.isEnabled

    def _createGifter(self, eventSettings):
        return GiftEventBaseGifter(eventSettings, self._onGifterResponse)

    def _createKeeper(self, eventSettings):
        return GiftEventBaseKeeper(eventSettings, self._onKeeperCleared)

    def _createMessenger(self, eventSettings, isMessagesAllowed):
        return GiftEventBaseMessenger(eventSettings, isMessagesAllowed)

    def _createStamper(self, eventSettings):
        return GiftEventBaseStamper(eventSettings, self._onStamperUpdate)

    def _onGifterResponse(self, responseData):
        self._messenger.pushOutcomeMessage(responseData)
        self._keeper.processOutcomeMessage(responseData)
        self.onHubUpdated(HubUpdateReason.OUTCOME_GIFT, responseData)
        return

    def _onKeeperCleared(self):
        self.onHubUpdated(HubUpdateReason.KEEPER_CLEAR)
        return

    def _onStamperUpdate(self):
        self.onHubUpdated(HubUpdateReason.STAMPER_UPDATE)
        return

    def _updateSettings(self, eventSettings):
        if not self._isHistoryEnabled(eventSettings):
            self._isHistoryReceived = False
        if not self._isWebStateEnabled(eventSettings):
            self._isWebStateReceived = False
        self._gifter.updateSettings(eventSettings)
        self._keeper.updateSettings(eventSettings)
        self._messenger.updateSettings(eventSettings)
        self._stamper.updateSettings(eventSettings)
        return
