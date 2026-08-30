from gui.battle_results.templates import regular
from helpers import i18n
from gui.Scaleform.locale.MENU import MENU
from gui.battle_results.components import base, epic
from gui.battle_results.components import personal
from gui.battle_results.components import vehicles
from gui.battle_results.components import common
from gui.battle_results.components import shared
from gui.battle_results.components import style
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
regular.FINISH_RESULT_VO_META.bind(common.EpicBattleBattleFinishResultBlock)
_EPIC_TABS_VO_META = base.ListMeta([
 {b'label': (i18n.makeString(MENU.FINALSTATISTIC_TABS_EPICSTATS)), 
    b'linkage': b'EpicStatsUI', 
    b'viewId': b'EpicStatsUI', 
    b'showWndBg': False},
 {b'label': (i18n.makeString(MENU.FINALSTATISTIC_TABS_TEAMSTATS)), 
    b'linkage': b'TeamStatsUI', 
    b'viewId': b'TeamStatsUI', 
    b'showWndBg': False},
 {b'label': (i18n.makeString(MENU.FINALSTATISTIC_TABS_DETAILSSTATS)), 
    b'linkage': b'DetailsStatsViewUI', 
    b'viewId': b'DetailsStatsViewUI', 
    b'showWndBg': True}])
EPIC_TABS_BLOCK = base.StatsBlock(_EPIC_TABS_VO_META, b'tabInfo')
EPIC_TIME_STATS_BLOCK = base.StatsBlock(base.ListMeta(runtime=False), b'timeStats', _RECORD.COMMON)
EPIC_TIME_STATS_BLOCK.addComponent(0, common.ArenaShortTimeVO(b'arenaCreateTimeOnlyStr', b'arenaCreateTime'))
EPIC_TIME_STATS_BLOCK.addComponent(1, common.ArenaDurationVO(b'duration', b'duration'))
EPIC_TIME_STATS_BLOCK.addNextComponent(common.ObjectivesReachedVO(b'objectivesReached'))
EPIC_TIME_STATS_BLOCK.addNextComponent(common.ObjectivesDestroyedVO(b'objectivesDestroyed'))
EPIC_TIME_STATS_BLOCK.addNextComponent(common.BasesCapturedVO(b'basesCaptured'))
EPIC_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone(7, 9, 10, 11, 15, 16)
EPIC_COMMON_STATS_BLOCK.addComponent(7, common.EpicBattleBattleFinishResultBlock())
EPIC_COMMON_STATS_BLOCK.addComponent(9, personal.EpicVehicleNamesBlock(base.ListMeta(), b'playerVehicleNames'))
EPIC_COMMON_STATS_BLOCK.addComponent(10, personal.EpicVehiclesBlock(base.ListMeta(), b'playerVehicles', _RECORD.PERSONAL))
EPIC_COMMON_STATS_BLOCK.addComponent(11, EPIC_TIME_STATS_BLOCK.clone())
EPIC_COMMON_STATS_BLOCK.addComponent(15, epic.StrBattleModificationItem(b'modificationStr'))
EPIC_COMMON_STATS_BLOCK.addComponent(16, epic.BattleModificationItem(b'modificationIconPath'))
EPIC_COMMON_STATS_BLOCK.addNextComponent(shared.WasInEpicBattleItem(b'epicMode'))
EPIC_PERSONAL_STATS_BLOCK = regular.REGULAR_PERSONAL_STATS_BLOCK.clone(8)
EPIC_PERSONAL_STATS_BLOCK.addComponent(8, vehicles.PersonalVehiclesEpicStatsBlock(base.ListMeta(), b'statValues', _RECORD.PERSONAL))
EPIC_PERSONAL_STATS_BLOCK.addNextComponent(personal.PlayerRank(b'playerRank'))
EPIC_TEAM_ITEM_VO_META = regular.TEAM_ITEM_VO_META.replace((
 b'statValues', vehicles.AllEpicVehicleStatValuesBlock(base.ListMeta(), b'statValues'), b'statValues'))
EPIC_TEAM_ITEM_VO_META.bind(vehicles.EpicVehicleStatsBlock)
EPIC_VEHICLE_STATS_BLOCK_VO_META = base.PropertyMeta((
 (b'shots', 0, b'shots'),
 (b'directHits', 0, b'directHits'),
 (b'piercingHits', 0, b'piercingHits'),
 (b'explosionHits', 0, b'explosionHits'),
 (b'damageDealt', 0, b'damageDealt'),
 (b'sniperDamageDealt', 0, b'sniperDamageDealt'),
 (b'destructiblesDamageDealt', 0, b'destructiblesDamageDealt'),
 (b'equipmentDamageDealt', 0, b'equipmentDamageDealt'),
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
 (b'equipmentDamageAssisted', 0, b'equipmentDamageAssisted'),
 (b'damageAssistedStun', 0, b'damageAssistedStun'),
 (b'stunNum', 0, b'stunNum'),
 (
  b'capturePointsVal', style.SlashedValuesBlock(b'capturePointsVal'), b'capturePoints'),
 (b'timesDestroyed', 0, b'timesDestroyed'),
 (b'teamSpecificStat', 0, b'teamSpecificStat')))
EPIC_VEHICLE_STATS_BLOCK_VO_META.bind(vehicles.EpicVehicleStatValuesBlock)
EPIC_TEAMS_STATS_BLOCK = vehicles.TwoTeamsStatsBlock(regular.TEAMS_VO_META.clone(), b'', _RECORD.VEHICLES)
EPIC_TEAMS_STATS_BLOCK.addNextComponent(vehicles.EpicTeamStatsBlock(meta=base.ListMeta(), field=b'team1'))
EPIC_TEAMS_STATS_BLOCK.addNextComponent(vehicles.EpicTeamStatsBlock(meta=base.ListMeta(), field=b'team2'))
