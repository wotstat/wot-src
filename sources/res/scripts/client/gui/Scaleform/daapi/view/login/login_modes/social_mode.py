from base_mode import BaseMode, INVALID_FIELDS
from connection_mgr import LOGIN_STATUS
from constants import IS_CHINA
from gui import makeHtmlString
from gui.Scaleform.Waiting import Waiting
from gui.login.social_networks import SOCIAL_NETWORKS
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.connection_mgr import IConnectionManager
SOCIAL_NETWORK_TO_DOMAIN_MAPPING = {(SOCIAL_NETWORKS.FACEBOOK): b'https://fb.com', 
   (SOCIAL_NETWORKS.GOOGLE): b'https://plus.google.com', 
   (SOCIAL_NETWORKS.WGNI): b'https://lesta.ru', 
   (SOCIAL_NETWORKS.VKONTAKTE): b'https://vk.com', 
   (SOCIAL_NETWORKS.YAHOO): b'https://yahoo.com', 
   (SOCIAL_NETWORKS.NAVER): b'http://naver.com', 
   (SOCIAL_NETWORKS.TWITTER): b'https://twitter.com', 
   (SOCIAL_NETWORKS.ODNOKLASSNIKI): b'https://ok.ru'}

class SocialMode(BaseMode):
    _connectionMgr = dependency.descriptor(IConnectionManager)

    @property
    def login(self):
        return self._fallbackMode.login

    @property
    def rememberUser(self):
        return self._fallbackMode.rememberUser

    @property
    def password(self):
        return self._fallbackMode.password

    @property
    def rememberPassVisible(self):
        return self._fallbackMode.rememberPassVisible

    def onPopulate(self):
        self._connectionMgr.onRejected += self.__onLoginRejected
        self._fallbackMode.onPopulate()
        return

    def destroy(self):
        self._connectionMgr.onRejected -= self.__onLoginRejected
        self._fallbackMode.destroy()
        super(SocialMode, self).destroy()
        return

    def isToken2(self):
        return self._fallbackMode.isToken2()

    def resetToken(self):
        self._fallbackMode.resetToken()
        return

    def setRememberPassword(self, *args):
        self._fallbackMode.setRememberPassword(*args)
        return

    def doLogin(self, *args):
        self._fallbackMode.doLogin(*args)
        return

    def doSocialLogin(self, socialNetworkName, serverName, isRegistration):
        if self._loginManager.initiateSocialLogin(socialNetworkName, serverName, self.rememberUser, isRegistration=isRegistration):
            initLoginError = b''
        else:
            initLoginError = _ms(b'#menu:login/social/status/SYSTEM_ERROR')
        self._view.as_setErrorMessageS(initLoginError, INVALID_FIELDS.ALL_VALID)
        return

    def updateForm(self):
        socialList = self._loginManager.getAvailableSocialNetworks()
        lastLoginType = self._loginManager.getPreference(b'login_type')
        if lastLoginType in socialList and self.rememberUser:
            self._view.as_showFilledLoginFormS({b'haveToken': (self.isToken2()), b'userName': (self._loginManager.getPreference(b'name')), 
               b'icoPath': (makeHtmlString(b'html_templates:socialNetworkLogin', b'transparentLogo', {b'socialNetwork': lastLoginType})), 
               b'socialId': lastLoginType})
        else:
            self._view.as_showSimpleFormS(True, self.__setSocialDataList(socialList), not IS_CHINA)
        return

    def changeAccount(self):
        logOutAccount = self._loginManager.getPreference(b'login_type')
        self._loginManager.clearPreferences()
        self._loginManager.writePreferences()
        self._view.as_setErrorMessageS(self.__getLogoutWarning(logOutAccount), INVALID_FIELDS.ALL_VALID)
        self._view.update()
        return

    def __onLoginRejected(self, loginStatus, _):
        socialList = self._loginManager.getAvailableSocialNetworks()
        lastLoginType = self._loginManager.getPreference(b'login_type')
        if lastLoginType in socialList and (loginStatus == LOGIN_STATUS.SESSION_END or loginStatus == LOGIN_STATUS.LOGIN_REJECTED_INVALID_PASSWORD):
            Waiting.hide(b'login')
            self._loginManager.clearToken2Preference()
            self._view.update()
            self._view.as_setErrorMessageS(_ms(b'#menu:login/status/SOCIAL_SESSION_END'), INVALID_FIELDS.PWD_INVALID)
        return

    def __setSocialDataList(self, socialList):
        socialDataList = []
        for socialId in socialList:
            socialDataList.append({b'socialId': socialId, 
               b'tpHeader': (self.__getTooltipHeader(socialId)), 
               b'tpBody': (self.__getTooltipBody(socialId))})

        return socialDataList

    def __getLogoutWarning(self, socialNetworkName):
        localizationString = b'#menu:login/social/warning/SOCIAL_NETWORK_LOGOUT'
        formatter = {b'userName': (self._loginManager.getPreference(b'name')), 
           b'socialNetworkLink': (makeHtmlString(b'html_templates:socialNetworkLogin', b'socialNetworkLink', {b'socialNetworkName': socialNetworkName, 
                                  b'socialNetworkOfficialName': (_ms(b'#tooltips:login/social/' + socialNetworkName))}))}
        if socialNetworkName != SOCIAL_NETWORKS.WGNI:
            localizationString += b'_BOTH'
            formatter[b'lestaGamesLink'] = makeHtmlString(b'html_templates:socialNetworkLogin', b'socialNetworkLink', {b'socialNetworkName': (SOCIAL_NETWORKS.WGNI), 
               b'socialNetworkOfficialName': (_ms(b'#tooltips:login/social/' + SOCIAL_NETWORKS.WGNI))})
        return makeHtmlString(b'html_templates:socialNetworkLogin', b'logoutWarning', {b'warningMessage': (_ms(localizationString) % formatter)})

    @staticmethod
    def __getTooltipHeader(socialNetworkName):
        if socialNetworkName == SOCIAL_NETWORKS.WGNI:
            return _ms(b'#tooltips:login/bySocial/' + SOCIAL_NETWORKS.WGNI + b'/header')
        return _ms(b'#tooltips:login/bySocial/header')

    @staticmethod
    def __getTooltipBody(socialNetworkName):
        if socialNetworkName == SOCIAL_NETWORKS.WGNI:
            return _ms(b'#tooltips:login/bySocial/' + SOCIAL_NETWORKS.WGNI + b'/body')
        return _ms(b'#tooltips:login/bySocial/body') % {b'social': (_ms(b'#tooltips:login/social/' + socialNetworkName))}
