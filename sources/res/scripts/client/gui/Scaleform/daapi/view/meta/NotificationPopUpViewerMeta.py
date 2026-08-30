from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class NotificationPopUpViewerMeta(BaseDAAPIComponent):

    def setListClear(self):
        self._printOverrideError(b'setListClear')
        return

    def onMessageHidden(self, byTimeout, wasNotified, typeID, entityID):
        self._printOverrideError(b'onMessageHidden')
        return

    def onClickAction(self, typeID, entityID, action):
        self._printOverrideError(b'onClickAction')
        return

    def getMessageActualTime(self, msTime):
        self._printOverrideError(b'getMessageActualTime')
        return

    def registerGFNotification(self, component, alias, gfViewName, isPopUp, linkageData):
        self._printOverrideError(b'registerGFNotification')
        return

    def as_hasPopUpIndexS(self, typeID, entityID):
        if self._isDAAPIInited():
            return self.flashObject.as_hasPopUpIndex(typeID, entityID)
        return

    def as_appendMessageS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(data)
        return

    def as_updateMessageS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(data)
        return

    def as_removeMessageS(self, typeID, entityID):
        if self._isDAAPIInited():
            return self.flashObject.as_removeMessage(typeID, entityID)
        return

    def as_removeAllMessagesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeAllMessages()
        return

    def as_initInfoS(self, maxMessagessCount, padding):
        if self._isDAAPIInited():
            return self.flashObject.as_initInfo(maxMessagessCount, padding)
        return

    def as_setViewPaddingS(self, enabled, paddingX, paddingY):
        if self._isDAAPIInited():
            return self.flashObject.as_setViewPadding(enabled, paddingX, paddingY)
        return
