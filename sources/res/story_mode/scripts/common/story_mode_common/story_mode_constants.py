from __future__ import absolute_import
import enum, constants
from constants import ARENA_BONUS_TYPE, ARENA_GUI_TYPE
from constants_utils import ConstInjector
EXTENSION_NAME = b'story_mode'
LOGGER_NAME = b'story_mode'
DEFAULT_BATTLES_LIMIT = 500
MM_STORY_MODE_STATS_KEY = b'stats/story_mode/'
BATTLES_LIMIT_KEY = MM_STORY_MODE_STATS_KEY + b'battlesLimit'
SM_CONGRATULATIONS_MESSAGE = b'StoryModeCongratulationsMessage'
STORY_MODE_BONUS_TYPES = (
 ARENA_BONUS_TYPE.STORY_MODE_ONBOARDING, ARENA_BONUS_TYPE.STORY_MODE_REGULAR)
STORY_MODE_GUI_TYPE_BY_BONUS_TYPE = {(ARENA_BONUS_TYPE.STORY_MODE_ONBOARDING): (ARENA_GUI_TYPE.STORY_MODE_ONBOARDING), 
   (ARENA_BONUS_TYPE.STORY_MODE_REGULAR): (ARENA_GUI_TYPE.STORY_MODE_REGULAR)}
VEHICLE_BUNKER_TURRET_TAG = b'bunkerTurret'

class PRIORITY(enum.IntEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2


@enum.unique
class MissionsDifficulty(str, enum.Enum):
    UNDEFINED = b''
    NORMAL = b'normal'
    HARD = b'hard'
    VERY_HARD = b'very_hard'


class EventMissionSelector(str, enum.Enum):
    DEFAULT = b'default'
    WITH_UNLOCK_MISSION = b'withUnlockMission'
    BATTLES_COUNT = b'battlesCount'


class MissionType(str, enum.Enum):
    ONBOARDING = b'onboarding'
    REGULAR = b'regular'
    EVENT = b'event'


class AwarenessState(enum.IntEnum):
    SPOTTED = 0
    SPOTTING = 1
    NOT_SPOTTED = 2


PROGRESS_PDATA_KEY = b'progress'
STORY_MODE_PDATA_KEY = b'storyMode'
LONG_INT_HALF_SHIFT = 32
STORY_MODE_AB_FEATURE = b'storyMode'
DISABLE_REGULAR_OPERATIONS = b'disableRegularOperations'
RECON_ABILITY = b'smn_recon_ability'
DISTRACTION_ABILITY = b'smn_distraction_ability'
SCC_AIRSTRIKE_ABILITY = b'sm_scc_airstrike'
SCC_AIRSTRIKE_ABILITY_HARD = b'sm_scc_airstrike_hard'
PLAYER_TEAM = 1
DEFAULT_SPAWN_GROUP = 0

class EQUIPMENT_STAGES(constants.EQUIPMENT_STAGES, ConstInjector):
    ACTIVATING = 101
    DEACTIVATING = 102


class MissionLockCondition(str, enum.Enum):
    BY_MISSION = b'byMission'
    BATTLES_COUNT = b'battlesCount'


class MissionId(enum.IntEnum):
    UNDEFINED = -1
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7


class TaskId(enum.IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


class MM_STORY_MODE_STATS(object):
    PLAYERS_COUNT_KEY = MM_STORY_MODE_STATS_KEY + b'Queue{}Players'
    BATTLES_COUNT_KEY = MM_STORY_MODE_STATS_KEY + b'Queue{}PlayerBattlesCount'
    AVG_WAIT_TIME_KEY = MM_STORY_MODE_STATS_KEY + b'Queue{}AvgWaitTime'
    ALL = (
     PLAYERS_COUNT_KEY, BATTLES_COUNT_KEY, AVG_WAIT_TIME_KEY)
