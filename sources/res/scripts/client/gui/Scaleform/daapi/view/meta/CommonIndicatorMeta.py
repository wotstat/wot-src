from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CommonIndicatorMeta(BaseDAAPIComponent):

    def as_setStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state)
        return

    def as_setVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(visible)
        return

    def as_setCountS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setCount(count)
        return

    def as_setProgressS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress)
        return

    def as_setActiveTimeS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setActiveTime(time)
        return

    def as_updateLayoutS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLayout(x, y)
        return
