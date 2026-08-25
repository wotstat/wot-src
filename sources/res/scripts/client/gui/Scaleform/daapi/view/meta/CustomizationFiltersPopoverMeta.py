from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationFiltersPopoverMeta(SmartPopOverView):

    def changeGroup(self, itemId):
        self._printOverrideError(b'changeGroup')
        return

    def setDefaultFilter(self):
        self._printOverrideError(b'setDefaultFilter')
        return

    def setShowOnlyHistoric(self, value):
        self._printOverrideError(b'setShowOnlyHistoric')
        return

    def setShowOnlyAcquired(self, value):
        self._printOverrideError(b'setShowOnlyAcquired')
        return

    def setHideOnAnotherVeh(self, value):
        self._printOverrideError(b'setHideOnAnotherVeh')
        return

    def setShowOnlyProgressionDecals(self, value):
        self._printOverrideError(b'setShowOnlyProgressionDecals')
        return

    def setShowOnlyEditableStyles(self, value):
        self._printOverrideError(b'setShowOnlyEditableStyles')
        return

    def onFilterChange(self, index, value):
        self._printOverrideError(b'onFilterChange')
        return

    def onFormChange(self, index, value):
        self._printOverrideError(b'onFormChange')
        return

    def onRarityChange(self, index, value):
        self._printOverrideError(b'onRarityChange')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_enableDefBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableDefBtn(value)
        return
