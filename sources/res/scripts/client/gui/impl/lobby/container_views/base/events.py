from functools import partial
from Event import Event
from debug_utils import LOG_DEBUG_DEV
from events_container import EventsContainer
from events_debugger import EventsDebugger

class EventsProviderSourceProxy(object):

    def __init__(self, component, eventsProvider):
        self.__component = component
        self.__eventsProvider = eventsProvider
        return

    def __getattr__(self, name):
        attr = getattr(self.__eventsProvider, name)
        if callable(attr) and isinstance(attr, Event):
            return self._proxy(attr)
        return attr

    def _proxy(self, method):

        def wrapper(*args, **kwargs):
            return method(self.__component, *args, **kwargs)

        return wrapper


class ContainerLifecycleEvents(EventsContainer):

    def __init__(self):
        EventsContainer.__init__(self)
        self.onLoading = self._createEvent()
        self.onLoaded = self._createEvent()
        self.initialize = self._createEvent()
        self.finalize = self._createEvent()
        self.onReady = self._createEvent()
        self.onShown = self._createEvent()
        self.onHidden = self._createEvent()
        self.onFocus = self._createEvent()
        self.swapStates = self._createEvent()
        self.swapShowingStates = self._createEvent()
        return

    def debugEvents(self):
        self._debugger = ContainerLifecycleEventsDebugger(self)
        return

    def events(self):
        events = []
        for name, value in self.__dict__.items():
            if isinstance(value, Event):
                events.append((name, value))

        return events


class ComponentEventsBase(EventsContainer):

    def __init__(self):
        EventsContainer.__init__(self)
        self.onMouseEnter = self._createEvent()
        self.onMouseLeave = self._createEvent()
        self.logClick = self._createEvent()
        return

    def debugEvents(self):
        self._debugger = ComponentEventsDebugger(self)
        return

    def events(self):
        events = []
        for name, value in self.__dict__.items():
            if isinstance(value, Event):
                events.append((name, value))

        return events


class ContainerLifecycleEventsDebugger(EventsDebugger):

    def __init__(self, events):
        for event in dir(events):
            if event.startswith(b'on') and event not in dir(self):
                setattr(self, event, partial(self._logEvent, event=event))

        super(ContainerLifecycleEventsDebugger, self).__init__(events)
        return

    def _getDebugPrefix(self):
        return b'[CONTAINER_LIFECYCLE_EVENT]'

    def _logEvent(self, event, *args, **kwargs):
        prefix = self._getDebugPrefix()
        LOG_DEBUG_DEV((b'{prefix} {event} called with args={args}, kwargs={kwargs}').format(prefix=prefix, event=event, args=args, kwargs=kwargs))
        return


class ComponentEventsDebugger(ContainerLifecycleEventsDebugger):

    def _getDebugPrefix(self):
        return b'[COMPONENT_EVENT]'
