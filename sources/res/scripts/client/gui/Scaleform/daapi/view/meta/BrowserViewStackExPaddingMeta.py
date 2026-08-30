from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BrowserViewStackExPaddingMeta(BaseDAAPIComponent):

    def setViewSize(self, width, height):
        self._printOverrideError(b'setViewSize')
        return

    def as_setAllowWaitingS(self, value, startImmediately):
        if self._isDAAPIInited():
            return self.flashObject.as_setAllowWaiting(value, startImmediately)
        return

    def as_setWaitingMessageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaitingMessage(value)
        return

    def as_createBrowserViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createBrowserView()
        return
