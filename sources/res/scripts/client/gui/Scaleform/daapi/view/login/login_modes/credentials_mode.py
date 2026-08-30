from collections import namedtuple
import constants
from external_strings_utils import _LOGIN_NAME_MIN_LENGTH
from external_strings_utils import isAccountLoginValid
from gui import GUI_SETTINGS
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.locale.MENU import MENU
from gui.game_loading.loading_sounds import handleLoadingSoundChangeEvent, DEFAULT_LOADING_SOUND
from gui.impl import backport
from gui.impl.gen import R
from helpers.i18n import makeString as _ms
from base_mode import BaseMode, INVALID_FIELDS
_ValidateCredentialsResult = namedtuple(b'ValidateCredentialsResult', (b'isValid', b'errorMessage', b'invalidFields'))

class CredentialsMode(BaseMode):
    firstRun = True

    def __init__(self, *args):
        super(CredentialsMode, self).__init__(*args)
        self._rememberUser = self._loginManager.getPreference(b'remember_user')
        return

    @property
    def login(self):
        if GUI_SETTINGS.clearLoginValue:
            return b''
        return self._loginManager.getPreference(b'login')

    @property
    def rememberUser(self):
        return self._rememberUser

    @property
    def password(self):
        if self._rememberUser and not GUI_SETTINGS.clearLoginValue:
            return b'*' * self._loginManager.getPreference(b'password_length')
        return b''

    @property
    def rememberPassVisible(self):
        return GUI_SETTINGS.rememberPassVisible

    def onPopulate(self):
        if CredentialsMode.firstRun:
            CredentialsMode.firstRun = False
        else:
            handleLoadingSoundChangeEvent(DEFAULT_LOADING_SOUND)
        return

    def setRememberPassword(self, rememberUser):
        self._rememberUser = rememberUser
        return

    def isToken2(self):
        return bool(self._loginManager.getPreference(b'token2'))

    def resetToken(self):
        self._loginManager.clearToken2Preference()
        return

    def doLogin(self, userName, password, serverName, isSocialToken2Login):
        if Waiting.isVisible():
            return False
        result = self.__validateCredentials(userName.lower().strip(), password.strip(), self.isToken2())
        if result.isValid:
            if not Waiting.isOpened(b'login'):
                Waiting.show(b'login')
            self._loginManager.initiateLogin(userName, password, serverName, isSocialToken2Login, isSocialToken2Login or self._rememberUser)
        else:
            self._view.as_setErrorMessageS(result.errorMessage, result.invalidFields)
        return True

    def updateForm(self):
        self._view.as_showSimpleFormS(False, None, not constants.IS_CHINA)
        if constants.IS_CHINA:
            self._view.as_showHealthNoticeS(backport.text(R.strings.menu.login.healthNotice()))
        return

    @staticmethod
    def __validateCredentials(userName, password, isToken2Login):
        isValid = True
        errorMessage = None
        invalidFields = None
        if isToken2Login and GUI_SETTINGS.rememberPassVisible or constants.IS_DEVELOPMENT and userName:
            return _ValidateCredentialsResult(isValid, errorMessage, invalidFields)
        else:
            if len(userName) < _LOGIN_NAME_MIN_LENGTH:
                isValid = False
                errorMessage = _ms(MENU.LOGIN_STATUS_INVALID_LOGIN_LENGTH, count=_LOGIN_NAME_MIN_LENGTH)
                invalidFields = INVALID_FIELDS.LOGIN_INVALID
            elif not isAccountLoginValid(userName):
                isValid = False
                errorMessage = _ms(MENU.LOGIN_STATUS_INVALID_LOGIN)
                invalidFields = INVALID_FIELDS.LOGIN_INVALID
            return _ValidateCredentialsResult(isValid, errorMessage, invalidFields)
