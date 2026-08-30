from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class AbstractRallyWindowMeta(AbstractWindowView):

    def canGoBack(self):
        self._printOverrideError(b'canGoBack')
        return

    def onBrowseRallies(self):
        self._printOverrideError(b'onBrowseRallies')
        return

    def onCreateRally(self):
        self._printOverrideError(b'onCreateRally')
        return

    def onJoinRally(self, rallyId, slotIndex, peripheryId):
        self._printOverrideError(b'onJoinRally')
        return

    def as_loadViewS(self, flashAlias, pyAlias):
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(flashAlias, pyAlias)
        return

    def as_enableWndCloseBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableWndCloseBtn(value)
        return
