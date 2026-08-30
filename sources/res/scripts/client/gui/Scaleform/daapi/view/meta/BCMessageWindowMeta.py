from tutorial.gui.Scaleform.pop_ups import TutorialDialog

class BCMessageWindowMeta(TutorialDialog):

    def onMessageRemoved(self):
        self._printOverrideError(b'onMessageRemoved')
        return

    def onMessageAppear(self, rendrerer):
        self._printOverrideError(b'onMessageAppear')
        return

    def onMessageDisappear(self, rendrerer, animation):
        self._printOverrideError(b'onMessageDisappear')
        return

    def onMessageExecuted(self, rendrerer):
        self._printOverrideError(b'onMessageExecuted')
        return

    def onMessageButtonClicked(self):
        self._printOverrideError(b'onMessageButtonClicked')
        return

    def onMessageAnimationStopped(self, animation):
        self._printOverrideError(b'onMessageAnimationStopped')
        return

    def onMessageAnimationStarted(self, animation):
        self._printOverrideError(b'onMessageAnimationStarted')
        return

    def hideBlur(self):
        self._printOverrideError(b'hideBlur')
        return

    def as_setMessageDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessageData(value)
        return

    def as_blurOtherWindowsS(self, layer):
        if self._isDAAPIInited():
            return self.flashObject.as_blurOtherWindows(layer)
        return
