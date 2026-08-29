from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ChannelComponentMeta(BaseDAAPIComponent):

    def isJoined(self):
        self._printOverrideError(b'isJoined')
        return

    def sendMessage(self, message):
        self._printOverrideError(b'sendMessage')
        return

    def getHistory(self):
        self._printOverrideError(b'getHistory')
        return

    def getMessageMaxLength(self):
        self._printOverrideError(b'getMessageMaxLength')
        return

    def onLinkClick(self, linkCode):
        self._printOverrideError(b'onLinkClick')
        return

    def as_notifyInfoChangedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_notifyInfoChanged()
        return

    def as_setJoinedS(self, flag):
        if self._isDAAPIInited():
            return self.flashObject.as_setJoined(flag)
        return

    def as_addMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_addMessage(message)
        return

    def as_getLastUnsentMessageS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getLastUnsentMessage()
        return

    def as_setLastUnsentMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setLastUnsentMessage(message)
        return
