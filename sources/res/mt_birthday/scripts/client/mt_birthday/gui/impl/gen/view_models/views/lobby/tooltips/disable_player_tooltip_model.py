from enum import Enum
from frameworks.wulf import ViewModel

class DisabledReason(Enum):
    NOTAVAILABLE = b'notAvailable'
    BANNED = b'banned'
    BOT = b'bot'
    BLACKLIST = b'blackList'


class DisablePlayerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DisablePlayerTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getTime(self):
        return self._getNumber(0)

    def setTime(self, value):
        self._setNumber(0, value)
        return

    def getDisabledReason(self):
        return DisabledReason(self._getString(1))

    def setDisabledReason(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(DisablePlayerTooltipModel, self)._initialize()
        self._addNumberProperty(b'time', 0)
        self._addStringProperty(b'disabledReason')
        return
