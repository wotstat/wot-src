from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class WindowViewMeta(WrapperViewMeta):

    def onWindowMinimize(self):
        self._printOverrideError(b'onWindowMinimize')
        return

    def onSourceLoaded(self):
        self._printOverrideError(b'onSourceLoaded')
        return

    def onTryClosing(self):
        self._printOverrideError(b'onTryClosing')
        return

    def as_getGeometryS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getGeometry()
        return

    def as_setGeometryS(self, x, y, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setGeometry(x, y, width, height)
        return
