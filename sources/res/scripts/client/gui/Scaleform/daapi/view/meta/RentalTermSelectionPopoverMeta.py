from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class RentalTermSelectionPopoverMeta(SmartPopOverView):

    def selectTerm(self, itemId):
        self._printOverrideError(b'selectTerm')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return
