from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class ContactsListPopoverMeta(SmartPopOverView):

    def addToFriends(self, uid, name):
        self._printOverrideError(b'addToFriends')
        return

    def addToIgnored(self, uid, name):
        self._printOverrideError(b'addToIgnored')
        return

    def isEnabledInRoaming(self, uid):
        self._printOverrideError(b'isEnabledInRoaming')
        return

    def changeGroup(self, dbId, contactName, groupData):
        self._printOverrideError(b'changeGroup')
        return

    def copyIntoGroup(self, contactDbId, groupData):
        self._printOverrideError(b'copyIntoGroup')
        return

    def as_setInitInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitInfo(data)
        return

    def as_editGroupS(self, targetGroupName):
        if self._isDAAPIInited():
            return self.flashObject.as_editGroup(targetGroupName)
        return

    def as_removeGroupS(self, targetGroupName):
        if self._isDAAPIInited():
            return self.flashObject.as_removeGroup(targetGroupName)
        return

    def as_createContactNoteS(self, userName, databaseID):
        if self._isDAAPIInited():
            return self.flashObject.as_createContactNote(userName, databaseID)
        return

    def as_editContactNoteS(self, userName, databaseID):
        if self._isDAAPIInited():
            return self.flashObject.as_editContactNote(userName, databaseID)
        return
