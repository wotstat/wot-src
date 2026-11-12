from enum import Enum
from frameworks.wulf import ViewModel

class EnvironmentState(Enum):
    DAY = b'Day'
    AUTO = b'Auto'
    NIGHT = b'Night'


class EnvironmentSwitcher(ViewModel):
    __slots__ = (b'onSwitch',)

    def __init__(self, properties=3, commands=1):
        super(EnvironmentSwitcher, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return EnvironmentState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getMode(self):
        return EnvironmentState(self._getString(1))

    def setMode(self, value):
        self._setString(1, value.value)
        return

    def getArrowDegree(self):
        return self._getNumber(2)

    def setArrowDegree(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(EnvironmentSwitcher, self)._initialize()
        self._addStringProperty(b'state')
        self._addStringProperty(b'mode')
        self._addNumberProperty(b'arrowDegree', 0)
        self.onSwitch = self._addCommand(b'onSwitch')
        return
