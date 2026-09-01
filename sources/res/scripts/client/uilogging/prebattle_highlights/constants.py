from enum import Enum
FEATURE = b'prebattle_highlights'

class PrebattleHighlightsLogAction(Enum):
    VIEWED = b'viewed'
    COLLAPSE = b'collapse'


class PrebattleHighlightsLogKeys(Enum):
    PBH = b'pbh'
    PBH_OUT_OF_FOCUS = b'pbh_out_of_focus'
    FULLY_VIEWED = b'fully_viewed'
    ESC = b'esc'
    SETTINGS_PBH = b'settings_pbh'
    SETTINGS_HISTORICAL = b'settings_historical'
    NOT_ENOUGH_TIME = b'not_enough_time'
