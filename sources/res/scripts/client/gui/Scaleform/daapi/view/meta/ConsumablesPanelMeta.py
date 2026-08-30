from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ConsumablesPanelMeta(BaseDAAPIComponent):

    def onClickedToSlot(self, keyCode, idx):
        self._printOverrideError(b'onClickedToSlot')
        return

    def onPopUpClosed(self):
        self._printOverrideError(b'onPopUpClosed')
        return

    def onPanelShown(self):
        self._printOverrideError(b'onPanelShown')
        return

    def onPanelHidden(self):
        self._printOverrideError(b'onPanelHidden')
        return

    def as_setKeysToSlotsS(self, slots):
        if self._isDAAPIInited():
            return self.flashObject.as_setKeysToSlots(slots)
        return

    def as_setItemQuantityInSlotS(self, idx, quantity):
        if self._isDAAPIInited():
            return self.flashObject.as_setItemQuantityInSlot(idx, quantity)
        return

    def as_setItemTimeQuantityInSlotS(self, idx, quantity, timeRemaining, maxTime, animation):
        if self._isDAAPIInited():
            return self.flashObject.as_setItemTimeQuantityInSlot(idx, quantity, timeRemaining, maxTime, animation)
        return

    def as_setCoolDownTimeS(self, idx, duration, baseTime, startTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownTime(idx, duration, baseTime, startTime)
        return

    def as_setCoolDownPosAsPercentS(self, idx, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownPosAsPercent(idx, percent)
        return

    def as_setCoolDownTimeSnapshotS(self, idx, time, isBaseTime, isFlash):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownTimeSnapshot(idx, time, isBaseTime, isFlash)
        return

    def as_addShellSlotS(self, idx, keyCode, sfKeyCode, quantity, clipCapacity, shellIconPath, noShellIconPath, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addShellSlot(idx, keyCode, sfKeyCode, quantity, clipCapacity, shellIconPath, noShellIconPath, tooltipText)
        return

    def as_setNextShellS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_setNextShell(idx)
        return

    def as_setCurrentShellS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_setCurrentShell(idx)
        return

    def as_addEquipmentSlotS(self, idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText, animation, tag):
        if self._isDAAPIInited():
            return self.flashObject.as_addEquipmentSlot(idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText, animation, tag)
        return

    def as_showEquipmentSlotsS(self, show):
        if self._isDAAPIInited():
            return self.flashObject.as_showEquipmentSlots(show)
        return

    def as_expandEquipmentSlotS(self, idx, slots):
        if self._isDAAPIInited():
            return self.flashObject.as_expandEquipmentSlot(idx, slots)
        return

    def as_collapseEquipmentSlotS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_collapseEquipmentSlot()
        return

    def as_updateLockedInformationS(self, idx, lockedID, tooltipStr):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLockedInformation(idx, lockedID, tooltipStr)
        return

    def as_updateLevelInformationS(self, idx, level):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLevelInformation(idx, level)
        return

    def as_updateTooltipS(self, idx, tooltipStr):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTooltip(idx, tooltipStr)
        return

    def as_addOptionalDeviceSlotS(self, idx, timeRemaining, iconPath, tooltipText, isTooltipSpecial, intCD, isUsed):
        if self._isDAAPIInited():
            return self.flashObject.as_addOptionalDeviceSlot(idx, timeRemaining, iconPath, tooltipText, isTooltipSpecial, intCD, isUsed)
        return

    def as_setOptionalDeviceUsedS(self, idx, isUsed):
        if self._isDAAPIInited():
            return self.flashObject.as_setOptionalDeviceUsed(idx, isUsed)
        return

    def as_setGlowS(self, idx, glowID):
        if self._isDAAPIInited():
            return self.flashObject.as_setGlow(idx, glowID)
        return

    def as_hideGlowS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_hideGlow(idx)
        return

    def as_setEquipmentActivatedS(self, idx, isActivated):
        if self._isDAAPIInited():
            return self.flashObject.as_setEquipmentActivated(idx, isActivated)
        return

    def as_handleAsReplayS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_handleAsReplay()
        return

    def as_handleAsObserverS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_handleAsObserver()
        return

    def as_isVisibleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_isVisible()
        return

    def as_resetS(self, slots=None):
        if self._isDAAPIInited():
            return self.flashObject.as_reset(slots)
        return

    def as_updateEntityStateS(self, entityName, entityState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEntityState(entityName, entityState)
        return

    def as_setPanelSettingsS(self, settingsId, isExtendedAnim):
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelSettings(settingsId, isExtendedAnim)
        return

    def as_setSPGShotResultS(self, shellIdx, shotResult):
        if self._isDAAPIInited():
            return self.flashObject.as_setSPGShotResult(shellIdx, shotResult)
        return

    def as_addAbilityEquipmentSlotS(self, idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText, animation):
        if self._isDAAPIInited():
            return self.flashObject.as_addAbilityEquipmentSlot(idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText, animation)
        return

    def as_setAbilityModifierS(self, value, immediately=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setAbilityModifier(value, immediately)
        return

    def as_addRoleSkillSlotS(self, idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText, animation):
        if self._isDAAPIInited():
            return self.flashObject.as_addRoleSkillSlot(idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText, animation)
        return

    def as_setRoleSkillSlotProgressS(self, idx, level=0, progress=0):
        if self._isDAAPIInited():
            return self.flashObject.as_setRoleSkillSlotProgress(idx, level, progress)
        return

    def as_setRoleSkillSlotCounterS(self, idx, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setRoleSkillSlotCounter(idx, value)
        return

    def as_addRespawnSlotS(self, idx, keyCode, sfKeyCode, quantity, tooltipText, isTooltipSpecial, isAvailable):
        if self._isDAAPIInited():
            return self.flashObject.as_addRespawnSlot(idx, keyCode, sfKeyCode, quantity, tooltipText, isTooltipSpecial, isAvailable)
        return

    def as_setRespawnSlotQuantityS(self, idx, quantity):
        if self._isDAAPIInited():
            return self.flashObject.as_setRespawnSlotQuantity(idx, quantity)
        return

    def as_setRespawnSlotStateS(self, idx, isAvailable):
        if self._isDAAPIInited():
            return self.flashObject.as_setRespawnSlotState(idx, isAvailable)
        return

    def as_showContextHintS(self, idx, label):
        if self._isDAAPIInited():
            return self.flashObject.as_showContextHint(idx, label)
        return

    def as_setContextHintStateS(self, idx, label, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setContextHintState(idx, label, state)
        return

    def as_hideContextHintS(self, animID):
        if self._isDAAPIInited():
            return self.flashObject.as_hideContextHint(animID)
        return
