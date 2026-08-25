from enum import Enum

class Features(str, Enum):
    METRICS = b'battle_metrics'


class Groups(str, Enum):
    SESSION = b'session'
    SYSTEM = b'system'


class LogActions(str, Enum):
    SPACE_DONE = b'space_done'
