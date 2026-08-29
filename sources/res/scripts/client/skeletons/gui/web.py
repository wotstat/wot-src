import typing
if typing.TYPE_CHECKING:
    from gui.clans.clan_account_profile import MyClanAccountProfile

class IWebController(object):

    def addListener(self, listener):
        raise NotImplementedError
        return

    def removeListener(self, listener):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    @property
    def isStarted(self):
        raise NotImplementedError
        return

    def start(self, force=True):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def invalidate(self):
        raise NotImplementedError
        return

    def getClanDossier(self, clanDbID=None):
        raise NotImplementedError
        return

    def login(self, callback):
        raise NotImplementedError
        return

    def resyncLogin(self, forceLogin=False):
        raise NotImplementedError
        return

    def sendRequest(self, ctx, callback=None, allowDelay=None):
        raise NotImplementedError
        return

    def getStateID(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def getWebRequester(self):
        raise NotImplementedError
        return

    def getAccountProfile(self):
        raise NotImplementedError
        return

    def getLimits(self):
        raise NotImplementedError
        return

    def getClanDbID(self):
        raise NotImplementedError
        return

    def changeState(self, state):
        raise NotImplementedError
        return

    def onStateUpdated(self):
        raise NotImplementedError
        return

    def isLoggedOn(self):
        raise NotImplementedError
        return

    def updateClanCommonDataCache(self, cache):
        raise NotImplementedError
        return

    def clearClanCommonDataCache(self):
        raise NotImplementedError
        return

    def getClanCommonData(self, clanDbID):
        raise NotImplementedError
        return

    def requestUsers(self, dbIDs, callback):
        raise NotImplementedError
        return

    def getAccessTokenData(self, force, callback=None):
        raise NotImplementedError
        return
