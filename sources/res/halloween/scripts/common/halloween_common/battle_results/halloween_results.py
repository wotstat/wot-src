from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
BATTLE_RESULTS = [
 (
  b'halloween_phase', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'halloween_phases_count', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'hwCompletedModifiedPhasesCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwFlawlessPhasesCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwDeathlessWin', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'artefactKeys', tuple, (0, 0), None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'hwTeamFightPlace', int, -1, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'hwBossFightPlace', int, -1, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'hwBossFightDamage', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'hwDealRamDamage', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwVehiclesRespawnCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'hwUnveiledAnomaliesCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwEpicAnomaliesUsageCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwIndividualAndEpicCollectedCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwAbilityUsageCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwSoulsCollected', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwTeamHealedHP', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwBombersKilledByShieldCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'hwHangarLoot', dict, {}, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'hwAnomaliesLoot', set, set(), None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'hwKafkaVehicleStats', dict, {}, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'hwKafkaAvatarStats', dict, {}, None, b'skip', ENTRY_TYPE.SERVER)]
