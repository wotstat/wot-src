import pickle, time, typing, logging, BigWorld, LGC, Settings, constants
from account_helpers.settings_core.settings_constants import GAME
from connection_mgr import CONNECTION_METHOD
from Preferences import Preferences
from Servers import Servers, DevelopmentServers
from debug_utils import LOG_DEBUG
from gui import SystemMessages, makeHtmlString, GUI_SETTINGS
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from helpers import dependency
from helpers.i18n import makeString as _ms
from helpers.time_utils import ONE_MINUTE
from predefined_hosts import g_preDefinedHosts, AUTO_LOGIN_QUERY_ENABLED, AUTO_LOGIN_QUERY_URL
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.login_manager import ILoginManager
from soft_exception import SoftException
from gui.Scaleform.Waiting import Waiting
from Event import Event
from PlayerEvents import g_playerEvents
from connection_mgr import LOGIN_STATUS
_PERIPHERY_DEFAULT_LIFETIME = 15 * ONE_MINUTE
_LIMIT_LOGIN_COUNT = 5
_logger = logging.getLogger(__name__)

class Manager(ILoginManager):
    lobbyContext = dependency.descriptor(ILobbyContext)
    connectionMgr = dependency.descriptor(IConnectionManager)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        self._preferences = None
        self.__servers = None
        self.__lgcPublication = constants.LGC_PUBLICATION.LGC_UNKNOWN
        self.__lgcManager = None
        self.__triedToInitLGC = False
        self.onConnectionInitiated = Event()
        self.onConnectionRejected = Event()
        return

    @property
    def lgcAvailable(self):
        return self.__lgcManager is not None

    def getLgcPublication(self):
        return self.__lgcPublication

    @property
    def isLgcSteam(self):
        return self.__lgcPublication == constants.LGC_PUBLICATION.LGC_STEAM

    def init(self):
        if LGC.prepare():
            publication = LGC.getPublication()
            self.__lgcPublication = constants.LGC_PUBLICATION.LGC_BASE if constants.LGC_PUBLICATION.LGC_PC == publication else publication
        else:
            _logger.error(b'LGC API initialization failed')
        self.tryPrepareLGCLogin()
        self._preferences = Preferences()
        if constants.IS_DEVELOPMENT:
            self.__servers = DevelopmentServers(self._preferences)
        else:
            self.__servers = Servers(self._preferences)
        self.connectionMgr.onLoggedOn += self._onLoggedOn
        g_clientUpdateManager.addCallbacks({b'serverSettings.periphery_routing_config': (self.__onServerSettingsChanged)})
        return

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.connectionMgr.onLoggedOn -= self._onLoggedOn
        self.connectionMgr.onRejected -= self._onRejected
        self._preferences = None
        self.__servers.fini()
        self.__servers = None
        self.stopLgc()
        self.onConnectionInitiated.clear()
        self.onConnectionRejected.clear()
        return

    def initiateLogin(self, email, password, serverName, isSocialToken2Login, rememberUser):
        self.onConnectionInitiated()
        self.connectionMgr.onRejected += self._onRejected
        isToken2Login = isSocialToken2Login or self._preferences[b'token2']
        authMethod = CONNECTION_METHOD.TOKEN2 if isToken2Login else CONNECTION_METHOD.BASIC
        serverName = self._getHost(authMethod, serverName)
        self._preferences[b'session'] = BigWorld.cpsalt(self._preferences[b'session'])
        self._preferences[b'password_length'] = len(password)
        self._preferences[b'remember_user'] = rememberUser
        self._preferences[b'login'] = email
        self._preferences[b'server_name'] = serverName
        loginParams = {b'login': (self._preferences[b'login']), 
           b'session': (self._preferences[b'session']), 
           b'temporary': (str(int(not rememberUser))), 
           b'auth_method': authMethod, 
           b'publication': (str(self.__lgcPublication))}
        if isToken2Login:
            loginParams[b'token2'] = self._preferences[b'token2']
        if not isSocialToken2Login:
            self._preferences[b'login_type'] = b'credentials'
        self.connectionMgr.initiateConnection(loginParams, password, serverName)
        self.connectionMgr.setLastLogin(email)
        return

    def initiateRelogin(self, login, token2, serverName):
        self.onConnectionInitiated()
        self.connectionMgr.onRejected += self._onRejected
        self._preferences[b'server_name'] = serverName
        if self.lgcAvailable:
            self.__lgcManager.relogin(token2, serverName)
        else:
            loginParams = {b'login': login, 
               b'token2': token2, 
               b'session': (BigWorld.cpsalt(self._preferences[b'session'])), 
               b'temporary': (str(int(not self._preferences[b'remember_user']))), 
               b'auth_method': (CONNECTION_METHOD.TOKEN2)}
            self.connectionMgr.initiateConnection(loginParams, b'', serverName)
        return

    def getPreference(self, key):
        return self._preferences[key]

    def clearPreferences(self):
        self._preferences.clear()
        return

    def clearToken2Preference(self):
        self._preferences[b'token2'] = b''
        return

    def writePreferences(self):
        self._preferences.writeLoginInfo()
        return

    @property
    def servers(self):
        return self.__servers

    def _onLoggedOn(self, responseData):
        name = responseData.get(b'name', b'UNKNOWN')
        token2 = responseData.get(b'token2', b'')
        self.lobbyContext.setCredentials(name, token2)
        serverName = self._preferences[b'server_name']
        serverSelect = self.settingsCore.getSetting(GAME.LOGIN_SERVER_SELECTION)
        if self.lgcAvailable and self.__lgcManager.onLoggedOn(responseData):
            self._preferences.clear()
            self._preferences[b'server_name'] = serverName
            self._preferences[b'server_select_was_set'] = serverSelect
            self._preferences.writeLoginInfo()
            self.__lgcManager.onRejected -= self._onRejected
            self.__lgcManager.onInitiated -= self._onLGCInitiated
            return
        loginCount = self._preferences.get(b'loginCount', 0)
        self._preferences[b'loginCount'] = 1 if loginCount >= _LIMIT_LOGIN_COUNT else loginCount + 1
        if self._preferences[b'remember_user']:
            self._preferences[b'name'] = name
            self._preferences[b'token2'] = token2
        else:
            email = self._preferences[b'login']
            session = self._preferences[b'session']
            loginCount = self._preferences[b'loginCount']
            self._preferences.clear()
            if not constants.IS_SINGAPORE and not GUI_SETTINGS.igrCredentialsReset:
                self._preferences[b'login'] = email
            self._preferences[b'server_name'] = serverName
            self._preferences[b'session'] = session
            self._preferences[b'loginCount'] = loginCount
        self._preferences[b'server_select_was_set'] = serverSelect
        self._preferences.writeLoginInfo()
        self.__dumpUserName(name)
        self._showSecurityMessage(responseData)
        self.connectionMgr.onRejected -= self._onRejected
        return

    def _onLGCInitiated(self, *_):
        self.onConnectionInitiated()
        return

    def _onRejected(self, *_):
        self.onConnectionRejected()
        return

    def _showSecurityMessage(self, responseData):
        securityWarningType = responseData.get(b'security_msg')
        if securityWarningType is not None:
            securityLink = b''
            if not GUI_SETTINGS.isEmpty(b'securitySettingsURL'):
                securityLink = makeHtmlString(b'html_templates:lobby/system_messages', b'link', {b'text': (_ms(SYSTEM_MESSAGES.SECURITYMESSAGE_CHANGE_SETINGS)), 
                   b'linkType': b'securityLink'})
            SystemMessages.pushI18nMessage(b'#system_messages:securityMessage/%s' % securityWarningType, type=SystemMessages.SM_TYPE.Warning, link=securityLink)
        return

    def writePeripheryLifetime(self):
        if AUTO_LOGIN_QUERY_ENABLED and self.connectionMgr.peripheryID:
            self._preferences[b'peripheryLifetime'] = pickle.dumps((
             self.connectionMgr.peripheryID,
             time.time() + _PERIPHERY_DEFAULT_LIFETIME))
            self._preferences.writeLoginInfo()
        return

    @staticmethod
    def getAvailableSocialNetworks():
        raise SoftException(b'This method should not be reached in this context')
        return

    def initiateSocialLogin(self, socialNetworkName, serverName, rememberUser, isRegistration):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _getHost(self, authMethod, hostName):
        if hostName != AUTO_LOGIN_QUERY_URL:
            return hostName
        else:
            pickledData = self._preferences[b'peripheryLifetime']
            if pickledData:
                try:
                    peripheryID, expirationTimestamp = pickle.loads(pickledData)
                except Exception:
                    LOG_DEBUG((b"Couldn't to read pickled periphery data. Connecting to {0}.").format(hostName))
                    return hostName

                if expirationTimestamp > time.time():
                    host = g_preDefinedHosts.periphery(peripheryID, False)
                    if host is None:
                        return hostName
                    if authMethod != CONNECTION_METHOD.BASIC and host.urlToken:
                        return host.urlToken
                    return host.url
            return hostName

    def __dumpUserName(self, name):
        Settings.g_instance.userPrefs[Settings.KEY_LOGIN_INFO].writeString(b'user', name)
        Settings.g_instance.save()
        return

    def addOnLgcErrorListener(self, listener):
        if self.lgcAvailable:
            self.__lgcManager.onLgcError += listener
        else:
            _logger.warning(b'Try to addOnLgcErrorListener while LGC is not available')
        return

    def removeOnLgcErrorListener(self, listener):
        if self.lgcAvailable:
            self.__lgcManager.onLgcError -= listener
        else:
            _logger.warning(b'Try to removeOnLgcErrorListener while LGC is not available')
        return

    def tryLgcLogin(self, serverName=None):
        if not self.lgcAvailable:
            _logger.warning(b'LGC is not available, no possibility to login via it, so return')
            return
        else:
            if serverName is None:
                selectedServer = self.__servers.selectedServer
                if not selectedServer:
                    _logger.warning(b'No server was selected when LGC connect happened, so return')
                    return
                serverName = selectedServer[b'data']
            else:
                self._preferences[b'server_name'] = serverName
            self.__lgcManager.onRejected += self._onRejected
            self.__lgcManager.onInitiated += self._onLGCInitiated
            hostName = self._getHost(CONNECTION_METHOD.TOKEN, serverName)
            self.__lgcManager.login(hostName)
            return

    def stopLgc(self):
        if self.lgcAvailable:
            self.__lgcManager.onRejected -= self._onRejected
            self.__lgcManager.onInitiated -= self._onLGCInitiated
            self.__lgcManager.destroy()
            self.__lgcManager = None
        return

    def tryPrepareLGCLogin(self):
        if self.lgcAvailable:
            if not LGC.prepareLogin():
                self.stopLgc()
                LGC.printLastError()
        elif not self.__triedToInitLGC:
            if LGC.prepareLogin():
                self.__lgcManager = _LgcModeManager()
            else:
                LGC.printLastError()
        self.__triedToInitLGC = True
        return

    def checkLgcCouldRetry(self, status):
        if self.lgcAvailable:
            return self.__lgcManager.checkLgcCouldRetry(status)
        return False

    def __onServerSettingsChanged(self, diff):
        if b'isEnabled' in diff and not diff[b'isEnabled']:
            self.connectionMgr.setPeripheryRoutingGroup(None, None)
            return
        else:
            if b'peripheryRoutingGroups' in diff:
                self.connectionMgr.setPeripheryRoutingGroup(self.connectionMgr.peripheryRoutingGroup, diff[b'peripheryRoutingGroups'].get(self.connectionMgr.peripheryRoutingGroup))
            return


class _LgcModeManager(object):
    connectionMgr = dependency.descriptor(IConnectionManager)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        self.onLgcError = Event()
        self.__token2ToStore = None
        self.__selectedServer = None
        g_playerEvents.onAccountShowGUI += self.__onAccountDone
        self.connectionMgr.onRejected += self.__onRejected
        self.connectionMgr.onDisconnected += self.__onDisconnected
        self.onInitiated = Event()
        self.onRejected = Event()
        return

    def destroy(self):
        g_playerEvents.onAccountShowGUI -= self.__onAccountDone
        self.connectionMgr.onRejected -= self.__onRejected
        self.connectionMgr.onDisconnected -= self.__onDisconnected
        self.onRejected.clear()
        return

    def login(self, selectedServer):
        self.__selectedServer = selectedServer
        self.__lobbyContext.setAccountComplete(LGC.isAccountComplete())
        self.onInitiated()
        LGC.prepareToken()
        Waiting.show(b'login')
        self.__lgcCheck()
        return

    def relogin(self, token2, selectedServer):
        self.__selectedServer = selectedServer
        loginParams = LGC.loginData()
        loginParams[b'token2'] = token2
        loginParams[b'auth_method'] = CONNECTION_METHOD.TOKEN2
        loginParams[b'auth_realm'] = constants.AUTH_REALM
        self.connectionMgr.initiateConnection(loginParams, b'', selectedServer)
        return

    def checkLgcCouldRetry(self, status):
        return self.connectionMgr.connectionMethod == CONNECTION_METHOD.TOKEN2 and (status == LOGIN_STATUS.SESSION_END or status == LOGIN_STATUS.LOGIN_REJECTED_INVALID_PASSWORD)

    def onLoggedOn(self, responseData):
        self.__token2ToStore = responseData[b'token2']
        if LGC.processingState() == constants.LGC_STATE.LOGIN_IN_PROGRESS:
            LGC.onServerResponse(True)
            return True
        return False

    def __lgcCheck(self):
        state = LGC.processingState()
        if state == constants.LGC_STATE.WAITING_TOKEN_1:
            BigWorld.callback(0.0, self.__lgcCheck)
        elif state == constants.LGC_STATE.LOGIN_IN_PROGRESS:
            self.__lgcConnect()
        else:
            LGC.printLastError()
            Waiting.hide(b'login')
            self.onRejected()
            self.onLgcError()
        return

    def __lgcConnect(self):
        if self.__selectedServer is not None:
            state = LGC.processingState()
            if state == constants.LGC_STATE.LOGIN_IN_PROGRESS:
                loginParams = LGC.loginData()
                if loginParams is not None:
                    self.connectionMgr.initiateConnection(loginParams, b'', self.__selectedServer)
                    self.connectionMgr.setLastLogin(b'')
                    return
                _logger.warning(b'No login params for LGC login, so return')
            else:
                _logger.warning(b'Could not login via LGC because wrong processingState (%d), so return', state)
        else:
            _logger.warning(b'No server was selected when LGC connect happened, so return')
        Waiting.hide(b'login')
        self.onRejected()
        return

    def __onRejected(self, status, _):
        Waiting.hide(b'login')
        if self.checkLgcCouldRetry(status):
            LGC.onToken2Expired()
            self.login(self.__selectedServer)
        else:
            LGC.onServerResponse(False)
            self.onRejected()
        return

    def __onDisconnected(self):
        LGC.onServerResponse(False)
        return

    def __onAccountDone(self, *args):
        if self.__token2ToStore:
            if LGC.processingState() == constants.LGC_STATE.LOGGEDIN and LGC.getUserId() == BigWorld.player().databaseID:
                LGC.storeToken2(self.__token2ToStore, BigWorld.player().databaseID)
            self.__token2ToStore = None
        return
