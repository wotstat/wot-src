import weakref
from helpers import dependency
from skeletons.gui.login_manager import ILoginManager

class INVALID_FIELDS(object):
    ALL_VALID = 0
    LOGIN_INVALID = 1
    PWD_INVALID = 2
    SERVER_INVALID = 4
    LOGIN_PWD_INVALID = LOGIN_INVALID | PWD_INVALID


class BaseMode(object):
    _loginManager = dependency.descriptor(ILoginManager)

    def __init__(self, view, fallbackMode=None):
        self._view = weakref.proxy(view)
        self._fallbackMode = fallbackMode
        return

    def onPopulate(self):
        return

    def destroy(self):
        self._view = None
        self._fallbackMode = None
        return

    @property
    def login(self):
        raise NotImplementedError
        return

    def doLogin(self, *args):
        raise NotImplementedError
        return

    def updateForm(self):
        raise NotImplementedError
        return

    @property
    def rememberUser(self):
        return False

    @property
    def password(self):
        return b''

    @property
    def rememberPassVisible(self):
        return False

    @property
    def showRememberServerWarning(self):
        return False

    def setRememberPassword(self, *args):
        return

    def isToken2(self):
        return False

    def resetToken(self):
        return

    def doSocialLogin(self, *args):
        return

    def changeAccount(self):
        return

    def skipRejectionError(self, *args):
        return False
