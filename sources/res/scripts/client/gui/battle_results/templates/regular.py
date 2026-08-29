from constants import ARENA_GUI_TYPE, MIN_VEHICLE_LEVEL
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.battle_results.components import base
from gui.battle_results.components import common
from gui.battle_results.components import details
from gui.battle_results.components import personal
from gui.battle_results.components import progress
from gui.battle_results.components import shared
from gui.battle_results.components import style
from gui.battle_results.components import vehicles
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.impl import backport
from gui.impl.gen.resources import R
from helpers import i18n
TEAM_STATS_UI_LINK = b'TeamStatsUI'
_COMMON_STATS_VO = base.DictMeta({b'label': (backport.text(R.strings.menu.finalStatistic.tabs.commonStats())), 
   b'linkage': b'CommonStats', 
   b'viewId': b'CommonStats', 
   b'showWndBg': False})
_TEAM_STATS_VO_META = base.DictMeta({b'label': (backport.text(R.strings.menu.finalStatistic.tabs.teamStats())), 
   b'linkage': TEAM_STATS_UI_LINK, 
   b'viewId': TEAM_STATS_UI_LINK, 
   b'showWndBg': False})
_DETAIL_STATS_VO_META = base.DictMeta({b'label': (backport.text(R.strings.menu.finalStatistic.tabs.detailsStats())), 
   b'linkage': b'DetailsStatsViewUI', 
   b'viewId': b'DetailsStatsViewUI', 
   b'showWndBg': True})
_MULTI_TEAM_STATS_VO_META = base.DictMeta({b'label': (backport.text(R.strings.menu.finalStatistic.tabs.teamStats())), 
   b'linkage': b'MultiteamStatsUI', 
   b'viewId': b'MultiteamStatsUI', 
   b'showWndBg': False})
REGULAR_TABS_BLOCK = base.StatsBlock(base.ListMeta(), b'tabInfo')
REGULAR_TABS_BLOCK.addNextComponent(base.StatsBlock(_COMMON_STATS_VO))
REGULAR_TABS_BLOCK.addNextComponent(base.StatsBlock(_TEAM_STATS_VO_META))
REGULAR_TABS_BLOCK.addNextComponent(base.StatsBlock(_DETAIL_STATS_VO_META))
MULTI_TEAM_TABS_BLOCK = base.StatsBlock(base.ListMeta(), b'tabInfo')
MULTI_TEAM_TABS_BLOCK.addNextComponent(base.StatsBlock(_COMMON_STATS_VO))
MULTI_TEAM_TABS_BLOCK.addNextComponent(base.StatsBlock(_MULTI_TEAM_STATS_VO_META))
MULTI_TEAM_TABS_BLOCK.addNextComponent(base.StatsBlock(_DETAIL_STATS_VO_META))
RANDOM_TABS_BLOCK = REGULAR_TABS_BLOCK.clone()
_TEXT_VO_META = base.DictMeta({b'windowTitle': (i18n.makeString(MENU.FINALSTATISTIC_WINDOW_TITLE)), 
   b'shareButtonLabel': (i18n.makeString(BATTLE_RESULTS.COMMON_RESULTSSHAREBTN)), 
   b'shareButtonTooltip': (i18n.makeString(TOOLTIPS.BATTLERESULTS_FORTRESOURCE_RESULTSSHAREBTN)), 
   b'ownTitle': (BATTLE_RESULTS.TEAM_STATS_OWNTEAM), 
   b'enemyTitle': (BATTLE_RESULTS.TEAM_STATS_ENEMYTEAM)})
REGULAR_TEXT_STATS_BLOCK = base.StatsBlock(_TEXT_VO_META, b'textData')
CLAN_TEXT_STATS_BLOCK = REGULAR_TEXT_STATS_BLOCK.clone()
CLAN_TEXT_STATS_BLOCK.addComponent(0, common.AllyTeamClanTitle(b'ownTitle'))
CLAN_TEXT_STATS_BLOCK.addComponent(1, common.EnemyTeamClanTitle(b'enemyTitle'))
_COMMON_VO_META = base.DictMeta({b'iconType': b'tank', 
   b'sortDirection': b'descending', 
   b'wasInBattle': True, 
   b'arenaCreateTimeStr': b'', 
   b'arenaStr': b'', 
   b'arenaIcon': b'', 
   b'duration': b'', 
   b'bonusType': 0, 
   b'clans': [], b'resultShortStr': b'', 
   b'resultStr': b'', 
   b'finishReasonStr': b'', 
   b'finishReasonClarificationStr': b'', 
   b'playerFakeNameStr': b'', 
   b'playerRealNameStr': b'', 
   b'clanNameStr': b'', 
   b'playerFullNameStr': b'', 
   b'regionNameStr': b'', 
   b'playerVehicles': [], b'playerVehicleNames': [], b'overtime': {}, b'totalFortResourceStr': b'', 
   b'totalInfluenceStr': b'', 
   b'timeStats': [], b'clientArenaIdx': 0, 
   b'uiVisibility': 0, 
   b'eligibleForCrystalRewards': False, 
   b'rank': None, 
   b'epicMode': False})
_CLAN_COMMON_VO_META = base.PropertyMeta((
 (b'clanDBID', -1, b'clanDBID'),
 (b'clanAbbrev', b'', b'clanAbbrev')))
_CLAN_COMMON_VO_META.bind(common.ClanInfoBlock)
CLANS_COMMON_VO_META = base.PropertyMeta((
 (
  b'allies', common.ClanInfoBlock(field=b'allies'), b'allies'),
 (
  b'enemies', common.ClanInfoBlock(field=b'enemies'), b'enemies')))
CLANS_COMMON_VO_META.bind(common.ClansInfoBlock)
_PERSONAL_VEHICLE_VO_META = base.PropertyMeta((
 (
  b'isPrematureLeave', False, b'isPrematureLeave'),
 (b'flag', b'', b'nationName'),
 (b'tankIcon', b'empty_tank', b'vehicleIcon'),
 (
  b'tankLevel', MIN_VEHICLE_LEVEL, b'vehicleLevel'),
 (b'killerID', 0, b'killerID'),
 (b'deathReason', -1, b'deathReason'),
 (b'vehicleStateStr', b'', b'vehicleState'),
 (b'vehicleStatePrefixStr', b'', b'vehicleStatePrefix'),
 (b'vehicleStateSuffixStr', b'', b'vehicleStateSuffix'),
 (
  b'isKilledByTeamKiller', False, b'isKilledByTeamKiller'),
 (
  b'isNotObserver', True, b'isVehicleStatusDefined')))
_PERSONAL_VEHICLE_VO_META.bind(personal.PersonalVehicleBlock)
_PERSONAL_PLAYER_NAME_VO_META = base.PropertyMeta((
 (b'playerFakeNameStr', b'', b'fakeNameLabel'),
 (b'playerRealNameStr', b'', b'realNameLabel'),
 (b'clanNameStr', b'', b'clanLabel'),
 (b'playerFullNameStr', b'', b'fullNameLabel'),
 (b'regionNameStr', b'', b'regionLabel')))
_PERSONAL_PLAYER_NAME_VO_META.bind(personal.PersonalPlayerNameBlock)
_PERSONAL_PLAYER_NAME_VO_META.bind(personal.DetailsPlayerNameBlock)
_KILLER_NAME_VO_META = base.PropertyMeta((
 (b'killerFakeNameStr', b'', b'fakeNameLabel'),
 (b'killerRealNameStr', b'', b'realNameLabel'),
 (b'killerClanNameStr', b'', b'clanLabel'),
 (b'killerFullNameStr', b'', b'fullNameLabel'),
 (b'killerRegionNameStr', b'', b'regionLabel')))
_KILLER_NAME_VO_META.bind(personal.KillerPlayerNameBlock)
_TIME_STATS_BLOCK = base.StatsBlock(base.ListMeta(runtime=False), b'timeStats', _RECORD.COMMON)
_TIME_STATS_BLOCK.addComponent(0, common.ArenaShortTimeVO(b'arenaCreateTimeOnlyStr', b'arenaCreateTime'))
_TIME_STATS_BLOCK.addComponent(1, common.ArenaDurationVO(b'duration', b'duration'))
_TIME_STATS_BLOCK.addComponent(2, common.PlayerKillingTimeVO(b'playerKilled'))
_STATS_SORTING_VO_META = base.PropertyMeta((
 (b'iconType', b'tank', b'criteria'),
 (b'sortDirection', b'descending', b'direction')))
_STATS_SORTING_VO_META.bind(shared.SortingBlock)
FINISH_RESULT_VO_META = base.PropertyMeta((
 (b'finishReasonStr', b'', b'finishReasonLabel'),
 (b'finishReasonClarificationStr', b'', b'finishReasonClarificationLabel'),
 (b'resultShortStr', b'', b'shortResultLabel'),
 (b'resultStr', b'', b'fullResultLabel')))
FINISH_RESULT_VO_META.bind(common.RegularFinishResultBlock)
REGULAR_COMMON_STATS_BLOCK = base.StatsBlock(_COMMON_VO_META, b'common')
REGULAR_COMMON_STATS_BLOCK.addComponent(0, shared.RegularSortingBlock())
REGULAR_COMMON_STATS_BLOCK.addComponent(1, shared.WasInBattleItem(b'wasInBattle'))
REGULAR_COMMON_STATS_BLOCK.addComponent(2, common.ArenaDateTimeItem(b'arenaCreateTimeStr', _RECORD.COMMON, b'arenaCreateTime'))
REGULAR_COMMON_STATS_BLOCK.addComponent(3, common.RegularArenaFullNameItem(b'arenaStr'))
REGULAR_COMMON_STATS_BLOCK.addComponent(4, common.ArenaIconItem(b'arenaIcon', _RECORD.COMMON))
REGULAR_COMMON_STATS_BLOCK.addComponent(5, common.ArenaDurationItem(b'duration', _RECORD.COMMON, b'duration'))
REGULAR_COMMON_STATS_BLOCK.addComponent(6, base.StatsItem(b'bonusType', _RECORD.COMMON, b'bonusType'))
REGULAR_COMMON_STATS_BLOCK.addComponent(7, common.RegularFinishResultBlock())
REGULAR_COMMON_STATS_BLOCK.addComponent(8, personal.PersonalPlayerNameBlock())
REGULAR_COMMON_STATS_BLOCK.addComponent(9, personal.PersonalVehicleNamesBlock(base.ListMeta(), b'playerVehicleNames'))
REGULAR_COMMON_STATS_BLOCK.addComponent(10, personal.PersonalVehiclesBlock(base.ListMeta(), b'playerVehicles', _RECORD.PERSONAL))
REGULAR_COMMON_STATS_BLOCK.addComponent(11, _TIME_STATS_BLOCK.clone())
REGULAR_COMMON_STATS_BLOCK.addComponent(12, shared.ClientIndexItem(b'clientArenaIdx'))
REGULAR_COMMON_STATS_BLOCK.addComponent(13, common.TeamsUiVisibility(b'uiVisibility'))
REGULAR_COMMON_STATS_BLOCK.addComponent(14, common.EligibleForCrystalRewards(b'eligibleForCrystalRewards'))
_PERSONAL_VO_META = base.DictMeta({b'isPremium': False, 
   b'isLegionnaire': False, 
   b'creditsStr': b'0', 
   b'xpStr': b'0', 
   b'fortResourceTotal': b'', 
   b'efficiencyHeader': {}, b'details': [], b'creditsData': [], b'xpData': [], b'resValues': [], b'resPremValues': [], b'resourceData': [], b'statValues': [], b'achievementsLeft': [], b'achievementsRight': [], b'showNoIncomeAlert': False, 
   b'noIncomeAlert': None, 
   b'isStunDataEnabled': False, 
   b'crystalStr': b'0', 
   b'crystalData': [], b'playerRank': 0, 
   b'isTeamKiller': False, 
   b'isPremiumPlus': False, 
   b'dynamicPremiumState': b'', 
   b'premiumInfo': {}, b'premiumBonus': {}, b'premiumEarnings': {}})
_PREMIUM_BLOCK_VO_META = base.PropertyMeta((
 (b'creditsPremiumBonusStr', b'', b'creditsPremiumBonusStr'),
 (b'xpPremiumBonusStr', b'', b'xpPremiumBonusStr'),
 (b'premiumBonusStr', b'', b'premiumBonusStr'),
 (b'backgroundIcon', b'', b'backgroundIcon'),
 (
  b'isGetPremium', False, b'isGetPremium'),
 (
  b'isUpgradeToPremiumPlus', False, b'isUpgradeToPremiumPlus'),
 (
  b'inBattleQueue', False, b'inBattleQueue'),
 (
  b'visibleDetailsBtn', False, b'visibleDetailsBtn')))
_PREMIUM_BLOCK_VO_META.bind(personal.PremiumInfoBlock)
_DAMAGE_DETAILS_VO_META = base.PropertyMeta((
 (b'damageTotalItems', 0, b'piercings'),
 (b'damageDealtVals', None, b'damageDealtValues'),
 (b'damageDealtNames', None, b'damageDealtNames')))
_DAMAGE_DETAILS_VO_META.bind(personal.DamageDetailsBlock)
_ARMOR_USING_DETAILS_VO_META = base.PropertyMeta((
 (b'armorTotalItems', 0, b'usedArmorCount'),
 (b'armorVals', None, b'armorValues'),
 (b'armorNames', None, b'armorNames')))
_ARMOR_USING_DETAILS_VO_META.bind(personal.ArmorUsingDetailsBlock)
_ASSIST_USING_DETAILS_VO_META = base.PropertyMeta((
 (b'damageAssisted', 0, b'damageAssisted'),
 (b'damageAssistedVals', None, b'damageAssistedValues'),
 (b'damageAssistedNames', None, b'damageAssistedNames')))
_ASSIST_USING_DETAILS_VO_META.bind(personal.AssistDetailsBlock)
_STUN_DETAILS_VO_META = base.PropertyMeta((
 (b'stunTotalItems', 0, b'stunNum'),
 (b'stunVals', None, b'stunValues'),
 (b'stunNames', None, b'stunNames'),
 (b'stunDuration', 0.0, b'stunDuration')))
_STUN_DETAILS_VO_META.bind(personal.StunDetailsBlock)
_CRITS_DETAILS_VO_META = base.PropertyMeta((
 (b'critsCount', 0, b'critsCount'),
 (
  b'criticalDevices', [], b'criticalDevices'),
 (
  b'destroyedDevices', [], b'destroyedDevices'),
 (
  b'destroyedTankmen', [], b'destroyedTankmen')))
_CRITS_DETAILS_VO_META.bind(personal.CritsDetailsBlock)
_TEAM_BASES_VO_META = base.PropertyMeta((
 (b'baseLabel', b'', b'label'),
 (b'captureTotalItems', 0, b'captureTotalItems'),
 (b'defenceTotalItems', 0, b'defenceTotalItems'),
 (b'captureVals', None, b'captureValues'),
 (b'captureNames', None, b'captureNames'),
 (b'defenceVals', None, b'defenceValues'),
 (b'defenceNames', None, b'defenceNames'),
 (b'isEnemyBase', None, b'isEnemyBase')))
_TEAM_BASES_VO_META.bind(personal.TeamBaseDetailsBlock)
_TEAM_BASES_VO_META.bind(personal.AllyTeamBaseDetailBlock)
_TEAM_BASES_VO_META.bind(personal.EnemyTeamBaseDetailBlock)
_DETAILS_PLAYER_NAME_VO_META = base.PropertyMeta((
 (b'playerFakeName', b'', b'fakeNameLabel'),
 (b'playerRealName', b'', b'realNameLabel'),
 (b'playerClan', b'', b'clanLabel'),
 (b'playerFullName', b'', b'fullNameLabel'),
 (b'playerRegion', b'', b'regionLabel')))
_DETAILS_PLAYER_NAME_VO_META.bind(personal.DetailsPlayerNameBlock)
_EFFICIENCY_DETAILS_VO_META = base.PropertyMeta((
 (b'deathReason', -1, b'deathReason'),
 (b'spotted', 0, b'spotted'),
 (b'piercings', 0, b'piercings'),
 (b'damageDealt', 0, b'damageDealt'),
 (b'killCount', 0, b'killCount'),
 (b'tankIcon', b'../maps/icons/vehicle/small/noImage.png', b'vehicleIcon'),
 (
  b'vehicleName',
  i18n.makeString(INGAME_GUI.PLAYERS_PANEL_UNKNOWN_VEHICLE), b'vehicleName')))
_EFFICIENCY_DETAILS_VO_META.bind(personal.EnemyDetailsBlock)
_ACHIEVEMENT_ICON_VO_META = base.PropertyMeta((
 (b'big', b'', b'big'),
 (b'small', b'', b'small')))
_ACHIEVEMENT_ICON_VO_META.bind(shared.AchievementIcon)
_ACHIEVEMENT_VO_META = base.PropertyMeta((
 (b'type', b'', b'type'),
 (b'block', b'', b'block'),
 (
  b'inactive', False, b'inactive'),
 (
  b'icon', shared.AchievementIcon(field=b'icon'), b'icon'),
 (b'rank', None, b'rank'),
 (b'localizedValue', None, b'i18nValue'),
 (
  b'unic', False, b'isUnique'),
 (
  b'isRare', False, b'isRare'),
 (b'title', b'', b'title'),
 (b'description', b'', b'description'),
 (b'rareIconId', None, b'rareIconID'),
 (
  b'isEpic', False, b'hasRibbon'),
 (b'specialIcon', None, b'specialIcon'),
 (
  b'customData', [], b'customData'),
 (
  b'arenaType', ARENA_GUI_TYPE.RANDOM, b'arenaType'),
 (b'vehicleLevel', 0, b'vehicleLevel')))
_ACHIEVEMENT_VO_META.bind(shared.AchievementBlock)
_ACHIEVEMENTS_LIST_VO_META = base.DictMeta({b'achievementsLeft': [], b'achievementsRight': []})
_PERSONAL_ACHIEVEMENTS_BLOCK = personal.TotalPersonalAchievementsBlock(_ACHIEVEMENTS_LIST_VO_META.clone(), b'', _RECORD.PERSONAL)
_PERSONAL_ACHIEVEMENTS_BLOCK.addNextComponent(shared.AchievementsBlock(base.ListMeta(), b'achievementsLeft'))
_PERSONAL_ACHIEVEMENTS_BLOCK.addNextComponent(shared.AchievementsBlock(base.ListMeta(), b'achievementsRight'))
_TOTAL_EFFICIENCY_HEADER_META = base.PropertyMeta((
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
 (b'hasEfficencyStats', None, b'hasEfficencyStats')))
_TOTAL_EFFICIENCY_HEADER_META.bind(personal.TotalEfficiencyDetailsHeader)
_PREMIUM_BONUS_VO_META = base.PropertyMeta((
 (b'description', b'', b'description'),
 (b'bonusLeft', b'', b'bonusLeft'),
 (b'xpValue', b'', b'xpValue'),
 (b'statusBonusLabel', b'', b'statusBonusLabel'),
 (b'statusBonusTooltip', b'', b'statusBonusTooltip'),
 (b'bonusIcon', b'', b'bonusIcon')))
_PREMIUM_BONUS_VO_META.bind(details.PremiumBonusDetailsBlock)
_PREMIUM_EARNINGS_VO_META = base.DictMeta({b'xpTitleStrings': [], b'xpTitleTooltips': [], b'xpPremValues': [], b'xpNoPremValues': [], b'creditsPremValues': [], b'creditsNoPremValues': [], b'backgroundIcon': (backport.image(R.images.gui.maps.icons.premacc.battleResult.premium()))})
_PREMIUM_EARNINGS_BLOCK = base.StatsBlock(_PREMIUM_EARNINGS_VO_META.clone(), b'premiumEarnings', _RECORD.PERSONAL)
_PREMIUM_EARNINGS_BLOCK.addComponent(0, details.XPTitleBlock(base.ListMeta(), b'xpTitleStrings'))
_PREMIUM_EARNINGS_BLOCK.addComponent(1, details.PremiumXPBlock(base.ListMeta(), b'xpPremValues'))
_PREMIUM_EARNINGS_BLOCK.addComponent(3, details.BaseXPBlock(base.ListMeta(), b'xpNoPremValues'))
_PREMIUM_EARNINGS_BLOCK.addComponent(4, details.PremiumCreditsBlock(base.ListMeta(), b'creditsPremValues'))
_PREMIUM_EARNINGS_BLOCK.addComponent(5, details.BaseCreditsBlock(base.ListMeta(), b'creditsNoPremValues'))
_PREMIUM_EARNINGS_BLOCK.addComponent(6, details.XPTitleTooltipBlock(base.ListMeta(), b'xpTitleTooltips'))
REGULAR_PERSONAL_STATS_BLOCK = base.StatsBlock(_PERSONAL_VO_META, b'personal')
REGULAR_PERSONAL_STATS_BLOCK.addComponent(0, personal.TotalEfficiencyDetailsHeader(_TOTAL_EFFICIENCY_HEADER_META, b'efficiencyHeader', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(1, personal.TotalEfficiencyDetailsBlock(base.ListMeta(), b'details', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(2, _PERSONAL_ACHIEVEMENTS_BLOCK)
REGULAR_PERSONAL_STATS_BLOCK.addComponent(3, personal.PremiumAccountFlag(b'isPremium'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(4, details.GainCreditsInBattleItem(b'creditsStr'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(5, details.GainXPInBattleItem(b'xpStr'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(6, details.TotalMoneyDetailsBlock(base.ListMeta(), b'creditsData', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(7, details.TotalXPDetailsBlock(base.ListMeta(), b'xpData', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(8, vehicles.PersonalVehiclesRegularStatsBlock(base.ListMeta(), b'statValues', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(9, personal.StunDataFlag(b'isStunDataEnabled'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(10, details.GainCrystalInBattleItem(b'crystalStr'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(11, details.TotalCrystalDetailsBlock(base.ListMeta(), b'crystalData', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(12, personal.IsTeamKillerFlag(b'isTeamKiller'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(13, personal.PremiumPlusFlag(b'isPremiumPlus'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(14, personal.PremiumInfoBlock(_PREMIUM_BLOCK_VO_META, b'premiumInfo', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(15, details.PremiumBonusDetailsBlock(_PREMIUM_BONUS_VO_META, b'premiumBonus', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(16, _PREMIUM_EARNINGS_BLOCK.clone())
REGULAR_PERSONAL_STATS_BLOCK.addComponent(17, personal.DynamicPremiumState(b'dynamicPremiumState'))
_TEAM_PLAYER_VO_META = base.PropertyMeta((
 (b'fakeName', b'', b'fakeNameLabel'),
 (b'userName', b'', b'realNameLabel'),
 (b'clanAbbrev', b'', b'clanLabel'),
 (b'fullName', b'', b'fullNameLabel'),
 (b'region', b'', b'regionLabel'),
 (b'igrType', 0, b'igrType'),
 (
  b'tags', set(), b'tags')))
_TEAM_PLAYER_VO_META.bind(vehicles.TeamPlayerNameBlock)
VEHICLE_STATS_BLOCK_VO_META = base.PropertyMeta((
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
VEHICLE_STATS_BLOCK_VO_META.bind(vehicles.RegularVehicleStatValuesBlock)
_BADGE_VO_META = base.PropertyMeta((
 (b'icon', b'', b'icon'),
 (b'content', b'', b'content'),
 (b'sizeContent', b'', b'sizeContent'),
 (
  b'isDynamic', False, b'isDynamic'),
 (
  b'isAtlasSource', False, b'isAtlasSource')))
_BADGE_VO_META.bind(vehicles.BadgeBlock)
TEAM_ITEM_VO_META = base.PropertyMeta((
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
  b'statValues', vehicles.AllRegularVehicleStatValuesBlock(base.ListMeta(), b'statValues'), b'statValues'),
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
 (b'suffixBadgeStripIcon', b'', b'suffixBadgeStripIcon')))
TEAM_ITEM_VO_META.bind(vehicles.RegularVehicleStatsBlock)
TEAMS_VO_META = base.DictMeta({b'team1': [], b'team2': []})
REGULAR_TEAMS_STATS_BLOCK = vehicles.TwoTeamsStatsBlock(TEAMS_VO_META.clone(), b'', _RECORD.VEHICLES)
REGULAR_TEAMS_STATS_BLOCK.addNextComponent(vehicles.RegularTeamStatsBlock(meta=base.ListMeta(), field=b'team1'))
REGULAR_TEAMS_STATS_BLOCK.addNextComponent(vehicles.RegularTeamStatsBlock(meta=base.ListMeta(), field=b'team2'))
VEHICLE_PROGRESS_STATS_BLOCK = progress.VehicleProgressBlock(base.ListMeta(), b'unlocks', _RECORD.PERSONAL)
PARAGONS_PROGRESS_STATS_BLOCK = progress.ParagonsProgressBlock(base.ListMeta(), b'paragons', _RECORD.PERSONAL)
BATTLE_PASS_PROGRESS_STATS_BLOCK = progress.BattlePassProgressBlock(base.ListMeta(), b'battlePass', _RECORD.PERSONAL)
QUESTS_PROGRESS_STATS_BLOCK = progress.QuestsProgressBlock(base.ListMeta(), b'quests', _RECORD.PERSONAL)
DOG_TAGS_PROGRESS_STATS_BLOCK = progress.DogTagsProgressBlock(base.ListMeta(), b'dog_tags', _RECORD.PERSONAL)
PROGRESSIVE_REWARD_VO = progress.ProgressiveRewardVO(b'progressiveReward')
