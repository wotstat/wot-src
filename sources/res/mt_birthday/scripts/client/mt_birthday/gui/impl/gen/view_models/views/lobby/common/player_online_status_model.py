from enum import Enum
from frameworks.wulf import ViewModel

class PlayerOnlineStatus(Enum):
    ONLINE = b'online'
    OFFLINE = b'offline'
    IN_BATTLE = b'inBattle'


class PlayerOnlineStatusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(PlayerOnlineStatusModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatus(self):
        return PlayerOnlineStatus(self._getString(0))

    def setStatus(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(PlayerOnlineStatusModel, self)._initialize()
        self._addStringProperty(b'status', PlayerOnlineStatus.OFFLINE.value)
        return
