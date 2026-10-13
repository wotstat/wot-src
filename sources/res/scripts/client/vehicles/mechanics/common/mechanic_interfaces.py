from __future__ import absolute_import
import typing
from vehicles.components.component_interfaces import IVehicleSlotComponent
if typing.TYPE_CHECKING:
    from items.vehicle_mechanics_types import VehicleMechanicVariant, VehicleMechanicKey

class IMechanicComponentLogic(object):

    @property
    def isValid(self):
        raise NotImplementedError
        return

    @property
    def vehicleMechanicKey(self):
        raise NotImplementedError
        return


class IMechanicComponent(IVehicleSlotComponent, IMechanicComponentLogic):
    pass


class IMechanicWithVariants(object):

    @property
    def mechanicVariant(self):
        raise NotImplementedError
        return
