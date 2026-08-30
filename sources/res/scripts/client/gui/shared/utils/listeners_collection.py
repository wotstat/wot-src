from __future__ import absolute_import
import itertools, logging
_logger = logging.getLogger(__name__)

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
        _logger.debug(b'Listeners collection was cleared: %r', self)
        while self._listeners:
            self._listeners.pop()

        self._clazz = None
        self._mutualListeners = None
        return

    def suspend(self):
        _logger.debug(b'Listeners collection was suspended: %r', self)
        self._isSuspended = True
        return

    def resume(self):
        _logger.debug(b'Listeners collection was resumed: %r', self)
        self._isSuspended = False
        return

    def addMutualListeners(self, mutualListeners):
        if isinstance(mutualListeners, ListenersCollection):
            self._mutualListeners = mutualListeners
        else:
            _logger.error((b'Object is not extend {0:>s} %r').format(ListenersCollection.__name__), mutualListeners)
        return

    def addListener(self, listener):
        if isinstance(listener, self._clazz):
            if not self.hasListener(listener):
                self._listeners.append(listener)
            else:
                _logger.error(b'Listener already added %r', listener)
        else:
            _logger.error((b'Object does not extend {0:>s} %r').format(self._clazz.__name__), listener)
        return

    def hasListener(self, listener):
        return listener in self._listeners

    def removeListener(self, listener):
        if listener in self._listeners:
            self._listeners.remove(listener)
        else:
            _logger.debug(b'Listener not found %r.', listener)
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
        else:
            _logger.debug(b'%r %r %r', event, args, kwargs)
            for listener in list(self.getListenersIterator()):
                if listener not in self.getListenersIterator():
                    continue
                notifier = getattr(listener, event, None)
                if notifier and callable(notifier):
                    try:
                        notifier(*args, **kwargs)
                    except Exception:
                        _logger.exception(b'Error while notifying listener %r for event %r', listener, event)

                else:
                    _logger.error(b'Listener method not found %r %r', listener, event)

            return
