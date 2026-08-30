from __future__ import absolute_import
from enum import Enum
FEATURE = b'ls_narration'
START_MARKER_KEY = b'start'
END_MARKER_KEY = b'end'
NARRATION_PREFIX = b'#ev_last_stand_quantum'

class NarrationLogAction(Enum):
    START = b'start'
    END = b'end'
