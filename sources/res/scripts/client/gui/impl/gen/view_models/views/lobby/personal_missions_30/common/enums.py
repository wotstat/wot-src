from enum import Enum

class MissionCategory(Enum):
    ASSAULT = b'assault'
    SNIPER = b'sniper'
    SUPPORT = b'support'


class OperationState(Enum):
    COMPLETED_WITH_HONORS = b'completedWithHonors'
    COMPLETED = b'completed'
    ACTIVE = b'active'
    AVAILABLE = b'available'
    UNAVAILABLE = b'unavailable'
    LOCKED = b'locked'


class ParamTooltipType(Enum):
    PROGRESSION = b'progression'
    PM3_POINTS = b'pm3_points'
    CUSTOM_SIMPLE = b'custom_simple'
