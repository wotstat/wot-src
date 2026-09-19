from __future__ import absolute_import
from functools import wraps
import BigWorld, Event
from constants import ARENA_PERIOD
from script_component.DynamicScriptComponent import DynamicScriptComponent
from vehicle_systems.stricted_loading import makeCallbackWeak

def delayEventWrapper(eventName, propertyName):

    def decorator(func):

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.scheduleEvent(eventName, propertyName)
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


class ScoreComponent(DynamicScriptComponent):

    def __init__(self):
        super(ScoreComponent, self).__init__()
        self.onTeamsScoreUpdated = Event.SafeEvent()
        self.onPersonalScoreUpdated = Event.SafeEvent()
        self._pendingEvents = []
        return

    def _onAvatarReady(self):
        arena = BigWorld.player().arena
        if arena.period >= ARENA_PERIOD.BATTLE:
            self.set_teamScore({})
            self.set_vehiclesScore({})
        return

    def onDestroy(self):
        self._pendingEvents = []
        self.onTeamsScoreUpdated.clear()
        self.onPersonalScoreUpdated.clear()
        super(ScoreComponent, self).onDestroy()
        return

    @delayEventWrapper(b'onTeamsScoreUpdated', b'teamScore')
    def set_teamScore(self, _):
        return

    @delayEventWrapper(b'onPersonalScoreUpdated', b'vehiclesScore')
    def set_vehiclesScore(self, _):
        return

    def scheduleEvent(self, eventName, propertyName):
        eventTuple = (
         eventName, propertyName)
        if eventTuple not in self._pendingEvents:
            needsScheduling = not self._pendingEvents
            self._pendingEvents.append(eventTuple)
            if needsScheduling:
                BigWorld.callback(0.095, makeCallbackWeak(self._sendPendingEvents))
        return

    def _sendPendingEvents(self):
        self._pendingEvents, pendingEvents = [], self._pendingEvents
        for eventName, propertyName in pendingEvents:
            event = getattr(self, eventName, None)
            propertyValue = getattr(self, propertyName, None)
            if event is not None and propertyValue is not None:
                event(propertyValue)

        return
