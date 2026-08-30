from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    NONE = b'none'
    NOVEHICLES = b'noVehicles'
    CEASEFIREAVAILABLE = b'ceasefireAvailable'
    CEASEFIREUNAVAILABLE = b'ceasefireUnavailable'
    MODEOFFLINE = b'modeOffline'


class AlertMessageModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=1, commands=1):
        super(AlertMessageModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(AlertMessageModel, self)._initialize()
        self._addStringProperty(b'state')
        self.onClick = self._addCommand(b'onClick')
        return
