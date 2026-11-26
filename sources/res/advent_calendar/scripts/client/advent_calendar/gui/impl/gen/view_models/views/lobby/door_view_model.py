from enum import Enum
from frameworks.wulf import ViewModel

class DoorState(Enum):
    CLOSED = b'closed'
    OPENED = b'opened'
    READY_TO_OPEN = b'readyToOpen'
    EXPIRED = b'expired'


class Mark(Enum):
    NONE = b'none'
    NY = b'ny'
    NY_EVENT = b'nyEvent'
    WDR = b'wdr'


class DoorViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(DoorViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDayId(self):
        return self._getNumber(0)

    def setDayId(self, value):
        self._setNumber(0, value)
        return

    def getDoorState(self):
        return DoorState(self._getString(1))

    def setDoorState(self, value):
        self._setString(1, value.value)
        return

    def getMark(self):
        return Mark(self._getString(2))

    def setMark(self, value):
        self._setString(2, value.value)
        return

    def getPrice(self):
        return self._getNumber(3)

    def setPrice(self, value):
        self._setNumber(3, value)
        return

    def getOpenTimeStamp(self):
        return self._getNumber(4)

    def setOpenTimeStamp(self, value):
        self._setNumber(4, value)
        return

    def getIsEnoughResources(self):
        return self._getBool(5)

    def setIsEnoughResources(self, value):
        self._setBool(5, value)
        return

    def getOpenAnimationRequired(self):
        return self._getBool(6)

    def setOpenAnimationRequired(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(DoorViewModel, self)._initialize()
        self._addNumberProperty(b'dayId', 0)
        self._addStringProperty(b'doorState', DoorState.CLOSED.value)
        self._addStringProperty(b'mark', Mark.NONE.value)
        self._addNumberProperty(b'price', 0)
        self._addNumberProperty(b'openTimeStamp', 0)
        self._addBoolProperty(b'isEnoughResources', False)
        self._addBoolProperty(b'openAnimationRequired', False)
        return
