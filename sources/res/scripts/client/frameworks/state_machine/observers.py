from .events import StateEvent
from .exceptions import StateError

class BaseStateObserver(object):
    __slots__ = ()

    def clear(self):
        return

    def getStateIDs(self):
        raise NotImplementedError
        return

    def onStateChanged(self, stateID, flag, event=None):
        raise NotImplementedError
        return


class SingleStateObserver(BaseStateObserver):
    __slots__ = (b'_stateID',)

    def __init__(self, stateID):
        super(SingleStateObserver, self).__init__()
        self._stateID = stateID
        return

    def getStateIDs(self):
        return (
         self._stateID,)

    def onStateChanged(self, stateID, flag, event=None):
        if flag:
            self.onEnterState(event=event)
        else:
            self.onExitState(event=event)
        return

    def onEnterState(self, event=None):
        return

    def onExitState(self, event=None):
        return


class MultipleStateObserver(SingleStateObserver):
    __slots__ = (b'_stateIDs',)

    def __init__(self, stateIDs):
        super(MultipleStateObserver, self).__init__(b'')
        self._stateIDs = stateIDs
        return

    def getStateIDs(self):
        return self._stateIDs[:]


class StateObserversContainer(BaseStateObserver):
    __slots__ = (b'_stateIDs', b'_observers')

    def __init__(self, *observers):
        super(StateObserversContainer, self).__init__()
        self._observers = []
        self._stateIDs = []
        for observer in observers:
            self.addObserver(observer)

        return

    def clear(self):
        while self._observers:
            observer = self._observers.pop()
            observer.clear()

        del self._stateIDs[:]
        return

    def addObserver(self, observer):
        if not isinstance(observer, BaseStateObserver):
            raise StateError(b'Instance of StateObserver class is required')
        if observer not in self._observers:
            self._observers.append(observer)
        stateIDs = observer.getStateIDs()
        for stateID in stateIDs:
            if stateID not in self._stateIDs:
                self._stateIDs.append(stateID)

        return

    def removeObserver(self, observer):
        if not isinstance(observer, BaseStateObserver):
            raise StateError(b'Instance of StateObserver class is required')
        if observer in self._observers:
            self._observers.remove(observer)
        stateIDs = observer.getStateIDs()
        for stateID in stateIDs:
            if stateID in self._stateIDs:
                self._stateIDs.remove(stateID)

        observer.clear()
        return

    def getStateIDs(self):
        return self._stateIDs[:]

    def onStateChanged(self, stateID, flag, event=None):
        for observer in self._observers:
            if stateID in observer.getStateIDs():
                observer.onStateChanged(stateID, flag, event=event)

        return
