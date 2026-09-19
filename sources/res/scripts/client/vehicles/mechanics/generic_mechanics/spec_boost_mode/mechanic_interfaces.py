from __future__ import absolute_import
import typing
from vehicles.mechanics.common.mechanic_interfaces import IMechanicWithVariants
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import SpecBoostModeParams

class ISpecBoostModeMechanicParams(IMechanicWithVariants):

    @classmethod
    def fromMechanicParams(cls, params):
        raise NotImplementedError
        return


class ISpecBoostModeMechanicState(IMechanicState):

    @classmethod
    def fromComponentStatus(cls, status):
        raise NotImplementedError
        return

    @property
    def progress(self):
        raise NotImplementedError
        return

    @property
    def timeLeft(self):
        raise NotImplementedError
        return

    @property
    def state(self):
        raise NotImplementedError
        return
