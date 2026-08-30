import enum, constants
from constants_utils import ConstInjector
EXTENSION_NAME = b'story_mode'
LOGGER_NAME = b'story_mode'
DEFAULT_BATTLES_LIMIT = 500
BATTLES_LIMIT_KEY = b'stats/story_mode/battlesLimit'
PLAYERS_COUNT_KEY = b'stats/story_mode/Queue{}Players'
PLAYER_BATTLES_COUNT_KEY = b'stats/story_mode/Queue{}PlayerBattlesCount'
AVG_WAIT_TIME_KEY = b'stats/story_mode/Queue{}AvgWaitTime'
SM_CONGRATULATIONS_MESSAGE = b'StoryModeCongratulationsMessage'
STORY_MODE_GAME_PARAMS_KEY = b'story_mode_settings'

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    STORY_MODE = 100


class ARENA_BONUS_TYPE(constants.ARENA_BONUS_TYPE, ConstInjector):
    STORY_MODE = 100


class QUEUE_TYPE(constants.QUEUE_TYPE, ConstInjector):
    STORY_MODE = 100


class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    STORY_MODE = 100


class FINISH_REASON(constants.FINISH_REASON, ConstInjector):
    AFK = 101


class PRIORITY(enum.IntEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2


PROGRESS_PDATA_KEY = b'progress'
STORY_MODE_PDATA_KEY = b'storyMode'
UNDEFINED_MISSION_ID = -1
FIRST_MISSION_ID = 1
