from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BrowserMeta(BaseDAAPIComponent):

    def browserAction(self, action):
        self._printOverrideError(b'browserAction')
        return

    def browserMove(self, x, y, z):
        self._printOverrideError(b'browserMove')
        return

    def browserDown(self, x, y, z):
        self._printOverrideError(b'browserDown')
        return

    def browserUp(self, x, y, z):
        self._printOverrideError(b'browserUp')
        return

    def browserFocusOut(self):
        self._printOverrideError(b'browserFocusOut')
        return

    def onBrowserShow(self, needRefresh):
        self._printOverrideError(b'onBrowserShow')
        return

    def onBrowserHide(self):
        self._printOverrideError(b'onBrowserHide')
        return

    def invalidateView(self):
        self._printOverrideError(b'invalidateView')
        return

    def setBrowserSize(self, width, height, scale):
        self._printOverrideError(b'setBrowserSize')
        return

    def as_loadBitmapS(self, url):
        if self._isDAAPIInited():
            return self.flashObject.as_loadBitmap(url)
        return

    def as_resizeS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_resize(width, height)
        return

    def as_loadingStartS(self, showContentUnderWaiting):
        if self._isDAAPIInited():
            return self.flashObject.as_loadingStart(showContentUnderWaiting)
        return

    def as_loadingStopS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loadingStop()
        return

    def as_showServiceViewS(self, header, description):
        if self._isDAAPIInited():
            return self.flashObject.as_showServiceView(header, description)
        return

    def as_hideServiceViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideServiceView()
        return

    def as_changeTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_changeTitle(title)
        return
