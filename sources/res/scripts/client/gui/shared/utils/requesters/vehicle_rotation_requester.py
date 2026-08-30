from __future__ import absolute_import
import BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IVehicleRotationRequester

class VehicleRotationRequester(AbstractSyncDataRequester, IVehicleRotationRequester):

    def getBattlesCount(self, groupNum):
        battlesCount = self._groupLocks[b'groupBattles']
        groupIdx = max(0, groupNum - 1)
        if len(battlesCount) > groupIdx:
            return battlesCount[groupIdx]
        return -1

    def isGroupLocked(self, groupNum):
        if groupNum == 0:
            return False
        groupsLocks = self._groupLocks[b'isGroupLocked']
        groupIdx = max(0, groupNum - 1)
        if len(groupsLocks) > groupIdx:
            return groupsLocks[groupIdx]
        return False

    def getGroupNum(self, vehIntCD):
        return self.getCacheValue(b'vehiclesGroupMapping', {}).get(vehIntCD, 0)

    def isInfinite(self, groupNum):
        return self.getBattlesCount(groupNum) == -1

    def unlockedBy(self, groupNum):
        playGroupsToUnlock = self._groupLocks[b'unlockedBy']
        return playGroupsToUnlock.get(groupNum, -1)

    @property
    def _groupLocks(self):
        return self.getCacheValue(b'groupLocks', {b'groupBattles': [], b'isGroupLocked': [], b'unlockedBy': {}})

    def _requestCache(self, callback=None):
        BigWorld.player().vehicleRotation.getCache((lambda resID, value: self._response(resID, value, callback)))
        return
