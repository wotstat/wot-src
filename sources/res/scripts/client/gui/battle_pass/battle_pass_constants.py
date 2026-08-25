from __future__ import absolute_import
from enum import Enum, unique
MIN_LEVEL = 1

class BonusesLayoutConsts(object):
    PRIORITY_KEY = b'priority'
    VISIBILITY_KEY = b'isVisible'
    OVERRIDE_KEY = b'override'
    ID_KEY = b'id'
    LEVEL_KEY = b'level'
    BIG_ICON_KEY = b'bigIcon'
    RARITY = b'rarity'
    MAIN_KEYS = (
     PRIORITY_KEY, VISIBILITY_KEY, BIG_ICON_KEY)
    INT_VALUES = (PRIORITY_KEY,)
    BOOL_VALUES = (VISIBILITY_KEY,)


@unique
class ChapterState(Enum):
    ACTIVE = b'active'
    PAUSED = b'paused'
    COMPLETED = b'completed'
    NOT_STARTED = b'notStarted'
