from __future__ import absolute_import
from gui.lobby_state_machine.states import SFViewLobbyState, SubScopeSubLayerState
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES

def registerStates(machine):
    machine.addState(FunRandomPrimeTimeState())
    return


def registerTransitions(machine):
    funRandomPrimeTime = machine.getStateByCls(FunRandomPrimeTimeState)
    machine.addNavigationTransitionFromParent(funRandomPrimeTime)
    return


@SubScopeSubLayerState.parentOf
class FunRandomPrimeTimeState(SFViewLobbyState):
    STATE_ID = b'funRandomPrimeTime'
    VIEW_KEY = ViewKey(FUNRANDOM_ALIASES.FUN_RANDOM_PRIME_TIME)
