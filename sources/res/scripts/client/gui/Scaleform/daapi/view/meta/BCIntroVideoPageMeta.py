from gui.Scaleform.framework.entities.View import View

class BCIntroVideoPageMeta(View):

    def videoStarted(self):
        self._printOverrideError(b'videoStarted')
        return

    def videoFinished(self):
        self._printOverrideError(b'videoFinished')
        return

    def goToBattle(self):
        self._printOverrideError(b'goToBattle')
        return

    def skipBootcamp(self):
        self._printOverrideError(b'skipBootcamp')
        return

    def handleError(self, data):
        self._printOverrideError(b'handleError')
        return

    def onHighlightShow(self):
        self._printOverrideError(b'onHighlightShow')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_updateProgressS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(percent)
        return

    def as_loadedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loaded()
        return

    def as_showIntroPageS(self, value, showRewards=False):
        if self._isDAAPIInited():
            return self.flashObject.as_showIntroPage(value, showRewards)
        return

    def as_pausePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_pausePlayback()
        return

    def as_resumePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resumePlayback()
        return
