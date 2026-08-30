class IClanListener(object):

    def onClanEnableChanged(self, enabled):
        return

    def onClanInvitesCountReceived(self, clanDbID, invitesCount):
        return

    def onClanAppsCountReceived(self, clanDbID, appsCount):
        return

    def onClanInfoReceived(self, clanDbID, clanInfo):
        return

    def onClanWebVitalInfoChanged(self, clanDbID, fieldName, value):
        return

    def onAccountClanProfileChanged(self, profile):
        return

    def onAccountClanInfoReceived(self, info):
        return

    def onAccountInvitesReceived(self, invites):
        return

    def onAccountAppsReceived(self, applications):
        return

    def onAccountWebVitalInfoChanged(self, fieldName, value):
        return

    def onClanAppStateChanged(self, appId, state):
        return

    def onClanInvitesStateChanged(self, inviteIds, state):
        return

    def onNotifyCenterNotificationReceived(self, notifID, item):
        return

    def onMembersListChanged(self, members):
        return
