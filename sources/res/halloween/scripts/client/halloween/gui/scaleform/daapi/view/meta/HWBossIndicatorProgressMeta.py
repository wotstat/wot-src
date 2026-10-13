from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HWBossIndicatorProgressMeta(BaseDAAPIComponent):

    def as_setValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setValue(value)
        return

    def as_setIndicatorEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setIndicatorEnabled(isEnabled)
        return

    def as_setAlphaS(self, alpha):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlpha(alpha)
        return
