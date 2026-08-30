from enum import IntEnum
from frameworks.wulf import ViewModel

class RoverEnum(IntEnum):
    OLD = 1
    NEW = 2


class QueueViewModel(ViewModel):
    __slots__ = (b'onLeave',)

    def __init__(self, properties=5, commands=1):
        super(QueueViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getPlayersInQueue(self):
        return self._getNumber(0)

    def setPlayersInQueue(self, value):
        self._setNumber(0, value)
        return

    def getOldRoverQueue(self):
        return self._getNumber(1)

    def setOldRoverQueue(self, value):
        self._setNumber(1, value)
        return

    def getNewRoverQueue(self):
        return self._getNumber(2)

    def setNewRoverQueue(self, value):
        self._setNumber(2, value)
        return

    def getSelectedVehicleResource(self):
        return self._getString(3)

    def setSelectedVehicleResource(self, value):
        self._setString(3, value)
        return

    def getVehicle(self):
        return RoverEnum(self._getNumber(4))

    def setVehicle(self, value):
        self._setNumber(4, value.value)
        return

    def _initialize(self):
        super(QueueViewModel, self)._initialize()
        self._addNumberProperty(b'playersInQueue', 0)
        self._addNumberProperty(b'oldRoverQueue', 0)
        self._addNumberProperty(b'newRoverQueue', 0)
        self._addStringProperty(b'selectedVehicleResource', b'')
        self._addNumberProperty(b'vehicle', RoverEnum.OLD.value)
        self.onLeave = self._addCommand(b'onLeave')
        return
