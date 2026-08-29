from enum import Enum
from frameworks.wulf import ViewModel

class StatusEnum(Enum):
    ANNOUNCE = b'announce'
    ACTIVE = b'active'
    DISABLED = b'disabled'


class PhaseEnum(Enum):
    LOOTBOX = b'lootbox'
    SPECIAL = b'special'


class BlackMarketViewModel(ViewModel):
    __slots__ = (b'toBlackMarketEvent',)

    def __init__(self, properties=5, commands=1):
        super(BlackMarketViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAloneBanner(self):
        return self._getBool(0)

    def setIsAloneBanner(self, value):
        self._setBool(0, value)
        return

    def getIsNew(self):
        return self._getBool(1)

    def setIsNew(self, value):
        self._setBool(1, value)
        return

    def getTimer(self):
        return self._getNumber(2)

    def setTimer(self, value):
        self._setNumber(2, value)
        return

    def getStatus(self):
        return StatusEnum(self._getString(3))

    def setStatus(self, value):
        self._setString(3, value.value)
        return

    def getEventPhase(self):
        return PhaseEnum(self._getString(4))

    def setEventPhase(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(BlackMarketViewModel, self)._initialize()
        self._addBoolProperty(b'isAloneBanner', False)
        self._addBoolProperty(b'isNew', False)
        self._addNumberProperty(b'timer', 123456789)
        self._addStringProperty(b'status', StatusEnum.ACTIVE.value)
        self._addStringProperty(b'eventPhase', PhaseEnum.SPECIAL.value)
        self.toBlackMarketEvent = self._addCommand(b'toBlackMarketEvent')
        return
