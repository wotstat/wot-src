from enum import Enum
from frameworks.wulf import ViewModel

class WTVehicleType(Enum):
    BOSS = b'boss'
    BOSS_2025 = b'boss_2025'
    BOSS_SPECIAL = b'boss_special'
    HUNTER = b'hunter'


class PortalType(Enum):
    HUNTER = b'hunter'
    BOSS = b'boss'
    TANK = b'tank'


class WtCommonConsts(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(WtCommonConsts, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(WtCommonConsts, self)._initialize()
        return
