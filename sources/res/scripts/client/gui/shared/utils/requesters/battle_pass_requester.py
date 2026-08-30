from __future__ import absolute_import
import BigWorld
from battle_pass_common import BATTLE_PASS_PDATA_KEY
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBattlePassRequester

class BattlePassRequester(AbstractSyncDataRequester, IBattlePassRequester):

    def getSeasonID(self):
        return self.getCacheValue(b'seasonID', 0)

    def getState(self):
        return self.getCacheValue(b'state', 0)

    def getActiveChapterID(self):
        return self.getCacheValue(b'chapterID', 0)

    def getPointsForVehicle(self, vehicleID, default=0):
        return self.getCacheValue(b'vehiclePoints', {}).get(vehicleID, default)

    def getChapterStats(self):
        return self.getCacheValue(b'seasonStats', {}).get(b'chaptersStats', {})

    def getCurrentLevelByChapterID(self, chapterID):
        return self.getChapterStats().get(chapterID, {}).get(b'level', 0)

    def getPointsByChapterID(self, chapterID):
        return self.getChapterStats().get(chapterID, {}).get(b'points', 0)

    def getNonChapterPoints(self):
        return self.getCacheValue(b'seasonStats', {}).get(b'nonChapterPoints', 0)

    def _preprocessValidData(self, data):
        return dict(data.get(BATTLE_PASS_PDATA_KEY, {}))

    def _requestCache(self, callback=None):
        BigWorld.player().battlePass.getCache((lambda resID, value: self._response(resID, value, callback)))
        return
