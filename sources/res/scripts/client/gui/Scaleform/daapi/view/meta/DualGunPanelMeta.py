from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DualGunPanelMeta(BaseDAAPIComponent):

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()
        return

    def as_setViewS(self, viewId):
        if self._isDAAPIInited():
            return self.flashObject.as_setView(viewId)
        return

    def as_setVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(visible)
        return

    def as_setPlaybackSpeedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlaybackSpeed(value)
        return

    def as_updateActiveGunS(self, activeGunId, timeLeft, totalTime):
        if self._isDAAPIInited():
            return self.flashObject.as_updateActiveGun(activeGunId, timeLeft, totalTime)
        return

    def as_readyForChargeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_readyForCharge()
        return

    def as_setGunStateS(self, gunId, state, timeLeft, totalTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setGunState(gunId, state, timeLeft, totalTime)
        return

    def as_startChargingS(self, timeLeft, totalTime):
        if self._isDAAPIInited():
            return self.flashObject.as_startCharging(timeLeft, totalTime)
        return

    def as_cancelChargeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_cancelCharge()
        return

    def as_disableChargeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_disableCharge()
        return

    def as_setCooldownS(self, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setCooldown(timeLeft)
        return

    def as_setDualShotModeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setDualShotMode()
        return

    def as_collapsePanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_collapsePanel()
        return

    def as_expandPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_expandPanel()
        return

    def as_setReloadingTimeIncreasedS(self, hasNegativeEffect):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingTimeIncreased(hasNegativeEffect)
        return

    def as_updateTotalTimeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTotalTime(value)
        return

    def as_setTimerVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerVisible(value)
        return

    def as_setChangeGunTweenPropsS(self, duration, delay):
        if self._isDAAPIInited():
            return self.flashObject.as_setChangeGunTweenProps(duration, delay)
        return
