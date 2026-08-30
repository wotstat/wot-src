from gui.battle_results.templates import regular
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES
from helpers import i18n
from gui.Scaleform.locale.MENU import MENU
from gui.battle_results.components import base
from gui.battle_results.components import personal
from gui.battle_results.components import vehicles
from gui.battle_results.components import common
from gui.battle_results.components import shared
from gui.battle_results.components import style
from gui.battle_results.components import epic
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
_TOTAL_EFFICIENCY_EPIC_HEADER_META = base.PropertyMeta((
 (
  BATTLE_EFFICIENCY_TYPES.DESTRUCTION, b'-', b'kills'),
 (
  BATTLE_EFFICIENCY_TYPES.DAMAGE, b'-', b'damageDealt'),
 (
  BATTLE_EFFICIENCY_TYPES.CRITS, b'-', b'criticalDamages'),
 (
  BATTLE_EFFICIENCY_TYPES.ARMOR, b'-', b'damageBlockedByArmor'),
 (
  BATTLE_EFFICIENCY_TYPES.ASSIST, b'-', b'damageAssisted'),
 (
  BATTLE_EFFICIENCY_TYPES.DETECTION, b'-', b'spotted'),
 (
  BATTLE_EFFICIENCY_TYPES.ASSIST_STUN, b'-', b'damageAssistedStun'),
 (b'killTooltip', None, b'killsTooltip'),
 (b'damageTooltip', None, b'damageDealtTooltip'),
 (b'critsTooltip', None, b'criticalDamagesTooltip'),
 (b'armorTooltip', None, b'damageBlockedTooltip'),
 (b'assistTooltip', None, b'damageAssistedTooltip'),
 (b'spottedTooltip', None, b'spottedTooltip'),
 (b'stunTooltip', None, b'damageAssistedStunTooltip'),
 (b'hasEfficencyStats', None, b'hasEfficencyStats'),
 (b'damageToSupplies', None, b'damageToSupplies'),
 (b'suppliesDestroyed', None, b'suppliesDestroyed'),
 (b'questsCompleted', None, b'questsCompleted')))
_TOTAL_EFFICIENCY_EPIC_HEADER_META.bind(epic.EpicTotalEfficiencyDetailsHeader)
EPIC_TABS_BLOCK = base.StatsBlock(_EPIC_TABS_VO_META, b'tabInfo')
EPIC_TIME_STATS_BLOCK = base.StatsBlock(base.ListMeta(runtime=False), b'timeStats', _RECORD.COMMON)
EPIC_TIME_STATS_BLOCK.addComponent(0, common.ArenaShortTimeVO(b'arenaCreateTimeOnlyStr', b'arenaCreateTime'))
EPIC_TIME_STATS_BLOCK.addComponent(1, common.ArenaDurationVO(b'duration', b'duration'))
EPIC_TIME_STATS_BLOCK.addNextComponent(common.ObjectivesReachedVO(b'objectivesReached'))
EPIC_TIME_STATS_BLOCK.addNextComponent(common.ObjectivesDestroyedVO(b'objectivesDestroyed'))
EPIC_TIME_STATS_BLOCK.addNextComponent(common.BasesCapturedVO(b'basesCaptured'))
EPIC_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone(7, 9, 10, 11)
EPIC_COMMON_STATS_BLOCK.addComponent(7, common.EpicBattleBattleFinishResultBlock())
EPIC_COMMON_STATS_BLOCK.addComponent(9, personal.EpicVehicleNamesBlock(base.ListMeta(), b'playerVehicleNames'))
EPIC_COMMON_STATS_BLOCK.addComponent(10, personal.EpicVehiclesBlock(base.ListMeta(), b'playerVehicles', _RECORD.PERSONAL))
EPIC_COMMON_STATS_BLOCK.addComponent(11, EPIC_TIME_STATS_BLOCK.clone())
EPIC_COMMON_STATS_BLOCK.addNextComponent(shared.WasInEpicBattleItem(b'epicMode'))
EPIC_PERSONAL_STATS_BLOCK = regular.REGULAR_PERSONAL_STATS_BLOCK.clone(0, 8)
EPIC_PERSONAL_STATS_BLOCK.addComponent(0, epic.EpicTotalEfficiencyDetailsHeader(_TOTAL_EFFICIENCY_EPIC_HEADER_META, b'efficiencyHeader', _RECORD.PERSONAL))
EPIC_PERSONAL_STATS_BLOCK.addComponent(8, vehicles.PersonalVehiclesEpicStatsBlock(base.ListMeta(), b'statValues', _RECORD.PERSONAL))
EPIC_PERSONAL_STATS_BLOCK.addNextComponent(personal.PlayerRank(b'playerRank'))
EPIC_TEAM_ITEM_VO_META = regular.TEAM_ITEM_VO_META.replace((
 b'statValues', vehicles.AllEpicVehicleStatValuesBlock(base.ListMeta(), b'statValues'), b'statValues'))
EPIC_TEAM_ITEM_VO_META.bind(vehicles.EpicVehicleStatsBlock)
EPIC_VEHICLE_STATS_BLOCK_VO_META = base.PropertyMeta((
 (b'shots', 0, b'shots'),
 (
  b'hits', style.SlashedValuesBlock(b'hits'), b'hits'),
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
 (b'teamSpecificStat', 0, b'teamSpecificStat'),
 (b'damageToSupplies', 0, b'damageToSupplies'),
 (b'damageFromSupplies', 0, b'damageFromSupplies'),
 (b'suppliesDestroyed', 0, b'suppliesDestroyed'),
 (b'distributedSupplyDamage', 0, b'distributedSupplyDamage'),
 (
  b'distributedSupplyBasePoints', style.SlashedValuesBlock(b'distributedSupplyBasePoints'),
  b'distributedSupplyBasePoints')))
EPIC_VEHICLE_STATS_BLOCK_VO_META.bind(vehicles.EpicVehicleStatValuesBlock)
EPIC_TEAMS_STATS_BLOCK = vehicles.TwoTeamsStatsBlock(regular.TEAMS_VO_META.clone(), b'', _RECORD.VEHICLES)
EPIC_TEAMS_STATS_BLOCK.addNextComponent(vehicles.EpicTeamStatsBlock(meta=base.ListMeta(), field=b'team1'))
EPIC_TEAMS_STATS_BLOCK.addNextComponent(vehicles.EpicTeamStatsBlock(meta=base.ListMeta(), field=b'team2'))
