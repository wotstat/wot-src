from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from comp7_core_common.battle_results.comp7_core import BATTLE_RESULTS as COMP7_BATTLE_RESULTS
BATTLE_RESULTS = COMP7_BATTLE_RESULTS + [
 (
  b'comp7Rating', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'comp7Rank', tuple, (0, 0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'comp7RatingDelta', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'comp7TeamStats', dict, {}, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'comp7QualActive', None, None, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'comp7QualBattleIndex', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'comp7QualRating', int, 0, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'comp7QualRank', tuple, (0, 0), None, b'skip', ENTRY_TYPE.SERVER)]
