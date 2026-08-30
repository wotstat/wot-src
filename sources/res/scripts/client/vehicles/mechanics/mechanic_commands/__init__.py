from __future__ import absolute_import
import typing
from events_containers.common.container_wrappers import activateEventsContainer
from vehicles.mechanics.mechanic_commands.mechanic_events import MechanicCommandsEvents
from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsComponent, IMechanicCommandsEvents, IMechanicCommandsListener, IMechanicCommandsListenerLogic
__all__ = (b'IMechanicCommandsComponent', b'IMechanicCommandsEvents', b'IMechanicCommandsListener', b'IMechanicCommandsListenerLogic', b'MechanicCommandsEvents', b'createMechanicCommandsEvents')

@activateEventsContainer()
def createMechanicCommandsEvents(component, **_):
    return MechanicCommandsEvents(component)
