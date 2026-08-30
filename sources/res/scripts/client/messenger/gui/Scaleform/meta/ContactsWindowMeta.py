from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ContactsWindowMeta(AbstractWindowView):

    def searchContact(self, criteria):
        self._printOverrideError(b'searchContact')
        return

    def addToFriends(self, uid, name):
        self._printOverrideError(b'addToFriends')
        return

    def addToIgnored(self, uid, name):
        self._printOverrideError(b'addToIgnored')
        return

    def isEnabledInRoaming(self, uid):
        self._printOverrideError(b'isEnabledInRoaming')
        return

    def as_getFriendsDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getFriendsDP()
        return

    def as_getClanDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getClanDP()
        return

    def as_getIgnoredDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getIgnoredDP()
        return

    def as_getMutedDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMutedDP()
        return

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()
        return

    def as_setSearchResultTextS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchResultText(message)
        return

    def as_frozenSearchActionS(self, flag):
        if self._isDAAPIInited():
            return self.flashObject.as_frozenSearchAction(flag)
        return
