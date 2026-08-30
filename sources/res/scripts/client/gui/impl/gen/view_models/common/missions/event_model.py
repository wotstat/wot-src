from enum import Enum
from frameworks.wulf import ViewModel

class EventStatus(Enum):
    DONE = b'done'
    UNDONESUBSCRIPTION = b'undoneSubscription'
    LOCKED = b'notAvailable'
    ACTIVE = b''


class EventModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(EventModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getGroupId(self):
        return self._getString(1)

    def setGroupId(self, value):
        self._setString(1, value)
        return

    def getType(self):
        return self._getNumber(2)

    def setType(self, value):
        self._setNumber(2, value)
        return

    def getTitle(self):
        return self._getString(3)

    def setTitle(self, value):
        self._setString(3, value)
        return

    def getDescription(self):
        return self._getString(4)

    def setDescription(self, value):
        self._setString(4, value)
        return

    def getDecoration(self):
        return self._getNumber(5)

    def setDecoration(self, value):
        self._setNumber(5, value)
        return

    def getStatus(self):
        return EventStatus(self._getString(6))

    def setStatus(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(EventModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'groupId', b'')
        self._addNumberProperty(b'type', 0)
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'decoration', 0)
        self._addStringProperty(b'status')
        return
