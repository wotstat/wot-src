from enum import Enum
from frameworks.wulf import ViewModel

class TooltipChapterState(Enum):
    ACTIVE = b'active'
    COMPLETED = b'completed'
    NOTAVAILABLE = b'notAvailable'
    POSTPROGRESSION = b'postProgression'
    LOCKED = b'locked'


class EarlyAccessTooltipChapterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(EarlyAccessTooltipChapterModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getState(self):
        return TooltipChapterState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getCompletedQuests(self):
        return self._getNumber(2)

    def setCompletedQuests(self, value):
        self._setNumber(2, value)
        return

    def getTotalQuests(self):
        return self._getNumber(3)

    def setTotalQuests(self, value):
        self._setNumber(3, value)
        return

    def getAnnouncementTimestamp(self):
        return self._getNumber(4)

    def setAnnouncementTimestamp(self, value):
        self._setNumber(4, value)
        return

    def getLockedUntilQuestsComplete(self):
        return self._getNumber(5)

    def setLockedUntilQuestsComplete(self, value):
        self._setNumber(5, value)
        return

    def getMinVehicleLvl(self):
        return self._getNumber(6)

    def setMinVehicleLvl(self, value):
        self._setNumber(6, value)
        return

    def getMaxVehicleLvl(self):
        return self._getNumber(7)

    def setMaxVehicleLvl(self, value):
        self._setNumber(7, value)
        return

    def getVehicleType(self):
        return self._getString(8)

    def setVehicleType(self, value):
        self._setString(8, value)
        return

    def getNation(self):
        return self._getString(9)

    def setNation(self, value):
        self._setString(9, value)
        return

    def _initialize(self):
        super(EarlyAccessTooltipChapterModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'state')
        self._addNumberProperty(b'completedQuests', 0)
        self._addNumberProperty(b'totalQuests', 0)
        self._addNumberProperty(b'announcementTimestamp', 0)
        self._addNumberProperty(b'lockedUntilQuestsComplete', 0)
        self._addNumberProperty(b'minVehicleLvl', 0)
        self._addNumberProperty(b'maxVehicleLvl', 10)
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'nation', b'')
        return
