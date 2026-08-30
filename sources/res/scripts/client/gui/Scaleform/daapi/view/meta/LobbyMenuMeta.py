from gui.Scaleform.framework.entities.View import View

class LobbyMenuMeta(View):

    def settingsClick(self):
        self._printOverrideError(b'settingsClick')
        return

    def cancelClick(self):
        self._printOverrideError(b'cancelClick')
        return

    def refuseTraining(self):
        self._printOverrideError(b'refuseTraining')
        return

    def logoffClick(self):
        self._printOverrideError(b'logoffClick')
        return

    def quitClick(self):
        self._printOverrideError(b'quitClick')
        return

    def postClick(self):
        self._printOverrideError(b'postClick')
        return

    def onCounterNeedUpdate(self):
        self._printOverrideError(b'onCounterNeedUpdate')
        return

    def bootcampClick(self):
        self._printOverrideError(b'bootcampClick')
        return

    def onEscapePress(self):
        self._printOverrideError(b'onEscapePress')
        return

    def manualClick(self):
        self._printOverrideError(b'manualClick')
        return

    def as_setVersionMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setVersionMessage(message)
        return

    def as_setCounterS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_setCounter(counters)
        return

    def as_removeCounterS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_removeCounter(counters)
        return

    def as_setBootcampButtonLabelS(self, label, icon):
        if self._isDAAPIInited():
            return self.flashObject.as_setBootcampButtonLabel(label, icon)
        return

    def as_setPostButtonIconsS(self, iconClose, iconOpen):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostButtonIcons(iconClose, iconOpen)
        return

    def as_setPostButtonVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostButtonVisible(isVisible)
        return

    def as_showBootcampButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showBootcampButton(value)
        return

    def as_showManualButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showManualButton(value)
        return

    def as_setManualButtonIconS(self, icon):
        if self._isDAAPIInited():
            return self.flashObject.as_setManualButtonIcon(icon)
        return

    def as_setMenuStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setMenuState(state)
        return
