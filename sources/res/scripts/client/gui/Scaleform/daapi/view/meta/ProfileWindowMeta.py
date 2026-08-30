from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ProfileWindowMeta(AbstractWindowView):

    def userAddFriend(self):
        self._printOverrideError(b'userAddFriend')
        return

    def userAddToClan(self):
        self._printOverrideError(b'userAddToClan')
        return

    def userSetIgnored(self):
        self._printOverrideError(b'userSetIgnored')
        return

    def userCreatePrivateChannel(self):
        self._printOverrideError(b'userCreatePrivateChannel')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_addFriendAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_addFriendAvailable(value)
        return

    def as_addToClanAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_addToClanAvailable(value)
        return

    def as_addToClanVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_addToClanVisible(value)
        return

    def as_setIgnoredAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIgnoredAvailable(value)
        return

    def as_setCreateChannelAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCreateChannelAvailable(value)
        return
