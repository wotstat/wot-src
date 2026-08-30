import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBattleRoyaleRequester

class BattleRoyaleRequester(AbstractSyncDataRequester, IBattleRoyaleRequester):

    @property
    def accTitle(self):
        return self.getCacheValue(b'accBRTitle', (1, 0))

    @property
    def battleCount(self):
        return self.getCacheValue(b'BRBattlesCount', 0)

    @property
    def killCount(self):
        return self.getCacheValue(b'BRTotalKills', 0)

    @property
    def testDriveExpired(self):
        return self.getCacheValue(b'testDriveExpired', {})

    @property
    def topCount(self):
        return self.getCacheValue(b'BRSoloTop1Count') + self.getCacheValue(b'BRSquadTop1Count')

    def getStats(self, arenaBonusType, playerDatabaseID=None):
        if playerDatabaseID:
            return {}
        return self.getCacheValue(b'brBattleStats').get(arenaBonusType, {})

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().battleRoyale.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    def _preprocessValidData(self, data):
        if b'battleRoyale' in data:
            return dict(data[b'battleRoyale'])
        return dict()
