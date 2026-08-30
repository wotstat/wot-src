from __future__ import absolute_import
import typing
from gui.battle_control.controllers.interfaces import IBattleController
if typing.TYPE_CHECKING:
    from vehicles.entities.vehicle_trackers import IVehicleEntityTrackerListener
    from vehicles.mechanics.mechanic_constants import VehicleMechanic
    from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListener

class IVehicleTrackers(object):

    def startCurrentVehicleTracking(self, listener):
        raise NotImplementedError
        return

    def stopCurrentVehicleTracking(self, listener):
        raise NotImplementedError
        return

    def startVehicleTracking(self, vehicleID, listener):
        raise NotImplementedError
        return

    def stopVehicleTracking(self, vehicleID, listener):
        raise NotImplementedError
        return


class IVehicleMechanicTrackers(object):

    def startCurrentMechanicsTracking(self, mechanics, listener):
        raise NotImplementedError
        return

    def stopCurrentMechanicsTracking(self, mechanics, listener):
        raise NotImplementedError
        return

    def startMechanicsTracking(self, vehicleID, mechanics, listener):
        raise NotImplementedError
        return

    def stopMechanicsTracking(self, vehicleID, mechanics, listener):
        raise NotImplementedError
        return


class IVehiclesTrackingWatcher(object):

    @classmethod
    def getVehiclesTrackingCtrl(cls):
        raise NotImplementedError
        return


class IVehiclesTrackingController(IBattleController):

    @property
    def vehicleTrackers(self):
        raise NotImplementedError
        return

    @property
    def vehicleMechanicTrackers(self):
        raise NotImplementedError
        return
