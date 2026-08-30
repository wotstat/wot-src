from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
BATTLE_RESULTS = [
 (
  b'updatedRankChange', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'accRank', tuple, (0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'vehRank', tuple, (0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'prevMaxRank', tuple, (0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'prevVehRank', tuple, (0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'shields', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'prevShields', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'rankedSeason', tuple, (0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'rankedSeasonNum', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'bonusBattleUsed', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'efficiencyBonusBattles', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'stepsBonusBattles', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'prevAccRank', tuple, (0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_ALL)]
