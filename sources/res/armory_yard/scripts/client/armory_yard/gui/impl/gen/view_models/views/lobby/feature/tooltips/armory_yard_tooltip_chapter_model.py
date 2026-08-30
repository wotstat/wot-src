from enum import Enum
from frameworks.wulf import ViewModel

class TooltipChapterState(Enum):
    ACTIVE = b'active'
    COMPLETED = b'completed'
    ANNOUNCEMENT = b'announcement'
    JUSTBEFORESTART = b'justBeforeStart'
    LOCKED = b'locked'


class ArmoryYardTooltipChapterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(ArmoryYardTooltipChapterModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
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

    def getJustBeforeStartTimestamp(self):
        return self._getNumber(5)

    def setJustBeforeStartTimestamp(self, value):
        self._setNumber(5, value)
        return

    def getLockedUntilQuestsComplete(self):
        return self._getNumber(6)

    def setLockedUntilQuestsComplete(self, value):
        self._setNumber(6, value)
        return

    def getIsPostProgression(self):
        return self._getBool(7)

    def setIsPostProgression(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(ArmoryYardTooltipChapterModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'state')
        self._addNumberProperty(b'completedQuests', 0)
        self._addNumberProperty(b'totalQuests', 0)
        self._addNumberProperty(b'announcementTimestamp', 0)
        self._addNumberProperty(b'justBeforeStartTimestamp', 0)
        self._addNumberProperty(b'lockedUntilQuestsComplete', 0)
        self._addBoolProperty(b'isPostProgression', False)
        return
