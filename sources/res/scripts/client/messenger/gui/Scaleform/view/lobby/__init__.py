from frameworks.wulf import WindowLayer
from gui.Scaleform.framework import GroupedViewSettings, ComponentSettings
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.CONTACTS_ALIASES import CONTACTS_ALIASES
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.utils.functions import getViewName
ACCOUNT_NAME_MIN_CHARS_LENGTH = 2
ACCOUNT_NAME_MAX_CHARS_LENGTH = 24

class MESSENGER_VIEW_ALIAS(object):
    FAQ_WINDOW = b'messenger/faqWindow'
    CHANNEL_MANAGEMENT_WINDOW = b'messenger/channelsManagementWindow'
    LAZY_CHANNEL_WINDOW = b'messenger/lazyChannelWindow'
    LOBBY_CHANNEL_WINDOW = b'messenger/lobbyChannelWindow'
    CONNECT_TO_SECURE_CHANNEL_WINDOW = b'messenger/connectToSecureChannelWindow'
    CHANNEL_COMPONENT = b'channelComponent'


def getContextMenuHandlers():
    from messenger.gui.Scaleform.data import contacts_cm_handlers
    return (
     (
      CONTEXT_MENU_HANDLER_TYPE.CONTACTS_GROUP, contacts_cm_handlers.SimpleContactsCMHandler),
     (
      CONTEXT_MENU_HANDLER_TYPE.PLAYER_CONTACTS, contacts_cm_handlers.PlayerContactsCMHandler))


def getViewSettings():
    from messenger.gui.Scaleform.view.lobby.ChannelComponent import ChannelComponent
    from messenger.gui.Scaleform.view.lobby.ChannelsManagementWindow import ChannelsManagementWindow
    from messenger.gui.Scaleform.view.lobby.ConnectToSecureChannelWindow import ConnectToSecureChannelWindow
    from messenger.gui.Scaleform.view.lobby.FAQWindow import FAQWindow
    from messenger.gui.Scaleform.view.lobby.LazyChannelWindow import LazyChannelWindow
    from messenger.gui.Scaleform.view.lobby.LobbyChannelWindow import LobbyChannelWindow
    from messenger.gui.Scaleform.view.lobby.contact_manage_note_views import ContactEditNoteView, ContactCreateNoteView
    from messenger.gui.Scaleform.view.lobby.ContactsSettingsView import ContactsSettingsView
    from messenger.gui.Scaleform.view.lobby.ContactsTreeComponent import ContactsTreeComponent
    from messenger.gui.Scaleform.view.lobby.GroupDeleteView import GroupDeleteView
    from messenger.gui.Scaleform.view.lobby.SearchContactView import SearchContactView
    from messenger.gui.Scaleform.view.lobby.ContactsListPopover import ContactsListPopover
    from messenger.gui.Scaleform.view.lobby.group_manage_views import GroupRenameView, GroupCreateView
    return (
     GroupedViewSettings(MESSENGER_VIEW_ALIAS.FAQ_WINDOW, FAQWindow, b'FAQWindow.swf', WindowLayer.WINDOW, b'', None, ScopeTemplates.DEFAULT_SCOPE, True, isCentered=False),
     GroupedViewSettings(MESSENGER_VIEW_ALIAS.CHANNEL_MANAGEMENT_WINDOW, ChannelsManagementWindow, b'channelsManagementWindow.swf', WindowLayer.WINDOW, b'', MESSENGER_VIEW_ALIAS.CHANNEL_MANAGEMENT_WINDOW, ScopeTemplates.DEFAULT_SCOPE, True, isCentered=False),
     GroupedViewSettings(MESSENGER_VIEW_ALIAS.LAZY_CHANNEL_WINDOW, LazyChannelWindow, b'lazyChannelWindow.swf', WindowLayer.WINDOW, b'', MESSENGER_VIEW_ALIAS.LAZY_CHANNEL_WINDOW, ScopeTemplates.DEFAULT_SCOPE, True, isCentered=False, canClose=False),
     GroupedViewSettings(MESSENGER_VIEW_ALIAS.LOBBY_CHANNEL_WINDOW, LobbyChannelWindow, b'lobbyChannelWindow.swf', WindowLayer.WINDOW, b'', MESSENGER_VIEW_ALIAS.LOBBY_CHANNEL_WINDOW, ScopeTemplates.DEFAULT_SCOPE, True, isCentered=False),
     GroupedViewSettings(MESSENGER_VIEW_ALIAS.CONNECT_TO_SECURE_CHANNEL_WINDOW, ConnectToSecureChannelWindow, b'connectToSecureChannelWindow.swf', WindowLayer.WINDOW, b'', MESSENGER_VIEW_ALIAS.CONNECT_TO_SECURE_CHANNEL_WINDOW, ScopeTemplates.DEFAULT_SCOPE, True, isCentered=True),
     GroupedViewSettings(CONTACTS_ALIASES.CONTACTS_POPOVER, ContactsListPopover, b'contactsListPopover.swf', WindowLayer.WINDOW, b'contactsListPopover', CONTACTS_ALIASES.CONTACTS_POPOVER, ScopeTemplates.WINDOW_VIEWED_MULTISCOPE),
     ComponentSettings(MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT, ChannelComponent, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CONTACTS_ALIASES.FIND_CONTACT_VIEW_ALIAS, SearchContactView, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CONTACTS_ALIASES.CONTACTS_TREE, ContactsTreeComponent, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CONTACTS_ALIASES.GROUP_RENAME_VIEW_ALIAS, GroupRenameView, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CONTACTS_ALIASES.GROUP_CREATE_VIEW_ALIAS, GroupCreateView, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CONTACTS_ALIASES.CONTACT_EDIT_NOTE_VIEW_ALIAS, ContactEditNoteView, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CONTACTS_ALIASES.CONTACT_CREATE_NOTE_VIEW_ALIAS, ContactCreateNoteView, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CONTACTS_ALIASES.GROUP_DELETE_VIEW_ALIAS, GroupDeleteView, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CONTACTS_ALIASES.CONTACTS_SETTINGS_VIEW_ALIAS, ContactsSettingsView, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (
     _MessengerPackageBusinessHandler(),)


class _MessengerPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          MESSENGER_VIEW_ALIAS.FAQ_WINDOW, self.loadViewByCtxEvent),
         (
          MESSENGER_VIEW_ALIAS.CHANNEL_MANAGEMENT_WINDOW, self.loadViewByCtxEvent),
         (
          MESSENGER_VIEW_ALIAS.LAZY_CHANNEL_WINDOW, self.__showLazyChannelWindow),
         (
          MESSENGER_VIEW_ALIAS.LOBBY_CHANNEL_WINDOW, self.__showLobbyChannelWindow),
         (
          MESSENGER_VIEW_ALIAS.CONNECT_TO_SECURE_CHANNEL_WINDOW, self.loadViewByCtxEvent),
         (
          CONTACTS_ALIASES.CONTACTS_POPOVER, self.loadViewByCtxEvent))
        super(_MessengerPackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
        return

    def __showLazyChannelWindow(self, event):
        alias = MESSENGER_VIEW_ALIAS.LAZY_CHANNEL_WINDOW
        self.loadViewWithDefName(alias, getViewName(MESSENGER_VIEW_ALIAS.LAZY_CHANNEL_WINDOW, event.ctx.get(b'clientID')), None, event.ctx)
        return

    def __showLobbyChannelWindow(self, event):
        alias = MESSENGER_VIEW_ALIAS.LOBBY_CHANNEL_WINDOW
        self.loadViewWithDefName(alias, getViewName(MESSENGER_VIEW_ALIAS.LOBBY_CHANNEL_WINDOW, event.ctx[b'clientID']), None, event.ctx)
        return
