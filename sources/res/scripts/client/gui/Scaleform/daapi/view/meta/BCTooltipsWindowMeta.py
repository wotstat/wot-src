from gui.Scaleform.framework.entities.View import View

class BCTooltipsWindowMeta(View):

    def animFinish(self):
        self._printOverrideError(b'animFinish')
        return

    def as_setRotateTipVisibilityS(self, Visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setRotateTipVisibility(Visible)
        return

    def as_showHandlerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showHandler()
        return

    def as_completeHandlerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_completeHandler()
        return

    def as_hideHandlerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHandler()
        return
