from __future__ import absolute_import
from frameworks.state_machine import StateEvent
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.events import OneSecondEvent
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.transitions import ToStateTransition, BaseTimerCondition
from pve_battle_hud import PrimaryObjectiveState

class ToAppearanceTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToAppearanceTransition, self).__init__(PrimaryObjectiveState.APPEARANCE)
        return


class ToRegularTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToRegularTransition, self).__init__(PrimaryObjectiveState.REGULAR)
        return


class ToRemindTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToRemindTransition, self).__init__(PrimaryObjectiveState.REMIND)
        return


class ToLastRemindTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToLastRemindTransition, self).__init__(PrimaryObjectiveState.LAST_REMIND)
        return


class ToLargeTimerTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToLargeTimerTransition, self).__init__(PrimaryObjectiveState.LARGE_TIMER)
        return


class ToCountdownTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToCountdownTransition, self).__init__(PrimaryObjectiveState.COUNTDOWN, priority=2)
        return


class ToSuccessTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToSuccessTransition, self).__init__(PrimaryObjectiveState.SUCCESS, priority=1)
        return


class ToFailureTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToFailureTransition, self).__init__(PrimaryObjectiveState.FAILURE, priority=1)
        return


class ToHiddenTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToHiddenTransition, self).__init__(PrimaryObjectiveState.HIDDEN, priority=0)
        return


class RemindTimerCondition(BaseTimerCondition):

    def _condition(self, event, timerValue=0):
        if isinstance(event, OneSecondEvent) and event.lastTime:
            source = self.getSource()
            _, clientSettings = source.getSettings()
            remindTimers = getattr(clientSettings, b'remindTimers')
            if remindTimers:
                for remindTimer in remindTimers[:-1]:
                    result = super(RemindTimerCondition, self)._condition(event, remindTimer)
                    if result:
                        return True

        return False


class LastRemindTimerCondition(BaseTimerCondition):

    def _condition(self, event, timerValue=0):
        if isinstance(event, OneSecondEvent) and event.lastTime:
            source = self.getSource()
            _, clientSettings = source.getSettings()
            remindTimers = getattr(clientSettings, b'remindTimers')
            if remindTimers:
                return super(LastRemindTimerCondition, self)._condition(event, remindTimers[-1])
        return False
