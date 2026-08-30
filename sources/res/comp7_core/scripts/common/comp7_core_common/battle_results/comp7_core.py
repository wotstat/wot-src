from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
BATTLE_RESULTS = [
 (
  b'comp7PrestigePoints', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'roleSkillUsed', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'healthRepair', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'alliedHealthRepair', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'fareTeamPrestigePointsPosition', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'isSuperSquad', bool, False, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'comp7BannedVehicles', dict, {}, None, b'skip', ENTRY_TYPE.COMMON)]
