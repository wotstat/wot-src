from gui.Scaleform.daapi.view.meta.DAAPISimpleContainerMeta import DAAPISimpleContainerMeta

class SplashScreenMeta(DAAPISimpleContainerMeta):

    def onComplete(self):
        self._printOverrideError(b'onComplete')
        return

    def onError(self):
        self._printOverrideError(b'onError')
        return

    def fadeOutComplete(self):
        self._printOverrideError(b'fadeOutComplete')
        return

    def as_playVideoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_playVideo(data)
        return

    def as_setSizeS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(width, height)
        return

    def as_fadeOutS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_fadeOut(time)
        return
