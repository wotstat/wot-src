from __future__ import absolute_import
import typing
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import HeatingZonesGunParams

class IHeatingZonesGunComponentParams(object):

    @classmethod
    def fromMechanicParams(cls, params):
        raise NotImplementedError
        return

    @property
    def lowZonePercent(self):
        raise NotImplementedError
        return

    @property
    def mediumZonePercent(self):
        raise NotImplementedError
        return


class IHeatingZonesGunMechanicState(IMechanicState):

    @classmethod
    def fromComponentStatus(cls, heatingZoneState, params):
        raise NotImplementedError
        return

    @property
    def isComfortZone(self):
        raise NotImplementedError
        return

    @property
    def heatingZoneState(self):
        raise NotImplementedError
        return
