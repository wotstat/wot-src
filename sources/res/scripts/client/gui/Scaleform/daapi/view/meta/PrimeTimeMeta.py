from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class PrimeTimeMeta(WrapperViewMeta):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def apply(self):
        self._printOverrideError(b'apply')
        return

    def selectServer(self, id):
        self._printOverrideError(b'selectServer')
        return

    def as_getServersDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getServersDP()
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
