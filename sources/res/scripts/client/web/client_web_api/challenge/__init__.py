from gui.ClientUpdateManager import g_clientUpdateManager
from web.client_web_api.api import C2WHandler, c2w
_TOKEN_PREFIX = b'gauntlet:'

class ChallengeEventHandler(C2WHandler):

    def init(self):
        super(ChallengeEventHandler, self).init()
        g_clientUpdateManager.addCallback(b'tokens', self.__onTokensUpdate)
        return

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self, True)
        super(ChallengeEventHandler, self).fini()
        return

    def __onTokensUpdate(self, diff):
        for token in diff.keys():
            if token.startswith(_TOKEN_PREFIX):
                self.__sendToken(token)

        return

    @c2w(name=b'tokens_update')
    def __sendToken(self, token):
        return token
