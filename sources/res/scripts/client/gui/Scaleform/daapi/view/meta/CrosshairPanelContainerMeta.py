from gui.Scaleform.daapi.view.meta.DAAPISimpleContainerMeta import DAAPISimpleContainerMeta

class CrosshairPanelContainerMeta(DAAPISimpleContainerMeta):

    def as_playSound(self, value):
        self._printOverrideError(b'as_playSound')
        return

    def as_setSettingsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(data)
        return

    def as_setSizeS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(width, height)
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

    def as_setReloadingS(self, duration, baseTime, startTime, isReloading, isShotAvailable=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloading(duration, baseTime, startTime, isReloading, isShotAvailable)
        return

    def as_setReloadingAsPercentS(self, time, percent, isReloading, isShotAvailable=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingAsPercent(time, percent, isReloading, isShotAvailable)
        return

    def as_setIsInControllableReloadS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsInControllableReload(value)
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

    def as_setClipParamsS(self, clipCapacity, burst, reloadingType):
        if self._isDAAPIInited():
            return self.flashObject.as_setClipParams(clipCapacity, burst, reloadingType)
        return

    def as_setDistanceS(self, dist):
        if self._isDAAPIInited():
            return self.flashObject.as_setDistance(dist)
        return

    def as_clearDistanceS(self, immediate):
        if self._isDAAPIInited():
            return self.flashObject.as_clearDistance(immediate)
        return

    def as_setAverageDamageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAverageDamage(value)
        return

    def as_clearAverageDamageS(self, immediate):
        if self._isDAAPIInited():
            return self.flashObject.as_clearAverageDamage(immediate)
        return

    def as_updatePlayerInfoS(self, info):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerInfo(info)
        return

    def as_updateAmmoStateS(self, ammoState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAmmoState(ammoState)
        return

    def as_setZoomS(self, zoomStr, zoomFactor):
        if self._isDAAPIInited():
            return self.flashObject.as_setZoom(zoomStr, zoomFactor)
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

    def as_autoloaderUpdateS(self, timeLeft, baseTime, isCritical=False, isTimerOn=False, isRedText=False):
        if self._isDAAPIInited():
            return self.flashObject.as_autoloaderUpdate(timeLeft, baseTime, isCritical, isTimerOn, isRedText)
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

    def as_setAutoloaderPercentS(self, percent, sec, isCritical, isTimerOn, isTimerRed):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoloaderPercent(percent, sec, isCritical, isTimerOn, isTimerRed)
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

    def as_setTwinGunMarkerActiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTwinGunMarkerActive(value)
        return

    def as_setTwinGunMarkerStateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTwinGunMarkerState(value)
        return

    def as_showPenetrationFxS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showPenetrationFx()
        return

    def as_runCameraTransitionFxS(self, direction, duration):
        if self._isDAAPIInited():
            return self.flashObject.as_runCameraTransitionFx(direction, duration)
        return

    def as_updateScaleWidgetS(self, positionValue):
        if self._isDAAPIInited():
            return self.flashObject.as_updateScaleWidget(positionValue)
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

    def as_setAimDamageStageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAimDamageStage(value)
        return

    def as_setAccuracyStacksProgressS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setAccuracyStacksProgress(count)
        return

    def as_setChargeGunActiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChargeGunActive(value)
        return

    def as_setChargeGunStateS(self, progress, stacks, isShootBlock):
        if self._isDAAPIInited():
            return self.flashObject.as_setChargeGunState(progress, stacks, isShootBlock)
        return

    def as_setLowChargeInitialTimeS(self, baseTime, lowChargeTime, almostFinishedTime, lowChargeCap):
        if self._isDAAPIInited():
            return self.flashObject.as_setLowChargeInitialTime(baseTime, lowChargeTime, almostFinishedTime, lowChargeCap)
        return

    def as_setLowChargeTimeLeftS(self, timeLeft, state, isReplay):
        if self._isDAAPIInited():
            return self.flashObject.as_setLowChargeTimeLeft(timeLeft, state, isReplay)
        return

    def as_setReloadBoostS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadBoost(value)
        return

    def as_setReloadBoostBorderS(self, boostVisible, active):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadBoostBorder(boostVisible, active)
        return

    def as_setReloadBoostBorderBlinkS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadBoostBorderBlink()
        return

    def as_setNetSeparatorTypeS(self, netSeparatorType):
        if self._isDAAPIInited():
            return self.flashObject.as_setNetSeparatorType(netSeparatorType)
        return

    def as_setChargeableBurstModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChargeableBurstMode(value)
        return

    def as_setSecondaryGunMarkerActiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryGunMarkerActive(value)
        return

    def as_setDispersionCircleThicknessS(self, isBold):
        if self._isDAAPIInited():
            return self.flashObject.as_setDispersionCircleThickness(isBold)
        return

    def as_setAlternateZoomPositionS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlternateZoomPosition(value)
        return
