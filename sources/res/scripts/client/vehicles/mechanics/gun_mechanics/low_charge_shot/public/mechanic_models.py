from __future__ import absolute_import
import typing
from constants import LowChargeShotVisualState
from gui.shared.utils.decorators import ReprInjector
from vehicles.mechanics.mechanic_states import IMechanicState

@ReprInjector.simple(b'visualState', b'fullShotChangeTime')
class LowChargeShotPublicMechanicState(typing.NamedTuple(b'LowChargeShotPublicMechanicState', (
 (
  b'visualState', LowChargeShotVisualState),
 (
  b'fullShotChangeTime', float),
 (
  b'almostFinishedTime', float))), IMechanicState):

    @classmethod
    def fromComponentStatus(cls, state, params):
        return cls(state.visualState, state.fullShotChangeTime, params.almostFinishedTime)

    def isTransition(self, other):
        return self.visualState != other.visualState
