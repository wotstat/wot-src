from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PvePrimaryObjectiveMeta(BaseDAAPIComponent):

    def as_showMessageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showMessage(value)
        return

    def as_hideMessageS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideMessage()
        return

    def as_playFxS(self, value, loop):
        if self._isDAAPIInited():
            return self.flashObject.as_playFx(value, loop)
        return

    def as_setHintStateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintState(value)
        return

    def as_setTimerBackgroundS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerBackground(value)
        return

    def as_setTimerStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerState(state)
        return

    def as_updateTimeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTime(value)
        return

    def as_updateProgressBarS(self, value, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressBar(value, vis)
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_showResultS(self, isWin, icon, header):
        if self._isDAAPIInited():
            return self.flashObject.as_showResult(isWin, icon, header)
        return

    def as_hideResultS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideResult()
        return
