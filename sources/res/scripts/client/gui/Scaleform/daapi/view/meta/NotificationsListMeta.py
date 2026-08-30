from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class NotificationsListMeta(SmartPopOverView):

    def onClickAction(self, typeID, entityID, action):
        self._printOverrideError(b'onClickAction')
        return

    def registerGFNotification(self, component, alias, gfViewName, isPopUp, linkageData):
        self._printOverrideError(b'registerGFNotification')
        return

    def getMessageActualTime(self, msTime):
        self._printOverrideError(b'getMessageActualTime')
        return

    def onGroupChange(self, groupIdx):
        self._printOverrideError(b'onGroupChange')
        return

    def onCheckNewsClick(self):
        self._printOverrideError(b'onCheckNewsClick')
        return

    def as_setInitDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)
        return

    def as_setMessagesListS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagesList(value)
        return

    def as_appendMessageS(self, messageData):
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(messageData)
        return

    def as_updateMessageS(self, messageData):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(messageData)
        return

    def as_updateCountersS(self, counts):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounters(counts)
        return

    def as_setProgressiveRewardEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressiveRewardEnabled(isEnabled)
        return

    def as_setIsNewsBlockEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsNewsBlockEnabled(isEnabled)
        return

    def as_setCheckNewsBtnEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckNewsBtnEnabled(isEnabled)
        return
