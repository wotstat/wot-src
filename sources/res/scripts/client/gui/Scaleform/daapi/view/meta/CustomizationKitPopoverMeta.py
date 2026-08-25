from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationKitPopoverMeta(SmartPopOverView):

    def removeCustomizationKit(self):
        self._printOverrideError(b'removeCustomizationKit')
        return

    def updateAutoProlongation(self):
        self._printOverrideError(b'updateAutoProlongation')
        return

    def as_setHeaderS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(title)
        return

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()
        return

    def as_showClearMessageS(self, isClear, message):
        if self._isDAAPIInited():
            return self.flashObject.as_showClearMessage(isClear, message)
        return

    def as_setAutoProlongationCheckboxSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoProlongationCheckboxSelected(value)
        return

    def as_setAutoProlongationCheckboxEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoProlongationCheckboxEnabled(value)
        return
