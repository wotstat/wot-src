import typing
if typing.TYPE_CHECKING:
    from gui.gift_system.constants import GiftMessageType
    from helpers.server_settings import GiftEventConfig

class BaseHubSubsystem(object):
    __slots__ = (b'_settings',)

    def __init__(self, eventSettings):
        super(BaseHubSubsystem, self).__init__()
        self._settings = eventSettings
        return

    def destroy(self):
        return

    def reset(self):
        return

    def updateSettings(self, eventSettings):
        self._settings = eventSettings
        return


class BaseMessegesDelayer(BaseHubSubsystem):
    __slots__ = (b'_msgQueue', b'_msgHandlers')

    def __init__(self, eventSettings):
        super(BaseMessegesDelayer, self).__init__(eventSettings)
        self._msgHandlers = {}
        self._msgQueue = []
        return

    def destroy(self):
        self._clearMessagesQueue()
        self._msgHandlers.clear()
        super(BaseMessegesDelayer, self).destroy()
        return

    def isMessagesEnabled(self):
        raise NotImplementedError
        return

    def isMessagesSuspended(self, *args, **kwargs):
        raise NotImplementedError
        return

    def addToQueue(self, msgType, msgData):
        self._msgQueue.append((msgType, msgData))
        return

    def _clearMessagesQueue(self):
        del self._msgQueue[:]
        return

    def _processMessagesQueue(self):
        for msgType, msgData in ((mType, mData) for mType, mData in self._msgQueue if mType in self._msgHandlers):
            self._msgHandlers[msgType](msgData)

        self._clearMessagesQueue()
        return
