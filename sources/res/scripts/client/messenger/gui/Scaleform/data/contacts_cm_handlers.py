from gui.Scaleform.daapi.view.lobby.user_cm_handlers import BaseUserCMHandler
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.MESSENGER import MESSENGER
from gui.shared import events, EVENT_BUS_SCOPE
from messenger import normalizeGroupId
from messenger.m_constants import USER_TAG

class CONTACTS_ACTION_ID(object):
    EDIT_GROUP = b'editGroup'
    REMOVE_GROUP = b'removeGroup'
    REMOVE_FROM_GROUP = b'removeFromGroup'
    CREATE_CONTACT_NOTE = b'createContactNote'
    EDIT_CONTACT_NOTE = b'editContactNote'
    REMOVE_CONTACT_NOTE = b'removeContactNote'
    REJECT_FRIENDSHIP = b'rejectFriendship'


class SimpleContactsCMHandler(AbstractContextMenuHandler, EventSystemEntity):

    def __init__(self, cmProxy, ctx=None):
        super(SimpleContactsCMHandler, self).__init__(cmProxy, ctx, {(CONTACTS_ACTION_ID.EDIT_GROUP): b'editGroup', 
           (CONTACTS_ACTION_ID.REMOVE_GROUP): b'removeGroup'})
        return

    def editGroup(self):
        self.fireEvent(events.ContactsEvent(events.ContactsEvent.EDIT_GROUP, ctx={b'targetGroupName': (self.targetGroupName)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def removeGroup(self):
        self.fireEvent(events.ContactsEvent(events.ContactsEvent.REMOVE_GROUP, ctx={b'targetGroupName': (self.targetGroupName)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _generateOptions(self, ctx=None):
        return [
         self._makeItem(CONTACTS_ACTION_ID.EDIT_GROUP, MESSENGER.MESSENGER_CONTACTS_CONTEXTMENU_EDITGROUP),
         self._makeItem(CONTACTS_ACTION_ID.REMOVE_GROUP, MESSENGER.MESSENGER_CONTACTS_CONTEXTMENU_REMOVEGROUP)]

    def _initFlashValues(self, ctx):
        self.targetGroupName = normalizeGroupId(ctx.targetGroupName)
        return

    def _clearFlashValues(self):
        self.targetGroupName = None
        return


class PlayerContactsCMHandler(BaseUserCMHandler):

    def createContactNote(self):
        self.fireEvent(events.ContactsEvent(events.ContactsEvent.CREATE_CONTACT_NOTE, ctx={b'databaseID': (self.databaseID), b'userName': (self.userName)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def editContactNote(self):
        self.fireEvent(events.ContactsEvent(events.ContactsEvent.EDIT_CONTACT_NOTE, ctx={b'databaseID': (self.databaseID), b'userName': (self.userName)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def removeContactNote(self):
        if self.proto.contacts.isNoteSupported():
            self.proto.contacts.removeNote(self.databaseID)
        return

    def removeFromGroup(self):
        self.proto.contacts.moveFriendToGroup(self.databaseID, None, self.targetGroupName)
        return

    def rejectFriendship(self):
        self.proto.contacts.cancelFriendship(self.databaseID)
        return

    def _getHandlers(self):
        handlers = super(PlayerContactsCMHandler, self)._getHandlers()
        handlers.update({(CONTACTS_ACTION_ID.CREATE_CONTACT_NOTE): b'createContactNote', 
           (CONTACTS_ACTION_ID.EDIT_CONTACT_NOTE): b'editContactNote', 
           (CONTACTS_ACTION_ID.REMOVE_CONTACT_NOTE): b'removeContactNote', 
           (CONTACTS_ACTION_ID.REMOVE_FROM_GROUP): b'removeFromGroup', 
           (CONTACTS_ACTION_ID.REJECT_FRIENDSHIP): b'rejectFriendship'})
        return handlers

    def _initFlashValues(self, ctx):
        super(PlayerContactsCMHandler, self)._initFlashValues(ctx)
        self.targetGroupName = normalizeGroupId(ctx.targetGroupName)
        self.showUserNotes = getattr(ctx, b'showUserNotes', True)
        return

    def _clearFlashValues(self):
        super(PlayerContactsCMHandler, self)._clearFlashValues()
        self.targetGroupName = None
        return

    def _addRejectFriendshipInfo(self, option, userCMInfo):
        if not userCMInfo.isFriend:
            if self.proto.contacts.isBidiFriendshipSupported():
                if userCMInfo.getTags() and USER_TAG.SUB_PENDING_IN in userCMInfo.getTags():
                    option.append(self._makeItem(CONTACTS_ACTION_ID.REJECT_FRIENDSHIP, MENU.contextmenu(CONTACTS_ACTION_ID.REJECT_FRIENDSHIP)))
        return option

    def _addContactsNoteInfo(self, options, userCMInfo):
        if self.showUserNotes and self.proto.contacts.isNoteSupported():
            userNote = userCMInfo.getNote()
            if userNote:
                options.extend([
                 self._makeItem(CONTACTS_ACTION_ID.EDIT_CONTACT_NOTE, MENU.contextmenu(CONTACTS_ACTION_ID.EDIT_CONTACT_NOTE)),
                 self._makeItem(CONTACTS_ACTION_ID.REMOVE_CONTACT_NOTE, MENU.contextmenu(CONTACTS_ACTION_ID.REMOVE_CONTACT_NOTE))])
            else:
                options.append(self._makeItem(CONTACTS_ACTION_ID.CREATE_CONTACT_NOTE, MENU.contextmenu(CONTACTS_ACTION_ID.CREATE_CONTACT_NOTE)))
        return options

    def _addRemoveFromGroupInfo(self, options, isIgnored):
        if self.proto.contacts.isGroupSupported():
            if self.targetGroupName:
                options.append(self._makeItem(CONTACTS_ACTION_ID.REMOVE_FROM_GROUP, MESSENGER.MESSENGER_CONTACTS_CONTEXTMENU_REMOVEFROMGROUP))
        return options
