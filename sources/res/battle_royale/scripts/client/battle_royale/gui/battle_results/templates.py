from gui.battle_results.components import base
from battle_royale.gui.battle_results import components
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.impl.gen import R
BR_TOTAL_VO_META = base.DictMeta({b'tabInfo': [], b'personal': {}, b'common': {}, b'leaderboard': []})
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
_PERSONAL_PLAYER_NAME_VO_META.bind(components.PersonalPlayerNameBlock)
_VEHICLE_STATUS_BLOCK_VO_META = base.PropertyMeta((
 (
  b'killer', {}, b'killer'),
 (b'vehicleState', -1, b'vehicleState'),
 (
  b'isSelfDestroyer', False, b'isSelfDestroyer')))
_VEHICLE_STATUS_BLOCK_VO_META.bind(components.BattleRoyaleVehicleStatusBlock)
BR_COMMON_STATS_BLOCK = base.StatsBlock(_COMMON_VO_META, b'common')
BR_COMMON_STATS_BLOCK.addNextComponent(components.PersonalPlayerNameBlock(_PERSONAL_PLAYER_NAME_VO_META))
BR_COMMON_STATS_BLOCK.addNextComponent(components.BattleRoyaleArenaNameBlock(b'arenaStr'))
BR_COMMON_STATS_BLOCK.addNextComponent(components.ArenaBonusTypeNameBlock(b'arenaBonusType'))
BR_COMMON_STATS_BLOCK.addNextComponent(components.BattleRoyalePlayerPlaceBlock(b'playerPlace'))
BR_COMMON_STATS_BLOCK.addNextComponent(components.BattleRoyaleIsSquadModeBlock(b'isSquadMode'))
BR_COMMON_STATS_BLOCK.addNextComponent(components.BattleRoyaleVehicleStatusBlock(_VEHICLE_STATUS_BLOCK_VO_META, b'vehicleStatus', _RECORD.PERSONAL))
BR_COMMON_STATS_BLOCK.addNextComponent(components.BattleRoyaleVehiclesBlock(base.ListMeta(), b'playerVehicles', _RECORD.PERSONAL))
BR_COMMON_STATS_BLOCK.addNextComponent(components.BattleRoyaleIsPremiumBlock(b'hasPremium'))
_PERSONAL_VO_META = base.DictMeta({b'financialBalance': {}, b'financialBalancePrem': {}, b'stats': [], b'rewards': {}, b'battlePass': {}, b'dailyBonusFactor': 0})
_PERSONAL_VEHICLE_VO_META = base.PropertyMeta((
 (b'vehicleName', b'', b'vehicleName'),
 (b'vehicleType', b'', b'vehicleType'),
 (b'isObserver', b'', b'isObserver')))
_PERSONAL_VEHICLE_VO_META.bind(components.BattleRoyalePersonalVehicleBlock)
_DAILY_BONUS_FACTOR_VO_META = base.PropertyMeta(((b'dailyBonusFactor', 0, b'dailyBonusFactor'),))
_DAILY_BONUS_FACTOR_VO_META.bind(components.BattleRoyaleDailyBonusFactorBlock)
_FINANCIAL_BLOCK_VO_META = base.PropertyMeta((
 (b'credits', 0, b'credits'),
 (b'xp', 0, b'xp'),
 (b'crystal', 0, b'crystal'),
 (b'brcoin', 0, b'brcoin'),
 (b'stpcoin', 0, b'stpcoin')))
_FINANCIAL_BLOCK_VO_META.bind(components.BattleRoyaleFinancialBlock)
_FINANCIAL_PREM_BLOCK_VO_META = base.PropertyMeta((
 (b'credits', 0, b'credits'),
 (b'xp', 0, b'xp')))
_FINANCIAL_PREM_BLOCK_VO_META.bind(components.BattleRoyaleFinancialPremBlock)
_STAT_ITEM_VO_META = base.PropertyMeta((
 (b'type', b'', b'type'),
 (b'value', 0, b'value'),
 (b'maxValue', 0, b'maxValue'),
 (
  b'wreathImage', R.invalid(), b'wreathImage')))
_STAT_ITEM_VO_META.bind(components.BattleRoyaleStatsItemBlock)
_BATTLE_PASS_VO_META = base.PropertyMeta(((b'bpTopPoints', 0, b'bpTopPoints'),))
_BATTLE_PASS_VO_META.bind(components.BattlePassBlock)
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
_REWARDS_VO_META.bind(components.BattleRoyaleRewardsBlock)
BR_PERSONAL_STATS_BLOCK = base.StatsBlock(_PERSONAL_VO_META, b'personal')
BR_PERSONAL_STATS_BLOCK.addNextComponent(components.BattleRoyaleFinancialBlock(_FINANCIAL_BLOCK_VO_META, b'financialBalance'))
BR_PERSONAL_STATS_BLOCK.addNextComponent(components.BattleRoyaleFinancialPremBlock(_FINANCIAL_PREM_BLOCK_VO_META, b'financialBalancePrem'))
BR_PERSONAL_STATS_BLOCK.addNextComponent(components.BattleRoyaleStatsBlock(base.ListMeta(), b'stats'))
BR_PERSONAL_STATS_BLOCK.addNextComponent(components.BattleRoyaleRewardsBlock(_REWARDS_VO_META, b'rewards'))
BR_PERSONAL_STATS_BLOCK.addNextComponent(components.BattlePassBlock(_BATTLE_PASS_VO_META, b'battlePass', _RECORD.PERSONAL))
BR_PERSONAL_STATS_BLOCK.addNextComponent(components.BattleRoyaleDailyBonusFactorBlock(_DAILY_BONUS_FACTOR_VO_META))
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
 (b'databaseID', 0, b'databaseID'),
 (b'prebattleID', 0, b'prebattleID')))
TEAM_ITEM_VO_META.bind(components.BattleRoyalePlayerBlock)
BR_TEAM_STATS_BLOCK = components.BattleRoyaleTeamStatsBlock(base.ListMeta(), b'leaderboard', _RECORD.VEHICLES)
