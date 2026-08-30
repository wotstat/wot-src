from __future__ import absolute_import
import typing
from constants import UNKNOWN_VEHICLE_ID
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener
if typing.TYPE_CHECKING:
    from Vehicle import Vehicle

class IVehicleEntityTrackerLogic(object):
    onVehicleEntityCatching = None
    onVehicleEntityReleasing = None

    @property
    def trackedVehicle(self):
        raise NotImplementedError
        return

    def startTracking(self):
        raise NotImplementedError
        return

    def stopTracking(self):
        raise NotImplementedError
        return

    def updateTracking(self, vehicleID=UNKNOWN_VEHICLE_ID, vehicle=None):
        raise NotImplementedError
        return


class IVehicleEntityTracker(IClientEventsContainer, IVehicleEntityTrackerLogic):
    pass


class IVehicleEntityTrackerListenerLogic(object):

    def onVehicleEntityCatching(self, vehicle):
        return

    def onVehicleEntityReleasing(self, vehicle):
        return


class IVehicleEntityTrackerListener(IClientEventsContainerListener, IVehicleEntityTrackerListenerLogic):
    pass
