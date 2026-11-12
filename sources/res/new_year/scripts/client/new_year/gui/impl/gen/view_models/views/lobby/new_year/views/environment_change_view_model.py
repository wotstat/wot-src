from enum import Enum
from frameworks.wulf import ViewModel

class EnvironmentState(Enum):
    DAY = b'Day'
    AUTO = b'Auto'
    NIGHT = b'Night'


class EnvironmentChangeViewModel(ViewModel):
    __slots__ = (b'onAnimationFinished', b'onAnimationFadeFinished')

    def __init__(self, properties=2, commands=2):
        super(EnvironmentChangeViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSwitchTo(self):
        return EnvironmentState(self._getString(0))

    def setSwitchTo(self, value):
        self._setString(0, value.value)
        return

    def getIsEnvironmentSwitched(self):
        return self._getBool(1)

    def setIsEnvironmentSwitched(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(EnvironmentChangeViewModel, self)._initialize()
        self._addStringProperty(b'switchTo')
        self._addBoolProperty(b'isEnvironmentSwitched', False)
        self.onAnimationFinished = self._addCommand(b'onAnimationFinished')
        self.onAnimationFadeFinished = self._addCommand(b'onAnimationFadeFinished')
        return
