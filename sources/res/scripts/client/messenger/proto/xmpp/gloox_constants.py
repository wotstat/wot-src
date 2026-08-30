import BigWorld
_XmppClient = BigWorld.XmppClient

class PRESENCE(object):
    UNKNOWN = _XmppClient.PRESENCE_UNKNOWN
    AVAILABLE = _XmppClient.PRESENCE_AVAILABLE
    CHAT = _XmppClient.PRESENCE_CHAT
    AWAY = _XmppClient.PRESENCE_AWAY
    DND = _XmppClient.PRESENCE_DND
    XA = _XmppClient.PRESENCE_XA
    UNAVAILABLE = _XmppClient.PRESENCE_UNAVAILABLE
    OFFLINE = (
     UNKNOWN, UNAVAILABLE)
    RANGE = (
     UNKNOWN, AVAILABLE, CHAT, AWAY, DND, XA, UNAVAILABLE)


PRESENCES_ORDER = (
 PRESENCE.AVAILABLE, PRESENCE.CHAT, PRESENCE.AWAY, PRESENCE.DND, PRESENCE.XA,
 PRESENCE.UNAVAILABLE, PRESENCE.UNKNOWN)
PRESENCES_NAMES = dict([(v, k) for k, v in PRESENCE.__dict__.iteritems() if v in PRESENCE.RANGE])

class SUBSCRIPTION(object):
    OFF = _XmppClient.SUBSCRIPTION_OFF
    ON = _XmppClient.SUBSCRIPTION_ON
    PENDING = _XmppClient.SUBSCRIPTION_PENDING


SUBSCRIPTION_NAMES = dict([(v, k) for k, v in SUBSCRIPTION.__dict__.iteritems() if not k.startswith(b'_')])

class CONNECTION_STATE(object):
    DISCONNECTED = _XmppClient.STATE_DISCONNECTED
    CONNECTING = _XmppClient.STATE_CONNECTING
    AUTHENTICATING = _XmppClient.STATE_AUTHENTICATING
    INITIALIZING = _XmppClient.STATE_INITIALIZING
    CONNECTED = _XmppClient.STATE_CONNECTED


class DISCONNECT_REASON(object):
    BY_REQUEST = _XmppClient.DISCONNECT_BY_REQUEST
    AUTHENTICATION = _XmppClient.DISCONNECT_AUTHENTICATION
    OTHER_ERROR = _XmppClient.DISCONNECT_OTHER_ERROR


class LOG_LEVEL(object):
    DEBUG = _XmppClient.LOG_LEVEL_DEBUG
    WARNING = _XmppClient.LOG_LEVEL_WARNING
    ERROR = _XmppClient.LOG_LEVEL_ERROR


class LOG_SOURCE(object):
    UNKNOWN = b'Unknown source'
    PARSER = b'Parser'
    CLIENT = b'Client'
    CLIENT_BASE = b'Clientbase'
    COMPONENT = b'Component'
    DND = b'Dns'
    USER = b'User'
    CONNECTION_TCP_BASE = b'ConnectionTCPBase'
    CONNECTION_HTTP_PROXY = b'ConnectionHTTPProxy'
    CONNECTION_S5_PROXY = b'ConnectionSOCKS5Proxy'
    CONNECTION_TCP_CLIENT = b'ConnectionTCPClient'
    CONNECTION_TCP_SERVER = b'ConnectionTCPServer'
    CONNECTION_BOSH = b'ConnectionBOSH'
    CONNECTION_TLS = b'ConnectionTLS'
    S5B_MANAGER = b'S5BManager'
    S5_BYTES_STREAM = b'SOCKS5Bytestream'
    XML_INCOMING = b'XmlIncoming'
    XML_OUTGOING = b'XmlOutgoing'
    XML_STREAM = (
     XML_INCOMING, XML_OUTGOING)


class IQ_TYPE(object):
    GET = _XmppClient.IQ_TYPE_GET
    SET = _XmppClient.IQ_TYPE_SET
    RESULT = _XmppClient.IQ_TYPE_RESULT
    ERROR = _XmppClient.IQ_TYPE_ERROR
    INVALID = _XmppClient.IQ_TYPE_INVALID


class MESSAGE_TYPE(object):
    CHAT = 1
    ERROR = 2
    GROUPCHAT = 4
    HEADLINE = 8
    NORMAL = 16
    INVALID = 32
    RANGE = (
     CHAT, ERROR, GROUPCHAT, HEADLINE, NORMAL, INVALID)


class MESSAGE_TYPE_ATTR(object):
    CHAT = b'chat'
    GROUPCHAT = b'groupchat'
    NORMAL = b'normal'
    ERROR = b'error'


MESSAGE_TYPE_TO_ATTR = {(MESSAGE_TYPE.CHAT): (MESSAGE_TYPE_ATTR.CHAT), 
   (MESSAGE_TYPE.GROUPCHAT): (MESSAGE_TYPE_ATTR.GROUPCHAT), 
   (MESSAGE_TYPE.NORMAL): (MESSAGE_TYPE_ATTR.NORMAL)}

class ERROR_TYPE(object):
    MODIFY = b'modify'
    CANCEL = b'cancel'
    AUTH = b'auth'
    WAIT = b'wait'


class CONNECTION_IMPL_TYPE(object):
    TCP = 1
    BOSH = 2


class ROSTER_CONTEXT(object):
    REQUEST_ROSTER = 0
    PUSH_ROSTER_ITEM = 1
    REMOVE_ROSTER_ITEM = 2


class GLOOX_EVENT(object):
    CONNECTED, LOGIN, DISCONNECTED, ROSTER_RESULT, ROSTER_ITEM_SET, ROSTER_ITEM_REMOVED, PRESENCE, SUBSCRIPTION_REQUEST, LOG, IQ, ROSTER_QUERY, MESSAGE, PRESENCE_ERROR, MESSAGE_ERROR = ALL = range(0, 14)


GLOOX_EVENTS_NAMES = dict([(v, k) for k, v in GLOOX_EVENT.__dict__.iteritems() if v in GLOOX_EVENT.ALL])
INBOUND_SUB_BATCH_SIZE = 100
INBOUND_SUB_INTERVAL = 2

class CHAT_STATE(object):
    UNDEFINED = b''
    ACTIVE = b'active'
    INACTIVE = b'inactive'
    GONE = b'gone'
    COMPOSING = b'composing'
    PAUSED = b'paused'
    RANGE = (
     ACTIVE, INACTIVE, GONE, COMPOSING, PAUSED)
