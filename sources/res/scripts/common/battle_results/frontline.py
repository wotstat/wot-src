from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from DictPackers import ValueReplayPacker
BATTLE_RESULTS = [
 (
  b'creditsAfterShellCosts', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'unchargedShellCosts', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'prevMetaLevel', tuple, (1, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'metaLevel', tuple, (1, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'flXP', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'originalFlXP', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'subtotalFlXP', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'boosterFlXP', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'boosterFlXPFactor100', int, 0, None, b'any', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'flXPReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'reservesModifier', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'avatarReserves', list, [], None, b'skip', ENTRY_TYPE.SERVER)]
