from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewModulesTabMeta(BaseDAAPIComponent):

    def setActiveState(self, isActive):
        self._printOverrideError(b'setActiveState')
        return

    def as_setStatusInfoS(self, message, tooltipId, vehicleType, needToShowAnim):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusInfo(message, tooltipId, vehicleType, needToShowAnim)
        return
