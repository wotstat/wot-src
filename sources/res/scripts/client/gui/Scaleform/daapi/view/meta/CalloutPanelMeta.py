from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CalloutPanelMeta(BaseDAAPIComponent):

    def onHideCompleted(self):
        self._printOverrideError(b'onHideCompleted')
        return

    def onHideStart(self):
        self._printOverrideError(b'onHideStart')
        return

    def as_setDataS(self, action, vehicleType, vehicleName, leftText, rightText, keyText):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(action, vehicleType, vehicleName, leftText, rightText, keyText)
        return

    def as_setHideDataS(self, wasAnswered, answeredAction):
        if self._isDAAPIInited():
            return self.flashObject.as_setHideData(wasAnswered, answeredAction)
        return

    def as_setCrosshairTypeS(self, viewID):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrosshairType(viewID)
        return
