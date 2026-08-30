from gui.battle_results.components import base
from gui.battle_results.components.common import ArenaDurationItem, ArenaDateTimeItem
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from story_mode.gui.battle_results.components import FinishResultItem, FinishReasonItem, MissionIdItem, VehicleNameItem, VehicleBlock, IsForceOnboardingItem
_STORY_MODE_VO_META = base.DictMeta({b'finishResult': b'', 
   b'finishReason': None, 
   b'missionId': 1, 
   b'isForceOnboarding': False, 
   b'arenaDuration': b'', 
   b'arenaDateTime': b'', 
   b'vehicleName': b'', 
   b'vehicle': {}})
_VEHICLE_VO_META = base.DictMeta({b'deathReason': (-1), 
   b'damageDealt': 0, 
   b'kills': 0, 
   b'damageAssisted': 0, 
   b'damageBlockedByArmor': 0})
STORY_MODE_RESULTS_BLOCK = base.StatsBlock(_STORY_MODE_VO_META, b'')
STORY_MODE_RESULTS_BLOCK.addNextComponent(FinishResultItem(b'finishResult', _RECORD.PERSONAL))
STORY_MODE_RESULTS_BLOCK.addNextComponent(FinishReasonItem(b'finishReason', _RECORD.PERSONAL))
STORY_MODE_RESULTS_BLOCK.addNextComponent(MissionIdItem(b'missionId', _RECORD.PERSONAL))
STORY_MODE_RESULTS_BLOCK.addNextComponent(IsForceOnboardingItem(b'isForceOnboarding', _RECORD.PERSONAL))
STORY_MODE_RESULTS_BLOCK.addNextComponent(ArenaDurationItem(b'arenaDuration', _RECORD.COMMON, b'duration'))
STORY_MODE_RESULTS_BLOCK.addNextComponent(ArenaDateTimeItem(b'arenaDateTime', _RECORD.COMMON, b'arenaCreateTime'))
STORY_MODE_RESULTS_BLOCK.addNextComponent(VehicleNameItem(b'vehicleName'))
STORY_MODE_RESULTS_BLOCK.addNextComponent(VehicleBlock(_VEHICLE_VO_META, b'vehicle'))
