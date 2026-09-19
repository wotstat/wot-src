from __future__ import absolute_import
from gui.battle_results.reusable.shared import VehicleSummarizeInfo, VehicleDetailedInfo, no_key_error

class HalloweenVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__ = (b'_hwPhase', b'_hwPhasesCount', b'_effectivenessKeys', b'_bossKeys', b'_totalKeys', b'_hwTeamFightPlace', b'_hwVehiclesRespawnCount', b'_hwBossFightDamage', b'_hwHangarLoot')

    @classmethod
    @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        info = super(HalloweenVehicleDetailedInfo, cls).makeForVehicle(vehicleID, vehicle, player, vehicleRecords, critsRecords=critsRecords)
        info._hwPhase = max(1, vehicleRecords[b'halloween_phase'])
        info._hwPhasesCount = vehicleRecords[b'halloween_phases_count']
        effectivenessKeys, bossKeys = vehicleRecords[b'artefactKeys']
        info._effectivenessKeys = effectivenessKeys
        info._bossKeys = bossKeys
        info._totalKeys = sum(vehicleRecords[b'artefactKeys'])
        info._hwTeamFightPlace = vehicleRecords[b'hwTeamFightPlace']
        info._hwVehiclesRespawnCount = vehicleRecords[b'hwVehiclesRespawnCount']
        info._hwBossFightDamage = vehicleRecords[b'hwBossFightDamage']
        info._hwHangarLoot = vehicleRecords[b'hwHangarLoot']
        return info

    @property
    def hwPhase(self):
        return self._hwPhase

    @property
    def hwPhasesCount(self):
        return self._hwPhasesCount

    @property
    def effectivenessKeys(self):
        return self._effectivenessKeys

    @property
    def bossKeys(self):
        return self._bossKeys

    @property
    def totalKeys(self):
        return self._totalKeys

    @property
    def hwTeamContribution(self):
        return max(1, self._damageDealt)

    @property
    def hwTeamFightPlace(self):
        return self._hwTeamFightPlace

    @property
    def hwBossFightDamage(self):
        return self._hwBossFightDamage

    @property
    def hwVehiclesRespawnCount(self):
        return self._hwVehiclesRespawnCount

    @property
    def hwHangarLoot(self):
        return self._hwHangarLoot


class HalloweenVehicleSummarizeInfo(VehicleSummarizeInfo):

    @property
    def hwPhase(self):
        return self._accumulate(b'hwPhase')

    @property
    def hwPhasesCount(self):
        return self._accumulate(b'hwPhasesCount')

    @property
    def effectivenessKeys(self):
        return self._accumulate(b'effectivenessKeys')

    @property
    def bossKeys(self):
        return self._accumulate(b'bossKeys')

    @property
    def totalKeys(self):
        return self._accumulate(b'totalKeys')

    @property
    def hwTeamContribution(self):
        return self._accumulate(b'hwTeamContribution')

    @property
    def hwTeamFightPlace(self):
        return self._accumulate(b'hwTeamFightPlace')

    @property
    def hwBossFightDamage(self):
        return self._accumulate(b'hwBossFightDamage')

    @property
    def hwVehiclesRespawnCount(self):
        return self._accumulate(b'hwVehiclesRespawnCount')

    @property
    def hwHangarLoot(self):
        return self._collectToDict(b'hwHangarLoot')
