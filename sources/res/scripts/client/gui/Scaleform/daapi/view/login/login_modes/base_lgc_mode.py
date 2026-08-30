import LGC
from account_helpers.settings_core.settings_constants import GAME
from base_mode import BaseMode
_g_firstEntry = True

class BaseLgcMode(BaseMode):

    @property
    def login(self):
        return LGC.getUserName()

    @property
    def showRememberServerWarning(self):
        return not self._loginManager.settingsCore.getSetting(GAME.LOGIN_SERVER_SELECTION) and self._loginManager.getPreference(b'server_select_was_set')

    def onPopulate(self):
        global _g_firstEntry
        if self._loginManager.lgcAvailable:
            self._loginManager.addOnLgcErrorListener(self._onLgcError)
        autoLogin = _g_firstEntry and not self._loginManager.settingsCore.getSetting(GAME.LOGIN_SERVER_SELECTION) and not self._loginManager.getPreference(b'server_select_was_set')
        if autoLogin:
            self._loginManager.tryLgcLogin()
        _g_firstEntry = False
        return

    def doLogin(self, userName, password, serverName, isSocialToken2Login):
        self._loginManager.tryLgcLogin(serverName)
        return

    def skipRejectionError(self, loginStatus):
        return self._loginManager.checkLgcCouldRetry(loginStatus)

    def updateForm(self):
        return

    def destroy(self):
        if self._loginManager.lgcAvailable:
            self._loginManager.removeOnLgcErrorListener(self._onLgcError)
        super(BaseLgcMode, self).destroy()
        return

    def _onLgcError(self):
        return
