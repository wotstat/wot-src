from __future__ import absolute_import
import time, account_helpers
from MemoryCriticalController import g_critMemHandler
from PlayerEvents import g_playerEvents
from debug_utils import LOG_DEBUG, LOG_ERROR
from gui import GUI_SETTINGS
from gui.SystemMessages import SM_TYPE
from gui.Scaleform.daapi.view.dialogs.SystemMessageMeta import SESSION_CONTROL_TYPE, SessionControlAuxData
from helpers import i18n, dependency
from messenger.m_constants import PROTO_TYPE
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
from messenger.proto import proto_getter
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.game_control import IEventsNotificationsController, IAOGASController, IGameSessionController
from skeletons.gui.shared import IItemsCache
from skeletons.gui.system_messages import ISystemMessages
from helpers import getClientLanguage
KOREA_TIME_TILL_MIDNIGHT = 7200

class SystemMessagesInterface(ISystemMessages):
    __CMD_BLOCK_PREFIX = b'cmd_'
    __PROMO_BLOCK_PREFIX = b'promo_'
    itemsCache = dependency.descriptor(IItemsCache)
    aogas = dependency.descriptor(IAOGASController)
    gameSession = dependency.descriptor(IGameSessionController)
    eventsNotification = dependency.descriptor(IEventsNotificationsController)
    connectionMgr = dependency.descriptor(IConnectionManager)

    def init(self):
        self.connectionMgr.onConnected += self.__onConnected
        self.__expirationShown = False
        g_playerEvents.onAccountShowGUI += self.__onAccountShowGUI
        g_playerEvents.onAvatarBecomePlayer += self.__onAvatarBecomePlayer
        self.aogas.onNotifyAccount += self.__AOGAS_onNotifyAccount
        self.gameSession.onClientNotify += self.__gameSession_onClientNotify
        self.eventsNotification.onEventNotificationsChanged += self.__onReceiveEventNotification
        return

    def destroy(self):
        self.connectionMgr.onConnected -= self.__onConnected
        g_playerEvents.onAccountShowGUI -= self.__onAccountShowGUI
        g_playerEvents.onAvatarBecomePlayer -= self.__onAvatarBecomePlayer
        self.aogas.onNotifyAccount -= self.__AOGAS_onNotifyAccount
        self.gameSession.onClientNotify -= self.__gameSession_onClientNotify
        self.eventsNotification.onEventNotificationsChanged -= self.__onReceiveEventNotification
        self.__clearLobbyListeners()
        return

    @proto_getter(PROTO_TYPE.BW)
    def proto(self):
        return

    def pushMessage(self, text, type, priority=None, messageData=None, savedData=None):
        if GUI_SETTINGS.isGuiEnabled():
            self.proto.serviceChannel.pushClientSysMessage(text, type, priority=priority, messageData=messageData, savedData=savedData)
        else:
            LOG_DEBUG(b'[SYSTEM MESSAGE]', text, type)
        return

    def pushI18nMessage(self, key, *args, **kwargs):
        text = i18n.makeString(key, *args, **kwargs)
        msgType = kwargs.get(b'type', SM_TYPE.Information)
        msgPriority = kwargs.get(b'priority')
        messageData = kwargs.get(b'messageData')
        self.pushMessage(text, msgType, msgPriority, messageData)
        return

    def __onAccountShowGUI(self, ctx):
        self.__checkPremiumAccountExpiry()
        for message in g_critMemHandler.messages:
            self.__onMemoryCritical(message)

        onMemCrit = getattr(g_critMemHandler, b'onMemCrit', None)
        if onMemCrit is not None:
            onMemCrit += self.__onMemoryCritical
        else:
            LOG_ERROR(b'MemoryCriticalController.onMemCrit is not defined')
        return

    def __onAvatarBecomePlayer(self):
        self.__clearLobbyListeners()
        return

    def __clearLobbyListeners(self):
        onMemCrit = getattr(g_critMemHandler, b'onMemCrit', None)
        if onMemCrit is not None:
            onMemCrit -= self.__onMemoryCritical
        return

    def __onConnected(self):
        self.pushI18nMessage(b'#system_messages:connected', self.connectionMgr.serverUserName, type=SM_TYPE.GameGreeting)
        return

    def __checkPremiumAccountExpiry(self, ctx=None):
        expiryUTCTime = self.itemsCache.items.stats.activePremiumExpiryTime
        delta = account_helpers.getPremiumExpiryDelta(expiryUTCTime)
        if delta.days == 0 and expiryUTCTime and not self.__expirationShown:
            self.proto.serviceChannel.pushClientMessage(expiryUTCTime, SCH_CLIENT_MSG_TYPE.PREMIUM_ACCOUNT_EXPIRY_MSG)
            self.__expirationShown = True
        return

    def __onMemoryCritical(self, message):
        msgType, key = message
        self.pushI18nMessage(b'#system_messages:memory_critical/%s' % key, type=SM_TYPE.Error if msgType == 1 else SM_TYPE.Warning)
        return

    def __AOGAS_onNotifyAccount(self, message):
        self.proto.serviceChannel.pushClientMessage(message, SCH_CLIENT_MSG_TYPE.AOGAS_NOTIFY_TYPE, isAlert=True, auxData=SessionControlAuxData(SESSION_CONTROL_TYPE.AOGAS, message.timeout))
        return

    def __gameSession_onClientNotify(self, sessionDuration, timeTillMidnight, playTimeLeft):
        LOG_DEBUG(b'onGameSessionNotification', sessionDuration, timeTillMidnight, playTimeLeft)
        if getClientLanguage() == b'ko':
            key = b'#system_messages:gameSessionControl/korea/{0:>s}'
            msgList = [
             i18n.makeString(key.format(b'sessionTime'), sessionTime=time.strftime(b'%H:%M', time.gmtime(sessionDuration))),
             i18n.makeString(key.format(b'note'))]
            self.proto.serviceChannel.pushClientMessage((b'\n').join(msgList), SCH_CLIENT_MSG_TYPE.KOREA_PARENTAL_CONTROL_TYPE, auxData=SessionControlAuxData(SESSION_CONTROL_TYPE.KOREA_PARENTAL_CONTROL, timeoutMS=0))
        return

    def __onReceiveEventNotification(self, added, removed):
        self.__processNotifications(added, b'Begin')
        self.__processNotifications(removed, b'End')
        return

    def __processNotifications(self, notifications, state):
        for notification in notifications:
            msgType = notification.eventType
            text = notification.text
            if msgType is not None and not msgType.startswith(self.__CMD_BLOCK_PREFIX) and not msgType.startswith(self.__PROMO_BLOCK_PREFIX) and text:
                message = {b'data': text, b'type': msgType, b'state': state}
                self.proto.serviceChannel.pushClientMessage(message, SCH_CLIENT_MSG_TYPE.ACTION_NOTIFY_TYPE)

        return
