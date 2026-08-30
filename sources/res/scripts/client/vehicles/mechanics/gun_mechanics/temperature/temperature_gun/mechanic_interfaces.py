from __future__ import absolute_import
import typing
from vehicles.mechanics.gun_mechanics.temperature.common import ITemperatureComponentParams, ITemperatureMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import TemperatureGunParams

class ITemperatureGunComponentParamsLogic(object):

    @classmethod
    def fromMechanicParams(cls, params):
        raise NotImplementedError
        return

    @property
    def coolingDelay(self):
        raise NotImplementedError
        return


class ITemperatureGunComponentParams(ITemperatureComponentParams, ITemperatureGunComponentParamsLogic):
    pass


class ITemperatureGunMechanicStateLogic(object):

    @classmethod
    def fromComponentStatus(cls, status, params):
        raise NotImplementedError
        return

    def getCoolingTime(self, targetTemperature):
        raise NotImplementedError
        return


class ITemperatureGunMechanicState(ITemperatureMechanicState, ITemperatureGunMechanicStateLogic):
    pass
