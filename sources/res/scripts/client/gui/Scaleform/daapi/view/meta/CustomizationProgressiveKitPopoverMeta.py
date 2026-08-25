from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationProgressiveKitPopoverMeta(SmartPopOverView):

    def remove(self, id, itemsList, seasonType):
        self._printOverrideError(b'remove')
        return

    def removeAll(self):
        self._printOverrideError(b'removeAll')
        return

    def setToDefault(self):
        self._printOverrideError(b'setToDefault')
        return

    def onFilterChanged(self, showHistoric, showNonHistoric, showFantastic, showProgressiveLocked):
        self._printOverrideError(b'onFilterChanged')
        return

    def as_setHeaderS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(value)
        return

    def as_showClearMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_showClearMessage(message)
        return

    def as_setDefaultButtonEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultButtonEnabled(value)
        return

    def as_setItemsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setItems(value)
        return
