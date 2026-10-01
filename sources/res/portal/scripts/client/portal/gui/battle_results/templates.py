from gui.battle_results.components import base
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.impl.gen import R
from portal.gui.battle_results import components as ex
from portal.gui.battle_results.components import StatsItemBlock, StatsBlock
PORTAL_TOTAL_VO_META = base.DictMeta({b'results': {}, b'reusable': {}, b'common': {}, b'personal': {}, b'leaderboard': {}, b'progressionTokens': 0, 
   b'vehicleExperience': 0, 
   b'portalBattleLevel': 0, 
   b'portalWaveCount': 0, 
   b'portalCurrentWave': 0})
PORTAL_TOTAL_RESULTS_BLOCK = base.StatsBlock(PORTAL_TOTAL_VO_META, b'victoryData')
PORTAL_TOTAL_RESULTS_BLOCK.addNextComponent(ex.ProgressionTokensItem(b'progressionTokens', _RECORD.PERSONAL))
PORTAL_TOTAL_RESULTS_BLOCK.addNextComponent(ex.VehicleExperienceItem(b'vehicleExperience', _RECORD.PERSONAL))
PORTAL_TOTAL_RESULTS_BLOCK.addNextComponent(ex.BattleLevelItem(b'portalBattleLevel', _RECORD.PERSONAL))
PORTAL_TOTAL_RESULTS_BLOCK.addNextComponent(ex.CurrentWaveItem(b'portalCurrentWave', _RECORD.PERSONAL))
PORTAL_TOTAL_RESULTS_BLOCK.addNextComponent(ex.WaveCountItem(b'portalWaveCount', _RECORD.PERSONAL))
STAT_ITEM_VO_META = base.PropertyMeta((
 (b'type', b'', b'type'),
 (b'value', 0, b'value'),
 (
  b'wreathImage', R.invalid(), b'wreathImage')))
STAT_ITEM_VO_META.bind(StatsItemBlock)
PERSONAL_VO_META = base.DictMeta({b'stats': []})
PERSONAL_STATS_BLOCK = base.StatsBlock(PERSONAL_VO_META, b'personal')
PERSONAL_STATS_BLOCK.addNextComponent(StatsBlock(base.ListMeta(), b'stats'))
TEAM_ITEM_VO_META = base.PropertyMeta((
 (
  b'isPersonal', False, b'isPersonal'),
 (
  b'isSquadMode', False, b'isSquadMode'),
 (b'squadIdx', 0, b'squadIdx'),
 (b'place', 0, b'place'),
 (b'userName', b'', b'userName'),
 (b'hiddenName', b'', b'hiddenName'),
 (b'clanAbbrev', b'', b'clanAbbrev'),
 (b'vehicleName', b'', b'vehicleName'),
 (b'vehicleType', b'', b'vehicleType'),
 (b'damage', 0, b'damage'),
 (b'damageBlocked', 0, b'damageBlocked'),
 (b'kills', 0, b'kills'),
 (b'databaseID', 0, b'databaseID')))
TEAM_ITEM_VO_META.bind(ex.PlayerBlock)
TEAM_STATS_BLOCK = ex.TeamStatsBlock(base.ListMeta(), b'leaderboard', _RECORD.VEHICLES)
