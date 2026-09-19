from __future__ import absolute_import
from collections import OrderedDict
from typing import TYPE_CHECKING
import BigWorld
from constants import IS_CLIENT, IS_CELLAPP
from dict2model import fields, models, schemas
from dict2model.exceptions import ValidationError
from dict2model.fields import Field
from frameworks_common.state_machine import State, StateFlags, StateEvent, StringEventTransition, StringEvent
if TYPE_CHECKING:
    from typing import List, Optional, Iterable

class TimedStateModel(State, models.Model):
    __slots__ = (b'_eventDuration', b'_callbackId', b'_prepareTransitions', b'_flags')

    def __init__(self, stateID=b'', eventDuration=0, transition=None, flags=None):
        super(TimedStateModel, self).__init__(stateID=stateID, flags=flags or StateFlags.UNDEFINED)
        self._eventDuration = eventDuration
        self._callbackId = None
        self._prepareTransitions = transition or []
        return

    def _onEntered(self, event):
        if self._eventDuration == 0:
            return
        if IS_CELLAPP:
            self._callbackId = BigWorld.addTimer(self._onTimeout, self._eventDuration)
        if IS_CLIENT:
            self._callbackId = BigWorld.callback(self._eventDuration, self._onTimeout)
        return

    def _onExited(self):
        if self._callbackId is not None:
            if IS_CELLAPP:
                BigWorld.delTimer(self._callbackId)
            if IS_CLIENT:
                BigWorld.cancelCallback(self._callbackId)
            self._callbackId = None
        return

    def _onTimeout(self, *_, **__):
        self._onExited()
        if not self.getMachine() or not self.getMachine().isRunning():
            return
        nextTransitions = self.getPreparedTransitions()
        if nextTransitions:
            self.getMachine().post(StringEvent(nextTransitions[0]))
        return

    def getEventDuration(self):
        return self._eventDuration

    def getPreparedTransitions(self):
        return self._prepareTransitions


class StateMachineModel(models.Model):
    __slots__ = (b'_states',)

    def __init__(self, state):
        super(StateMachineModel, self).__init__()
        self._states = OrderedDict()
        for state_ in state:
            self._states[state_.getStateID()] = state_

        self.setTimedStateTransition(state)
        return

    def setTimedStateTransition(self, states):
        for state in states:
            if not isinstance(state, TimedStateModel):
                continue
            for transition in state.getPreparedTransitions():
                state.addTransition(StringEventTransition(transition), target=self._states[transition])

        return

    def getStates(self):
        return list(self._states.values())


class StateFlagField(Field):

    def _serialize(self, incoming, **kwargs):
        if hasattr(StateFlags, incoming):
            return getattr(StateFlags, incoming, StateFlags.UNDEFINED)
        raise ValidationError((b"Wrong value for flag: {}, value doesn't exists in StateFlags.").format(incoming))
        return

    def _deserialize(self, incoming, **kwargs):
        if hasattr(StateFlags, incoming):
            return getattr(StateFlags, incoming, StateFlags.UNDEFINED)
        raise ValidationError((b"Wrong value for flag: {}, value doesn't exists in StateFlags.").format(incoming))
        return


timedStateSchema = schemas.Schema(modelClass=TimedStateModel, fields={b'stateID': (fields.String(required=True)), 
   b'eventDuration': (fields.Integer(required=False, default=0)), 
   b'transition': (fields.UniCapList(required=False, fieldOrSchema=fields.String(required=True))), 
   b'flags': (StateFlagField(required=False))})
stateMachineSchema = schemas.Schema(modelClass=StateMachineModel, fields={b'state': (fields.UniCapList(required=False, fieldOrSchema=timedStateSchema))})
