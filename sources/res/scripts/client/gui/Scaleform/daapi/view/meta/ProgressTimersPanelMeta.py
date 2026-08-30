from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ProgressTimersPanelMeta(BaseDAAPIComponent):

    def as_setLocalizedDataS(self, type, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setLocalizedData(type, data)
        return

    def as_showS(self, timerTypeID, state, id):
        if self._isDAAPIInited():
            return self.flashObject.as_show(timerTypeID, state, id)
        return

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
        return

    def as_setStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state)
        return

    def as_setTimeStringS(self, cooldownTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeString(cooldownTime)
        return

    def as_setProgressValueS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressValue(progress)
        return
