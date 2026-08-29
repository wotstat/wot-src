import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IRankedRequester

class RankedRequester(AbstractSyncDataRequester, IRankedRequester):

    @property
    def season(self):
        return self.getCacheValue(b'season', (-1, -1))

    @property
    def accRank(self):
        return self.getCacheValue(b'accRank', (0, 0))

    @property
    def maxRank(self):
        return self.getCacheValue(b'maxRank', (0, 0))

    @property
    def stepsCount(self):
        return self.getCacheValue(b'stepsCount', 0)

    @property
    def seasonStepsCount(self):
        return self.getCacheValue(b'seasonStepsCount', 0)

    @property
    def seasonEfficiencyStamp(self):
        return self.getCacheValue(b'currentEfficiency', {})

    @property
    def divisionsStats(self):
        return self.getCacheValue(b'divisions', {})

    @property
    def shields(self):
        return self.getCacheValue(b'shields', {})

    @property
    def persistentBonusBattles(self):
        return self.getCacheValue(b'bonusBattlesCount', 0)

    @property
    def dailyBonusBattles(self):
        return self.getCacheValue(b'dailyBonusBattlesCount', 0)

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().ranked.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    def _preprocessValidData(self, data):
        if b'ranked' in data:
            return dict(data[b'ranked'])
        return dict()
