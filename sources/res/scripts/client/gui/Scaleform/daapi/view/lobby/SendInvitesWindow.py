from debug_utils import LOG_ERROR
from gui import SystemMessages
from gui.Scaleform.daapi.view.meta.SendInvitesWindowMeta import SendInvitesWindowMeta
from gui.Scaleform.genConsts.CONTACTS_ALIASES import CONTACTS_ALIASES
from gui.Scaleform.locale.DIALOGS import DIALOGS
from gui.prb_control import prbDispatcherProperty, prbEntityProperty
from gui.prb_control.entities.base.ctx import SendInvitesCtx
from gui.prb_control.settings import REQUEST_TYPE, CTRL_ENTITY_TYPE
from gui.shared import EVENT_BUS_SCOPE, events
from helpers import i18n
from messenger.gui.Scaleform.data.contacts_vo_converter import ContactConverter
from messenger.gui.Scaleform.view.lobby.ContactsTreeComponent import ContactsTreeComponent
from messenger.proto.events import g_messengerEvents
from messenger.proto.interfaces import ISearchHandler
from messenger.storage import storage_getter

class SendInvitesWindow(SendInvitesWindowMeta, ISearchHandler):

    def __init__(self, ctx=None):
        super(SendInvitesWindow, self).__init__()
        self._onlineMode = True
        self._ctx = ctx
        self._converter = ContactConverter()
        if b'ctrlType' in ctx:
            self._ctrlType = ctx[b'ctrlType']
        else:
            self._ctrlType = CTRL_ENTITY_TYPE.UNKNOWN
            LOG_ERROR(b'Control type is not defined', ctx)
        if b'prbName' in ctx:
            self._prbName = ctx[b'prbName']
        else:
            self._prbName = b'prebattle'
        if b'showClanOnly' in ctx:
            self._showClanOnly = ctx[b'showClanOnly']
        else:
            self._showClanOnly = False
        if b'invites' in ctx:
            self._invites = ctx[b'invites']
        else:
            self._invites = ()
        return

    def getAllAvailableContacts(self):
        return self.pyTree.getMainDP().getContactsList()

    @storage_getter(b'users')
    def usersStorage(self):
        return

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @prbEntityProperty
    def prbEntity(self):
        return

    @property
    def pyTree(self):
        tree = None
        if CONTACTS_ALIASES.CONTACTS_TREE in self.components:
            tree = self.components[CONTACTS_ALIASES.CONTACTS_TREE]
        return tree

    def showError(self, value):
        SystemMessages.pushI18nMessage(value, type=SystemMessages.SM_TYPE.Error)
        return

    def setOnlineFlag(self, value):
        if value is False:
            self._onlineMode = None
        else:
            self._onlineMode = True
        tree = self.pyTree
        if tree:
            tree.showContacts(onlineMode=self._onlineMode, showEmptyGroups=False, showFriends=not self._showClanOnly, showGroupMenu=False)
        return

    def _getTitle(self):
        return i18n.makeString(DIALOGS.SENDINVITES_COMMON_TITLE)

    def sendInvites(self, accountsToInvite, comment):
        self.prbEntity.request(SendInvitesCtx(accountsToInvite, comment))
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(SendInvitesWindow, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == CONTACTS_ALIASES.CONTACTS_TREE:
            tree = viewPy
            tree.onListStateChanged += self.__onTreeListStateChanged
            tree.showContacts(onlineMode=self._onlineMode, showEmptyGroups=False, showFriends=not self._showClanOnly, showGroupMenu=False)
        return

    def _populate(self):
        super(SendInvitesWindow, self)._populate()
        usersEvents = g_messengerEvents.users
        usersEvents.onUserActionReceived += self.__onUserDataChanged
        usersEvents.onUserStatusUpdated += self.__onUserStatusUpdated
        self._initCooldown()
        self.as_setWindowTitleS(self._getTitle())
        self.as_setDefaultOnlineFlagS(self._onlineMode)
        return

    def _dispose(self):
        self.pyTree.onListStateChanged -= self.__onTreeListStateChanged
        usersEvents = g_messengerEvents.users
        usersEvents.onUserActionReceived -= self.__onUserDataChanged
        usersEvents.onUserStatusUpdated -= self.__onUserStatusUpdated
        self._finiCooldown()
        super(SendInvitesWindow, self)._dispose()
        return

    def _initCooldown(self):
        self.addListener(events.CoolDownEvent.PREBATTLE, self._handleSetCoolDown, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _finiCooldown(self):
        self.removeListener(events.CoolDownEvent.PREBATTLE, self._handleSetCoolDown, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _handleSetCoolDown(self, event):
        if event.requestID is REQUEST_TYPE.SEND_INVITE:
            self.as_onReceiveSendInvitesCooldownS(event.coolDown)
        return

    def __onUserDataChanged(self, _, user, shadowMode):
        self.as_onContactUpdatedS(self._converter.makeVO(user))
        return

    def __onUserStatusUpdated(self, user):
        self.as_onContactUpdatedS(self._converter.makeVO(user))
        return

    def __onTreeListStateChanged(self, state, isEmpty):
        if state == ContactsTreeComponent.LIST_EMPTY_STATE:
            self.as_onListStateChangedS(isEmpty)
        return
