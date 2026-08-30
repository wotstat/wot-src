from enum import Enum
DEFAULT_LOGGER_NAME = b'UI_LOG'

class LogLevels(object):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30


class CommonLogActions(str, Enum):
    CLICK = b'click'
    KEYDOWN = b'keydown'
