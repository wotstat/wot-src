from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesViewWithTable import ClanInvitesViewWithTable

class ClanInvitesWindowAbstractTabViewMeta(ClanInvitesViewWithTable):

    def filterBy(self, filterName):
        self._printOverrideError(b'filterBy')
        return

    def as_updateFilterStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFilterState(data)
        return
