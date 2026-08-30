from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SendInvitesWindowMeta(AbstractWindowView):

    def showError(self, value):
        self._printOverrideError(b'showError')
        return

    def setOnlineFlag(self, value):
        self._printOverrideError(b'setOnlineFlag')
        return

    def sendInvites(self, accountsToInvite, comment):
        self._printOverrideError(b'sendInvites')
        return

    def getAllAvailableContacts(self):
        self._printOverrideError(b'getAllAvailableContacts')
        return

    def as_onReceiveSendInvitesCooldownS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_onReceiveSendInvitesCooldown(value)
        return

    def as_setDefaultOnlineFlagS(self, onlineFlag):
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultOnlineFlag(onlineFlag)
        return

    def as_setInvalidUserTagsS(self, tags):
        if self._isDAAPIInited():
            return self.flashObject.as_setInvalidUserTags(tags)
        return

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)
        return

    def as_onContactUpdatedS(self, contact):
        if self._isDAAPIInited():
            return self.flashObject.as_onContactUpdated(contact)
        return

    def as_onListStateChangedS(self, isEmpty):
        if self._isDAAPIInited():
            return self.flashObject.as_onListStateChanged(isEmpty)
        return

    def as_enableDescriptionS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_enableDescription(isEnabled)
        return

    def as_enableMassSendS(self, isEnabled, addAllTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_enableMassSend(isEnabled, addAllTooltip)
        return
