from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleMessengerMeta(BaseDAAPIComponent):

    def sendMessageToChannel(self, cid, message):
        self._printOverrideError(b'sendMessageToChannel')
        return

    def focusReceived(self):
        self._printOverrideError(b'focusReceived')
        return

    def focusLost(self):
        self._printOverrideError(b'focusLost')
        return

    def getToxicStatus(self, messageID):
        self._printOverrideError(b'getToxicStatus')
        return

    def onToxicButtonClicked(self, messageID, actionID):
        self._printOverrideError(b'onToxicButtonClicked')
        return

    def onToxicPanelClosed(self, messageID):
        self._printOverrideError(b'onToxicPanelClosed')
        return

    def as_enableToxicPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_enableToxicPanel()
        return

    def as_updateMessagesS(self, messageID, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessages(messageID, value)
        return

    def as_showGreenMessageS(self, message, messageID):
        if self._isDAAPIInited():
            return self.flashObject.as_showGreenMessage(message, messageID)
        return

    def as_showRedMessageS(self, message, messageID):
        if self._isDAAPIInited():
            return self.flashObject.as_showRedMessage(message, messageID)
        return

    def as_showBlackMessageS(self, message, messageID):
        if self._isDAAPIInited():
            return self.flashObject.as_showBlackMessage(message, messageID)
        return

    def as_showSelfMessageS(self, message, messageID):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelfMessage(message, messageID)
        return

    def as_setupListS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setupList(data)
        return

    def as_setReceiverS(self, data, isResetReceivers):
        if self._isDAAPIInited():
            return self.flashObject.as_setReceiver(data, isResetReceivers)
        return

    def as_changeReceiverS(self, receiver):
        if self._isDAAPIInited():
            return self.flashObject.as_changeReceiver(receiver)
        return

    def as_setActiveS(self, isActive):
        if self._isDAAPIInited():
            return self.flashObject.as_setActive(isActive)
        return

    def as_setFocusS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setFocus()
        return

    def as_unSetFocusS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_unSetFocus()
        return

    def as_setUserPreferencesS(self, tooltipStr):
        if self._isDAAPIInited():
            return self.flashObject.as_setUserPreferences(tooltipStr)
        return

    def as_setReceiversS(self, receivers):
        if self._isDAAPIInited():
            return self.flashObject.as_setReceivers(receivers)
        return

    def as_enableToSendMessageS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_enableToSendMessage()
        return

    def as_toggleCtrlPressFlagS(self, isCtrlPressed):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleCtrlPressFlag(isCtrlPressed)
        return

    def as_enterPressedS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_enterPressed(index)
        return

    def as_updateToxicPanelS(self, messageID, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateToxicPanel(messageID, value)
        return

    def as_restoreMessagesS(self, messageID):
        if self._isDAAPIInited():
            return self.flashObject.as_restoreMessages(messageID)
        return
