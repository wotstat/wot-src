import typing
if typing.TYPE_CHECKING:
    from constants import LGC_PUBLICATION

class ILoginManager(object):
    onConnectionInitiated = None
    onConnectionRejected = None

    @property
    def servers(self):
        raise NotImplementedError
        return

    @property
    def lgcAvailable(self):
        raise NotImplementedError
        return

    def getLgcPublication(self):
        raise NotImplementedError
        return

    @property
    def isLgcSteam(self):
        raise NotImplementedError
        return

    def tryPrepareLGCLogin(self):
        raise NotImplementedError
        return

    def checkLgcCouldRetry(self, loginStatus):
        raise NotImplementedError
        return

    def addOnLgcErrorListener(self, listener):
        raise NotImplementedError
        return

    def removeOnLgcErrorListener(self, listener):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def initiateLogin(self, email, password, serverName, isSocialToken2Login, rememberUser):
        raise NotImplementedError
        return

    def initiateSocialLogin(self, socialNetworkName, serverName, rememberUser, isRegistration):
        raise NotImplementedError
        return

    def tryLgcLogin(self, serverName=None):
        raise NotImplementedError
        return

    def stopLgc(self):
        raise NotImplementedError
        return

    def initiateRelogin(self, login, token2, serverName):
        raise NotImplementedError
        return

    def getPreference(self, key):
        raise NotImplementedError
        return

    def clearPreferences(self):
        raise NotImplementedError
        return

    def clearToken2Preference(self):
        raise NotImplementedError
        return

    def writePreferences(self):
        raise NotImplementedError
        return

    def writePeripheryLifetime(self):
        raise NotImplementedError
        return

    @staticmethod
    def getAvailableSocialNetworks():
        raise NotImplementedError
        return
