from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl.lobby.stronghold.stronghold_helpers import getClanSeasonProgressLevel
from web.client_web_api.api import C2WHandler, c2w
_ALLOWED_TOKEN = b'clan_season_progress'

class StrongholdEventHandler(C2WHandler):

    def init(self):
        super(StrongholdEventHandler, self).init()
        g_clientUpdateManager.addCallback(b'tokens', self.__onTokensUpdate)
        return

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self, True)
        super(StrongholdEventHandler, self).fini()
        return

    def __onTokensUpdate(self, diff):
        if _ALLOWED_TOKEN in diff:
            self.__sendToken({_ALLOWED_TOKEN: (getClanSeasonProgressLevel())})
        return

    @c2w(name=b'stronghold_token_update')
    def __sendToken(self, tokenInfo):
        return tokenInfo
