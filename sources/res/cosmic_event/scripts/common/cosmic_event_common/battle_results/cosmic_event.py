from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from cosmic_event_common.cosmic_event_common import ScoreEvents
BATTLE_RESULTS = [
 (
  b'cosmicTotalScore', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'respawns', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'deaths', list, [], None, b'extend', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'afk_teleports', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/SHOT', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/RAMMING', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/KILL', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/PICKUP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/ABILITY_HIT', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/ARTIFACT_SCAN', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/ASSIST', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/FIRST_BLOOD', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/KILL_STREAK', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/LOOT_RESEARCHING', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/LOOT_RESEARCHING_DONE', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/LOOT_RESEARCHABLE_PICK_UP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicScore/MAX_KILL_SERIES', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/SHOT', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/RAMMING', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/KILL', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/PICKUP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/ABILITY_HIT', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/ARTIFACT_SCAN', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/ASSIST', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/FIRST_BLOOD', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/KILL_STREAK', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/LOOT_RESEARCHING', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/LOOT_RESEARCHING_DONE', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/LOOT_RESEARCHABLE_PICK_UP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicBattleEvent/MAX_KILL_SERIES', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'cosmicEquipment/2458107', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicEquipment/2458619', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicEquipment/2459899', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicEquipment/cosmic_event_shield', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicEquipment/cosmic_event_rocket_booster', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicEquipment/cosmic_event_wave', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicEquipment/cosmic_event_mine', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicEquipment/cosmic_event_teleport', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicAbilitiesImpacts/BLACK_HOLE', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicAbilitiesImpacts/GRAVITY_FIELD', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicAbilitiesImpacts/SNIPER_SHOT', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicAbilitiesImpacts/POWER_SHOT', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'cosmicAbilitiesImpacts/TELEPORT', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF)]
BATTLE_RESULTS_NAMES = set([i[0] for i in BATTLE_RESULTS])
SCORE_EVENT_NAMES = set([b'cosmicScore/' + i.name for i in ScoreEvents])
BATTLE_EVENT_NAMES = set([b'cosmicBattleEvent/' + i.name for i in ScoreEvents])
