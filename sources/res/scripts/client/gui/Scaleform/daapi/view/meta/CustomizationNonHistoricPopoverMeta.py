from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationNonHistoricPopoverMeta(SmartPopOverView):

    def remove(self, id, itemsList):
        self._printOverrideError(b'remove')
        return

    def removeAll(self):
        self._printOverrideError(b'removeAll')
        return

    def showOnlyNonHistoric(self, value):
        self._printOverrideError(b'showOnlyNonHistoric')
        return

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)
        return

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()
        return

    def as_showClearMessageS(self, isClear, message):
        if self._isDAAPIInited():
            return self.flashObject.as_showClearMessage(isClear, message)
        return
