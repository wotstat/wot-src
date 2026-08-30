from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ReceivedInviteWindowMeta(AbstractWindowView):

    def acceptInvite(self):
        self._printOverrideError(b'acceptInvite')
        return

    def declineInvite(self):
        self._printOverrideError(b'declineInvite')
        return

    def cancelInvite(self):
        self._printOverrideError(b'cancelInvite')
        return

    def as_setTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(value)
        return

    def as_setReceivedInviteInfoS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReceivedInviteInfo(value)
        return
