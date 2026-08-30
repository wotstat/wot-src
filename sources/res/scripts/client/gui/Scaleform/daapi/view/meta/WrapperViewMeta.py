from gui.Scaleform.framework.entities.View import View

class WrapperViewMeta(View):

    def onWindowClose(self):
        self._printOverrideError(b'onWindowClose')
        return

    def as_showWaitingS(self, msg, props):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(msg, props)
        return

    def as_hideWaitingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideWaiting()
        return
