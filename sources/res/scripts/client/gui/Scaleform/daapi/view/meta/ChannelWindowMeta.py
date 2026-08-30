from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ChannelWindowMeta(AbstractWindowView):

    def showFAQWindow(self):
        self._printOverrideError(b'showFAQWindow')
        return

    def getClientID(self):
        self._printOverrideError(b'getClientID')
        return

    def as_setTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)
        return

    def as_setCloseEnabledS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setCloseEnabled(enabled)
        return
