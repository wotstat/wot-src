from adisp import adisp_process
from gui.battle_results.settings import EMBLEM_TYPE
from gui.clans.clan_cache import g_clanCache

class EmblemFetcher(object):
    __slots__ = (b'_formationDBID', b'_url', b'_callback')

    def __init__(self, formationDBID):
        super(EmblemFetcher, self).__init__()
        self._formationDBID = formationDBID
        self._url = b''
        self._callback = None
        return

    def clear(self):
        self._callback = None
        return

    def fetch(self, callback):
        callback(None)
        return

    def getURL(self):
        return self._url


class ClanEmblemFetcher(EmblemFetcher):
    __slots__ = (b'_url',)

    def __init__(self, formationDBID, textureID):
        super(ClanEmblemFetcher, self).__init__(formationDBID)
        self._url = textureID
        return

    @adisp_process
    def fetch(self, callback):
        self._url = yield g_clanCache.getClanEmblemTextureID(self._formationDBID, False, self._url)
        callback(self._url)
        return


def createFetcher(ctx):
    emblemType = ctx.getEmblemType()
    fetcher = None
    if emblemType == EMBLEM_TYPE.CLAN:
        fetcher = ClanEmblemFetcher(ctx.getFormationDBID(), ctx.getTextureID())
    return fetcher
