from __future__ import absolute_import
import typing
from vehicles.components.component_interfaces import IVehicleSlotComponent
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_constants import VehicleMechanic

class IMechanicComponentLogic(object):

    @property
    def isValid(self):
        raise NotImplementedError
        return

    @property
    def vehicleMechanic(self):
        raise NotImplementedError
        return


class IMechanicComponent(IVehicleSlotComponent, IMechanicComponentLogic):
    pass
