from helpers.i18n import makeString
from timer_base import PreBattleTimerBase
from gui.battle_control.battle_constants import COUNTDOWN_STATE
_g_timerSettings = {}

class CustomTextPrebattleTimer(PreBattleTimerBase):

    def __init__(self):
        super(CustomTextPrebattleTimer, self).__init__()
        self.wasCustomWinConditionAdded = False
        return

    def updateBattleCtx(self, battleCtx):
        self._battleTypeStr = battleCtx.getArenaDescriptionString(isInBattle=False)
        self.as_setMessageS(self._getMessage())
        return

    def setCountdown(self, state, timeLeft):
        if not self.wasCustomWinConditionAdded:
            if _g_timerSettings:
                msg = makeString(_g_timerSettings.get(b'subheader', b''))
                self.as_setWinConditionTextS(msg)
                self.as_setMessageS(self._getMessage())
                self.wasCustomWinConditionAdded = True
        super(CustomTextPrebattleTimer, self).setCountdown(state, timeLeft)
        return

    def hideCountdown(self, state, speed):
        if _g_timerSettings:
            msg = makeString(_g_timerSettings.get(b'battleStartMessage', b''))
            self.as_setMessageS(msg)
            self._clearTimeShiftCallback()
            self.as_hideAllS(speed != 0)
        else:
            super(CustomTextPrebattleTimer, self).hideCountdown(state, speed)
        return

    def _getMessage(self):
        if self._state == COUNTDOWN_STATE.WAIT:
            msg = super(CustomTextPrebattleTimer, self)._getMessage()
        elif _g_timerSettings:
            msg = makeString(_g_timerSettings.get(b'header', b''))
        else:
            msg = super(CustomTextPrebattleTimer, self)._getMessage()
        return msg

    def _dispose(self):
        _g_timerSettings.clear()
        super(CustomTextPrebattleTimer, self)._dispose()
        return


def setTimerSettings(header, message, subheader=None):
    _g_timerSettings[b'header'] = header
    _g_timerSettings[b'battleStartMessage'] = message
    if subheader is not None:
        _g_timerSettings[b'subheader'] = subheader
    return
