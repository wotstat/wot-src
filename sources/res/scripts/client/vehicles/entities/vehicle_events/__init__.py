from __future__ import absolute_import
import typing
from events_containers.common.container_wrappers import activateEventsContainer
from vehicles.entities.vehicle_events.interfaces import IVehicleEvents, IVehicleEventsListener, IVehicleEventsListenerLogic
from vehicles.entities.vehicle_events.events import VehicleEvents
if typing.TYPE_CHECKING:
    from Vehicle import Vehicle
__all__ = (b'IVehicleEvents', b'IVehicleEventsListener', b'IVehicleEventsListenerLogic', b'VehicleEvents', b'createVehicleEvents')

@activateEventsContainer()
def createVehicleEvents(vehicle, **_):
    return VehicleEvents(vehicle)
