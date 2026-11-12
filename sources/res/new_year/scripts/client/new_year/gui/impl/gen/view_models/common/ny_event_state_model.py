from enum import Enum
from frameworks.wulf import ViewModel

class EventState(Enum):
    ACTIVE = b'active'
    PAUSED = b'paused'


class NyEventStateModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NyEventStateModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return EventState(self._getString(0))

    def setValue(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(NyEventStateModel, self)._initialize()
        self._addStringProperty(b'value', EventState.PAUSED.value)
        return
