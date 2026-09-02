from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleDamageLogPanelMeta(BaseDAAPIComponent):

    def as_setSettingsDamageLogComponentS(self, isVisible, isColorBlind):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettingsDamageLogComponent(isVisible, isColorBlind)
        return

    def as_summaryStatsS(self, damage, blocked, assist, stun):
        if self._isDAAPIInited():
            return self.flashObject.as_summaryStats(damage, blocked, assist, stun)
        return

    def as_updateSummaryDamageValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryDamageValue(value)
        return

    def as_updateSummaryBlockedValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryBlockedValue(value)
        return

    def as_updateSummaryAssistValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryAssistValue(value)
        return

    def as_updateSummaryStunValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryStunValue(value)
        return

    def as_detailStatsTopS(self, isVisible, isShortMode, messages):
        if self._isDAAPIInited():
            return self.flashObject.as_detailStatsTop(isVisible, isShortMode, messages)
        return

    def as_addDetailMessageTopS(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG, shellModeImg=b''):
        if self._isDAAPIInited():
            return self.flashObject.as_addDetailMessageTop(value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG, shellModeImg)
        return

    def as_detailStatsBottomS(self, isVisible, isShortMode, messages):
        if self._isDAAPIInited():
            return self.flashObject.as_detailStatsBottom(isVisible, isShortMode, messages)
        return

    def as_addDetailMessageBottomS(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG, shellModeImg=b''):
        if self._isDAAPIInited():
            return self.flashObject.as_addDetailMessageBottom(value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG, shellModeImg)
        return

    def as_isDownCtrlButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isDownCtrlButton(value)
        return

    def as_isDownAltButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isDownAltButton(value)
        return
