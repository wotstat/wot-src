from gui.Scaleform.framework.entities.View import View

class LobbyPageMeta(View):

    def moveSpace(self, x, y, delta):
        self._printOverrideError(b'moveSpace')
        return

    def getSubContainerTypes(self):
        self._printOverrideError(b'getSubContainerTypes')
        return

    def notifyCursorOver3dScene(self, isOver3dScene):
        self._printOverrideError(b'notifyCursorOver3dScene')
        return

    def notifyCursorDragging(self, isDragging):
        self._printOverrideError(b'notifyCursorDragging')
        return

    def setRequiresOldStyle(self, value):
        self._printOverrideError(b'setRequiresOldStyle')
        return

    def as_showHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showHelpLayout()
        return

    def as_closeHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closeHelpLayout()
        return

    def as_showWaitingS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(message)
        return

    def as_hideWaitingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideWaiting()
        return

    def as_setSubContainerItemsVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setSubContainerItemsVisibility(isVisible)
        return

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)
        return
