from __future__ import absolute_import
import typing
from . import states as _states
from . import visitor
from .exceptions import StateMachineError
if typing.TYPE_CHECKING:
    from .transitions import BaseTransition
    from . import StateMachine

def _validateTransition(transition, upper=None):
    source = transition.getSource()
    if source is None:
        raise StateMachineError((b'{} has no source').format(transition))
    targets = transition.getTargets()
    if not targets:
        raise StateMachineError((b'{} has no targets').format(transition))
    if None in targets:
        raise StateMachineError((b'{} cannot have a None target').format(transition))
    if visitor.getLCA([source] + targets, upper=upper) is None:
        raise StateMachineError((b'States have no LCA in {}').format(transition))
    return


def _validateInitialState(state):
    initial = state.getInitial()
    if not initial:
        raise StateMachineError((b'{} has no initial state').format(state))
    return


def _validateState(state, machine):
    if state.isCompound():
        _validateInitialState(state)
    if state.isHistory() and len(state.getTransitions()) > 1:
        raise StateMachineError((b'History state {} should have only one transition').format(state))
    if not state.isFinal():
        for transition in state.getTransitions():
            _validateTransition(transition, upper=machine.getParent())

    return


def validate(machine):
    _validateInitialState(machine)
    ids = []
    for state in machine.visitInOrder((lambda item: isinstance(item, _states.State))):
        if state.isMachine():
            if state != machine:
                validate(state)
        else:
            stateID = state.getStateID()
            if stateID:
                if stateID not in ids:
                    ids.append(stateID)
                else:
                    raise StateMachineError((b'{} is not unique, each state must have unique ID').format(state))
            _validateState(state, machine)

    return
