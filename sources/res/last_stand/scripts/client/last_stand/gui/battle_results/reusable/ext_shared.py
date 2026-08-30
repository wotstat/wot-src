from __future__ import absolute_import
from gui.battle_results.reusable.shared import VehicleSummarizeInfo, VehicleDetailedInfo, no_key_error

class LSVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__ = (b'_phase', b'_phasesCount', b'_effectivenessPoints', b'_totalPoints', b'_teamFightPlace', b'_respawnsCount', b'_prevBestMissionsCount', b'_completedDifficultyMissions', b'_obeliskPoints')

    @classmethod
    @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        info = super(LSVehicleDetailedInfo, cls).makeForVehicle(vehicleID, vehicle, player, vehicleRecords, critsRecords=critsRecords)
        info._phase = vehicleRecords.get(b'ls_phase', 0)
        info._phasesCount = vehicleRecords.get(b'ls_phasesCount', 0)
        effectivenessPoints, obeliskPoints = vehicleRecords[b'ls_progressPoints']
        info._effectivenessPoints = effectivenessPoints
        info._obeliskPoints = obeliskPoints
        info._totalPoints = sum(vehicleRecords[b'ls_progressPoints'])
        info._teamFightPlace = vehicleRecords[b'ls_teamFightPlace']
        info._respawnsCount = vehicleRecords[b'ls_respawnCount']
        info._prevBestMissionsCount = vehicleRecords.get(b'ls_prevBestMissionsCount', 0)
        info._completedDifficultyMissions = vehicleRecords.get(b'ls_completedDifficultyMissions', [])
        return info

    @property
    def prevBestMissionsCount(self):
        return self._prevBestMissionsCount

    @property
    def phase(self):
        return self._phase

    @property
    def phasesCount(self):
        return self._phasesCount

    @property
    def effectivenessPoints(self):
        return self._effectivenessPoints

    @property
    def obeliskPoints(self):
        return self._obeliskPoints

    @property
    def totalPoints(self):
        return self._totalPoints

    @property
    def teamContribution(self):
        return max(1, self._damageDealt)

    @property
    def teamFightPlace(self):
        return self._teamFightPlace

    @property
    def respawnsCount(self):
        return self._respawnsCount

    @property
    def completedDifficultyMissions(self):
        return self._completedDifficultyMissions


class LSVehicleSummarizeInfo(VehicleSummarizeInfo):

    @property
    def prevBestMissionsCount(self):
        return min(self._getAtrributeGenerator(b'prevBestMissionsCount'))

    @property
    def phase(self):
        return self._accumulate(b'phase')

    @property
    def phasesCount(self):
        return self._accumulate(b'phasesCount')

    @property
    def effectivenessPoints(self):
        return self._accumulate(b'effectivenessPoints')

    @property
    def obeliskPoints(self):
        return self._accumulate(b'obeliskPoints')

    @property
    def totalPoints(self):
        return self._accumulate(b'totalPoints')

    @property
    def teamContribution(self):
        return self._accumulate(b'teamContribution')

    @property
    def teamFightPlace(self):
        return self._accumulate(b'teamFightPlace')

    @property
    def respawnsCount(self):
        return self._accumulate(b'respawnsCount')

    @property
    def completedDifficultyMissions(self):
        return next(self._getAtrributeGenerator(b'completedDifficultyMissions'), [])
