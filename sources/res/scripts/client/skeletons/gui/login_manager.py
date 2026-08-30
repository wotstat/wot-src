from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from constants import WGC_PUBLICATION

class ILoginManager(object):
    onConnectionInitiated = None
    onConnectionRejected = None

    @property
    def servers(self):
        raise NotImplementedError
        return

    @property
    def wgcAvailable(self):
        raise NotImplementedError
        return

    def getWgcPublication(self):
        raise NotImplementedError
        return

    @property
    def isWgcSteam(self):
        raise NotImplementedError
        return

    def tryPrepareWGCLogin(self):
        raise NotImplementedError
        return

    def checkWgcCouldRetry(self, loginStatus):
        raise NotImplementedError
        return

    def addOnWgcErrorListener(self, listener):
        raise NotImplementedError
        return

    def removeOnWgcErrorListener(self, listener):
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

    def tryWgcLogin(self, serverName=None):
        raise NotImplementedError
        return

    def stopWgc(self):
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
