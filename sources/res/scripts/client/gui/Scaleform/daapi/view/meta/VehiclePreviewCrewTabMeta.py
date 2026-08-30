from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewCrewTabMeta(BaseDAAPIComponent):

    def setActiveState(self, isActive):
        self._printOverrideError(b'setActiveState')
        return

    def getTooltipData(self, crewId):
        self._printOverrideError(b'getTooltipData')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
