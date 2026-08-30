from enum import Enum, IntEnum
from frameworks.wulf import ViewModel

class PingStatus(IntEnum):
    REQUESTED = 0
    HIGH = 1
    NORM = 2
    LOW = 3


class ColorBlindMode(Enum):
    DISABLED = b'disabled'
    PROTANOPIA = b'protanopia'


class ServerInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ServerInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getServerName(self):
        return self._getString(0)

    def setServerName(self, value):
        self._setString(0, value)
        return

    def getStatus(self):
        return PingStatus(self._getNumber(1))

    def setStatus(self, value):
        self._setNumber(1, value.value)
        return

    def getColorBlind(self):
        return ColorBlindMode(self._getString(2))

    def setColorBlind(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(ServerInfoModel, self)._initialize()
        self._addStringProperty(b'serverName', b'')
        self._addNumberProperty(b'status')
        self._addStringProperty(b'colorBlind')
        return
