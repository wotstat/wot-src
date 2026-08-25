from __future__ import absolute_import
import typing
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import OverheatGunParams
    from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import ITemperatureGunMechanicState

class IOverheatGunComponentParams(object):

    @classmethod
    def fromMechanicParams(cls, params):
        raise NotImplementedError
        return

    @property
    def overheatWarnPercent(self):
        raise NotImplementedError
        return

    @property
    def overheatOffPercent(self):
        raise NotImplementedError
        return

    @property
    def overheatOffThreshold(self):
        raise NotImplementedError
        return


class IOverheatGunMechanicState(IMechanicState):

    @classmethod
    def fromComponentStatus(cls, overheatState, params):
        raise NotImplementedError
        return

    @property
    def isOverheated(self):
        raise NotImplementedError
        return

    @property
    def overheatState(self):
        raise NotImplementedError
        return

    def overheatTimeLeft(self, temperatureGunState):
        raise NotImplementedError
        return
