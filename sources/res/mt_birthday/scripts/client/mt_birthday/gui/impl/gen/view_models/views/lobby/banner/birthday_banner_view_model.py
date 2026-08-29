from enum import Enum
from frameworks.wulf import ViewModel

class StatusEnum(Enum):
    ACTIVE = b'active'
    ENDING = b'ending'
    DISABLED = b'disabled'


class BirthdayBannerViewModel(ViewModel):
    __slots__ = (b'toBirthdayEvent',)

    def __init__(self, properties=3, commands=1):
        super(BirthdayBannerViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAloneBanner(self):
        return self._getBool(0)

    def setIsAloneBanner(self, value):
        self._setBool(0, value)
        return

    def getTimer(self):
        return self._getNumber(1)

    def setTimer(self, value):
        self._setNumber(1, value)
        return

    def getStatus(self):
        return StatusEnum(self._getString(2))

    def setStatus(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(BirthdayBannerViewModel, self)._initialize()
        self._addBoolProperty(b'isAloneBanner', False)
        self._addNumberProperty(b'timer', 123456789)
        self._addStringProperty(b'status', StatusEnum.ACTIVE.value)
        self.toBirthdayEvent = self._addCommand(b'toBirthdayEvent')
        return
