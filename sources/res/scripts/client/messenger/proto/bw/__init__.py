from chat_shared import CHAT_RESPONSES
from debug_utils import LOG_ERROR, LOG_DEBUG
from messenger import g_settings
from messenger.m_constants import PROTO_TYPE
from messenger.proto.bw import errors
from messenger.proto.bw.ChannelsManager import ChannelsManager
from messenger.proto.bw.ChatActionsListener import ChatActionsListener
from messenger.proto.bw.ClanListener import ClanListener
from messenger.proto.bw.ServiceChannelManager import ServiceChannelManager
from messenger.proto.bw.UsersManager import UsersManager
from messenger.proto.events import g_messengerEvents
from messenger.proto.interfaces import IProtoPlugin

class BWProtoPlugin(ChatActionsListener, IProtoPlugin):
    __slots__ = (b'__isConnected', b'channels', b'users', b'clanListener', b'serviceChannel')

    def __init__(self):
        super(BWProtoPlugin, self).__init__()
        self.__isConnected = False
        self.channels = ChannelsManager()
        self.users = UsersManager()
        self.clanListener = None
        self.serviceChannel = ServiceChannelManager()
        return

    def isConnected(self):
        return self.__isConnected

    def clear(self):
        self.__isConnected = False
        self._removeChatActionsListeners()
        self.channels.clear()
        self.users.clear()
        self.serviceChannel.clear()
        if self.clanListener is not None:
            self.clanListener.stop()
        return

    def connect(self, scope):
        if not self.__isConnected:
            self.__isConnected = True
            self._addChatActionsListeners()
            self.clanListener = self.__getClanListener()
            if self.clanListener is not None:
                self.clanListener.start()
            self.__isConnected = True
            g_messengerEvents.onPluginConnected(PROTO_TYPE.BW)
        self.channels.switch(scope)
        self.users.switch(scope)
        self.serviceChannel.switch(scope)
        return

    def disconnect(self):
        self.serviceChannel.clear()
        if self.__isConnected:
            self.clear()
            g_messengerEvents.onPluginDisconnected(PROTO_TYPE.BW)
        return

    def view(self, scope):
        self.users.view(scope)
        return

    def setFilters(self, msgFilterChain):
        self.channels.setFiltersChain(msgFilterChain)
        return

    def onChatActionFailure(self, chatAction):
        actionResponse = CHAT_RESPONSES[chatAction[b'actionResponse']]
        LOG_DEBUG(b'onChatActionFailure', dict(chatAction))
        for name in (b'channels', b'users'):
            manager = getattr(self, name)
            if manager.handleChatActionFailureEvent(actionResponse, dict(chatAction)):
                return

        responseProcessor = self.__errorsHandlers.get(actionResponse, self.__defaultErrorHandler)
        if hasattr(self, responseProcessor):
            getattr(self, responseProcessor)(chatAction)
        else:
            LOG_ERROR(b'onChatActionFailure: response processor for response %s(%s) not registered' % (
             actionResponse, actionResponse.index()))
        return

    def _addChatActionsListeners(self):
        self.channels.addListeners()
        self.users.addListeners()
        self.serviceChannel.addListeners()
        return

    def _removeChatActionsListeners(self):
        self.removeAllListeners()
        self.channels.removeAllListeners()
        self.users.removeAllListeners()
        self.serviceChannel.removeAllListeners()
        return

    @classmethod
    def __getClanListener(cls):
        if g_settings.server.isXmppClansEnabled():
            return None
        else:
            return ClanListener()

    __errorsHandlers = {(CHAT_RESPONSES.channelNotExists): b'_BWProtoPlugin__onChannelNotExists', 
       (CHAT_RESPONSES.memberBanned): b'_BWProtoPlugin__onMemberBanned', 
       (CHAT_RESPONSES.chatBanned): b'_BWProtoPlugin__onChatBanned', 
       (CHAT_RESPONSES.actionInCooldown): b'_BWProtoPlugin__passError', 
       (CHAT_RESPONSES.commandInCooldown): b'_BWProtoPlugin__onCommandInCooldown', 
       (CHAT_RESPONSES.inviteCommandError): b'_BWProtoPlugin__passError', 
       (CHAT_RESPONSES.inviteCreateError): b'_BWProtoPlugin__passError', 
       (CHAT_RESPONSES.inviteCreationNotAllowed): b'_BWProtoPlugin__passError'}
    __defaultErrorHandler = b'_BWProtoPlugin__onActionFailure'

    def __onMemberBanned(self, chatAction):
        error = errors.MemberBannedError.create(chatAction)
        if error:
            g_messengerEvents.onErrorReceived(error)
        return

    def __onChatBanned(self, chatAction):
        error = errors.ChatBannedError.create(chatAction)
        if error:
            g_messengerEvents.onErrorReceived(error)
        return

    def __onCommandInCooldown(self, chatAction):
        error = errors.CommandInCooldownError.create(chatAction)
        if error:
            g_messengerEvents.onErrorReceived(error)
        return

    def __onActionFailure(self, chatAction):
        error = errors.ChatActionError.create(chatAction)
        if error:
            g_messengerEvents.onErrorReceived(error)
        return

    def __passError(self, chatAction):
        return
