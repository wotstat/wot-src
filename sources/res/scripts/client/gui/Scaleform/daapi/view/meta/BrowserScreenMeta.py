from gui.Scaleform.framework.entities.View import View

class BrowserScreenMeta(View):

    def onCloseBtnClick(self):
        self._printOverrideError(b'onCloseBtnClick')
        return

    def onEscapePress(self):
        self._printOverrideError(b'onEscapePress')
        return

    def onFocusChange(self, hasFocus):
        self._printOverrideError(b'onFocusChange')
        return

    def viewSize(self, width, height):
        self._printOverrideError(b'viewSize')
        return

    def as_loadBrowserS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loadBrowser()
        return

    def as_setBrowserParamsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBrowserParams(data)
        return
