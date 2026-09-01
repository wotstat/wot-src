from __future__ import absolute_import
from constants import DEATH_REASON_ALIVE
from gui.battle_results.reusable.shared import VehicleSummarizeInfo, VehicleDetailedInfo

class FallTanksVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__ = (b'_finishTime', b'_finishPosition', b'_checkpointsPassed')

    def __init__(self, vehicleID, vehicle, player, deathReason=DEATH_REASON_ALIVE):
        super(FallTanksVehicleDetailedInfo, self).__init__(vehicleID, vehicle, player, deathReason)
        self._finishPosition = 0
        self._finishTime = 0
        self._checkpointsPassed = 0
        return

    @property
    def finishTime(self):
        return self._finishTime

    @property
    def finishPosition(self):
        return self._finishPosition

    @property
    def checkpointsPassed(self):
        return self._checkpointsPassed

    @classmethod
    def _setSharedRecords(cls, info, records):
        super(FallTanksVehicleDetailedInfo, cls)._setSharedRecords(info, records)
        info._finishTime = records.get(b'fallTanksFinishTime', 0)
        info._finishPosition = records.get(b'fallTanksPosition', 0)
        info._checkpointsPassed = records.get(b'fallTanksCheckpointsPassed', 0)
        return


class FallTanksVehicleSummarizeInfo(VehicleSummarizeInfo):

    @property
    def finishTime(self):
        return self._accumulate(b'finishTime')

    @property
    def finishPosition(self):
        return self._accumulate(b'finishPosition')

    @property
    def checkpointsPassed(self):
        return self._accumulate(b'checkpointsPassed')
