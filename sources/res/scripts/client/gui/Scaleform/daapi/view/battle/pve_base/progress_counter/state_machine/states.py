from __future__ import absolute_import
from frameworks_common.state_machine import StateFlags
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.states import BaseState
from pve_battle_hud import ProgressCounterState

class InitialState(BaseState):
    __slots__ = ()

    def __init__(self):
        super(InitialState, self).__init__(stateID=ProgressCounterState.INITIAL, flags=StateFlags.INITIAL)
        return


class BaseProgressCounterState(BaseState):

    def _showProgress(self, isAnimated):
        serverSettings, clientSettings = self.getSettings()
        icon = clientSettings.icon
        title = clientSettings.getHeader(serverSettings.params)
        self._view.as_setDataS(icon, title, isAnimated=isAnimated)
        return

    def _updateView(self):
        self._showProgress(isAnimated=True)
        return


class AppearanceState(BaseProgressCounterState):
    __slots__ = ()

    def __init__(self):
        super(AppearanceState, self).__init__(stateID=ProgressCounterState.APPEARANCE, flags=StateFlags.UNDEFINED)
        return

    def _showView(self):
        self._showProgress(isAnimated=True)
        return


class RegularState(BaseProgressCounterState):
    __slots__ = ()

    def __init__(self):
        super(RegularState, self).__init__(stateID=ProgressCounterState.REGULAR, flags=StateFlags.UNDEFINED)
        return

    def _showView(self):
        self._showProgress(isAnimated=False)
        return


class HiddenState(BaseState):
    __slots__ = ()

    def __init__(self):
        super(HiddenState, self).__init__(stateID=ProgressCounterState.HIDDEN, flags=StateFlags.FINAL)
        return

    def _showView(self):
        self._view.as_setDataS(b'', b'', isAnimated=True)
        return
