from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ClanInvitesWindowMeta(AbstractWindowView):

    def onInvitesButtonClick(self):
        self._printOverrideError(b'onInvitesButtonClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
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

    def as_setControlsEnabledS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsEnabled(enabled)
        return
