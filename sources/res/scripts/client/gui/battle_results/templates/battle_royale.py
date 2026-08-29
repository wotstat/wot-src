from gui.battle_results.components import base, battle_royale
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.impl.gen import R
from gui.Scaleform.genConsts.BATTLEROYALE_ALIASES import BATTLEROYALE_ALIASES
BR_TOTAL_VO_META = base.DictMeta({b'tabInfo': [], b'personal': {}, b'common': {}, b'leaderboard': []})
_BR_TABS_VO_META = base.ListMeta([
 {b'id': (BATTLEROYALE_ALIASES.BATTLE_ROYALE_SUMMARY_RESULTS_CMP), 
    b'label': b'', 
    b'selected': True, 
    b'enabled': True},
 {b'id': (BATTLEROYALE_ALIASES.BATTLE_ROYALE_SCORE_RESULTS_CMP), 
    b'label': b'', 
    b'selected': False, 
    b'enabled': True}])
BR_TABS_BLOCK = base.StatsBlock(_BR_TABS_VO_META, b'tabInfo')
_COMMON_VO_META = base.DictMeta({b'arenaStr': b'', 
   b'userName': b'', 
   b'clanAbbrev': b'', 
   b'playerVehicles': [], b'playerPlace': 0, 
   b'isSquadMode': False, 
   b'vehicleStatus': {}, b'arenaBonusType': 0, 
   b'hasPremium': False})
_PERSONAL_PLAYER_NAME_VO_META = base.PropertyMeta((
 (b'userName', b'', b'userName'),
 (b'clanAbbrev', b'', b'clanAbbrev')))
_PERSONAL_PLAYER_NAME_VO_META.bind(battle_royale.PersonalPlayerNameBlock)
_VEHICLE_STATUS_BLOCK_VO_META = base.PropertyMeta((
 (
  b'killer', {}, b'killer'),
 (b'vehicleState', -1, b'vehicleState'),
 (
  b'isSelfDestroyer', False, b'isSelfDestroyer')))
_VEHICLE_STATUS_BLOCK_VO_META.bind(battle_royale.BattleRoyaleVehicleStatusBlock)
BR_COMMON_STATS_BLOCK = base.StatsBlock(_COMMON_VO_META, b'common')
BR_COMMON_STATS_BLOCK.addNextComponent(battle_royale.PersonalPlayerNameBlock(_PERSONAL_PLAYER_NAME_VO_META))
BR_COMMON_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyaleArenaNameBlock(b'arenaStr'))
BR_COMMON_STATS_BLOCK.addNextComponent(battle_royale.ArenaBonusTypeNameBlock(b'arenaBonusType'))
BR_COMMON_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyalePlayerPlaceBlock(b'playerPlace'))
BR_COMMON_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyaleIsSquadModeBlock(b'isSquadMode'))
BR_COMMON_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyaleVehicleStatusBlock(_VEHICLE_STATUS_BLOCK_VO_META, b'vehicleStatus', _RECORD.PERSONAL))
BR_COMMON_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyaleVehiclesBlock(base.ListMeta(), b'playerVehicles', _RECORD.PERSONAL))
BR_COMMON_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyaleIsPremiumBlock(b'hasPremium'))
_PERSONAL_VO_META = base.DictMeta({b'financialBalance': {}, b'financialBalancePrem': {}, b'stats': [], b'rewards': {}, b'battlePass': {}})
_PERSONAL_VEHICLE_VO_META = base.PropertyMeta((
 (b'vehicleName', b'', b'vehicleName'),
 (b'vehicleType', b'', b'vehicleType'),
 (b'isObserver', b'', b'isObserver')))
_PERSONAL_VEHICLE_VO_META.bind(battle_royale.BattleRoyalePersonalVehicleBlock)
_FINANCIAL_BLOCK_VO_META = base.PropertyMeta((
 (b'credits', 0, b'credits'),
 (b'xp', 0, b'xp'),
 (b'crystal', 0, b'crystal'),
 (b'brcoin', 0, b'brcoin')))
_FINANCIAL_BLOCK_VO_META.bind(battle_royale.BattleRoyaleFinancialBlock)
_FINANCIAL_PREM_BLOCK_VO_META = base.PropertyMeta((
 (b'credits', 0, b'credits'),
 (b'xp', 0, b'xp'),
 (b'crystal', 0, b'crystal'),
 (b'brcoin', 0, b'brcoin')))
_FINANCIAL_PREM_BLOCK_VO_META.bind(battle_royale.BattleRoyaleFinancialPremBlock)
_STAT_ITEM_VO_META = base.PropertyMeta((
 (b'type', b'', b'type'),
 (b'value', 0, b'value'),
 (b'maxValue', 0, b'maxValue'),
 (
  b'wreathImage', R.invalid(), b'wreathImage')))
_STAT_ITEM_VO_META.bind(battle_royale.BattleRoyaleStatsItemBlock)
_BATTLE_PASS_VO_META = base.PropertyMeta((
 (b'currentLevel', 1, b'currentLevel'),
 (b'maxPoints', 0, b'maxPoints'),
 (b'earnedPoints', 0, b'earnedPoints'),
 (b'currentLevelPoints', 0, b'currentLevelPoints'),
 (b'isDone', 0, b'isDone'),
 (b'hasBattlePass', 0, b'hasBattlePass'),
 (b'battlePassComplete', 0, b'battlePassComplete'),
 (b'chapterID', 0, b'chapterID'),
 (b'pointsTotal', 0, b'pointsTotal'),
 (b'bpTopPoints', 0, b'bpTopPoints'),
 (b'pointsAux', 0, b'pointsAux'),
 (b'availablePoints', 0, b'availablePoints')))
_BATTLE_PASS_VO_META.bind(battle_royale.BattlePassBlock)
_REWARDS_VO_META = base.PropertyMeta((
 (
  b'achievements', [], b'achievements'),
 (
  b'bonuses', [], b'bonuses'),
 (b'completedQuestsCount', 0, b'completedQuestsCount'),
 (
  b'completedQuests', {}, b'completedQuests'),
 (
  b'brAwardTokens', {}, b'brAwardTokens')))
_REWARDS_VO_META.bind(battle_royale.BattleRoyaleRewardsBlock)
BR_PERSONAL_STATS_BLOCK = base.StatsBlock(_PERSONAL_VO_META, b'personal')
BR_PERSONAL_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyaleFinancialBlock(_FINANCIAL_BLOCK_VO_META, b'financialBalance'))
BR_PERSONAL_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyaleFinancialPremBlock(_FINANCIAL_PREM_BLOCK_VO_META, b'financialBalancePrem'))
BR_PERSONAL_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyaleStatsBlock(base.ListMeta(), b'stats'))
BR_PERSONAL_STATS_BLOCK.addNextComponent(battle_royale.BattleRoyaleRewardsBlock(_REWARDS_VO_META, b'rewards'))
BR_PERSONAL_STATS_BLOCK.addNextComponent(battle_royale.BattlePassBlock(_BATTLE_PASS_VO_META, b'battlePass', _RECORD.PERSONAL))
TEAM_ITEM_VO_META = base.PropertyMeta((
 (
  b'isPersonal', False, b'isPersonal'),
 (
  b'isPersonalSquad', False, b'isPersonalSquad'),
 (b'squadIdx', 0, b'squadIdx'),
 (b'place', 0, b'place'),
 (b'userName', b'', b'userName'),
 (b'hiddenName', b'', b'hiddenName'),
 (b'clanAbbrev', b'', b'clanAbbrev'),
 (b'vehicleName', b'', b'vehicleName'),
 (b'vehicleType', b'', b'vehicleType'),
 (b'achievedLevel', 0, b'achievedLevel'),
 (b'damage', 0, b'damage'),
 (b'kills', 0, b'kills'),
 (b'databaseID', 0, b'databaseID')))
TEAM_ITEM_VO_META.bind(battle_royale.BattleRoyalePlayerBlock)
BR_TEAM_STATS_BLOCK = battle_royale.BattleRoyaleTeamStatsBlock(base.ListMeta(), b'leaderboard', _RECORD.VEHICLES)
