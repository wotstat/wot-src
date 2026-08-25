from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RadarButtonMeta(BaseDAAPIComponent):

    def onClick(self):
        self._printOverrideError(b'onClick')
        return

    def as_initS(self, keyCode, sfKeyCode, iconPath, tooltipText, isReplay):
        if self._isDAAPIInited():
            return self.flashObject.as_init(keyCode, sfKeyCode, iconPath, tooltipText, isReplay)
        return

    def as_setCoolDownTimeS(self, duration, baseTime, startTime, animation):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownTime(duration, baseTime, startTime, animation)
        return

    def as_updateEnableS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEnable(isEnabled)
        return

    def as_setCoolDownPosAsPercentS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownPosAsPercent(percent)
        return

    def as_setCoolDownTimeSnapshotS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownTimeSnapshot(time)
        return
