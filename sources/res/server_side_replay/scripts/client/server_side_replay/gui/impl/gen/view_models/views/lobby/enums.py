from enum import Enum, IntEnum

class ReplaysViews(IntEnum):
    BESTREPLAYS = 0
    MYREPLAYS = 1
    FINDREPLAY = 2


class TankmanLocation(Enum):
    INBARRACKS = b'in_barracks'
    INTANK = b'in_tank'
    DISMISSED = b'dismissed'
