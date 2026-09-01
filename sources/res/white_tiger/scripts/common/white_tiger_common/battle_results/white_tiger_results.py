from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
BATTLE_RESULTS = [
 (
  b'wtBattleVSPriorityBoss', bool, False, None, b'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'wtBossVulnerableDamage', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'maxWtPlasmaBonus', int, 0, None, b'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'wtGeneratorsCaptured', int, 0, None, b'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'wtDeathCount', int, 0, None, b'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'wtMiniBossDestroyed', int, 0, None, b'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'wtKilledByHyperionCount', int, 0, None, b'max', ENTRY_TYPE.VEHICLE_ALL)]
