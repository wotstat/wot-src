from comp7.gui.battle_results.components import comp7_components
from comp7_core.gui.battle_results.components import comp7_core_components
from comp7_core.gui.battle_results.components import progress
from comp7_core.gui.battle_results.components import shared as comp7_shared
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI
from gui.battle_results.components import base, vehicles, shared, style
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.battle_results.templates.regular import _PERSONAL_VO_META, _COMMON_VO_META, REGULAR_PERSONAL_STATS_BLOCK, REGULAR_COMMON_STATS_BLOCK, TEAMS_VO_META
from helpers import i18n
_PRESTIGE_POINTS_VO_META = base.PropertyMeta((
 (
  b'isVisible', False, b'isVisible'),
 (b'value', b'', b'value'),
 (b'label', b'', b'label'),
 (b'tooltip', b'', b'tooltip')))
_PRESTIGE_POINTS_VO_META.bind(comp7_components.PrestigePointsBlock)
_RANK_COMMON_VO_META = base.PropertyMeta((
 (b'linkage', b'', b'linkage'),
 (b'title', b'', b'title'),
 (b'descr', b'', b'descr'),
 (b'icon', b'', b'icon'),
 (b'ratingDiff', b'', b'ratingDiff'),
 (
  b'hasProgressBar', False, b'hasProgressBar'),
 (b'progressBarBegin', 0, b'progressBegin'),
 (b'progressBarCurrent', 0, b'progressCurrent'),
 (b'progressBarTotal', 0, b'progressTotal'),
 (b'ratingTotal', b'', b'ratingTotal')))
_RANK_COMMON_VO_META.bind(comp7_components.Comp7RankBlock)
_PERSONAL_VO_META.addMeta({b'prestigePoints': {}, b'deserterStr': b''})
_COMMON_VO_META.addMeta({b'comp7Rating': None})
STATS_COMPONENT_NUMBER = 8
COMPONENTS_TO_EXCLUDE = (STATS_COMPONENT_NUMBER,)
COMP7_PERSONAL_STATS_BLOCK = REGULAR_PERSONAL_STATS_BLOCK.clone(*COMPONENTS_TO_EXCLUDE)
COMP7_PERSONAL_STATS_BLOCK.addComponent(STATS_COMPONENT_NUMBER, comp7_core_components.PersonalVehiclesComp7CoreStatsBlock(base.ListMeta(), b'statValues', _RECORD.PERSONAL))
RATING_POINTS_BLOCK_NUMBER = COMP7_PERSONAL_STATS_BLOCK.getNextComponentIndex()
COMP7_PERSONAL_STATS_BLOCK.addComponent(RATING_POINTS_BLOCK_NUMBER, comp7_components.PrestigePointsBlock(_PRESTIGE_POINTS_VO_META, b'prestigePoints', _RECORD.PERSONAL))
COMP7_PERSONAL_STATS_BLOCK.addNextComponent(comp7_components.IsDeserterFlag(b'deserterStr', _RECORD.PERSONAL))
COMPONENTS_TO_EXCLUDE = (
 RATING_POINTS_BLOCK_NUMBER,)
TOURNAMENT_COMP7_PERSONAL_STATS_BLOCK = COMP7_PERSONAL_STATS_BLOCK.clone(*COMPONENTS_TO_EXCLUDE)
TRAINING_COMP7_PERSONAL_STATS_BLOCK = COMP7_PERSONAL_STATS_BLOCK.clone(*COMPONENTS_TO_EXCLUDE)
TOURNAMENT_COMP7_PERSONAL_STATS_BLOCK.addComponent(RATING_POINTS_BLOCK_NUMBER, comp7_components.TournamentRatingPointsBlock(_PRESTIGE_POINTS_VO_META, b'prestigePoints', _RECORD.PERSONAL))
TRAINING_COMP7_PERSONAL_STATS_BLOCK.addComponent(RATING_POINTS_BLOCK_NUMBER, comp7_components.TrainingRatingPointsBlock(_PRESTIGE_POINTS_VO_META, b'prestigePoints', _RECORD.PERSONAL))
SORTING_COMPONENT_NUMBER = 0
COMPONENTS_TO_EXCLUDE = (SORTING_COMPONENT_NUMBER,)
COMP7_COMMON_STATS_BLOCK = REGULAR_COMMON_STATS_BLOCK.clone(*COMPONENTS_TO_EXCLUDE)
TOURNAMENT_COMP7_COMMON_STATS_BLOCK = REGULAR_COMMON_STATS_BLOCK.clone(*COMPONENTS_TO_EXCLUDE)
TRAINING_COMP7_COMMON_STATS_BLOCK = REGULAR_COMMON_STATS_BLOCK.clone(*COMPONENTS_TO_EXCLUDE)
COMP7_COMMON_STATS_BLOCK.addComponent(SORTING_COMPONENT_NUMBER, comp7_shared.Comp7CoreSortingBlock())
COMP7_COMMON_STATS_BLOCK.addNextComponent(comp7_components.Comp7RankBlock(_RANK_COMMON_VO_META, b'comp7Rating', _RECORD.PERSONAL))
COMP7_BATTLE_PASS_PROGRESS_STATS_BLOCK = progress.Comp7CoreBattlePassProgressBlock(base.ListMeta(), b'battlePass', _RECORD.PERSONAL)
VEHICLE_STATS_BLOCK_VO_META = base.PropertyMeta((
 (b'shots', 0, b'shots'),
 (
  b'hits', style.SlashedValuesBlock(b'hits'), b'hits'),
 (b'explosionHits', 0, b'explosionHits'),
 (b'damageDealt', 0, b'damageDealt'),
 (b'sniperDamageDealt', 0, b'sniperDamageDealt'),
 (b'damageDealtBySkills', 0, b'damageDealtBySkills'),
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
  b'mileage', style.MetersToKillometersItem(b'mileage'), b'mileage'),
 (
  b'healed', style.SlashedValuesBlock(b'healed'), b'healed'),
 (b'capturedPointsOfInterest', 0, b'capturedPointsOfInterest'),
 (b'roleSkillUsed', 0, b'roleSkillUsed')))
VEHICLE_STATS_BLOCK_VO_META.bind(comp7_core_components.Comp7CoreVehicleStatValuesBlock)
COMP7_TEAM_ITEM_VO_META = base.PropertyMeta((
 (
  b'achievements', shared.AchievementsBlock(base.ListMeta(), b'achievements'), b'achievements'),
 (b'medalsCount', 0, b'achievementsCount'),
 (b'vehicleStateStr', b'', b'vehicleState'),
 (b'vehicleStatePrefixStr', b'', b'vehicleStatePrefix'),
 (b'vehicleStateSuffixStr', b'', b'vehicleStateSuffix'),
 (b'killerID', 0, b'killerID'),
 (b'deathReason', -1, b'deathReason'),
 (
  b'isPrematureLeave', False, b'isPrematureLeave'),
 (b'vehicleCD', 0, b'intCD'),
 (
  b'vehicleFullName', i18n.makeString(INGAME_GUI.PLAYERS_PANEL_UNKNOWN_VEHICLE), b'vehicleName'),
 (b'tankIcon', b'../maps/icons/vehicle/small/noImage.png', b'vehicleIcon'),
 (
  b'vehicleName', i18n.makeString(INGAME_GUI.PLAYERS_PANEL_UNKNOWN_VEHICLE), b'vehicleShortName'),
 (
  b'vehicles', [{b'icon': b'../maps/icons/vehicle/noImage.png'}], b'vehicles'),
 (b'vehicleSort', b'', b'vehicleSort'),
 (b'xpSort', 0, b'xpSort'),
 (
  b'isSelf', False, b'isPersonal'),
 (b'kills', 0, b'kills'),
 (b'tkills', 0, b'tkills'),
 (b'realKills', 0, b'realKills'),
 (b'xp', 0, b'xp'),
 (b'damageDealt', 0, b'damageDealt'),
 (b'playerId', 0, b'playerID'),
 (
  b'userVO', vehicles.TeamPlayerNameBlock(field=b'userVO'), b'player'),
 (b'squadID', 0, b'squadIndex'),
 (
  b'isOwnSquad', False, b'isPersonalSquad'),
 (
  b'isTeamKiller', False, b'isTeamKiller'),
 (
  b'isKilledByTeamKiller', False, b'isKilledByTeamKiller'),
 (
  b'statValues',
  comp7_core_components.AllComp7CoreVehicleStatValuesBlock(base.ListMeta(), b'statValues'), b'statValues'),
 (b'resourceCount', 0, b'fortResource'),
 (b'rank', 0, b'rank'),
 (b'rankIcon', b'', b'rankIcon'),
 (
  b'hasSelectedBadge', False, b'hasSelectedBadge'),
 (
  b'badgeVO', vehicles.BadgeBlock(field=b'badgeVO'), b'badge'),
 (b'playerRank', 0, b'playerRank'),
 (b'respawns', 0, b'respawns'),
 (b'suffixBadgeIcon', b'', b'suffixBadgeIcon'),
 (b'suffixBadgeStripIcon', b'', b'suffixBadgeStripIcon'),
 (b'prestigePoints', 0, b'prestigePoints'),
 (
  b'isSuperSquad', False, b'isSuperSquad')))
COMP7_TEAM_ITEM_VO_META.bind(comp7_core_components.Comp7CoreVehicleStatsBlock)
COMP7_TEAMS_STATS_BLOCK = vehicles.TwoTeamsStatsBlock(TEAMS_VO_META, b'', _RECORD.VEHICLES)
COMP7_TEAMS_STATS_BLOCK.addNextComponent(comp7_core_components.Comp7CoreTeamStatsBlock(meta=base.ListMeta(), field=b'team1'))
COMP7_TEAMS_STATS_BLOCK.addNextComponent(comp7_core_components.Comp7CoreTeamStatsBlock(meta=base.ListMeta(), field=b'team2'))
EFFICIENCY_TITLE_WITH_SKILLS_VO = comp7_core_components.EfficiencyTitleWithSkills(b'efficiencyTitle')
