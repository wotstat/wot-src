from enum import Enum
from frameworks.wulf import ViewModel

class KPITypes(Enum):
    BATTLES = b'battles'
    ASSISTANCE = b'assistance'
    DESTROYED = b'destroyed'
    BLOCKED = b'blocked'
    EXPERIENCE = b'experience'
    DAMAGE = b'damage'


class AchievementsConstants(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(AchievementsConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(AchievementsConstants, self)._initialize()
        return
