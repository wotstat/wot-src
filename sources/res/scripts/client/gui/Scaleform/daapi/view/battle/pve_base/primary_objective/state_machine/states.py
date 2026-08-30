from __future__ import absolute_import
import enum
from frameworks.state_machine import StateFlags
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.states import BaseTimerState, BaseState
from math_common import round_py2_style
from pve_battle_hud import PrimaryObjectiveState, getPveHudLogger
_logger = getPveHudLogger()

class TimerState(enum.IntEnum):
    SMALL = 0
    BIG = 1
    NO_TIMER = 2


class InitialState(BaseState):
    __slots__ = ()

    def __init__(self):
        super(InitialState, self).__init__(stateID=PrimaryObjectiveState.INITIAL, flags=StateFlags.INITIAL)
        return


class BaseViewTimerState(BaseTimerState):
    __slots__ = ()

    def tick(self, currentTime):
        super(BaseViewTimerState, self).tick(currentTime)
        serverSettings, _ = self.getSettings()
        finishTime = serverSettings.finishTime
        timeLeft = round_py2_style(finishTime - currentTime) if finishTime is not None else None
        self._view.updateTimer(timeLeft)
        return

    @property
    def _subheader(self):
        serverSettings, clientSettings = self.getSettings()
        return clientSettings.getSubheader(serverSettings.params)


class AppearanceState(BaseViewTimerState):
    __slots__ = ()

    def __init__(self):
        super(AppearanceState, self).__init__(stateID=PrimaryObjectiveState.APPEARANCE, flags=StateFlags.UNDEFINED)
        return

    def _showView(self):
        super(AppearanceState, self)._showView()
        serverSettings, clientSettings = self.getSettings()
        self._view.setTimerState(serverSettings.timer, TimerState.BIG)
        self._view.as_setTimerBackgroundS(True)
        self._view.updateHeaderWithSubheader(clientSettings.getHeader(), self._subheader)
        self._view.updateProgress(isVisible=False)
        self._view.playSound(clientSettings.startSound)
        return

    def _updateView(self):
        super(AppearanceState, self)._updateView()
        _, clientSettings = self.getSettings()
        self._view.updateHeaderWithSubheader(clientSettings.getHeader(), self._subheader)
        return


class RegularState(BaseViewTimerState):
    __slots__ = ()

    def __init__(self):
        super(RegularState, self).__init__(stateID=PrimaryObjectiveState.REGULAR, flags=StateFlags.UNDEFINED)
        return

    def _showView(self):
        super(RegularState, self)._showView()
        serverSettings, _ = self.getSettings()
        self._view.setTimerState(serverSettings.timer, TimerState.SMALL)
        self._view.as_setTimerBackgroundS(False)
        self._view.updateSubheader(self._subheader)
        self._view.updateProgress(serverSettings.progresses)
        return

    def _updateView(self):
        super(RegularState, self)._updateView()
        serverSettings, _ = self.getSettings()
        self._view.updateSubheader(self._subheader)
        self._view.updateProgress(serverSettings.progresses)
        return


class RemindState(BaseViewTimerState):
    __slots__ = ()

    def __init__(self, stateID=PrimaryObjectiveState.REMIND, flags=StateFlags.UNDEFINED):
        super(RemindState, self).__init__(stateID=stateID, flags=flags)
        return

    def _showView(self):
        super(RemindState, self)._showView()
        serverSettings, clientSettings = self.getSettings()
        self._view.setTimerState(serverSettings.timer, TimerState.BIG)
        self._view.as_playFxS(True, False)
        self._view.as_setTimerBackgroundS(True)
        self._view.updateHeaderWithSubheader(clientSettings.getHeader(), self._subheader)
        self._view.updateProgress(isVisible=False)
        self._view.playSound(clientSettings.remindSound)
        return

    def _updateView(self):
        super(RemindState, self)._updateView()
        _, clientSettings = self.getSettings()
        self._view.updateHeaderWithSubheader(clientSettings.getHeader(), self._subheader)
        return


class LastRemindState(RemindState):
    __slots__ = ()

    def __init__(self):
        super(LastRemindState, self).__init__(stateID=PrimaryObjectiveState.LAST_REMIND, flags=StateFlags.UNDEFINED)
        return


class LargeTimerState(BaseViewTimerState):
    __slots__ = ()

    def __init__(self):
        super(LargeTimerState, self).__init__(stateID=PrimaryObjectiveState.LARGE_TIMER, flags=StateFlags.UNDEFINED)
        return

    def _showView(self):
        super(LargeTimerState, self)._showView()
        serverSettings, _ = self.getSettings()
        self._view.setTimerState(serverSettings.timer, TimerState.BIG)
        self._view.as_setTimerBackgroundS(False)
        self._view.updateSubheader(self._subheader)
        self._view.updateProgress(serverSettings.progresses)
        return

    def _updateView(self):
        super(LargeTimerState, self)._updateView()
        serverSettings, _ = self.getSettings()
        self._view.updateSubheader(self._subheader)
        self._view.updateProgress(serverSettings.progresses)
        return


class CountdownState(BaseViewTimerState):
    __slots__ = ()

    def __init__(self):
        super(CountdownState, self).__init__(stateID=PrimaryObjectiveState.COUNTDOWN, flags=StateFlags.UNDEFINED)
        return

    def tick(self, currentTime):
        super(CountdownState, self).tick(currentTime)
        _, clientSettings = self.getSettings()
        self._view.playSound(clientSettings.countdownSound)
        return

    def _showView(self):
        super(CountdownState, self)._showView()
        serverSettings, _ = self.getSettings()
        self._view.setTimerState(serverSettings.timer, TimerState.BIG)
        self._view.as_setTimerBackgroundS(False)
        self._view.updateSubheader(self._subheader)
        self._view.updateProgress(serverSettings.progresses)
        self._view.as_playFxS(True, True)
        return

    def _updateView(self):
        super(CountdownState, self)._updateView()
        serverSettings, _ = self.getSettings()
        self._view.updateSubheader(self._subheader)
        self._view.updateProgress(serverSettings.progresses)
        return

    def _onExited(self):
        self._view.as_playFxS(False, False)
        super(CountdownState, self)._onExited()
        return


class SuccessState(BaseState):
    __slots__ = ()

    def __init__(self):
        super(SuccessState, self).__init__(stateID=PrimaryObjectiveState.SUCCESS, flags=StateFlags.UNDEFINED)
        return

    def _showView(self):
        super(SuccessState, self)._showView()
        _, clientSettings = self.getSettings()
        self._view.hideObjective()
        self._view.showMessage(True, clientSettings.successIcon, clientSettings.getSuccess())
        self._view.playSound(clientSettings.successSound)
        return


class FailureState(BaseState):
    __slots__ = ()

    def __init__(self):
        super(FailureState, self).__init__(stateID=PrimaryObjectiveState.FAILURE, flags=StateFlags.UNDEFINED)
        return

    def _showView(self):
        super(FailureState, self)._showView()
        _, clientSettings = self.getSettings()
        self._view.hideObjective()
        self._view.showMessage(False, clientSettings.failureIcon, clientSettings.getFailure())
        self._view.as_setTimerBackgroundS(True)
        self._view.playSound(clientSettings.failureSound)
        return


class HiddenState(BaseState):
    __slots__ = ()

    def __init__(self):
        super(HiddenState, self).__init__(stateID=PrimaryObjectiveState.HIDDEN, flags=StateFlags.FINAL)
        return

    def _showView(self):
        super(HiddenState, self)._showView()
        self._view.hideMessage()
        self._view.hideObjective()
        return
