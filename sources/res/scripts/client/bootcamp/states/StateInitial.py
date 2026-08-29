from bootcamp.states import STATE
from bootcamp.states.AbstractState import AbstractState

class StateInitial(AbstractState):

    def __init__(self):
        super(StateInitial, self).__init__(STATE.INITIAL)
        return

    def handleKeyEvent(self, event):
        return

    def _doActivate(self):
        return

    def _doDeactivate(self):
        return
