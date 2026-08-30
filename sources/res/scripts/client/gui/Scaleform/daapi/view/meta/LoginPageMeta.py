from gui.Scaleform.framework.entities.View import View

class LoginPageMeta(View):

    def onLogin(self, user, password, host, isSocial):
        self._printOverrideError(b'onLogin')
        return

    def onRegister(self, host):
        self._printOverrideError(b'onRegister')
        return

    def onRecovery(self):
        self._printOverrideError(b'onRecovery')
        return

    def onTextLinkClick(self, linkId):
        self._printOverrideError(b'onTextLinkClick')
        return

    def onLoginBySocial(self, socialId, host):
        self._printOverrideError(b'onLoginBySocial')
        return

    def onSetRememberPassword(self, remember):
        self._printOverrideError(b'onSetRememberPassword')
        return

    def onLoginNameUpdated(self):
        self._printOverrideError(b'onLoginNameUpdated')
        return

    def isToken(self):
        self._printOverrideError(b'isToken')
        return

    def resetToken(self):
        self._printOverrideError(b'resetToken')
        return

    def onEscape(self):
        self._printOverrideError(b'onEscape')
        return

    def isCSISUpdateOnRequest(self):
        self._printOverrideError(b'isCSISUpdateOnRequest')
        return

    def startListenCsisUpdate(self, startListenCsis):
        self._printOverrideError(b'startListenCsisUpdate')
        return

    def showLegal(self):
        self._printOverrideError(b'showLegal')
        return

    def changeAccount(self):
        self._printOverrideError(b'changeAccount')
        return

    def as_setDefaultValuesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultValues(data)
        return

    def as_setErrorMessageS(self, msg, errorCode):
        if self._isDAAPIInited():
            return self.flashObject.as_setErrorMessage(msg, errorCode)
        return

    def as_setVersionS(self, version):
        if self._isDAAPIInited():
            return self.flashObject.as_setVersion(version)
        return

    def as_setCopyrightS(self, copyrightVal, legalInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setCopyright(copyrightVal, legalInfo)
        return

    def as_setLoginWarningS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setLoginWarning(value)
        return

    def as_setLoginWarningHideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setLoginWarningHide()
        return

    def as_setCapsLockStateS(self, isActive):
        if self._isDAAPIInited():
            return self.flashObject.as_setCapsLockState(isActive)
        return

    def as_setKeyboardLangS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setKeyboardLang(value)
        return

    def as_doAutoLoginS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_doAutoLogin()
        return

    def as_enableS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_enable(enabled)
        return

    def as_switchToAutoAndSubmitS(self, key):
        if self._isDAAPIInited():
            return self.flashObject.as_switchToAutoAndSubmit(key)
        return

    def as_showSimpleFormS(self, isShow, socialList, showRegisterLink):
        if self._isDAAPIInited():
            return self.flashObject.as_showSimpleForm(isShow, socialList, showRegisterLink)
        return

    def as_showFilledLoginFormS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilledLoginForm(data)
        return

    def as_showSteamLoginFormS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showSteamLoginForm(data)
        return

    def as_resetPasswordS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetPassword()
        return

    def as_getServersDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getServersDP()
        return

    def as_setSelectedServerIndexS(self, serverIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedServerIndex(serverIndex)
        return

    def as_showHealthNoticeS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showHealthNotice(text)
        return
