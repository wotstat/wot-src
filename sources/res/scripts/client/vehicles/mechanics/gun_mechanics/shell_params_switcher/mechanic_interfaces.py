from __future__ import absolute_import
import typing
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import ShellSwitcherParams

class IShellParamsSwitcherComponentParams(object):

    @classmethod
    def fromMechanicParams(cls, params, vehIntCD):
        raise NotImplementedError
        return

    @property
    def shellSubtypes(self):
        raise NotImplementedError
        return


class IShellParamsSwitcherMechanicState(IMechanicState):

    @property
    def state(self):
        raise NotImplementedError
        return

    @property
    def baseState(self):
        raise NotImplementedError
        return

    @property
    def isActive(self):
        raise NotImplementedError
        return

    @property
    def lastActiveShotTimestamp(self):
        raise NotImplementedError
        return

    @property
    def mechanicSubtype(self):
        raise NotImplementedError
        return

    def isNoAmmo(self):
        raise NotImplementedError
        return

    def isCritState(self):
        raise NotImplementedError
        return

    def timeLeft(self):
        raise NotImplementedError
        return
