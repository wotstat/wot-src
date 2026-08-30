from enum import Enum
from frameworks.wulf import ViewModel

class FrontlineState(Enum):
    ANNOUNCE = b'announce'
    ACTIVE = b'active'
    FINISHED = b'finished'
    FROZEN = b'frozen'
    INTRO = b'intro'


class FrontlineConst(ViewModel):
    __slots__ = ()
    BATTLE_ABILITIES = b'battleAbilities'

    def __init__(self, properties=0, commands=0):
        super(FrontlineConst, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(FrontlineConst, self)._initialize()
        return
