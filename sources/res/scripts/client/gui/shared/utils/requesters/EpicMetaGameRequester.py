from __future__ import absolute_import, division
import typing
from past.utils import old_div
import BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IEpicMetaGameRequester

class EpicMetaGameRequester(AbstractSyncDataRequester, IEpicMetaGameRequester):

    @property
    def playerLevelInfo(self):
        return self.getCacheValue(b'metaLevel', (1, 0))

    @property
    def seasonData(self):
        return self.getCacheValue(b'seasonData', (0, None, {}))

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
            return old_div(self.getCacheValue(b'famePts', 0), self.battleCount)
        return 0

    def _requestCache(self, callback=None):
        BigWorld.player().epicMetaGame.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    def _preprocessValidData(self, data):
        if b'epicMetaGame' in data:
            return dict(data[b'epicMetaGame'])
        return {}
