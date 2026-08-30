from __future__ import absolute_import
from gui.battle_results.components import base
from gui.battle_results.components.details import GainCreditsValueInBattleItem
from gui.battle_results.components.progress import QuestsProgressBlock
from gui.battle_results.templates import regular
from last_stand.gui.battle_results import components as ex
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
LS_TOTAL_VO_META = base.DictMeta({b'common': {}, b'phase': 0, 
   b'phasesCount': 0, 
   b'players': [], b'quests': None, 
   b'rewards': {}, b'prevBestMissionsCount': 0, 
   b'time': (-1), 
   b'completedDifficultyMissions': [], b'geometryId': 0})
LS_TEAM_ITEM_VO_META = base.PropertyMeta((
 (b'playerDBID', 0, b'playerDBID'),
 (b'playerName', b'', b'playerName'),
 (b'vehicleName', b'', b'vehicleName'),
 (b'vehicleShortName', b'', b'vehicleShortName'),
 (b'vehicleIsIGR', b'', b'vehicleIsIGR'),
 (b'vehicleType', b'', b'vehicleType'),
 (b'vehicleCD', 0, b'vehicleCD'),
 (b'vehicleLvl', -1, b'vehicleLvl'),
 (b'clanAbbrev', b'', b'clanAbbrev'),
 (b'progressPoints', 0, b'progressPoints'),
 (
  b'isPlayer', False, b'isPlayer'),
 (b'squadID', 0, b'squadID'),
 (
  b'isOwnSquad', False, b'isOwnSquad'),
 (b'killerName', b'', b'killerName'),
 (b'deathReason', -1, b'deathReason'),
 (b'kills', 0, b'kills'),
 (b'damageDealt', 0, b'damageDealt'),
 (b'badgeID', 0, b'badgeID'),
 (b'badgeSuffixID', 0, b'badgeSuffixID'),
 (b'respawnsCount', 0, b'respawnsCount'),
 (
  b'hasPenalties', False, b'hasPenalties')))
LS_TEAM_ITEM_VO_META.bind(ex.LSVehicleStatsBlock)
LS_TOTAL_RESULTS_BLOCK = base.StatsBlock(LS_TOTAL_VO_META, b'lsVictoryData')
LS_PERSONAL_REWARDS_VO_META = base.DictMeta({b'credits': 0, 
   b'effectivenessPoints': 0, 
   b'obeliskPoints': 0})
LS_PERSONAL_REWARDS_BLOCK = base.StatsBlock(LS_PERSONAL_REWARDS_VO_META, b'rewards')
LS_PERSONAL_REWARDS_BLOCK.addNextComponent(GainCreditsValueInBattleItem(b'credits', _RECORD.PERSONAL))
LS_PERSONAL_REWARDS_BLOCK.addNextComponent(ex.LSEffectivenessPointsItem(b'effectivenessPoints', _RECORD.PERSONAL))
LS_PERSONAL_REWARDS_BLOCK.addNextComponent(ex.LSObeliskPointsItem(b'obeliskPoints', _RECORD.PERSONAL))
LS_BATTLE_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone(7)
regular.FINISH_RESULT_VO_META.bind(ex.LSBattleFinishResultBlock)
LS_TOTAL_RESULTS_BLOCK.addNextComponent(LS_BATTLE_COMMON_STATS_BLOCK)
LS_BATTLE_COMMON_STATS_BLOCK.addComponent(7, ex.LSBattleFinishResultBlock())
LS_TOTAL_RESULTS_BLOCK.addNextComponent(ex.LSGeometryIdItem(b'geometryId', _RECORD.COMMON))
LS_TOTAL_RESULTS_BLOCK.addNextComponent(ex.LSPrevBestMissionsCountItem(b'prevBestMissionsCount', _RECORD.PERSONAL))
LS_TOTAL_RESULTS_BLOCK.addNextComponent(ex.LSTimeItem(b'time', _RECORD.COMMON, b'duration'))
LS_TOTAL_RESULTS_BLOCK.addNextComponent(ex.LSCompletedDifficultyMissions(b'completedDifficultyMissions', _RECORD.PERSONAL))
LS_TOTAL_RESULTS_BLOCK.addNextComponent(ex.LSPhaseItem(b'phase', _RECORD.PERSONAL))
LS_TOTAL_RESULTS_BLOCK.addNextComponent(ex.LSPhasesCountItem(b'phasesCount', _RECORD.PERSONAL))
LS_TOTAL_RESULTS_BLOCK.addNextComponent(ex.LSBattlesTeamStatsBlock(base.ListMeta(), b'players', _RECORD.VEHICLES))
LS_TOTAL_RESULTS_BLOCK.addNextComponent(QuestsProgressBlock(base.ListMeta(), b'quests', _RECORD.PERSONAL))
LS_TOTAL_RESULTS_BLOCK.addNextComponent(LS_PERSONAL_REWARDS_BLOCK)
