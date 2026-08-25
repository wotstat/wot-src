from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContactsTreeComponentMeta(BaseDAAPIComponent):

    def onGroupSelected(self, mainGroup, groupData):
        self._printOverrideError(b'onGroupSelected')
        return

    def searchLocalContact(self, flt):
        self._printOverrideError(b'searchLocalContact')
        return

    def hasDisplayingContacts(self):
        self._printOverrideError(b'hasDisplayingContacts')
        return

    def as_updateInfoMessageS(self, enableSearchInput, title, message, warn):
        if self._isDAAPIInited():
            return self.flashObject.as_updateInfoMessage(enableSearchInput, title, message, warn)
        return

    def as_getMainDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMainDP()
        return

    def as_setInitDataS(self, val):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(val)
        return
