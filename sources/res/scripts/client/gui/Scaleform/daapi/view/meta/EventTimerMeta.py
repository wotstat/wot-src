from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventTimerMeta(BaseDAAPIComponent):

    def as_updateTimeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTime(value)
        return

    def as_setTimerStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerState(state)
        return

    def as_playFxS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playFx()
        return

    def as_updateTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTitle(value)
        return

    def as_updateProgressBarS(self, value, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressBar(value, vis)
        return
