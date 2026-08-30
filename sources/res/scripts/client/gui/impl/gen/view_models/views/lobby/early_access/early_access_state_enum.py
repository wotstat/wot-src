from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    ACTIVE = b'active'
    POSTPROGRESSION = b'postProgression'
    BUY = b'buy'
    COMPLETED = b'completed'


class EarlyAccessStateEnum(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(EarlyAccessStateEnum, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(EarlyAccessStateEnum, self)._initialize()
        return
