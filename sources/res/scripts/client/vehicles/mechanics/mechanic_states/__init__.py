from __future__ import absolute_import
import typing
from constants import SERVER_TICK_LENGTH
from events_containers.common.container_wrappers import activateEventsContainer
from vehicles.mechanics.mechanic_states.mechanic_events import MechanicStatesEvents
from vehicles.mechanics.mechanic_states.mechanic_interfaces import IMechanicState, IMechanicStatesComponent, IMechanicStatesEvents, IMechanicStatesListener, IMechanicStatesListenerLogic
__all__ = (b'IMechanicState', b'IMechanicStatesComponent', b'IMechanicStatesEvents', b'IMechanicStatesListener', b'IMechanicStatesListenerLogic', b'MechanicStatesEvents', b'createMechanicStatesEvents')

@activateEventsContainer()
def createMechanicStatesEvents(component, tickInterval=SERVER_TICK_LENGTH, **_):
    return MechanicStatesEvents(component, tickInterval)
