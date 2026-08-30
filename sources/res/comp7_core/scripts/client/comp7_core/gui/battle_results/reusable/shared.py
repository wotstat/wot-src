from gui.battle_results.reusable.shared import VehicleDetailedInfo, VehicleSummarizeInfo, no_key_error
from constants import DEATH_REASON_ALIVE

class Comp7CoreVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__ = (b'_prestigePoints', b'_roleSkillUsed', b'_healthRepair', b'_alliedHealthRepair', b'_entityCaptured')

    def __init__(self, vehicleID, vehicle, player, deathReason=DEATH_REASON_ALIVE):
        super(Comp7CoreVehicleDetailedInfo, self).__init__(vehicleID, vehicle, player, deathReason)
        self._prestigePoints = 0
        self._roleSkillUsed = 0
        self._healthRepair = 0
        self._alliedHealthRepair = 0
        self._entityCaptured = {}
        return

    @property
    def prestigePoints(self):
        return self._prestigePoints

    @property
    def roleSkillUsed(self):
        return self._roleSkillUsed

    @property
    def healthRepair(self):
        return self._healthRepair

    @property
    def alliedHealthRepair(self):
        return self._alliedHealthRepair

    @property
    def entityCaptured(self):
        return self._entityCaptured

    @classmethod
    @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        info = super(Comp7CoreVehicleDetailedInfo, cls).makeForVehicle(vehicleID, vehicle, player, vehicleRecords, critsRecords)
        info._prestigePoints = vehicleRecords.get(b'comp7PrestigePoints', 0)
        info._roleSkillUsed = vehicleRecords.get(b'roleSkillUsed', 0)
        info._healthRepair = vehicleRecords.get(b'healthRepair', 0)
        info._alliedHealthRepair = vehicleRecords.get(b'alliedHealthRepair', 0)
        info._entityCaptured = vehicleRecords.get(b'entityCaptured', {})
        return info


class Comp7CoreVehicleSummarizeInfo(VehicleSummarizeInfo):

    @property
    def prestigePoints(self):
        return self._accumulate(b'prestigePoints')

    @property
    def roleSkillUsed(self):
        return self._accumulate(b'roleSkillUsed')

    @property
    def healthRepair(self):
        return self._accumulate(b'healthRepair')

    @property
    def alliedHealthRepair(self):
        return self._accumulate(b'alliedHealthRepair')

    @property
    def entityCaptured(self):
        return self._collectToDict(b'entityCaptured')
