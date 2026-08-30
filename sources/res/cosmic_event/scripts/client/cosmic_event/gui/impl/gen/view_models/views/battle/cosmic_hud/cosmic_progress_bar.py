from enum import Enum
from frameworks.wulf import ViewModel

class ProgressBarType(Enum):
    CORAL = b'coral'
    ARTIFACT_ZONE = b'artifactZone'


class CosmicProgressBar(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(CosmicProgressBar, self).__init__(properties=properties, commands=commands)
        return

    def getBarType(self):
        return ProgressBarType(self._getString(0))

    def setBarType(self, value):
        self._setString(0, value.value)
        return

    def getTimeLeft(self):
        return self._getNumber(1)

    def setTimeLeft(self, value):
        self._setNumber(1, value)
        return

    def getTotalTime(self):
        return self._getNumber(2)

    def setTotalTime(self, value):
        self._setNumber(2, value)
        return

    def getActivePlayers(self):
        return self._getNumber(3)

    def setActivePlayers(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(CosmicProgressBar, self)._initialize()
        self._addStringProperty(b'barType')
        self._addNumberProperty(b'timeLeft', 0)
        self._addNumberProperty(b'totalTime', 0)
        self._addNumberProperty(b'activePlayers', 0)
        return
