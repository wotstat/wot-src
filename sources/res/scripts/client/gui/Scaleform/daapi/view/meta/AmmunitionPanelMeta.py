from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AmmunitionPanelMeta(BaseDAAPIComponent):

    def showRepairDialog(self):
        self._printOverrideError(b'showRepairDialog')
        return

    def showCustomization(self):
        self._printOverrideError(b'showCustomization')
        return

    def toRentContinue(self):
        self._printOverrideError(b'toRentContinue')
        return

    def showChangeNation(self):
        self._printOverrideError(b'showChangeNation')
        return

    def as_setWarningStateS(self, stateWarning):
        if self._isDAAPIInited():
            return self.flashObject.as_setWarningState(stateWarning)
        return

    def as_updateVehicleStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)
        return

    def as_setCustomizationBtnCounterS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCustomizationBtnCounter(value)
        return
