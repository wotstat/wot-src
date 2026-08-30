from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView

class ClanProfileSummaryViewMeta(ClanProfileBaseView):

    def hyperLinkGotoMap(self):
        self._printOverrideError(b'hyperLinkGotoMap')
        return

    def hyperLinkGotoDetailsMap(self):
        self._printOverrideError(b'hyperLinkGotoDetailsMap')
        return

    def sendRequestHandler(self):
        self._printOverrideError(b'sendRequestHandler')
        return

    def as_updateStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStatus(data)
        return

    def as_updateGeneralBlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGeneralBlock(data)
        return

    def as_updateFortBlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFortBlock(data)
        return

    def as_updateGlobalMapBlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGlobalMapBlock(data)
        return

    def as_updateLeaguesBlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLeaguesBlock(data)
        return
