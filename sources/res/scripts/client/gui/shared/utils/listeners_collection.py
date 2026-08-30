import itertools
from debug_utils import LOG_ERROR, LOG_DEBUG

class IListenersCollection(object):

    def addMutualListeners(self, mutualListeners):
        return

    def addListener(self, listener):
        return

    def removeListener(self, listener):
        return


class ListenersCollection(IListenersCollection):

    def __init__(self):
        super(ListenersCollection, self).__init__()
        self._listeners = []
        self._clazz = None
        self._mutualListeners = None
        self._isSuspended = False
        return

    def clear(self):
        LOG_DEBUG(b'Listeners collection was cleared: ', self)
        while self._listeners:
            self._listeners.pop()

        self._clazz = None
        self._mutualListeners = None
        return

    def suspend(self):
        LOG_DEBUG(b'Listeners collection was suspended: ', self)
        self._isSuspended = True
        return

    def resume(self):
        LOG_DEBUG(b'Listeners collection was resumed: ', self)
        self._isSuspended = False
        return

    def addMutualListeners(self, mutualListeners):
        if isinstance(mutualListeners, ListenersCollection):
            self._mutualListeners = mutualListeners
        else:
            LOG_ERROR((b'Object is not extend {0:>s}').format(ListenersCollection.__name__), mutualListeners)
        return

    def addListener(self, listener):
        if isinstance(listener, self._clazz):
            if not self.hasListener(listener):
                self._listeners.append(listener)
            else:
                LOG_ERROR(b'Listener already added', listener)
        else:
            LOG_ERROR((b'Object does not extend {0:>s}').format(self._clazz.__name__), listener)
        return

    def hasListener(self, listener):
        return listener in self._listeners

    def removeListener(self, listener):
        if listener in self._listeners:
            self._listeners.remove(listener)
        else:
            LOG_DEBUG(b'Listener not found.', listener)
        return

    def getListenersIterator(self):
        if self._mutualListeners is not None:
            return itertools.chain(iter(self._listeners), self._mutualListeners.getListenersIterator())
        else:
            return iter(self._listeners)

    def _setListenerClass(self, listenerClass):
        self._clazz = listenerClass
        return

    def _invokeListeners(self, event, *args, **kwargs):
        if self._isSuspended:
            return
        LOG_DEBUG(event, args, kwargs)
        for listener in list(self.getListenersIterator()):
            notifier = getattr(listener, event)
            if notifier and callable(notifier):
                notifier(*args, **kwargs)
            else:
                LOG_ERROR(b'Listener method not found', listener, event)

        return
