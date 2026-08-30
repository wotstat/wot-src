from __future__ import absolute_import
from vehicles.mechanics.mechanic_states import IMechanicState

class ITemperatureComponentParams(object):

    @property
    def coolingPerSec(self):
        raise NotImplementedError
        return

    @property
    def maxTemperature(self):
        raise NotImplementedError
        return


class ITemperatureMechanicState(IMechanicState):

    @property
    def state(self):
        raise NotImplementedError
        return

    @property
    def currentTemperature(self):
        raise NotImplementedError
        return

    @property
    def maxTemperature(self):
        raise NotImplementedError
        return

    @property
    def temperatureProgress(self):
        raise NotImplementedError
        return
