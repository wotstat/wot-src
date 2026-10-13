from __future__ import absolute_import
import typing
from gui.shared.utils.decorators import ReprInjector
from vehicles.mechanics.common.mechanic_interfaces import IMechanicWithVariants
if typing.TYPE_CHECKING:
    from items.vehicle_mechanics_types import VehicleMechanicVariant

@ReprInjector.simple(b'mechanicVariant')
class MechanicParamsWithVariants(IMechanicWithVariants):

    def __init__(self, mechanicVariant):
        super(MechanicParamsWithVariants, self).__init__()
        self._mechanicVariant = mechanicVariant
        return

    @property
    def mechanicVariant(self):
        return self._mechanicVariant
