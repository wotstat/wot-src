import typing
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
        for observer in self._observers:
            if observer.isObservingState(state):
                observer.onStateChanged(state, stateEntered, event=event)

        return
