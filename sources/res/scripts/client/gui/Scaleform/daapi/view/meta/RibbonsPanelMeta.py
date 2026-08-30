from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RibbonsPanelMeta(BaseDAAPIComponent):

    def onShow(self, ribbonId):
        self._printOverrideError(b'onShow')
        return

    def onChange(self):
        self._printOverrideError(b'onChange')
        return

    def onHide(self, ribbonId):
        self._printOverrideError(b'onHide')
        return

    def as_setupS(self, items, isExtendedAnim, isVisible, isWithRibbonName, isWithVehName, bonusLabels):
        if self._isDAAPIInited():
            return self.flashObject.as_setup(items, isExtendedAnim, isVisible, isWithRibbonName, isWithVehName, bonusLabels)
        return

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()
        return

    def as_addBattleEfficiencyEventS(self, ribbonType, ribbonId, leftFieldStr, vehName, vehType, rightFieldStr, bonusLabelIndex, role):
        if self._isDAAPIInited():
            return self.flashObject.as_addBattleEfficiencyEvent(ribbonType, ribbonId, leftFieldStr, vehName, vehType, rightFieldStr, bonusLabelIndex, role)
        return

    def as_updateBattleEfficiencyEventS(self, ribbonType, ribbonId, leftFieldStr, vehName, vehType, rightFieldStr, bonusLabelIndex, role):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBattleEfficiencyEvent(ribbonType, ribbonId, leftFieldStr, vehName, vehType, rightFieldStr, bonusLabelIndex, role)
        return

    def as_setSettingsS(self, isVisible, isExtendedAnim, isWithRibbonName, isWithVehName):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(isVisible, isExtendedAnim, isWithRibbonName, isWithVehName)
        return
