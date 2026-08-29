from gui.Scaleform.daapi.view.meta.DAAPISimpleContainerMeta import DAAPISimpleContainerMeta

class CrosshairPanelContainerMeta(DAAPISimpleContainerMeta):

    def as_playSound(self, value):
        self._printOverrideError(b'as_playSound')
        return

    def as_setSettingsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(data)
        return

    def as_setScaleS(self, scale):
        if self._isDAAPIInited():
            return self.flashObject.as_setScale(scale)
        return

    def as_setViewS(self, viewId, settingId):
        if self._isDAAPIInited():
            return self.flashObject.as_setView(viewId, settingId)
        return

    def as_recreateDeviceS(self, offsetX, offsetY):
        if self._isDAAPIInited():
            return self.flashObject.as_recreateDevice(offsetX, offsetY)
        return

    def as_setReloadingCounterShownS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingCounterShown(visible)
        return

    def as_setReloadingS(self, duration, baseTime, startTime, isReloading):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloading(duration, baseTime, startTime, isReloading)
        return

    def as_setReloadingAsPercentS(self, percent, isReloading):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingAsPercent(percent, isReloading)
        return

    def as_setBoostAsPercentS(self, percent, duration):
        if self._isDAAPIInited():
            return self.flashObject.as_setBoostAsPercent(percent, duration)
        return

    def as_setHealthS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setHealth(percent)
        return

    def as_setAmmoStockS(self, quantity, quantityInClip, clipState, clipReloaded=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setAmmoStock(quantity, quantityInClip, clipState, clipReloaded)
        return

    def as_setClipParamsS(self, clipCapacity, burst, clipType=0):
        if self._isDAAPIInited():
            return self.flashObject.as_setClipParams(clipCapacity, burst, clipType)
        return

    def as_setDistanceS(self, dist):
        if self._isDAAPIInited():
            return self.flashObject.as_setDistance(dist)
        return

    def as_clearDistanceS(self, immediate):
        if self._isDAAPIInited():
            return self.flashObject.as_clearDistance(immediate)
        return

    def as_updatePlayerInfoS(self, info):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerInfo(info)
        return

    def as_updateAmmoStateS(self, ammoState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAmmoState(ammoState)
        return

    def as_setZoomS(self, zoomStr):
        if self._isDAAPIInited():
            return self.flashObject.as_setZoom(zoomStr)
        return

    def as_createGunMarkerS(self, viewID, linkage, name):
        if self._isDAAPIInited():
            return self.flashObject.as_createGunMarker(viewID, linkage, name)
        return

    def as_destroyGunMarkerS(self, name):
        if self._isDAAPIInited():
            return self.flashObject.as_destroyGunMarker(name)
        return

    def as_setGunMarkerColorS(self, name, colorName):
        if self._isDAAPIInited():
            return self.flashObject.as_setGunMarkerColor(name, colorName)
        return

    def as_setNetVisibleS(self, mask):
        if self._isDAAPIInited():
            return self.flashObject.as_setNetVisible(mask)
        return

    def as_setNetSeparatorVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setNetSeparatorVisible(isVisible)
        return

    def as_setNetTypeS(self, netType):
        if self._isDAAPIInited():
            return self.flashObject.as_setNetType(netType)
        return

    def as_autoloaderUpdateS(self, timeLeft, baseTime, isPause=False, isStun=False, isTimerOn=False, isRedText=False):
        if self._isDAAPIInited():
            return self.flashObject.as_autoloaderUpdate(timeLeft, baseTime, isPause, isStun, isTimerOn, isRedText)
        return

    def as_setAutoloaderReloadingS(self, duration, baseTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoloaderReloading(duration, baseTime)
        return

    def as_showBoostS(self, duration, baseTime):
        if self._isDAAPIInited():
            return self.flashObject.as_showBoost(duration, baseTime)
        return

    def as_hideBoostS(self, showAnimation):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBoost(showAnimation)
        return

    def as_showShotS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showShot()
        return

    def as_setAutoloaderReloadasPercentS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoloaderReloadasPercent(percent)
        return

    def as_setAutoloaderPercentS(self, percent, sec, isTimerOn, isTimerRed):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoloaderPercent(percent, sec, isTimerOn, isTimerRed)
        return

    def as_setSpeedModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeedMode(value)
        return

    def as_updateSpeedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSpeed(value)
        return

    def as_updateBurnoutS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBurnout(value)
        return

    def as_addSpeedometerS(self, maxSpeedNormalMode, maxSpeedSpeedMode):
        if self._isDAAPIInited():
            return self.flashObject.as_addSpeedometer(maxSpeedNormalMode, maxSpeedSpeedMode)
        return

    def as_removeSpeedometerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeSpeedometer()
        return

    def as_setBurnoutWarningS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBurnoutWarning(value)
        return

    def as_stopBurnoutWarningS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_stopBurnoutWarning()
        return

    def as_setEngineCrushErrorS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEngineCrushError(value)
        return

    def as_stopEngineCrushErrorS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_stopEngineCrushError()
        return

    def as_startDualGunChargingS(self, timeLeft, totalTime):
        if self._isDAAPIInited():
            return self.flashObject.as_startDualGunCharging(timeLeft, totalTime)
        return

    def as_cancelDualGunChargeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_cancelDualGunCharge()
        return

    def as_updateDualGunMarkerStateS(self, markerState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDualGunMarkerState(markerState)
        return

    def as_runCameraTransitionFxS(self, activeGunId, animationDuration):
        if self._isDAAPIInited():
            return self.flashObject.as_runCameraTransitionFx(activeGunId, animationDuration)
        return

    def as_updateScaleWidgetS(self, positionValue):
        if self._isDAAPIInited():
            return self.flashObject.as_updateScaleWidget(positionValue)
        return

    def as_updateScaleStepsS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_updateScaleSteps(count)
        return

    def as_setGunMarkersIndicatorsS(self, indicators):
        if self._isDAAPIInited():
            return self.flashObject.as_setGunMarkersIndicators(indicators)
        return

    def as_setShotFlyTimesS(self, shotFlyTimes):
        if self._isDAAPIInited():
            return self.flashObject.as_setShotFlyTimes(shotFlyTimes)
        return

    def as_setShellChangeTimeS(self, quickChangerIsActive, shellChangeTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setShellChangeTime(quickChangerIsActive, shellChangeTime)
        return

    def as_isFadedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isFaded(value)
        return

    def as_blinkReloadTimeS(self, blinkType):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkReloadTime(blinkType)
        return

    def as_setDualAccActiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDualAccActive(value)
        return

    def as_addOverheatS(self, overheatMark):
        if self._isDAAPIInited():
            return self.flashObject.as_addOverheat(overheatMark)
        return

    def as_removeOverheatS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeOverheat()
        return

    def as_setDistanceVisibilityS(self, value, distance):
        if self._isDAAPIInited():
            return self.flashObject.as_setDistanceVisibility(value, distance)
        return

    def as_setOverheatProgressS(self, value, timeLeft, isSnapshot=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setOverheatProgress(value, timeLeft, isSnapshot)
        return

    def as_setOverheatStatusS(self, isOverheated=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setOverheatStatus(isOverheated)
        return

    def as_setOverheatStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setOverheatState(state)
        return

    def as_setCoolantAbilityReloadingPenaltyS(self, baseValue, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolantAbilityReloadingPenalty(baseValue, seconds)
        return

    def as_addCoolantAbilityReloadingPenaltyS(self, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_addCoolantAbilityReloadingPenalty(seconds)
        return

    def as_setAbilityModifierS(self, value, immediately=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setAbilityModifier(value, immediately)
        return

    def as_setShotFlyTimeIndVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setShotFlyTimeIndVisibility(isVisible)
        return

    def as_setShotFlyTimeIndValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setShotFlyTimeIndValue(value)
        return

    def as_setShotDamageIndVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setShotDamageIndVisibility(isVisible)
        return

    def as_setShotDamageIndValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setShotDamageIndValue(value)
        return

    def as_animShotHitMarkerS(self, animState):
        if self._isDAAPIInited():
            return self.flashObject.as_animShotHitMarker(animState)
        return

    def as_setShotHitMarkerVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setShotHitMarkerVisibility(isVisible)
        return

    def as_setGunCoolingTimeS(self, isActive, secondsLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setGunCoolingTime(isActive, secondsLeft)
        return

    def as_setGunCoolingVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setGunCoolingVisibility(isVisible)
        return
