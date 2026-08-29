from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StoryModeTimerMeta(BaseDAAPIComponent):

    def as_updateTimeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTime(value)
        return

    def as_showMessageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showMessage(value)
        return

    def as_hideMessageS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideMessage()
        return

    def as_setTimerStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerState(state)
        return

    def as_setTimerBackgroundS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerBackground(value)
        return

    def as_setHintStateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintState(value)
        return

    def as_playFxS(self, value, loop, color):
        if self._isDAAPIInited():
            return self.flashObject.as_playFx(value, loop, color)
        return

    def as_updateTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTitle(value)
        return

    def as_updateObjectiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateObjective(value)
        return

    def as_updateObjectiveBigS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateObjectiveBig(value)
        return

    def as_updateProgressBarS(self, value, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressBar(value, vis)
        return
