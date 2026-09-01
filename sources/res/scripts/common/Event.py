from __future__ import absolute_import
from future.utils import viewvalues
from WeakMethod import WeakMethodProxy
from debug_utils import LOG_CURRENT_EXCEPTION

class Event(list):
    __slots__ = (b'__weakref__',)

    def __init__(self, manager=None):
        list.__init__(self)
        if manager is not None:
            manager.register(self)
        return

    def __call__(self, *args, **kwargs):
        for delegate in self[:]:
            try:
                delegate(*args, **kwargs)
            except:
                LOG_CURRENT_EXCEPTION()
                raise

        return

    def __iadd__(self, delegate):
        if not callable(delegate):
            raise TypeError(b'Event listener is not callable.')
        if delegate not in self:
            self.append(delegate)
        return self

    def __isub__(self, delegate):
        if delegate in self:
            self.remove(delegate)
        return self

    def clear(self):
        del self[:]
        return

    def __repr__(self):
        return b'Event(%s)(%s):%s' % (self.__class__.__name__, len(self), repr(self[:]))


class SafeEvent(Event):
    __slots__ = ()

    def __call__(self, *args, **kwargs):
        for delegate in self[:]:
            try:
                delegate(*args, **kwargs)
            except:
                LOG_CURRENT_EXCEPTION()

        return


class LateEvent(SafeEvent):
    __slots__ = (b'__lateCallback',)

    def __init__(self, lateCallback, manager=None):
        super(LateEvent, self).__init__(manager)
        self.__lateCallback = WeakMethodProxy(lateCallback)
        return

    def lateAdd(self, delegate):
        self.__lateCallback(delegate)
        self.__iadd__(delegate)
        return

    def clear(self):
        self.__lateCallback = None
        super(LateEvent, self).clear()
        return


class Handler(object):
    __slots__ = (b'__delegate',)

    def __init__(self, manager=None):
        self.__delegate = None
        if manager is not None:
            manager.register(self)
        return

    def __call__(self, *args, **kwargs):
        if self.__delegate is not None:
            return self.__delegate(*args, **kwargs)
        else:
            return

    def set(self, delegate):
        self.__delegate = delegate
        return

    def clear(self):
        self.__delegate = None
        return


class EventManager(object):
    __slots__ = (b'__events',)

    def __init__(self):
        self.__events = []
        return

    @property
    def hasAnyListener(self):
        return any(self.__events)

    def register(self, event):
        self.__events.append(event)
        return

    def clear(self):
        for event in self.__events:
            event.clear()

        return


class SuspendedEvent(Event):
    __slots__ = (b'__manager',)

    def __init__(self, manager):
        super(SuspendedEvent, self).__init__(manager)
        self.__manager = manager
        return

    def clear(self):
        self.__manager = None
        super(SuspendedEvent, self).clear()
        return

    def __call__(self, *args, **kwargs):
        if self.__manager.isSuspended():
            self.__manager.suspendEvent(self, *args, **kwargs)
        else:
            super(SuspendedEvent, self).__call__(*args, **kwargs)
        return


class SuspendedEventManager(EventManager):
    __slots__ = (b'__isSuspended', b'__suspendedEvents')

    def __init__(self):
        super(SuspendedEventManager, self).__init__()
        self.__isSuspended = False
        self.__suspendedEvents = []
        return

    def suspendEvent(self, e, *args, **kwargs):
        self.__suspendedEvents.append((e, args, kwargs))
        return

    def isSuspended(self):
        return self.__isSuspended

    def suspend(self):
        self.__isSuspended = True
        return

    def resume(self):
        if self.__isSuspended:
            self.__isSuspended = False
            while self.__suspendedEvents:
                e, args, kwargs = self.__suspendedEvents.pop(0)
                e(*args, **kwargs)

        return

    def clear(self):
        self.__isSuspended = False
        self.__suspendedEvents = []
        super(SuspendedEventManager, self).clear()
        return


class EventsSubscriber(object):

    def __init__(self):
        super(EventsSubscriber, self).__init__()
        self.__subscribeList = []
        self.__contextSubscribeList = []
        self.__callbacksOnUnsubscribe = []
        return

    def subscribeToContextEvent(self, event, delegate, *contextIDs):
        event.subscribe(delegate, *contextIDs)
        self.__contextSubscribeList.append((event, delegate))
        return

    def subscribeToEvent(self, event, delegate):
        event += delegate
        self.__subscribeList.append((event, delegate))
        return

    def addCallbackOnUnsubscribe(self, callback):
        self.__callbacksOnUnsubscribe.append(callback)
        return

    def unsubscribeFromAllEvents(self):
        for event, delegate in self.__subscribeList:
            event -= delegate

        for event, delegate in self.__contextSubscribeList:
            event.unsubscribe(delegate)

        while self.__callbacksOnUnsubscribe:
            callback = self.__callbacksOnUnsubscribe.pop(0)
            callback()

        self.__subscribeList = []
        self.__callbacksOnUnsubscribe = []
        return


class ContextEvent(object):
    __allContexts = object()

    def __init__(self, manager=None):
        self.__contextSubscribers = {}
        if manager is not None:
            manager.register(self)
        return

    def __call__(self, contextID, *args, **kwargs):
        subscribers = self.__contextSubscribers.get(contextID)
        if subscribers:
            for subscriber in subscribers:
                subscriber(contextID, *args, **kwargs)

        subscribers = self.__contextSubscribers.get(self.__allContexts)
        if subscribers:
            for subscriber in subscribers:
                subscriber(contextID, *args, **kwargs)

        return

    def subscribe(self, delegate, *contextIDs):
        if contextIDs:
            for contextID in contextIDs:
                self.__contextSubscribers.setdefault(contextID, set())
                self.__contextSubscribers[contextID].add(delegate)

        else:
            self.__contextSubscribers.setdefault(self.__allContexts, set())
            self.__contextSubscribers[self.__allContexts].add(delegate)
        return

    def unsubscribe(self, delegate):
        for contextSubscribers in viewvalues(self.__contextSubscribers):
            contextSubscribers.discard(delegate)

        return

    def clear(self):
        self.__contextSubscribers.clear()
        return


class EventCallback(object):
    __slots__ = (b'event', b'_callback')

    def __init__(self, event, callback):
        self.event = event
        self._callback = callback
        self.event += self.callback
        return

    def callback(self, *args, **kwargs):
        self._callback(*args, **kwargs)
        self.event -= self.callback
        return
