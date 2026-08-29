from collections import defaultdict
import weakref, BigWorld
from debug_utils import LOG_CURRENT_EXCEPTION
from external_strings_utils import unicode_from_utf8
from messenger.proto.xmpp.extensions.custom_items import makeExtInfoFromPresence
from messenger.proto.xmpp.gloox_constants import PRESENCE, CONNECTION_STATE, DISCONNECT_REASON, GLOOX_EVENT, INBOUND_SUB_BATCH_SIZE, INBOUND_SUB_INTERVAL
from messenger.proto.xmpp.jid import ContactBareJID, JID
from messenger.proto.xmpp.log_output import CLIENT_LOG_AREA, g_logOutput
from messenger.proto.xmpp.resources import Resource
from messenger.proto.xmpp.wrappers import makeClanInfo, makeMucInfo
_GLOOX_EVENTS_LISTENERS = (
 (
  b'onConnect', b'onConnected'),
 (
  b'onReady', b'onLogin'),
 (
  b'onDisconnect', b'onDisconnected'),
 (
  b'onRosterResultReceived', b'onRosterResultReceived'),
 (
  b'onNewRosterItem', b'onRosterItemSet'),
 (
  b'onRosterItemRemove', b'onRosterItemRemoved'),
 (
  b'onSubscribe', b'onSubscriptionRequest'),
 (
  b'onLog', b'onLog'),
 (
  b'onHandleIq', b'onHandleIq'),
 (
  b'onRosterQuerySend', b'onRosterQuerySend'),
 (
  b'onHandleMsg', b'onHandleMsg'),
 (
  b'onHandleMsgError', b'onHandleMsgError'),
 (
  b'onHandlePresence', b'onHandlePresence'),
 (
  b'onHandlePresenceError', b'onHandlePresenceError'))

class ClientDecorator(object):

    def __init__(self):
        super(ClientDecorator, self).__init__()
        self.__client = BigWorld.XmppClient()
        self.__handlers = defaultdict(set)
        self.__address = None
        self.__inboundSubs = []
        self.__subsCallbackID = None
        return

    def init(self):
        client = self.__client
        ClientHolder._clearClient()
        for handlerName, listenerName in _GLOOX_EVENTS_LISTENERS:
            if not hasattr(client, handlerName):
                g_logOutput.error(CLIENT_LOG_AREA.PY_WRAPPER, b'Handler no is found', handlerName)
                continue
            listener = getattr(self, listenerName, None)
            if listener is None or not callable(listener):
                g_logOutput.error(CLIENT_LOG_AREA.PY_WRAPPER, b'Listener no is found', listenerName)
                continue
            if not getattr(client, handlerName):
                setattr(client, handlerName, listener)

        ClientEventsHandler._setClient(self)
        return

    def fini(self):
        self.__cancelInboundSubsCallback()
        client = self.__client
        for handlerName, _ in _GLOOX_EVENTS_LISTENERS:
            if not hasattr(client, handlerName):
                g_logOutput.error(CLIENT_LOG_AREA.PY_WRAPPER, b'Handler no is found', handlerName)
                continue
            setattr(client, handlerName, None)

        self.__handlers.clear()
        g_logOutput.clear()
        ClientHolder._clearClient()
        return

    def connect(self, jid, host=b'', port=-1):
        self.__address = (jid, host, port)
        self.__client.connect(jid, host, port)
        return

    def connectBosh(self, jid, host=b'', port=-1, url=b''):
        self.__address = (jid, host, port)
        self.__client.connectBosh(jid, host, port, url)
        return

    def login(self, password):
        self.__client.login(password)
        return

    def disconnect(self):
        self.__client.disconnect()
        return

    def getConnectionState(self):
        return self.__client.connectionState

    def getConnectionAddress(self):
        return self.__address

    def isConnected(self):
        return self.__client.connectionState == CONNECTION_STATE.CONNECTED

    def isDisconnected(self):
        return self.__client.connectionState == CONNECTION_STATE.DISCONNECTED

    def isConnecting(self):
        state = self.__client.connectionState
        return state in [
         CONNECTION_STATE.CONNECTING, CONNECTION_STATE.AUTHENTICATING,
         CONNECTION_STATE.INITIALIZING]

    def getClientPresence(self):
        return self.__client.presence

    def setClientPresence(self, presence):
        if presence not in PRESENCE.RANGE:
            g_logOutput.error(CLIENT_LOG_AREA.PY_WRAPPER, b'Value of presence is invalid', presence)
            return
        self.__client.presence = presence
        return

    def sendPresence(self, query):
        self.__client.sendCustomPresence(query.getType(), str(query.getTo()), query.getTag(), query.getStatus())
        return

    def sendMUCPresence(self, query, password=b''):
        self.__client.sendMUCPresence(query.getType(), str(query.getTo()), password)
        return

    def sendIQ(self, query):
        return self.__client.sendCustomQuery(query.getType(), query.getTag(), str(query.getTo()))

    def sendMessage(self, message):
        self.__client.sendCustomMessage(message.getType(), str(message.getTo()), message.getBody(), message.getTag())
        return

    def setContactToRoster(self, jid, name=b'', groups=None):
        if groups is None:
            groups = set()
        self.__client.add(str(jid), name, groups)
        return

    def removeContactFromRoster(self, jid):
        self.__client.remove(str(jid))
        return

    def askSubscription(self, jid, message=b''):
        self.__client.subscribe(str(jid), message)
        return

    def removeSubscribeTo(self, jid):
        self.__client.unsubscribe(str(jid))
        return

    def approveSubscription(self, jid, message=b''):
        self.__client.setSubscribed(str(jid), message)
        return

    def cancelSubscription(self, jid, message=b''):
        self.__client.setUnsubscribed(str(jid), message)
        return

    def registerHandler(self, event, handler):
        if event in GLOOX_EVENT.ALL:
            handlers = self.__handlers[event]
            if handler in handlers:
                g_logOutput.warning(CLIENT_LOG_AREA.PY_WRAPPER, b'handler already exists', event, handler)
            elif not hasattr(handler, b'__self__') or not isinstance(handler.__self__, ClientEventsHandler):
                g_logOutput.error(CLIENT_LOG_AREA.PY_WRAPPER, b'Class of handler is not subclass of ClientEventsHandler', handler)
                return
            if callable(handler):
                handlers.add(handler)
            else:
                g_logOutput.error(CLIENT_LOG_AREA.PY_WRAPPER, b'Handler is invalid', handler)
        else:
            g_logOutput.error(CLIENT_LOG_AREA.PY_WRAPPER, b'Event is not found', event)
        return

    def unregisterHandler(self, event, handler):
        if event in GLOOX_EVENT.ALL:
            handlers = self.__handlers[event]
            if handler in handlers:
                handlers.remove(handler)
        else:
            g_logOutput.error(CLIENT_LOG_AREA.PY_WRAPPER, b'Event is not found', event)
        return

    def onConnected(self):
        self.__handleEvent(GLOOX_EVENT.CONNECTED)
        return

    def onLogin(self):
        self.__handleEvent(GLOOX_EVENT.LOGIN)
        return

    def onDisconnected(self, reason=DISCONNECT_REASON.BY_REQUEST, description=None):
        if reason != DISCONNECT_REASON.BY_REQUEST:
            self.__address = None
        self.__cancelInboundSubsCallback()
        self.__handleEvent(GLOOX_EVENT.DISCONNECTED, reason, description)
        return

    def onRosterResultReceived(self, roster):

        def generator():
            for jid, name, groups, to, from_, clanInfo in roster:
                yield (
                 ContactBareJID(jid), name, groups, (to, from_),
                 makeClanInfo(*clanInfo))

            return

        self.__handleEvent(GLOOX_EVENT.ROSTER_RESULT, generator)
        return

    def onRosterItemSet(self, jid, name, groups, to, from_, clanInfo):
        self.__handleEvent(GLOOX_EVENT.ROSTER_ITEM_SET, ContactBareJID(jid), name, groups, (
         to, from_), makeClanInfo(*clanInfo))
        return

    def onRosterItemRemoved(self, jid):
        remainingInboundSubs = [sub for sub in self.__inboundSubs if sub[0] != jid]
        if len(remainingInboundSubs) != len(self.__inboundSubs):
            self.__inboundSubs = remainingInboundSubs
            self.__cancelInboundSubsCallback()
        self.__handleEvent(GLOOX_EVENT.ROSTER_ITEM_REMOVED, ContactBareJID(jid))
        return

    def onHandlePresence(self, jid, priority, status, presence, exts, mucInfo):
        self.__handleEvent(GLOOX_EVENT.PRESENCE, JID(jid), Resource(priority, status, presence, makeExtInfoFromPresence(exts), makeMucInfo(mucInfo)))
        return

    def onHandlePresenceError(self, jid, pyGlooxTag):
        self.__handleEvent(GLOOX_EVENT.PRESENCE_ERROR, JID(jid), pyGlooxTag)
        return

    def onSubscriptionRequest(self, jid, message, nickname, exts):
        self.__cancelInboundSubsCallback()
        self.__inboundSubs.append((
         ContactBareJID(jid), nickname, message, makeExtInfoFromPresence(exts)))
        if len(self.__inboundSubs) >= INBOUND_SUB_BATCH_SIZE:
            self.__fireInboundSubsEvent()
        else:
            self.__subsCallbackID = BigWorld.callback(INBOUND_SUB_INTERVAL, self.__invokeInboundSubsCallback)
        return

    def onLog(self, level, source, message):
        self.__handleEvent(GLOOX_EVENT.LOG, level, source, message)
        return

    def onHandleMsg(self, msgID, msgType, body, jidFrom, pyGlooxTag):
        try:
            body, _ = unicode_from_utf8(body)
        except (UnicodeDecodeError, TypeError, ValueError):
            LOG_CURRENT_EXCEPTION()

        self.__handleEvent(GLOOX_EVENT.MESSAGE, msgID, msgType, body, ContactBareJID(jidFrom), pyGlooxTag)
        return

    def onHandleMsgError(self, msgID, msgType, jidFrom, pyGlooxTag):
        self.__handleEvent(GLOOX_EVENT.MESSAGE_ERROR, msgID, msgType, ContactBareJID(jidFrom), pyGlooxTag)
        return

    def onHandleIq(self, iqID, iqType, pyGlooxTag):
        self.__handleEvent(GLOOX_EVENT.IQ, iqID, iqType, pyGlooxTag)
        return

    def onRosterQuerySend(self, iqID, jid, context):
        self.__handleEvent(GLOOX_EVENT.ROSTER_QUERY, iqID, ContactBareJID(jid), context)
        return

    def __handleEvent(self, eventName, *args, **kwargs):
        handlers = self.__handlers[eventName]
        for handler in handlers:
            try:
                handler(*args, **kwargs)
            except TypeError:
                g_logOutput.error(CLIENT_LOG_AREA.PY_WRAPPER, b' Handler is invoked with error', handler)
                LOG_CURRENT_EXCEPTION()

        return

    def __fireInboundSubsEvent(self):
        self.__handleEvent(GLOOX_EVENT.SUBSCRIPTION_REQUEST, self.__inboundSubs)
        self.__inboundSubs = []
        return

    def __cancelInboundSubsCallback(self):
        if self.__subsCallbackID is not None:
            BigWorld.cancelCallback(self.__subsCallbackID)
            self.__subsCallbackID = None
        return

    def __invokeInboundSubsCallback(self):
        self.__subsCallbackID = None
        self.__fireInboundSubsEvent()
        return


class ClientHolder(object):
    __slots__ = (b'_client',)
    _client = None

    @classmethod
    def _setClient(cls, client):
        ClientEventsHandler._client = weakref.proxy(client)
        return

    @classmethod
    def _clearClient(cls):
        cls._client = lambda *args: None
        return

    def client(self):
        return ClientEventsHandler._client


class ClientEventsHandler(ClientHolder):

    def clear(self):
        return

    def registerHandlers(self):
        raise NotImplementedError
        return

    def unregisterHandlers(self):
        raise NotImplementedError
        return
