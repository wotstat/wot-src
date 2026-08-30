from __future__ import absolute_import
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener

class IMechanicState(object):

    def isTransition(self, other):
        raise NotImplementedError
        return


class IMechanicStatesComponent(object):

    @property
    def statesEvents(self):
        raise NotImplementedError
        return

    def getMechanicState(self):
        raise NotImplementedError
        return


class IMechanicStatesEventsLogic(object):
    onStatePrepared = None
    onStateObservation = None
    onStateTransition = None
    onStateTick = None

    def processStatePrepared(self):
        raise NotImplementedError
        return

    def updateMechanicState(self, state):
        raise NotImplementedError
        return


class IMechanicStatesEvents(IClientEventsContainer, IMechanicStatesEventsLogic):
    pass


class IMechanicStatesListenerLogic(object):

    def onStatePrepared(self, state):
        return

    def onStateObservation(self, state):
        return

    def onStateTransition(self, prevState, newState):
        return

    def onStateTick(self, state):
        return


class IMechanicStatesListener(IClientEventsContainerListener, IMechanicStatesListenerLogic):
    pass
