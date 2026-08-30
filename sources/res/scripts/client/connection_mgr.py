from __future__ import absolute_import
import hashlib, json, ResMgr, BigWorld, constants, pwd_token
from Event import Event, SafeEvent, EventManager
from PlayerEvents import g_playerEvents
from debug_utils import LOG_DEBUG, LOG_NOTE, LOG_WARNING
from shared_utils import nextTick
from predefined_hosts import g_preDefinedHosts, AUTO_LOGIN_QUERY_URL
from helpers import getClientLanguage, uniprof
from account_shared import isValidClientVersion
from skeletons.connection_mgr import IConnectionManager
_MIN_RECONNECTION_TIMEOUT = 5
_RECONNECTION_TIMEOUT_INCREMENT = 5
_MAX_RECONNECTION_TIMEOUT = 20

class CONNECTION_METHOD(object):
    BASIC = b'basic'
    TOKEN = b'token'
    TOKEN2 = b'token2'


class LOGIN_STATUS(object):
    NOT_SET = b'NOT_SET'
    LOGGED_ON = b'LOGGED_ON'
    LOGGED_ON_OFFLINE = b'LOGGED_ON_OFFLINE'
    CONNECTION_FAILED = b'CONNECTION_FAILED'
    DNS_LOOKUP_FAILED = b'DNS_LOOKUP_FAILED'
    UNKNOWN_ERROR = b'UNKNOWN_ERROR'
    CANCELLED = b'CANCELLED'
    ALREADY_ONLINE_LOCALLY = b'ALREADY_ONLINE_LOCALLY'
    LOGIN_REJECTED_BAN = b'LOGIN_REJECTED_BAN'
    LOGIN_REJECTED_NO_SUCH_USER = b'LOGIN_REJECTED_NO_SUCH_USER'
    LOGIN_REJECTED_INVALID_PASSWORD = b'LOGIN_REJECTED_INVALID_PASSWORD'
    SESSION_END = b'SESSION_END'
    LOGIN_REJECTED_ALREADY_LOGGED_IN = b'LOGIN_REJECTED_ALREADY_LOGGED_IN'
    LOGIN_REJECTED_BAD_DIGEST = b'LOGIN_REJECTED_BAD_DIGEST'
    LOGIN_REJECTED_DB_GENERAL_FAILURE = b'LOGIN_REJECTED_DB_GENERAL_FAILURE'
    LOGIN_REJECTED_DB_NOT_READY = b'LOGIN_REJECTED_DB_NOT_READY'
    LOGIN_REJECTED_ILLEGAL_CHARACTERS = b'LOGIN_REJECTED_ILLEGAL_CHARACTERS'
    LOGIN_CUSTOM_DEFINED_ERROR = b'LOGIN_CUSTOM_DEFINED_ERROR'
    LOGIN_BAD_PROTOCOL_VERSION = b'LOGIN_BAD_PROTOCOL_VERSION'
    LOGIN_REJECTED_SERVER_NOT_READY = b'LOGIN_REJECTED_SERVER_NOT_READY'
    LOGIN_REJECTED_RATE_LIMITED = b'LOGIN_REJECTED_RATE_LIMITED'


INVALID_TOKEN2_EXPIRED = (b'Token2 expires time', b'Invalid token2')

class ConnectionData(object):

    def __init__(self):
        self.username = None
        self.password = None
        self.inactivityTimeout = None
        self.publicKeyPath = None
        self.clientContext = None
        self.peripheryRoutingGroup = None
        return


class ConnectionManager(IConnectionManager):

    def __init__(self):
        self.__connectionData = ConnectionData()
        self.__connectionUrl = None
        self.__connectionMethod = CONNECTION_METHOD.BASIC
        self.__connectionStatus = LOGIN_STATUS.NOT_SET
        self.__lastLoginName = None
        self.__hostItem = g_preDefinedHosts._makeHostItem(b'', b'', b'')
        self.__availableHosts = None
        self.__lastSessionID = b''
        self.__retryConnectionPeriod = _MIN_RECONNECTION_TIMEOUT
        self.__retryConnectionCallbackID = None
        self.__connectionInProgress = False
        g_playerEvents.onKickWhileLoginReceived += self.__processKick
        g_playerEvents.onLoginQueueNumberReceived += self.__processQueue
        g_playerEvents.onPeripheryRoutingGroupReceived += self.setPeripheryRoutingGroup
        self.__eManager = EventManager()
        self.onLoggedOn = SafeEvent(self.__eManager)
        self.onConnected = SafeEvent(self.__eManager)
        self.onRejected = Event(self.__eManager)
        self.onDisconnected = Event(self.__eManager)
        self.onKickedFromServer = Event(self.__eManager)
        self.onKickWhileLoginReceived = Event(self.__eManager)
        self.onQueued = SafeEvent(self.__eManager)
        self.onPeripheryRoutingGroupUpdated = Event(self.__eManager)
        return

    def fini(self):
        g_playerEvents.onPeripheryRoutingGroupReceived -= self.setPeripheryRoutingGroup
        g_playerEvents.onKickWhileLoginReceived -= self.__processKick
        g_playerEvents.onLoginQueueNumberReceived -= self.__processQueue
        self.__eManager.clear()
        self.stopRetryConnection()
        return

    def initiateConnection(self, params, password, serverName):
        self.__setConnectionData(params, password)
        if serverName == AUTO_LOGIN_QUERY_URL:
            g_preDefinedHosts.autoLoginQuery(self.__setHostDataAndConnect)
        else:
            self.__setHostDataAndConnect(g_preDefinedHosts.byUrl(serverName))
        return

    def stopRetryConnection(self):
        if self.__retryConnectionCallbackID is not None:
            BigWorld.cancelCallback(self.__retryConnectionCallbackID)
            self.__retryConnectionPeriod = 0
            self.__retryConnectionCallbackID = None
        return

    @uniprof.regionDecorator(label=b'offline.connect', scope=b'enter')
    def __connect(self):
        self.__retryConnectionCallbackID = None
        if constants.IS_DEVELOPMENT:
            LOG_DEBUG((b'Calling BigWorld.connect with params: {0}, serverName: {1}, inactivityTimeout: {2}, publicKeyPath: {3}').format(self.__connectionData.username, self.__connectionUrl, constants.CLIENT_INACTIVITY_TIMEOUT, self.__connectionData.publicKeyPath))
        if self.__connectionInProgress:
            LOG_WARNING(b'Try to call BigWorld.connect while connection in progress')
            return
        else:
            nextTick(self.__tryConnect)()
            if g_preDefinedHosts.predefined(self.__connectionUrl) or g_preDefinedHosts.roaming(self.__connectionUrl):
                self.__hostItem = g_preDefinedHosts.byUrl(self.__connectionUrl)
            else:
                for server in BigWorld.serverDiscovery.servers:
                    if server.serverString == self.__connectionUrl:
                        self.__hostItem = self.__hostItem._replace(name=server.ownerName, shortName=server.ownerName)
                        break
                else:
                    self.__hostItem = self.__hostItem._replace(name=self.__connectionUrl, shortName=self.__connectionUrl)

            return

    def __tryConnect(self):
        if self.__connectionInProgress:
            LOG_WARNING(b'Try to call BigWorld.connect while connection in progress, but on nextTick')
            return
        self.__connectionInProgress = True
        BigWorld.connect(self.__connectionUrl, self.__connectionData, self.__serverResponseHandler)
        return

    @uniprof.regionDecorator(label=b'offline.connect', scope=b'exit')
    def __serverResponseHandler(self, stage, status, responseDataJSON):
        if constants.IS_DEVELOPMENT:
            LOG_DEBUG((b'Received server response with stage: {0}, status: {1}, responseData: {2}').format(stage, status, responseDataJSON))
        status = str(status)
        self.__connectionInProgress = False
        self.__connectionStatus = status
        try:
            responseData = json.loads(responseDataJSON)
        except ValueError:
            responseData = {b'errorMessage': responseDataJSON}

        if status == LOGIN_STATUS.LOGGED_ON:
            if stage == 1:
                if self.__connectionMethod == CONNECTION_METHOD.TOKEN and b'token2' in responseData:
                    self.__swtichToToken2(responseData[b'token2'])
                self.__lastSessionID = responseData.get(b'session_id', b'')
                self.onLoggedOn(responseData)
                self.onConnected()
        elif self.__retryConnectionCallbackID is None:
            status_ = self.__connectionStatus
            errorMsg = responseData.get(b'errorMessage', b'')
            if errorMsg in INVALID_TOKEN2_EXPIRED:
                status_ = LOGIN_STATUS.SESSION_END
            self.onRejected(status_, responseData)
        if status == LOGIN_STATUS.LOGIN_REJECTED_RATE_LIMITED:
            self.__reconnect()
        if stage == 6:
            self.onDisconnected()
            g_playerEvents.onDisconnected()
        return

    def __setConnectionData(self, params, password):
        self.__connectionMethod = params[b'auth_method']
        if b'auth_realm' not in params:
            params[b'auth_realm'] = constants.AUTH_REALM
        m = hashlib.md5()
        m.update(params[b'session'])
        params[b'session'] = m.hexdigest()
        if constants.IS_IGR_ENABLED:
            params[b'is_igr'] = b'1'
        username_ = json.dumps(params, encoding=b'utf-8')
        LOG_NOTE((b'User authentication method: {0}').format(params[b'auth_method']))
        if b'token2' in params and params[b'token2']:
            password = b''
        else:
            password = pwd_token.generate(password)
        if b'allowed_peripheries' in params:
            g_preDefinedHosts.setAvailablePeripheriesByRoutingGroup([int(x) for x in params[b'allowed_peripheries'].split() if x.isdigit()])
        else:
            LOG_NOTE(b'Not found allowed_peripheries in params: ', params)
        self.__connectionData.username = username_
        self.__connectionData.password = password
        self.__connectionData.inactivityTimeout = constants.CLIENT_INACTIVITY_TIMEOUT
        self.__connectionData.clientContext = json.dumps({b'lang_id': (getClientLanguage()), 
           b'publication': (params.get(b'publication'))})
        if constants.IS_DEVELOPMENT and params[b'auth_method'] == CONNECTION_METHOD.BASIC and params[b'login'][0] == b'@':
            try:
                self.__connectionData.username = params[b'login'][1:]
            except IndexError:
                self.__connectionData.username = params[b'login']

        return

    def __swtichToToken2(self, token2):
        self.__connectionMethod = CONNECTION_METHOD.TOKEN2
        params = json.loads(self.__connectionData.username, encoding=b'utf-8')
        params.pop(b'token', None)
        params[b'token2'] = token2
        params[b'auth_method'] = CONNECTION_METHOD.TOKEN2
        self.__connectionData.username = json.dumps(params, encoding=b'utf-8')
        return

    def __setHostData(self, predefinedHost):
        self.__connectionData.publicKeyPath = predefinedHost.keyPath
        self.__connectionUrl = predefinedHost.urlToken if (self.__connectionMethod == CONNECTION_METHOD.TOKEN or self.__connectionMethod == CONNECTION_METHOD.TOKEN2) and predefinedHost.urlToken else predefinedHost.url
        return

    def __setHostDataAndConnect(self, predefinedHost):
        self.__setHostData(predefinedHost)
        self.__connect()
        return

    def __reconnect(self):
        self.stopRetryConnection()
        self.__retryConnectionCallbackID = BigWorld.callback(self.__getRetryConnectionPeriod(), self.__connect)
        return

    def __getRetryConnectionPeriod(self):
        if self.__retryConnectionPeriod != _MAX_RECONNECTION_TIMEOUT:
            self.__retryConnectionPeriod += _RECONNECTION_TIMEOUT_INCREMENT
        return self.__retryConnectionPeriod

    def __processKick(self, peripheryID):
        if peripheryID > 0:
            host = g_preDefinedHosts.periphery(peripheryID, False)
            if host is not None:
                self.__setHostData(host)
            self.__reconnect()
        self.onKickWhileLoginReceived(peripheryID)
        return

    def __processQueue(self, queueNumber):
        self.onQueued(queueNumber)
        return

    @property
    def serverUserName(self):
        return self.__hostItem.name

    @property
    def serverUserNameShort(self):
        return self.__hostItem.shortName

    @property
    def peripheryID(self):
        return self.__hostItem.peripheryID

    @property
    def areaID(self):
        if not self.isDisconnected():
            return self.__hostItem.areaID
        else:
            return

    @property
    def url(self):
        return self.__hostItem.url

    @property
    def loginName(self):
        if not self.isDisconnected():
            return self.__lastLoginName
        else:
            return

    @property
    def lastLoginName(self):
        return self.__lastLoginName

    @property
    def lastSessionID(self):
        return self.__lastSessionID

    @property
    def databaseID(self):
        if not self.isDisconnected():
            return BigWorld.player().databaseID
        else:
            return

    @property
    def connectionMethod(self):
        return self.__connectionMethod

    @property
    def peripheryRoutingGroup(self):
        return self.__connectionData.peripheryRoutingGroup

    @property
    def availableHosts(self):
        if self.peripheryRoutingGroup is not None and self.__availableHosts is not None:
            return [p for p in g_preDefinedHosts.peripheries() if p.peripheryID in self.__availableHosts]
        else:
            return g_preDefinedHosts.hosts()

    def isAvailablePeriphery(self, peripheryID=None):
        if self.__connectionData.peripheryRoutingGroup is None or self.__availableHosts is None:
            return True
        if peripheryID is None:
            peripheryID = self.peripheryID
        return peripheryID in self.__availableHosts

    def disconnect(self):
        BigWorld.disconnect()
        return

    def setKickedFromServer(self, reason, kickReasonType, expiryTime):
        self.disconnect()
        self.onKickedFromServer(reason, kickReasonType, expiryTime)
        return

    def isDisconnected(self):
        return self.__connectionStatus != LOGIN_STATUS.LOGGED_ON

    def isStandalone(self):
        return self.peripheryID == constants.STANDALONE_CLUSTER_ID

    def isConnected(self):
        return self.__connectionStatus == LOGIN_STATUS.LOGGED_ON

    def checkClientServerVersions(self, clientVersion, serverVersion):
        if not isValidClientVersion(clientVersion, serverVersion) or ResMgr.activeContentType() in (constants.CONTENT_TYPE.INCOMPLETE,
         constants.CONTENT_TYPE.TUTORIAL):
            LOG_DEBUG(b'Version mismatch. Client is "%s", server needs "%s".' % (
             clientVersion, serverVersion))
            self.onRejected(LOGIN_STATUS.LOGIN_BAD_PROTOCOL_VERSION, {})
            BigWorld.disconnect()
        return

    def setLastLogin(self, email):
        self.__lastLoginName = email
        return

    def setPeripheryRoutingGroup(self, routingGroup, availableHosts):
        self.__connectionData.peripheryRoutingGroup = routingGroup
        self.__availableHosts = availableHosts
        g_preDefinedHosts.setAvailablePeripheriesByRoutingGroup(availableHosts)
        self.onPeripheryRoutingGroupUpdated()
        return
