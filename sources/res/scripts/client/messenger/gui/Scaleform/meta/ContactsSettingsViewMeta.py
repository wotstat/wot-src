from messenger.gui.Scaleform.view.lobby.BaseContactView import BaseContactView

class ContactsSettingsViewMeta(BaseContactView):

    def showOfflineUsers(self, value):
        self._printOverrideError(b'showOfflineUsers')
        return

    def showOthers(self, value):
        self._printOverrideError(b'showOthers')
        return

    def messagesNotFromContacts(self, value):
        self._printOverrideError(b'messagesNotFromContacts')
        return
