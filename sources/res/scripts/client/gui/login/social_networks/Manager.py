import BigWorld
from gui import GUI_SETTINGS
from connection_mgr import CONNECTION_METHOD
from gui.login.Manager import Manager as CredentialsLoginManager
from WebBridge import WebBridge

class SOCIAL_NETWORKS(object):
    FACEBOOK = b'facebook'
    GOOGLE = b'google'
    WGNI = b'wgni'
    VKONTAKTE = b'vkontakte'
    YAHOO = b'yahoo'
    NAVER = b'naver'
    TWITTER = b'twitter'
    ODNOKLASSNIKI = b'odnoklassniki'


class Manager(CredentialsLoginManager):

    def __init__(self):
        CredentialsLoginManager.__init__(self)
        self.__webBridge = None
        return

    def init(self):
        CredentialsLoginManager.init(self)
        self.__webBridge = WebBridge(self._preferences)
        return

    def fini(self):
        CredentialsLoginManager.fini(self)
        self.__webBridge.fini()
        self.__webBridge = None
        return

    def initiateSocialLogin(self, socialNetworkName, serverName, rememberUser, isRegistration):
        authMethod = CONNECTION_METHOD.TOKEN
        serverName = self._getHost(authMethod, serverName)
        self._preferences[b'session'] = BigWorld.wg_cpsalt(self._preferences[b'session'])
        self._preferences[b'remember_user'] = rememberUser
        self._preferences[b'login_type'] = socialNetworkName
        self._preferences[b'server_name'] = serverName
        loginParams = {b'login': (self._preferences[b'login']), 
           b'session': (self._preferences[b'session']), 
           b'temporary': (str(int(not rememberUser))), 
           b'auth_method': authMethod, 
           b'requested_for': b'wot', 
           b'ip': b'127.0.0.1'}
        return self.__webBridge.initiateLogin(loginParams, socialNetworkName != SOCIAL_NETWORKS.WGNI, isRegistration)

    @staticmethod
    def getAvailableSocialNetworks():
        socialNetworks = []
        if GUI_SETTINGS.socialNetworkLogin[SOCIAL_NETWORKS.VKONTAKTE]:
            socialNetworks.append(SOCIAL_NETWORKS.VKONTAKTE)
        if GUI_SETTINGS.socialNetworkLogin[SOCIAL_NETWORKS.FACEBOOK]:
            socialNetworks.append(SOCIAL_NETWORKS.FACEBOOK)
        if GUI_SETTINGS.socialNetworkLogin[SOCIAL_NETWORKS.GOOGLE]:
            socialNetworks.append(SOCIAL_NETWORKS.GOOGLE)
        if GUI_SETTINGS.socialNetworkLogin[SOCIAL_NETWORKS.WGNI]:
            socialNetworks.append(SOCIAL_NETWORKS.WGNI)
        if GUI_SETTINGS.socialNetworkLogin[SOCIAL_NETWORKS.YAHOO]:
            socialNetworks.append(SOCIAL_NETWORKS.YAHOO)
        if GUI_SETTINGS.socialNetworkLogin[SOCIAL_NETWORKS.NAVER]:
            socialNetworks.append(SOCIAL_NETWORKS.NAVER)
        return socialNetworks
