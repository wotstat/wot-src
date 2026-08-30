from __future__ import absolute_import
from events_container import EventsContainer

class EntityEvents(EventsContainer):
    __slots__ = (b'onDynComponentGroupAdded', b'onDynComponentGroupRemoved')

    def __init__(self):
        super(EntityEvents, self).__init__()
        self.onDynComponentGroupAdded = self._createEvent()
        self.onDynComponentGroupRemoved = self._createEvent()
        return

    def createEvent(self):
        return self._createEvent()
