from enum import Enum
from frameworks.wulf import ViewModel

class NyCurrencyType(Enum):
    MANDARIN = b'ny_mandarin'
    NYGIFTMACHINETOKEN = b'nyGiftMachineToken'
    NYLOOTBOXFRAGMENT = b'nyLootboxFragment'
    GOLD = b'gold'
    CREDITS = b'credits'


class NyCurrencyTypeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NyCurrencyTypeModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return NyCurrencyType(self._getString(0))

    def setValue(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(NyCurrencyTypeModel, self)._initialize()
        self._addStringProperty(b'value', NyCurrencyType.MANDARIN.value)
        return
