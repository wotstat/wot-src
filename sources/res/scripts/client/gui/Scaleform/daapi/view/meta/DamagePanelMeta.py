from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DamagePanelMeta(BaseDAAPIComponent):

    def clickToTankmanIcon(self, entityName):
        self._printOverrideError(b'clickToTankmanIcon')
        return

    def clickToDeviceIcon(self, entityName):
        self._printOverrideError(b'clickToDeviceIcon')
        return

    def clickToFireIcon(self):
        self._printOverrideError(b'clickToFireIcon')
        return

    def clickToStunTimer(self):
        self._printOverrideError(b'clickToStunTimer')
        return

    def getTooltipData(self, entityName, state):
        self._printOverrideError(b'getTooltipData')
        return

    def as_setPlayerInfoS(self, playerName, clanName, regionName, vehicleTypeName):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerInfo(playerName, clanName, regionName, vehicleTypeName)
        return

    def as_setupS(self, healthStr, progress, indicatorType, crewLayout, yawLimits, hasTurretRotator, isAutoRotationOn):
        if self._isDAAPIInited():
            return self.flashObject.as_setup(healthStr, progress, indicatorType, crewLayout, yawLimits, hasTurretRotator, isAutoRotationOn)
        return

    def as_setupWheeledS(self, wheelsCount):
        if self._isDAAPIInited():
            return self.flashObject.as_setupWheeled(wheelsCount)
        return

    def as_updateHealthS(self, healthStr, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHealth(healthStr, progress)
        return

    def as_updateSpeedS(self, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSpeed(speed)
        return

    def as_showRammingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showRamming()
        return

    def as_setCruiseModeS(self, mode):
        if self._isDAAPIInited():
            return self.flashObject.as_setCruiseMode(mode)
        return

    def as_setAutoRotationS(self, isOn):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoRotation(isOn)
        return

    def as_updateDeviceStateS(self, deviceName, deviceState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDeviceState(deviceName, deviceState)
        return

    def as_updateRepairingDeviceS(self, deviceName, percents, seconds, repairMode):
        if self._isDAAPIInited():
            return self.flashObject.as_updateRepairingDevice(deviceName, percents, seconds, repairMode)
        return

    def as_setVehicleDestroyedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleDestroyed()
        return

    def as_setCrewDeactivatedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewDeactivated()
        return

    def as_showS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_show(isShow)
        return

    def as_setFireInVehicleS(self, isInFire):
        if self._isDAAPIInited():
            return self.flashObject.as_setFireInVehicle(isInFire)
        return

    def as_setStaticDataS(self, fireMsg):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(fireMsg)
        return

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()
        return

    def as_setPlaybackSpeedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlaybackSpeed(value)
        return

    def as_showStatusS(self, statusID, time, animated):
        if self._isDAAPIInited():
            return self.flashObject.as_showStatus(statusID, time, animated)
        return

    def as_hideStatusS(self, statusID, animated):
        if self._isDAAPIInited():
            return self.flashObject.as_hideStatus(statusID, animated)
        return

    def as_setStatusTimerSnapshotS(self, statusID, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusTimerSnapshot(statusID, timeLeft)
        return

    def as_setSpeedModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeedMode(value)
        return

    def as_setRepairTimesVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setRepairTimesVisible(value)
        return
