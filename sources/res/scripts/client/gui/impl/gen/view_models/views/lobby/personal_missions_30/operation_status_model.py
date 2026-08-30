from enum import Enum
from frameworks.wulf import ViewModel

class OperationStatus(Enum):
    CAMPAIGN_FINISHED = b'campaignFinished'
    NOT_ALL_COMPLETED = b'notAllCompleted'
    NOT_ALL_COMPLETED_WITH_HONOR = b'notAllCompletedWithHonor'
    PAUSED = b'paused'
    NEXT_OPERATION_AVAILABLE = b'nextOperationAvailable'
    COMPLETED = b'completed'
    PRECEDING_OPERATION_NOT_COMPLETED = b'precedingOperationNotCompleted'
    REQUIRES_VEHICLE = b'requiresVehicle'
    VEHICLE_IS_IN_BATTLE = b'vehicleIsInBattle'
    ACTIVE = b'active'
    AVAILABLE = b'available'


class OperationStatusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(OperationStatusModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatus(self):
        return OperationStatus(self._getString(0))

    def setStatus(self, value):
        self._setString(0, value.value)
        return

    def getRequiredVehicleLevel(self):
        return self._getNumber(1)

    def setRequiredVehicleLevel(self, value):
        self._setNumber(1, value)
        return

    def getCurrentOperationId(self):
        return self._getNumber(2)

    def setCurrentOperationId(self, value):
        self._setNumber(2, value)
        return

    def getNextOperationName(self):
        return self._getString(3)

    def setNextOperationName(self, value):
        self._setString(3, value)
        return

    def getCurrentOperationName(self):
        return self._getString(4)

    def setCurrentOperationName(self, value):
        self._setString(4, value)
        return

    def getOperationIdToPerform(self):
        return self._getNumber(5)

    def setOperationIdToPerform(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(OperationStatusModel, self)._initialize()
        self._addStringProperty(b'status')
        self._addNumberProperty(b'requiredVehicleLevel', 0)
        self._addNumberProperty(b'currentOperationId', 0)
        self._addStringProperty(b'nextOperationName', b'')
        self._addStringProperty(b'currentOperationName', b'')
        self._addNumberProperty(b'operationIdToPerform', 0)
        return
