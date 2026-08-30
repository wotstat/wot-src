from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
BATTLE_RESULTS = [
 (
  b'ls_phase', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'ls_phasesCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'ls_progressPoints', tuple, (0, 0), None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'ls_obelisksCountByPhase', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'ls_teamFightPlace', int, -1, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'ls_respawnCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'ls_prevBestMissionsCount', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'ls_has_vehicle_daily_bonuses', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'ls_completedDifficultyMissions', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'ls_killsByTeam', int, 0, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'ls_pickedUpSouls', int, 0, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'ls_phasesCompleted', int, 0, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'ls_kafkaVehStats', dict, {}, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'ls_kafkaAvatarStats', dict, {}, None, b'skip', ENTRY_TYPE.SERVER)]
