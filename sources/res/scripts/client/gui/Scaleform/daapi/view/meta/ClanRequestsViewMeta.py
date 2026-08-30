from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesWindowAbstractTabView import ClanInvitesWindowAbstractTabView

class ClanRequestsViewMeta(ClanInvitesWindowAbstractTabView):

    def acceptRequest(self, dbId):
        self._printOverrideError(b'acceptRequest')
        return

    def declineRequest(self, dbId):
        self._printOverrideError(b'declineRequest')
        return

    def sendInvite(self, dbId):
        self._printOverrideError(b'sendInvite')
        return
