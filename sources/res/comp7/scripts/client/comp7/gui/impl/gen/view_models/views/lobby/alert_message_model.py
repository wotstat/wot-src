from enum import Enum
from frameworks.wulf import Array, ViewModel

class State(Enum):
    NONE = b'none'
    BAN = b'ban'
    PREANNOUNCE = b'preannounce'
    NOVEHICLES = b'noVehicles'
    NOTENOUGHVEHICLES = b'notEnoughVehicles'
    QUALIFICATION = b'qualification'
    CEASEFIREAVAILABLE = b'ceasefireAvailable'
    CEASEFIREUNAVAILABLE = b'ceasefireUnavailable'
    MODEOFFLINE = b'modeOffline'
    SEASONEND = b'seasonEnd'


class AlertMessageModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=5, commands=1):
        super(AlertMessageModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getBanTimeleftInSeconds(self):
        return self._getNumber(1)

    def setBanTimeleftInSeconds(self, value):
        self._setNumber(1, value)
        return

    def getStartEventDateTime(self):
        return self._getString(2)

    def setStartEventDateTime(self, value):
        self._setString(2, value)
        return

    def getLevels(self):
        return self._getArray(3)

    def setLevels(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getLevelsType():
        return int

    def getMinVehiclesRequired(self):
        return self._getNumber(4)

    def setMinVehiclesRequired(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(AlertMessageModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'banTimeleftInSeconds', 0)
        self._addStringProperty(b'startEventDateTime', b'')
        self._addArrayProperty(b'levels', Array())
        self._addNumberProperty(b'minVehiclesRequired', 0)
        self.onClick = self._addCommand(b'onClick')
        return
