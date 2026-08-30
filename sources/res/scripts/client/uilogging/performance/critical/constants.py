from enum import Enum

class Features(str, Enum):
    MEMORY_CRITICAL = b'memory_critical'


class Groups(str, Enum):
    EVENT = b'event'


class LogActions(str, Enum):
    MEMORY_CRITICAL_EVENT = b'memory_critical_event'
