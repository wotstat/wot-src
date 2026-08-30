from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    PRE_EVENT = b'preEvent'
    EVENT_ACTIVE = b'eventActive'
    POST_EVENT = b'postEvent'


class EntryPointBase(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(EntryPointBase, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getPreviousState(self):
        return State(self._getString(1))

    def setPreviousState(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(EntryPointBase, self)._initialize()
        self._addStringProperty(b'state')
        self._addStringProperty(b'previousState')
        return
