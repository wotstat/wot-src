from gui.Scaleform.framework.entities.View import View

class BCOutroVideoPageMeta(View):

    def videoFinished(self, skipped):
        self._printOverrideError(b'videoFinished')
        return

    def handleError(self, data):
        self._printOverrideError(b'handleError')
        return

    def as_playVideoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_playVideo(data)
        return

    def as_pausePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_pausePlayback()
        return

    def as_resumePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resumePlayback()
        return
