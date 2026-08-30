from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class GameMessagesPanelMeta(BaseDAAPIComponent):

    def onMessageStarted(self, type, modificator, id):
        self._printOverrideError(b'onMessageStarted')
        return

    def onMessagePhaseStarted(self, type, modificator, id):
        self._printOverrideError(b'onMessagePhaseStarted')
        return

    def onMessageEnded(self, type, id):
        self._printOverrideError(b'onMessageEnded')
        return

    def onMessageHiding(self, type, id):
        self._printOverrideError(b'onMessageHiding')
        return

    def as_addMessageS(self, messageVO):
        if self._isDAAPIInited():
            return self.flashObject.as_addMessage(messageVO)
        return

    def as_clearMessagesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearMessages()
        return
