from enum import Enum
from account_helpers import AccountSettings
from account_helpers.AccountSettings import BLUEPRINTS_CONVERT_SALE_STARTED_SEEN
from helpers import dependency, isPlayerAccount
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
from skeletons.gui.game_control import IBlueprintsConvertSaleController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.system_messages import ISystemMessages
_ACTION_POSTFIX = b'_BCS'

class BCSActionState(Enum):
    STARTED = b'begin'
    PAUSED = b'pause'
    RESTORE = b'restore'
    END = b'end'


class BlueprintsConvertSaleController(IBlueprintsConvertSaleController):
    __slots__ = (b'_isEnabled',)
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _systemMessages = dependency.descriptor(ISystemMessages)
    _eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self):
        super(BlueprintsConvertSaleController, self).__init__()
        self._isEnabled = False
        self._isStarted = False
        return

    def onLobbyStarted(self, event):
        if not isPlayerAccount():
            return
        self._isEnabled = int(self._lobbyContext.getServerSettings().getBlueprintsConvertSaleConfig().isEnabled())
        self.__updateActionState()
        self._lobbyContext.getServerSettings().onServerSettingsChange += self.__onSettingsChanged
        self._eventsCache.onSyncCompleted += self.__onEventsCacheSyncCompleted
        return

    def fini(self):
        self.__stop()
        super(BlueprintsConvertSaleController, self).fini()
        return

    def onDisconnected(self):
        self.__stop()
        super(BlueprintsConvertSaleController, self).onDisconnected()
        return

    def onAvatarBecomePlayer(self):
        self.__stop()
        super(BlueprintsConvertSaleController, self).onAvatarBecomePlayer()
        return

    def __stop(self):
        self._lobbyContext.getServerSettings().onServerSettingsChange -= self.__onSettingsChanged
        return

    def __onSettingsChanged(self, diff):
        if b'blueprints_convert_sale_config' in diff:
            newState = int(self._lobbyContext.getServerSettings().getBlueprintsConvertSaleConfig().isEnabled())
            if self._isEnabled != newState and self._isStarted:
                state = BCSActionState.PAUSED if newState == 0 else BCSActionState.RESTORE
                self.__showNotification(state)
                self._isEnabled = newState
        return

    def __onEventsCacheSyncCompleted(self, *_):
        self.__updateActionState()
        return

    def __updateActionState(self):
        actions = self._eventsCache.getActions().keys()
        for name in actions:
            if _ACTION_POSTFIX in name:
                self._isStarted = True
                if not AccountSettings.getNotifications(BLUEPRINTS_CONVERT_SALE_STARTED_SEEN) and self._isEnabled:
                    AccountSettings.setNotifications(BLUEPRINTS_CONVERT_SALE_STARTED_SEEN, True)
                    self.__showNotification(BCSActionState.STARTED)
                return

        if self._isStarted:
            self._isStarted = False
            self.__showNotification(BCSActionState.END)
        return

    def __showNotification(self, state):
        self._systemMessages.proto.serviceChannel.pushClientMessage({b'data': b'', b'type': b'', b'state': state}, SCH_CLIENT_MSG_TYPE.BLUEPRINTS_CONVERT_SALE)
        return
