from enum import Enum

class Features(str, Enum):
    METRICS = b'hangar_metrics'


class Groups(str, Enum):
    SPACE = b'space'
    VIEWS = b'views'


class LogActions(str, Enum):
    SPACE_DISPOSED = b'space_disposed'
