from enum import Enum
from frameworks.wulf import ViewModel

class EventState(Enum):
    NOTSTARTED = b'notStarted'
    FORBIDDEN = b'forbidden'
    PAUSED = b'paused'
    REGULARREWARDAVAILABLE = b'regularRewardAvailable'
    TOPREWARDAVAILABLE = b'topRewardAvailable'
    NOREWARDS = b'noRewards'
    REGULARREWARDRECEIVED = b'regularRewardReceived'
    TOPREWARDRECEIVED = b'topRewardReceived'


class EntryPointTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(EntryPointTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)
        return

    def getStartDate(self):
        return self._getNumber(1)

    def setStartDate(self, value):
        self._setNumber(1, value)
        return

    def getEndDate(self):
        return self._getNumber(2)

    def setEndDate(self, value):
        self._setNumber(2, value)
        return

    def getTimeLeft(self):
        return self._getNumber(3)

    def setTimeLeft(self, value):
        self._setNumber(3, value)
        return

    def getIsEventEndingSoon(self):
        return self._getBool(4)

    def setIsEventEndingSoon(self, value):
        self._setBool(4, value)
        return

    def getRewardCount(self):
        return self._getNumber(5)

    def setRewardCount(self, value):
        self._setNumber(5, value)
        return

    def getEventState(self):
        return EventState(self._getString(6))

    def setEventState(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(EntryPointTooltipModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'timeLeft', 0)
        self._addBoolProperty(b'isEventEndingSoon', False)
        self._addNumberProperty(b'rewardCount', 0)
        self._addStringProperty(b'eventState')
        return
