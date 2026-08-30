from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileBaseViewMeta(BaseDAAPIComponent):

    def onHeaderButtonClick(self, actionId):
        self._printOverrideError(b'onHeaderButtonClick')
        return

    def viewSize(self, width, height):
        self._printOverrideError(b'viewSize')
        return

    def as_setClanInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanInfo(data)
        return

    def as_setHeaderStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderState(data)
        return

    def as_setClanEmblemS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(source)
        return

    def as_setDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(value)
        return

    def as_showWaitingS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(value)
        return

    def as_showDummyS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showDummy(data)
        return

    def as_hideDummyS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideDummy()
        return

    def as_loadBrowserS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loadBrowser()
        return
