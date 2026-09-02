from __future__ import absolute_import
import weakref, typing
from .states import State
from .exceptions import StateError
if typing.TYPE_CHECKING:
    from .events import StateEvent

class BaseStateObserver(object):
    __slots__ = ()

    def clear(self):
        return

    def isObservingState(self, state):
        raise NotImplementedError
        return

    def onStateChanged(self, state, stateEntered, event=None):
        if stateEntered:
            self.onEnterState(state, event)
        else:
            self.onExitState(state, event)
        return

    def onEnterState(self, state, event):
        return

    def onExitState(self, state, event):
        return


class StateIdsObserver(BaseStateObserver):
    __slots__ = (b'_stateIDs',)

    def __init__(self, stateIDs):
        super(StateIdsObserver, self).__init__()
        if isinstance(stateIDs, str):
            self._stateIDs = [
             stateIDs]
        else:
            self._stateIDs = list(stateIDs)
        return

    def getStateIDs(self):
        return self._stateIDs[:]

    def isObservingState(self, state):
        return state.getStateID() in self.getStateIDs()


class StateObserversContainer(BaseStateObserver):
    __slots__ = (b'_observers',)

    def __init__(self, *observers):
        super(StateObserversContainer, self).__init__()
        self._observers = []
        for observer in observers:
            self.addObserver(observer)

        return

    def clear(self):
        while self._observers:
            observer = self._observers.pop()
            observer.clear()

        return

    def addObserver(self, observer):
        if not isinstance(observer, BaseStateObserver):
            raise StateError(b'Instance of StateObserver class is required')
        if observer not in self._observers:
            self._observers.append(observer)
        return

    def removeObserver(self, observer):
        if not isinstance(observer, BaseStateObserver):
            raise StateError(b'Instance of StateObserver class is required')
        if observer in self._observers:
            self._observers.remove(observer)
        observer.clear()
        return

    def isObservingState(self, state):
        return True

    def onStateChanged(self, state, stateEntered, event=None):
        for observer in self._observers[:]:
            if observer.isObservingState(state):
                observer.onStateChanged(state, stateEntered, event=event)

        return


class _LifetimeWrapper(object):

    def __init__(self, trackedObj, onDelete):
        self._obj = weakref.ref(trackedObj, onDelete)
        return

    @property
    def trackedObj(self):
        return self._obj

    def makeCallable(self, fn):
        weakObj = self._obj

        def wrapper(state, event):
            obj = weakObj()
            if obj is None:
                return
            else:
                return fn(obj, state, event)

        return wrapper


class OneshotStateIdsObserver(StateIdsObserver):

    def __init__(self, stateIds, machine, lifetimeObj, enterFn=None, exitFn=None):
        super(OneshotStateIdsObserver, self).__init__(stateIds)
        self._lifetimeWrapper = _LifetimeWrapper(lifetimeObj, self._tryDisconnect)
        self._enterFn = self._lifetimeWrapper.makeCallable(enterFn) if enterFn else None
        self._exitFn = self._lifetimeWrapper.makeCallable(exitFn) if exitFn else None
        self._machine = weakref.ref(machine)
        return

    def clear(self):
        self._lifetimeWrapper = None
        self._machine = lambda : None
        self._exitFn = None
        self._enterFn = None
        return

    def onEnterState(self, state, event):
        if self._enterFn:
            self._enterFn(state, event)
            self._enterFn = None
        self._tryDisconnect(forceRemove=False)
        return

    def onExitState(self, state, event):
        if self._exitFn:
            self._exitFn(state, event)
            self._exitFn = None
        self._tryDisconnect(forceRemove=False)
        return

    def _tryDisconnect(self, forceRemove=True, *_, **__):
        machine = self._machine()
        if machine and (forceRemove or not self._enterFn and not self._exitFn):
            machine.disconnect(self)
        return
