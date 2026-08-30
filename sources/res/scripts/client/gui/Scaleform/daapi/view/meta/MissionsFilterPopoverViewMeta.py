from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class MissionsFilterPopoverViewMeta(SmartPopOverView):

    def changeFilter(self, hideUnavailable, hideDone):
        self._printOverrideError(b'changeFilter')
        return

    def setDefaultFilter(self):
        self._printOverrideError(b'setDefaultFilter')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(data)
        return

    def as_enableDefaultBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableDefaultBtn(value)
        return
