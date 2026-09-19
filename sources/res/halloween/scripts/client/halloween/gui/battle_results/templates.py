from __future__ import absolute_import
from gui.battle_results.components import base
from gui.battle_results.components.details import GainCreditsValueInBattleItem
from gui.battle_results.components.progress import QuestsProgressBlock
from gui.battle_results.templates import regular
from halloween.gui.battle_results import components as ex
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
HW_TOTAL_VO_META = base.DictMeta({b'common': {}, b'hwPhase': 0, 
   b'hwPhasesCount': 0, 
   b'players': [], b'quests': None, 
   b'rewards': {}})
HW_TEAM_ITEM_VO_META = base.PropertyMeta((
 (b'playerDBID', 0, b'playerDBID'),
 (b'playerName', b'', b'playerName'),
 (b'vehicleName', b'', b'vehicleName'),
 (b'vehicleType', b'', b'vehicleType'),
 (b'vehicleCD', 0, b'vehicleCD'),
 (b'vehicleLvl', -1, b'vehicleLvl'),
 (b'clanAbbrev', b'', b'clanAbbrev'),
 (b'artefactKeys', 0, b'artefactKeys'),
 (
  b'isPlayer', False, b'isPlayer'),
 (b'squadID', 0, b'squadID'),
 (
  b'isOwnSquad', False, b'isOwnSquad'),
 (b'killerName', b'', b'killerName'),
 (b'deathReason', -1, b'deathReason'),
 (b'kills', 0, b'kills'),
 (b'damageDealt', 0, b'damageDealt'),
 (b'hwBossFightDamage', 0, b'hwBossFightDamage'),
 (b'badgeID', 0, b'badgeID'),
 (b'badgeSuffixID', 0, b'badgeSuffixID'),
 (b'hwVehiclesRespawnCount', 0, b'hwVehiclesRespawnCount'),
 (
  b'hasPenalties', False, b'hasPenalties'),
 (
  b'hwHangarLoot', {}, b'hwHangarLoot')))
HW_TEAM_ITEM_VO_META.bind(ex.HWVehicleStatsBlock)
HW_TOTAL_RESULTS_BLOCK = base.StatsBlock(HW_TOTAL_VO_META, b'hwVictoryData')
HW_PERSONAL_REWARDS_VO_META = base.DictMeta({b'credits': 0, 
   b'effectivenessKeys': 0, 
   b'bossKeys': 0, 
   b'hangarLoot': {}})
HW_PERSONAL_REWARDS_BLOCK = base.StatsBlock(HW_PERSONAL_REWARDS_VO_META, b'rewards')
HW_PERSONAL_REWARDS_BLOCK.addNextComponent(GainCreditsValueInBattleItem(b'credits', _RECORD.PERSONAL))
HW_PERSONAL_REWARDS_BLOCK.addNextComponent(ex.HwEffectivenessArtefactKeysItem(b'effectivenessKeys', _RECORD.PERSONAL))
HW_PERSONAL_REWARDS_BLOCK.addNextComponent(ex.HwBossArtefactKeysItem(b'bossKeys', _RECORD.PERSONAL))
HW_PERSONAL_REWARDS_BLOCK.addNextComponent(ex.HwHangarLoot(b'hangarLoot', _RECORD.PERSONAL))
HW_BATTLE_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone(7)
regular.FINISH_RESULT_VO_META.bind(ex.HWBattleFinishResultBlock)
HW_TOTAL_RESULTS_BLOCK.addNextComponent(HW_BATTLE_COMMON_STATS_BLOCK)
HW_BATTLE_COMMON_STATS_BLOCK.addComponent(7, ex.HWBattleFinishResultBlock())
HW_TOTAL_RESULTS_BLOCK.addNextComponent(ex.HwPhaseItem(b'hwPhase', _RECORD.PERSONAL))
HW_TOTAL_RESULTS_BLOCK.addNextComponent(ex.HwPhasesCountItem(b'hwPhasesCount', _RECORD.PERSONAL))
HW_TOTAL_RESULTS_BLOCK.addNextComponent(ex.HWBattlesTeamStatsBlock(base.ListMeta(), b'players', _RECORD.VEHICLES))
HW_TOTAL_RESULTS_BLOCK.addNextComponent(QuestsProgressBlock(base.ListMeta(), b'quests', _RECORD.PERSONAL))
HW_TOTAL_RESULTS_BLOCK.addNextComponent(HW_PERSONAL_REWARDS_BLOCK)
