from gui.battle_results.components import common
from gui.battle_results.components import base
from gui.battle_results.templates import regular
from gui.battle_results.components import style
from gui.battle_results.components import vehicles
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
regular.FINISH_RESULT_VO_META.bind(common.StrongholdBattleFinishResultBlock)
STRONGHOLD_BATTLE_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone()
STRONGHOLD_BATTLE_COMMON_STATS_BLOCK.addNextComponent(common.StrongholdBattleFinishResultBlock(None, b'', _RECORD.PERSONAL, _RECORD.PERSONAL_AVATAR))
STRONGHOLD_VEHICLE_STATS_BLOCK_VO_META = base.PropertyMeta((
 (b'shots', 0, b'shots'),
 (
  b'hits', style.SlashedValuesBlock(b'hits'), b'hits'),
 (b'explosionHits', 0, b'explosionHits'),
 (b'damageDealt', 0, b'damageDealt'),
 (b'sniperDamageDealt', 0, b'sniperDamageDealt'),
 (b'artilleryFortEquipDamageDealt', 0, b'artilleryFortEquipDamageDealt'),
 (b'directHitsReceived', 0, b'directHitsReceived'),
 (b'piercingsReceived', 0, b'piercingsReceived'),
 (b'noDamageDirectHitsReceived', 0, b'noDamageDirectHitsReceived'),
 (b'explosionHitsReceived', 0, b'explosionHitsReceived'),
 (b'damageBlockedByArmor', 0, b'damageBlockedByArmor'),
 (
  b'teamHitsDamage', style.RedSlashedValuesBlock(b'teamHitsDamage'), b'teamHitsDamage'),
 (b'spotted', 0, b'spotted'),
 (
  b'damagedKilled', style.SlashedValuesBlock(b'damagedKilled'), b'damagedKilled'),
 (b'damageAssisted', 0, b'damageAssisted'),
 (b'stunDuration', 0.0, b'stunDuration'),
 (b'damageAssistedStun', 0, b'damageAssistedStun'),
 (b'stunNum', 0, b'stunNum'),
 (
  b'capturePointsVal', style.SlashedValuesBlock(b'capturePointsVal'), b'capturePoints'),
 (
  b'mileage', style.MetersToKillometersItem(b'mileage'), b'mileage')))
STRONGHOLD_VEHICLE_STATS_BLOCK_VO_META.bind(vehicles.StrongholdVehicleStatValuesBlock)
STRONGHOLD_TEAM_ITEM_VO_META = regular.TEAM_ITEM_VO_META.replace((
 b'statValues', vehicles.AllStrongholdVehicleStatValuesBlock(base.ListMeta(), b'statValues'), b'statValues'))
STRONGHOLD_TEAM_ITEM_VO_META.bind(vehicles.StrongholdVehicleStatsBlock)
STRONGHOLD_TEAMS_STATS_BLOCK = vehicles.TwoTeamsStatsBlock(regular.TEAMS_VO_META.clone(), b'', _RECORD.VEHICLES)
STRONGHOLD_TEAMS_STATS_BLOCK.addComponent(0, vehicles.StrongholdTeamStatsBlock(base.ListMeta(), field=b'team1'))
STRONGHOLD_TEAMS_STATS_BLOCK.addComponent(1, vehicles.StrongholdTeamStatsBlock(base.ListMeta(), field=b'team2'))
STRONGHOLD_PERSONAL_STATS_BLOCK = regular.REGULAR_PERSONAL_STATS_BLOCK.clone(8)
STRONGHOLD_PERSONAL_STATS_BLOCK.addComponent(8, vehicles.PersonalVehiclesStrongholdStatsBlock(base.ListMeta(), b'statValues', _RECORD.PERSONAL))
STRONGHOLD_TABS_BLOCK = regular.REGULAR_TABS_BLOCK.clone()
