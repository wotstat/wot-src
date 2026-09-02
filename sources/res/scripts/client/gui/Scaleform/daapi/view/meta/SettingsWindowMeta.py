from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SettingsWindowMeta(AbstractWindowView):

    def applySettings(self, settings, isCloseWnd):
        self._printOverrideError(b'applySettings')
        return

    def autodetectQuality(self):
        self._printOverrideError(b'autodetectQuality')
        return

    def startVOIPTest(self, isVoiceTestStarted):
        self._printOverrideError(b'startVOIPTest')
        return

    def updateCaptureDevices(self):
        self._printOverrideError(b'updateCaptureDevices')
        return

    def onSettingsChange(self, controlID, controlVal):
        self._printOverrideError(b'onSettingsChange')
        return

    def altVoicesPreview(self):
        self._printOverrideError(b'altVoicesPreview')
        return

    def altBulbPreview(self, sampleID):
        self._printOverrideError(b'altBulbPreview')
        return

    def artyBulbPreview(self, sampleID):
        self._printOverrideError(b'artyBulbPreview')
        return

    def isSoundModeValid(self):
        self._printOverrideError(b'isSoundModeValid')
        return

    def showWarningDialog(self, dialogID, settings, isCloseWnd):
        self._printOverrideError(b'showWarningDialog')
        return

    def onTabSelected(self, tabId):
        self._printOverrideError(b'onTabSelected')
        return

    def onCounterTargetVisited(self, viewId, subViewId, controlsIDs):
        self._printOverrideError(b'onCounterTargetVisited')
        return

    def autodetectAcousticType(self):
        self._printOverrideError(b'autodetectAcousticType')
        return

    def canSelectAcousticType(self, index):
        self._printOverrideError(b'canSelectAcousticType')
        return

    def openGammaWizard(self, x, y, size):
        self._printOverrideError(b'openGammaWizard')
        return

    def openColorSettings(self):
        self._printOverrideError(b'openColorSettings')
        return

    def as_setDataS(self, settingsData):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(settingsData)
        return

    def as_setCaptureDevicesS(self, captureDeviceIdx, devicesData):
        if self._isDAAPIInited():
            return self.flashObject.as_setCaptureDevices(captureDeviceIdx, devicesData)
        return

    def as_updateVideoSettingsS(self, videoSettings):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVideoSettings(videoSettings)
        return

    def as_confirmWarningDialogS(self, isOk, dialogID):
        if self._isDAAPIInited():
            return self.flashObject.as_confirmWarningDialog(isOk, dialogID)
        return

    def as_showLimitedUISettingS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_showLimitedUISetting(isVisible)
        return

    def as_ConfirmationOfApplicationS(self, isApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_ConfirmationOfApplication(isApplied)
        return

    def as_openTabS(self, tabIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_openTab(tabIndex)
        return

    def as_setGraphicsPresetS(self, presetNum):
        if self._isDAAPIInited():
            return self.flashObject.as_setGraphicsPreset(presetNum)
        return

    def as_isPresetAppliedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_isPresetApplied()
        return

    def as_setCountersDataS(self, countersData):
        if self._isDAAPIInited():
            return self.flashObject.as_setCountersData(countersData)
        return

    def as_onSoundSpeakersPresetApplyS(self, isApply):
        if self._isDAAPIInited():
            return self.flashObject.as_onSoundSpeakersPresetApply(isApply)
        return

    def as_disableControlS(self, tabId, controlID, subTabId):
        if self._isDAAPIInited():
            return self.flashObject.as_disableControl(tabId, controlID, subTabId)
        return

    def as_setColorGradingTechniqueS(self, icon, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setColorGradingTechnique(icon, label)
        return

    def as_setFeedbackDataProviderS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_setFeedbackDataProvider(dataProvider)
        return

    def as_setDisabledTabsOverlayS(self, tabIndexes, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setDisabledTabsOverlay(tabIndexes, text)
        return

    def as_setBattleContextHintsEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleContextHintsEnabled(isEnabled)
        return

    def as_setBattleContextHintsResetEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleContextHintsResetEnabled(isEnabled)
        return

    def as_setTigerEventS(self, isInEvent):
        if self._isDAAPIInited():
            return self.flashObject.as_setTigerEvent(isInEvent)
        return

    def as_setVOIPTestReadyS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVOIPTestReady(value)
        return

    def as_setVOIPButtonStateS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setVOIPButtonState(enabled)
        return
