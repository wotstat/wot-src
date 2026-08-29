import copy, logging, typing
from gui import SystemMessages
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import MessengerEvent
from messenger.formatters.chat_message import LobbyMessageBuilder
from messenger.formatters.users_messages import getBroadcastIsInCoolDownMessage
from messenger.gui.interfaces import IChannelController
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.bw_chat2.wrappers import UnitMessageVO
from messenger_common_chat2 import MESSENGER_LIMITS
_logger = logging.getLogger(__name__)
if typing.TYPE_CHECKING:
    from messenger.proto.entities import ChannelEntity
    from typing import List, Union
    from messenger.gui.gameface.view.gf_channel_view_interface import GFChannelViewInterface

class GFChannelController(IChannelController):

    def __init__(self, channel):
        self.__channel = None
        self.__mBuilder = LobbyMessageBuilder()
        self._isNotifyInit = False
        self.__channel = channel
        self.__subscribedViews = list()
        self._addListeners()
        self.fireInitEvent()
        return

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def proto(self):
        return

    def deactivate(self, entryClosing=False):
        self._removeListeners()
        self.removeView()
        return

    def clear(self):
        self._removeListeners()
        self.removeView()
        return

    def removeView(self):
        self.__subscribedViews = list()
        return

    def fireInitEvent(self):
        if not self._isNotifyInit:
            self._fireInitEvent()
            self._isNotifyInit = True
        return

    def setHistory(self, history):
        if self.__channel:
            self.__channel.clearHistory()
            for message in history:
                self.addMessage(message, isHistoryMessage=True)

        return

    def getHistory(self):
        if self.__channel is None:
            return []
        else:
            self._getChat().addHistory()
            history = self.__channel.getHistory()
            return history

    def canSendMessage(self):
        if self.__channel is None:
            return (False, b'')
        else:
            result, errorMsg = True, b''
            if self._getChat().isBroadcastInCooldown():
                result, errorMsg = False, getBroadcastIsInCoolDownMessage(MESSENGER_LIMITS.BROADCASTS_FROM_CLIENT_COOLDOWN_SEC)
            return (result, errorMsg)

    def getChannel(self):
        return self.__channel

    def getClientID(self):
        if self.__channel:
            return self.__channel.getClientID()
        else:
            return

    def sendMessage(self, message):
        result, errorMsg = self.canSendMessage()
        if result:
            self._broadcast(message)
        else:
            SystemMessages.pushI18nMessage(errorMsg, type=SystemMessages.SM_TYPE.Error)
        return result

    def sendCommand(self, command):
        self._getChat().send(command)
        return

    def addMessage(self, message, doFormatting=True, isHistoryMessage=False):
        if self.__channel:
            if isinstance(message, (str, unicode)):
                message = UnitMessageVO(0, -1, message, u'')
            if doFormatting:
                message = copy.copy(message)
                message.text = self.__formatText(message.text)
            self.__channel.addMessage(message)
            return self.__addMessageToView(message, isHistoryMessage)
        return False

    def addToSubscribedList(self, view):
        if view not in self.__subscribedViews:
            self.__subscribedViews.append(view)
            if self.__channel:
                view.onChannelControllerInited(self)
        return

    def removeFromSubscribedList(self, view):
        if view in self.__subscribedViews:
            self.__subscribedViews.remove(view)
        return

    def getSubscribedViews(self):
        return self.__subscribedViews

    def _addListeners(self):
        self.__channel.onConnectStateChanged += self._onConnectStateChanged
        return

    def _removeListeners(self):
        self.__channel.onConnectStateChanged -= self._onConnectStateChanged
        return

    def _onConnectStateChanged(self, channel):
        if channel == self.__channel:
            if channel.isJoined():
                self.fireInitEvent()
            else:
                self.removeView()
        return

    def _fireInitEvent(self):
        g_eventBus.handleEvent(MessengerEvent(MessengerEvent.PRB_CHANNEL_CTRL_INITED, {b'prbType': (self.__channel.getPrebattleType()), 
           b'controller': self}), scope=EVENT_BUS_SCOPE.LOBBY)
        self.__notifyViews()
        return

    def _getChat(self):
        return self.proto.unitChat

    def _broadcast(self, message):
        self._getChat().broadcast(message)
        return

    def __notifyViews(self):
        for view in self.__subscribedViews:
            view.onChannelControllerInited(self)

        return

    def __addMessageToView(self, message, isHistoryMessage=False):
        isShowing = False
        for view in self.__subscribedViews:
            isShowing |= view.addMessageToView(message, isHistoryMessage)

        return isShowing

    def __formatText(self, text):
        text = text.replace(b'&amp;', b'&')
        text = text.replace(b'&lt;', b'<')
        text = text.replace(b'&gt;', b'>')
        text = text.replace(b'&apos;', b"'")
        return text.replace(b'&quot;', b'"')
