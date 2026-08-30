from battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
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
  b'frontlineXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'damageToSupplies', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageFromSupplies', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'suppliesDestroyed', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'distributedSupplyDamage', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'distributedSupplyCapturePoints', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'distributedSupplyDefensePoints', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'distributedXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'frontlineQuestsCompleted', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'suppliesKilled', set, set(), None, b'joinSets', ENTRY_TYPE.ACCOUNT_SELF),
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
  b'flXPReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.ACCOUNT_ALL)]
