from enum import Enum
from frameworks.wulf import ViewModel

class MissionStatus(Enum):
    AVAILABLE = b'available'
    AVAILABLEPAUSED = b'availablePaused'
    ACTIVE = b'active'
    ACTIVEPAUSED = b'activePaused'
    DISABLED = b'disabled'
    DISABLEDPAUSED = b'disabledPaused'
    COMPLETED = b'completed'
    COMPLETEDPERFECTLY = b'completedPerfectly'
    COMPLETEDPAUSED = b'completedPaused'


class LastMissionStatus(Enum):
    DEVELOPMENT = b'development'
    DISABLED = b'disabled'
    ACTIVE = b'active'
    COMPLETED = b'completed'


class Pm3OperationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(Pm3OperationModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getOperationId(self):
        return self._getNumber(1)

    def setOperationId(self, value):
        self._setNumber(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getLevel(self):
        return self._getString(3)

    def setLevel(self, value):
        self._setString(3, value)
        return

    def getTypeIcon(self):
        return self._getString(4)

    def setTypeIcon(self, value):
        self._setString(4, value)
        return

    def getTotalQuests(self):
        return self._getNumber(5)

    def setTotalQuests(self, value):
        self._setNumber(5, value)
        return

    def getCompletedQuests(self):
        return self._getNumber(6)

    def setCompletedQuests(self, value):
        self._setNumber(6, value)
        return

    def getDelta(self):
        return self._getNumber(7)

    def setDelta(self, value):
        self._setNumber(7, value)
        return

    def getStatus(self):
        return MissionStatus(self._getString(8))

    def setStatus(self, value):
        self._setString(8, value.value)
        return

    def getVehicleName(self):
        return self._getString(9)

    def setVehicleName(self, value):
        self._setString(9, value)
        return

    def getIsElite(self):
        return self._getBool(10)

    def setIsElite(self, value):
        self._setBool(10, value)
        return

    def getPrevOperationName(self):
        return self._getString(11)

    def setPrevOperationName(self, value):
        self._setString(11, value)
        return

    def getIsHasLevels(self):
        return self._getBool(12)

    def setIsHasLevels(self, value):
        self._setBool(12, value)
        return

    def _initialize(self):
        super(Pm3OperationModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'operationId', 0)
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'level', b'')
        self._addStringProperty(b'typeIcon', b'')
        self._addNumberProperty(b'totalQuests', 0)
        self._addNumberProperty(b'completedQuests', 0)
        self._addNumberProperty(b'delta', 0)
        self._addStringProperty(b'status')
        self._addStringProperty(b'vehicleName', b'')
        self._addBoolProperty(b'isElite', False)
        self._addStringProperty(b'prevOperationName', b'')
        self._addBoolProperty(b'isHasLevels', True)
        return
