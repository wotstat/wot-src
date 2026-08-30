from __future__ import absolute_import
import weakref
from events_containers.common.containers import ClientEventsContainerDebugger

class ClientComponentEventsDebugger(ClientEventsContainerDebugger):
    _EVENTS_DEBUG_PREFIX = b''

    def __init__(self, events, component):
        super(ClientComponentEventsDebugger, self).__init__(events)
        self.__componentRef = weakref.ref(component)
        self.__entityID = component.entity.id
        return

    def _getDebugPrefix(self):
        return (b'[{}][{}][{}]').format(self._EVENTS_DEBUG_PREFIX, self.__entityID, self.__componentRef())
