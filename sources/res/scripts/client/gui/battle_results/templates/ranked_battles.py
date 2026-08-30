from gui.impl import backport
from gui.impl.gen import R
from gui.battle_results.components import base, vehicles, ranked
from gui.battle_results.components import style
from gui.battle_results.templates import regular
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.shared.formatters import text_styles
RANKED_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone()
_RANK_COMMON_VO_META = base.PropertyMeta((
 (b'state', b'', b'state'),
 (b'linkage', b'', b'linkage'),
 (b'title', b'', b'title'),
 (b'description', b'', b'description'),
 (b'descriptionIcon', b'', b'descriptionIcon'),
 (b'icon', b'', b'icon'),
 (b'plateIcon', b'', b'plateIcon'),
 (b'shieldIcon', b'', b'shieldIcon'),
 (b'shieldCount', b'', b'shieldCount')))
_RANK_COMMON_VO_META.bind(ranked.RankChangesBlock)
RANKED_VEHICLE_STATS_BLOCK_VO_META = base.PropertyMeta((
 (
  b'xp', style.XpStatsItem(b'xp'), b'xp'),
 (
  b'xpForAttack', style.XpStatsItem(b'xpForAttack'), b'xpForAttack'),
 (
  b'xpForAssist', style.XpStatsItem(b'xpForAssist'), b'xpForAssist'),
 (
  b'xpOther', style.XpStatsItem(b'xpOther'), b'xpOther'),
 (b'shots', 0, b'shots'),
 (
  b'hits', style.SlashedValuesBlock(b'hits'), b'hits'),
 (b'explosionHits', 0, b'explosionHits'),
 (b'damageDealt', 0, b'damageDealt'),
 (b'sniperDamageDealt', 0, b'sniperDamageDealt'),
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
RANKED_VEHICLE_STATS_BLOCK_VO_META.bind(vehicles.RankedVehicleStatValuesBlock)
RANKED_COMMON_STATS_BLOCK.addNextComponent(ranked.RankChangesBlock(_RANK_COMMON_VO_META, b'rank', _RECORD.VEHICLES))
RANKED_TEAMS_STATS_BLOCK = vehicles.TwoTeamsStatsBlock(regular.TEAMS_VO_META.clone(), b'', _RECORD.VEHICLES)
RANKED_PERSONAL_STATS_BLOCK = regular.REGULAR_PERSONAL_STATS_BLOCK.clone(8)
RANKED_PERSONAL_STATS_BLOCK.addComponent(8, vehicles.PersonalVehiclesRankedStatsBlock(base.ListMeta(), b'statValues', _RECORD.PERSONAL))
RANKED_RESULTS_BLOCK = base.DictMeta({b'title': (text_styles.promoTitle(backport.text(R.strings.ranked_battles.battleresult.headerText()))), 
   b'readyBtn': (backport.text(R.strings.ranked_battles.battleResult.yes())), 
   b'readyBtnVisible': True, 
   b'mainBackground': (backport.image(R.images.gui.maps.icons.rankedBattles.bg.main())), 
   b'leftData': {}, b'rightData': {}, b'animationEnabledLabel': (text_styles.main(backport.text(R.strings.ranked_battles.rankedBattlesBattleResults.animationCheckBoxLabel()))), 
   b'animationEnabled': True, 
   b'showWidgetAnimation': True, 
   b'statusText': b'', 
   b'state': None})
RANKED_ENABLE_ANIMATION_BLOCK = ranked.RankedResultsEnableAnimation(b'animationEnabled')
RANKED_SHOW_WIDGET_BLOCK = ranked.RankedResultsShowWidgetAnimation(b'showWidgetAnimation')
RANKED_RESULTS_STATUS_BLOCK = ranked.RankedResultsStatusBlock(b'statusText')
RANKED_RESULTS_STATE_BLOCK = ranked.RankedResultsStateBlock(b'state')
_RANKED_RESULTS_TEAMS_VO_META = base.DictMeta({b'leftData': {}, b'rightData': {}})
_RANKED_RESULTS_TEAM_DATA_VO_META = base.PropertyMeta((
 (b'title', b'', b'title'),
 (b'titleAlpha', 1.0, b'titleAlpha'),
 (
  b'tops', [], b'teamList')))
_RANKED_RESULTS_TEAM_DATA_VO_META.bind(vehicles.RankedResultsTeamDataStatsBlock)
_RANKED_RESULTS_TEAM_PART_DATA_VO_META = base.PropertyMeta((
 (
  b'listData', [], b'listData'),
 (b'backgroundType', b'', b'backgroundType'),
 (b'iconType', b'', b'iconType'),
 (
  b'backgroundBlink', False, b'backgroundBlink'),
 (b'topIcon', b'', b'icon'),
 (b'topCapacity', 0, b'capacity'),
 (
  b'isColorBlind', False, b'isColorBlind')))
_RANKED_RESULTS_TEAM_PART_DATA_VO_META.bind(vehicles.RankedResultsTeamPartDataStatsBlock)
RANKED_RESULTS_TEAMS_STATS_BLOCK = vehicles.RankedResultsTeamStatsBlock(_RANKED_RESULTS_TEAMS_VO_META.clone(), b'', _RECORD.VEHICLES)
RANKED_RESULTS_TEAMS_STATS_BLOCK.addNextComponent(vehicles.RankedResultsTeamDataStatsBlock(field=b'leftData'))
RANKED_RESULTS_TEAMS_STATS_BLOCK.addNextComponent(vehicles.RankedResultsTeamDataStatsBlock(field=b'rightData'))
_RANKED_RESULTS_LIST_ITEM_VO_META = base.PropertyMeta((
 (b'nickName', b'', b'nickName'),
 (b'nickNameHuge', b'', b'nickNameHuge'),
 (b'fakeName', b'', b'fakeName'),
 (b'fakeNameHuge', b'', b'fakeNameHuge'),
 (b'points', b'', b'points'),
 (b'pointsHuge', b'', b'pointsHuge'),
 (
  b'selected', False, b'selected'),
 (b'standoff', 0, b'standoff'),
 (
  b'tags', set(), b'tags')))
_RANKED_RESULTS_LIST_ITEM_VO_META.bind(vehicles.RankedResultsListItemStatsBlock)
