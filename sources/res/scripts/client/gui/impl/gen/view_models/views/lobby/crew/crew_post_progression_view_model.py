from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class PauseReasonType(Enum):
    NONE = b''
    LOWEFFICIENCY = b'lowEfficiency'
    RETIRE = b'retire'


class CrewPostProgressionViewModel(ViewModel):
    __slots__ = (b'onClaim',)

    def __init__(self, properties=7, commands=1):
        super(CrewPostProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)
        return

    def getCount(self):
        return self._getNumber(3)

    def setCount(self, value):
        self._setNumber(3, value)
        return

    def getProgressCurrent(self):
        return self._getNumber(4)

    def setProgressCurrent(self, value):
        self._setNumber(4, value)
        return

    def getProgressMax(self):
        return self._getNumber(5)

    def setProgressMax(self, value):
        self._setNumber(5, value)
        return

    def getPauseReason(self):
        return PauseReasonType(self._getString(6))

    def setPauseReason(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(CrewPostProgressionViewModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addStringProperty(b'description', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'progressCurrent', 0)
        self._addNumberProperty(b'progressMax', 0)
        self._addStringProperty(b'pauseReason', PauseReasonType.NONE.value)
        self.onClaim = self._addCommand(b'onClaim')
        return
