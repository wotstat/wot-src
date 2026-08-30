from enum import Enum
from frameworks.wulf import ViewModel

class TimerIconType(Enum):
    CLOCK = b'clock'
    FLAG = b'flag'
    NONE = b'none'


class UniversalFlagEntryTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(UniversalFlagEntryTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCaption(self):
        return self._getString(0)

    def setCaption(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getTimerTime(self):
        return self._getNumber(2)

    def setTimerTime(self, value):
        self._setNumber(2, value)
        return

    def getTimerText(self):
        return self._getString(3)

    def setTimerText(self, value):
        self._setString(3, value)
        return

    def getTimerIconType(self):
        return TimerIconType(self._getString(4))

    def setTimerIconType(self, value):
        self._setString(4, value.value)
        return

    def getTimestamp(self):
        return self._getNumber(5)

    def setTimestamp(self, value):
        self._setNumber(5, value)
        return

    def getTooltipBackground(self):
        return self._getString(6)

    def setTooltipBackground(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(UniversalFlagEntryTooltipModel, self)._initialize()
        self._addStringProperty(b'caption', b'')
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'timerTime', 0)
        self._addStringProperty(b'timerText', b'')
        self._addStringProperty(b'timerIconType')
        self._addNumberProperty(b'timestamp', 0)
        self._addStringProperty(b'tooltipBackground', b'')
        return
