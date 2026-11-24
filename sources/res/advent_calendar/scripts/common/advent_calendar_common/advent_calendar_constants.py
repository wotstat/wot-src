GAME_PARAMS_KEY = b'advent_calendar_config'
ADVENT_POINTS_TOKEN = b'advent:points'

class DoorMarkType(object):
    WDR = b'wdr'
    NY_START = b'ny_start'
    NY_MODE = b'ny_mode'
    NONE = b'none'
    RANGE = [
     WDR, NY_START, NY_MODE]
