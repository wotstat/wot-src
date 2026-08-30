from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener
from vehicles.entities.vehicle_trackers import IVehicleEntityTrackerListenerLogic
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_constants import VehicleMechanic

class IVehicleMechanicsTrackerLogic(IVehicleEntityTrackerListenerLogic):
    onMechanicComponentCatching = None
    onMechanicComponentReleasing = None
    onMechanicComponentsUpdate = None

    @property
    def trackedComponents(self):
        raise NotImplementedError
        return

    def getTrackedComponent(self, mechanic):
        raise NotImplementedError
        return


class IVehicleMechanicsTracker(IClientEventsContainer, IVehicleMechanicsTrackerLogic):
    pass


class IVehicleMechanicsTrackerListenerLogic(object):

    def onMechanicComponentCatching(self, component):
        return

    def onMechanicComponentReleasing(self, component):
        return

    def onMechanicComponentsUpdate(self, components):
        return


class IVehicleMechanicsTrackerListener(IClientEventsContainerListener, IVehicleMechanicsTrackerListenerLogic):
    pass
