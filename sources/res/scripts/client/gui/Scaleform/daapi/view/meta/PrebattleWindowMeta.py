from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class PrebattleWindowMeta(AbstractWindowView):

    def requestToReady(self, value):
        self._printOverrideError(b'requestToReady')
        return

    def requestToLeave(self):
        self._printOverrideError(b'requestToLeave')
        return

    def showPrebattleSendInvitesWindow(self):
        self._printOverrideError(b'showPrebattleSendInvitesWindow')
        return

    def showFAQWindow(self):
        self._printOverrideError(b'showFAQWindow')
        return

    def canSendInvite(self):
        self._printOverrideError(b'canSendInvite')
        return

    def canKickPlayer(self):
        self._printOverrideError(b'canKickPlayer')
        return

    def isPlayerReady(self):
        self._printOverrideError(b'isPlayerReady')
        return

    def isPlayerCreator(self):
        self._printOverrideError(b'isPlayerCreator')
        return

    def isReadyBtnEnabled(self):
        self._printOverrideError(b'isReadyBtnEnabled')
        return

    def isLeaveBtnEnabled(self):
        self._printOverrideError(b'isLeaveBtnEnabled')
        return

    def getClientID(self):
        self._printOverrideError(b'getClientID')
        return

    def as_setRosterListS(self, team, assigned, rosters):
        if self._isDAAPIInited():
            return self.flashObject.as_setRosterList(team, assigned, rosters)
        return

    def as_setPlayerStateS(self, team, assigned, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerState(team, assigned, data)
        return

    def as_enableLeaveBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableLeaveBtn(value)
        return

    def as_enableReadyBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableReadyBtn(value)
        return

    def as_setCoolDownForReadyButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownForReadyButton(value)
        return

    def as_resetReadyButtonCoolDownS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetReadyButtonCoolDown()
        return

    def as_toggleReadyBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleReadyBtn(value)
        return

    def as_refreshPermissionsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_refreshPermissions()
        return
