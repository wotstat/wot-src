from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PveSecondaryObjectivesMeta(BaseDAAPIComponent):

    def as_addObjectS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addObject(data)
        return

    def as_removeObjectS(self, id, state):
        if self._isDAAPIInited():
            return self.flashObject.as_removeObject(id, state)
        return

    def as_setProgressBarValueS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressBarValue(id, value)
        return

    def as_updateTimeS(self, id, value, isWarning):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTime(id, value, isWarning)
        return

    def as_setAlarmS(self, id, isAlarm):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlarm(id, isAlarm)
        return

    def as_setTitleS(self, id, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(id, title)
        return

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()
        return
