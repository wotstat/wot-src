from battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
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
  b'comp7Rating', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'comp7Rank', tuple, (0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'comp7RatingDelta', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'comp7TeamStats', dict, {}, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'fareTeamPrestigePointsPosition', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'comp7QualActive', bool, False, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'comp7QualBattleIndex', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF)]
