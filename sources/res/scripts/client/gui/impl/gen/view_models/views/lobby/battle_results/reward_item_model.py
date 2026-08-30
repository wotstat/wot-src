from enum import Enum
from frameworks.wulf import ViewModel

class RewardTypes(Enum):
    CREDITS = b'credits'
    CRYSTALS = b'crystal'
    XP = b'xp'


class RewardItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(RewardItemModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'value', 0)
        return
