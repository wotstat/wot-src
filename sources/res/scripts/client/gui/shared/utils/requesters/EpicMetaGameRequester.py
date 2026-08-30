import typing, BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IEpicMetaGameRequester

class EpicMetaGameRequester(AbstractSyncDataRequester, IEpicMetaGameRequester):

    @property
    def playerLevelInfo(self):
        return self.getCacheValue(b'metaLevel', (1, 0))

    @property
    def seasonData(self):
        return self.getCacheValue(b'seasonData', (0, None, dict()))

    @property
    def skillPoints(self):
        return self.getCacheValue(b'abilityPts', 0)

    def selectedSkills(self, vehicleCD):
        skillsDict = self.getCacheValue(b'selectedAbilities', None)
        if skillsDict is not None:
            return skillsDict.get(vehicleCD, [])
        else:
            return []

    @property
    def skillLevels(self):
        return self.getCacheValue(b'abilities', {})

    @property
    def battleCount(self):
        return self.getCacheValue(b'battleCount', 0)

    @property
    def averageXP(self):
        if self.battleCount > 0:
            return self.getCacheValue(b'famePts', 0) / self.battleCount
        return 0

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().epicMetaGame.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    def _preprocessValidData(self, data):
        if b'epicMetaGame' in data:
            return dict(data[b'epicMetaGame'])
        return dict()
