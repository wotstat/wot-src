import typing
from gui.gift_system.constants import GiftMessageType
from gui.gift_system.hubs.subsystems import BaseMessegesDelayer
from gui.gift_system.wrappers import ifMessagesEnabled, ifMessagesAllowed
if typing.TYPE_CHECKING:
    from helpers.server_settings import GiftEventConfig
    from gui.gift_system.wrappers import GiftsHistoryData, IncomeSysMessage, SendGiftResponse

class IGiftEventMessenger(BaseMessegesDelayer):

    def isMessagesEnabled(self):
        raise NotImplementedError
        return

    def isMessagesSuspended(self, *args, **kwargs):
        raise NotImplementedError
        return

    def setMessagesAllowed(self, isMessagesAllowed):
        raise NotImplementedError
        return

    def pushHistoryMessage(self, history):
        raise NotImplementedError
        return

    def pushIncomeMessage(self, incomeData):
        raise NotImplementedError
        return

    def pushOutcomeMessage(self, outcomeData):
        raise NotImplementedError
        return


class GiftEventBaseMessenger(IGiftEventMessenger):
    __slots__ = (b'__isMessagesAllowed',)

    def __init__(self, eventSettings, isMessagesAllowed):
        super(GiftEventBaseMessenger, self).__init__(eventSettings)
        self._msgHandlers.update({(GiftMessageType.HISTORY): (self._pushHistoryMessage), 
           (GiftMessageType.INCOME): (self._pushIncomeMessage), 
           (GiftMessageType.OUTCOME): (self._pushOutcomeMessage)})
        self.__isMessagesAllowed = isMessagesAllowed
        return

    def isMessagesEnabled(self):
        return not self._settings.isDisabled

    def isMessagesSuspended(self, *args, **kwargs):
        return not self.__isMessagesAllowed

    def setMessagesAllowed(self, isMessagesAllowed):
        self.__isMessagesAllowed = isMessagesAllowed
        if not self.isMessagesSuspended():
            self._processMessagesQueue()
        return

    @ifMessagesEnabled
    @ifMessagesAllowed(GiftMessageType.HISTORY)
    def pushHistoryMessage(self, history):
        self._pushHistoryMessage(history)
        return

    @ifMessagesEnabled
    @ifMessagesAllowed(GiftMessageType.INCOME)
    def pushIncomeMessage(self, incomeData):
        self._pushIncomeMessage(incomeData)
        return

    @ifMessagesEnabled
    @ifMessagesAllowed(GiftMessageType.OUTCOME)
    def pushOutcomeMessage(self, outcomeData):
        self._pushOutcomeMessage(outcomeData)
        return

    def updateSettings(self, eventSettings):
        super(GiftEventBaseMessenger, self).updateSettings(eventSettings)
        if not self.isMessagesEnabled():
            self._clearMessagesQueue()
        return

    def _pushHistoryMessage(self, history):
        return

    def _pushIncomeMessage(self, incomeData):
        return

    def _pushOutcomeMessage(self, outcomeData):
        return
