from enum import Enum
from frameworks.wulf import ViewModel

class BankState(Enum):
    AVAILABLE = b'available'
    ACTIVE = b'active'
    DISABLE = b'disable'


class PiggyBankStates(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(PiggyBankStates, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(PiggyBankStates, self)._initialize()
        return
