from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesViewWithTable import ClanInvitesViewWithTable

class ClanPersonalInvitesViewMeta(ClanInvitesViewWithTable):

    def acceptInvite(self, dbID):
        self._printOverrideError(b'acceptInvite')
        return

    def declineInvite(self, dbID):
        self._printOverrideError(b'declineInvite')
        return

    def setInviteSelected(self, dbID, selected):
        self._printOverrideError(b'setInviteSelected')
        return

    def setSelectAllInvitesCheckBoxSelected(self, selected):
        self._printOverrideError(b'setSelectAllInvitesCheckBoxSelected')
        return

    def declineAllSelectedInvites(self):
        self._printOverrideError(b'declineAllSelectedInvites')
        return

    def as_setDeclineAllSelectedInvitesStateS(self, text, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setDeclineAllSelectedInvitesState(text, enabled)
        return

    def as_setSelectAllCheckboxStateS(self, selected, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectAllCheckboxState(selected, visible)
        return
