from gui.Scaleform.framework.entities.View import View

class IntroVideoMeta(View):

    def onVideoStarted(self):
        self._printOverrideError(b'onVideoStarted')
        return

    def onVideoComplete(self):
        self._printOverrideError(b'onVideoComplete')
        return

    def onSkipButtonVisible(self):
        self._printOverrideError(b'onSkipButtonVisible')
        return

    def onSkipButtonClicked(self):
        self._printOverrideError(b'onSkipButtonClicked')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setCurrentSubtitleS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setCurrentSubtitle(text)
        return

    def as_loadedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loaded()
        return

    def as_pausePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_pausePlayback()
        return

    def as_resumePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resumePlayback()
        return

    def as_handleKeydownS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_handleKeydown()
        return
