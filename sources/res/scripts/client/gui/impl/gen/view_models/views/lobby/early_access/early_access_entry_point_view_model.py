from enum import Enum
from frameworks.wulf import ViewModel

class ExtendedStates(Enum):
    WAITFORNEXTCHAPTER = b'waitForNextChapter'
    DISABLED = b'disabled'


class EarlyAccessEntryPointViewModel(ViewModel):
    __slots__ = (b'onAction',)

    def __init__(self, properties=4, commands=1):
        super(EarlyAccessEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(1)

    def setProgressionLevel(self, value):
        self._setNumber(1, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(2)

    def setEndTimestamp(self, value):
        self._setNumber(2, value)
        return

    def getIsFirstEnter(self):
        return self._getBool(3)

    def setIsFirstEnter(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(EarlyAccessEntryPointViewModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        self._addNumberProperty(b'progressionLevel', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addBoolProperty(b'isFirstEnter', True)
        self.onAction = self._addCommand(b'onAction')
        return
