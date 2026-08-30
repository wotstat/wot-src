from enum import Enum
from frameworks.wulf import ViewModel

class WinbackState(Enum):
    IN_PROGRESS = b'inProgress'
    COMPLETE = b'complete'
    DISABLE = b'disable'


class WidgetTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(WidgetTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return WinbackState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getIsTimerDisplayed(self):
        return self._getBool(1)

    def setIsTimerDisplayed(self, value):
        self._setBool(1, value)
        return

    def getCurrentTimerDate(self):
        return self._getNumber(2)

    def setCurrentTimerDate(self, value):
        self._setNumber(2, value)
        return

    def getProgressionName(self):
        return self._getString(3)

    def setProgressionName(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(WidgetTooltipViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isTimerDisplayed', False)
        self._addNumberProperty(b'currentTimerDate', 0)
        self._addStringProperty(b'progressionName', b'')
        return
