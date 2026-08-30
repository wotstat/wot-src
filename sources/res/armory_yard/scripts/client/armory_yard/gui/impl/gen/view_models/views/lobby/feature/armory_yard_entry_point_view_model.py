from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    BEFOREPROGRESSION = b'beforeProgression'
    ACTIVE = b'active'
    PURCHASESTAGE = b'purchaseStage'
    COMPLETED = b'completed'
    DISABLED = b'disabled'


class ArmoryYardEntryPointViewModel(ViewModel):
    __slots__ = (b'onAction',)

    def __init__(self, properties=3, commands=1):
        super(ArmoryYardEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
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

    def _initialize(self):
        super(ArmoryYardEntryPointViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'progressionLevel', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self.onAction = self._addCommand(b'onAction')
        return
