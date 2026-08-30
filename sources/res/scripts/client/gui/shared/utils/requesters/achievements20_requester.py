import typing, BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IAchievements20Requester
from constants import AchievementsLayoutStates
if typing.TYPE_CHECKING:
    from typing import List

class Achievements20Requester(AbstractSyncDataRequester, IAchievements20Requester):

    def getLayout(self):
        return self.getCacheValue(b'achievementsLayout', {}).get(b'layout', [])

    def getLayoutState(self):
        return self.getCacheValue(b'achievementsLayout', {}).get(b'state', AchievementsLayoutStates.AUTO)

    def getAchievementBitmask(self):
        return self.getCacheValue(b'achievementsLayout', {}).get(b'achievementBitmask', AchievementsLayoutStates.AUTO)

    def getLayoutLength(self):
        return self.getCacheValue(b'achievementsLayout', {}).get(b'layoutLength', 0)

    def _preprocessValidData(self, data):
        return dict(data.get(b'achievements20', {}))

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().achievements20.getCache((lambda resID, value: self._response(resID, value, callback)))
        return
