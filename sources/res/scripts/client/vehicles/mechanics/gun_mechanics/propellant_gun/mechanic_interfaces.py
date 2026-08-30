from __future__ import absolute_import
import typing
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import PropellantGunParams

class IPropellantGunComponentParams(object):

    @classmethod
    def fromMechanicParams(cls, params):
        raise NotImplementedError
        return

    @property
    def chargePerSec(self):
        raise NotImplementedError
        return

    @property
    def dischargePerSec(self):
        raise NotImplementedError
        return

    @property
    def maxCharge(self):
        raise NotImplementedError
        return

    @property
    def maxOvercharge(self):
        raise NotImplementedError
        return

    @property
    def stages(self):
        raise NotImplementedError
        return

    @property
    def forbiddenShells(self):
        raise NotImplementedError
        return


class IPropellantGunMechanicState(IMechanicState):

    @classmethod
    def fromComponentStatus(cls, status, params):
        raise NotImplementedError
        return

    @property
    def state(self):
        raise NotImplementedError
        return

    @property
    def currentStage(self):
        raise NotImplementedError
        return

    @property
    def currentCharge(self):
        raise NotImplementedError
        return

    @property
    def currentThreshold(self):
        raise NotImplementedError
        return

    @property
    def isOvercharge(self):
        raise NotImplementedError
        return

    @property
    def isAvailable(self):
        raise NotImplementedError
        return

    @property
    def timeLeft(self):
        raise NotImplementedError
        return

    @property
    def isLastStage(self):
        raise NotImplementedError
        return

    @property
    def isUsableShell(self):
        raise NotImplementedError
        return

    @property
    def lastShotTimestamp(self):
        raise NotImplementedError
        return

    @property
    def lastShotCharge(self):
        raise NotImplementedError
        return

    def getCurrentDamageFactor(self, progress=None):
        raise NotImplementedError
        return
