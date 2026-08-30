from __future__ import absolute_import
import typing, BigWorld
from frameworks_common.state_machine import StateMachine
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.events import OneSecondEvent, ToStateEvent
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.states import BaseTimerState
from helpers.CallbackDelayer import CallbackDelayer
if typing.TYPE_CHECKING:
    from frameworks_common.state_machine import StateEvent
STATE_TICK_INTERVAL = 1

class BaseStateMachine(StateMachine):

    def post(self, event):
        if not self.isRunning():
            return
        super(BaseStateMachine, self).post(event)
        return

    def postFinalState(self):
        for state in self.getChildrenStates():
            if state.isFinal():
                super(BaseStateMachine, self).post(ToStateEvent(state.getStateID()))
                return

        return

    def update(self):
        if not self.isRunning():
            return
        for state in self.getChildrenStates():
            if self.isStateEntered(state.getStateID()):
                state.update()

        return


class BaseTimerStateMachine(BaseStateMachine):
    __slots__ = (b'_callbackDelayer', b'_lastTime')

    def __init__(self):
        super(BaseTimerStateMachine, self).__init__()
        self._callbackDelayer = CallbackDelayer()
        self._lastTime = 0
        return

    def start(self, doValidate=True):
        super(BaseTimerStateMachine, self).start(doValidate)
        self._callbackDelayer.delayCallback(0, self._tick)
        return

    def stop(self):
        self._callbackDelayer.clearCallbacks()
        super(BaseTimerStateMachine, self).stop()
        return

    def _tick(self):
        currentTime = BigWorld.serverTime()
        self.post(OneSecondEvent(lastTime=self._lastTime, currentTime=currentTime))
        for state in self.getChildrenStates():
            if self.isStateEntered(state.getStateID()) and isinstance(state, BaseTimerState):
                state.tick(currentTime)

        self._lastTime = currentTime
        return STATE_TICK_INTERVAL
