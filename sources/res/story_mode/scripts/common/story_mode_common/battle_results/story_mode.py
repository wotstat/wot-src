from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from story_mode_common.story_mode_constants import MissionId
BATTLE_RESULTS = [
 (
  b'missionId', int, MissionId.UNDEFINED, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'isForceOnboarding', bool, False, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'rewards', None, None, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'progressionInfo', None, None, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF)]
