from PlayerEvents import g_playerEvents
from adisp import adisp_process
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import getProfileCommonInfo
from gui.Scaleform.daapi.view.meta.ProfileWindowMeta import ProfileWindowMeta
from gui.Scaleform.locale.PROFILE import PROFILE
from gui.clans.clan_helpers import ClanListener, showClanInviteSystemMsg
from gui.impl import backport
from gui.impl.gen import R
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events
from gui.clientgw.clan.contexts import CreateInviteCtx
from helpers import dependency
from helpers.i18n import makeString
from messenger import g_settings
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.events import g_messengerEvents
from messenger.storage import storage_getter
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class ProfileWindow(ProfileWindowMeta, ClanListener):
    itemsCache = dependency.descriptor(IItemsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, ctx=None):
        super(ProfileWindow, self).__init__()
        self.__userName = ctx.get(b'userName')
        self.__databaseID = ctx.get(b'databaseID')
        self.__selectedAlias = ctx.get(b'selectedAlias')
        self.__eventOwner = ctx.get(b'eventOwner')
        return

    def onClanEnableChanged(self, enabled):
        self.__updateAddToClanBtn()
        return

    def _populate(self):
        super(ProfileWindow, self)._populate()
        g_playerEvents.onDossiersResync += self.__dossierResyncHandler
        self.__updateUserInfo()
        g_messengerEvents.users.onUserActionReceived += self._onUserActionReceived
        g_eventBus.addListener(events.Achievements20Event.CLOSE_SUMMARY_VIEW, self.onWindowCloseByIndex, EVENT_BUS_SCOPE.LOBBY)
        self.__checkUserRosterInfo()
        self.startClanListening()
        return

    def _dispose(self):
        self.stopClanListening()
        g_messengerEvents.users.onUserActionReceived -= self._onUserActionReceived
        g_playerEvents.onDossiersResync -= self.__dossierResyncHandler
        g_eventBus.removeListener(events.Achievements20Event.CLOSE_SUMMARY_VIEW, self.onWindowCloseByIndex, EVENT_BUS_SCOPE.LOBBY)
        self.itemsCache.items.unloadUserDossier(self.__databaseID)
        super(ProfileWindow, self)._dispose()
        return

    def __checkUserRosterInfo(self):
        user = self.usersStorage.getUser(self.__databaseID)
        enabledInroaming = self.__isEnabledInRoaming(self.__databaseID)
        isFriend = user is not None and user.isFriend()
        self.as_addFriendAvailableS(enabledInroaming and not isFriend)
        isIgnored = user is not None and user.isIgnored()
        self.as_setIgnoredAvailableS(enabledInroaming and not isIgnored)
        self.as_setCreateChannelAvailableS(enabledInroaming and not isIgnored)
        self.__updateAddToClanBtn()
        return

    def __updateAddToClanBtn(self):
        _, clanInfo = self.itemsCache.items.getClanInfo(self.__databaseID)
        isVisible = self.lobbyContext.getServerSettings().clanProfile.isEnabled()
        isEnabled = self.webCtrl.isAvailable()
        if isEnabled and clanInfo is None:
            profile = self.webCtrl.getAccountProfile()
            dossier = profile.getClanDossier()
            isEnabled = profile.getMyClanPermissions().canHandleClanInvites() and not dossier.isClanInviteSent(self.__databaseID) and not dossier.hasClanApplication(self.__databaseID)
        userIsNotInClan = clanInfo is None
        self.as_addToClanAvailableS(isEnabled)
        self.as_addToClanVisibleS(isVisible and userIsNotInClan)
        return

    def __isEnabledInRoaming(self, dbID):
        roaming = self.lobbyContext.getServerSettings().roaming
        if g_settings.server.XMPP.isEnabled():
            isEnabled = roaming.isSameRealm(dbID)
        else:
            isEnabled = not roaming.isInRoaming() and not roaming.isPlayerInRoaming(dbID)
        return isEnabled

    @storage_getter(b'users')
    def usersStorage(self):
        return

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    def _onUserActionReceived(self, _, user, shadowMode):
        if user.getID() == self.__databaseID:
            self.__checkUserRosterInfo()
        return

    def __dossierResyncHandler(self, *args):
        self.__updateUserInfo()
        return

    def __updateUserInfo(self):
        dossier = self.itemsCache.items.getAccountDossier(self.__databaseID)
        _, clanInfo = self.itemsCache.items.getClanInfo(self.__databaseID)
        info = getProfileCommonInfo(self.__userName, dossier.getDossierDescr())
        clanAbbrev = clanInfo[1] if clanInfo is not None else None
        self.as_setInitDataS({b'fullName': (self.lobbyContext.getPlayerFullName(info[b'name'], clanAbbrev=clanAbbrev, regionCode=self.lobbyContext.getRegionCode(self.__databaseID)))})
        return

    def registerFlashComponent(self, component, alias, *args):
        if alias == VIEW_ALIAS.PROFILE_TAB_NAVIGATOR:
            super(ProfileWindow, self).registerFlashComponent(component, alias, self.__userName, self.__databaseID, self.__databaseID, {b'selectedAlias': (self.__selectedAlias), 
               b'sectionsData': [
                               self.__getSectionDataObject(PROFILE.SECTION_SUMMARY_TITLE, PROFILE.PROFILE_TABS_TOOLTIP_SUMMARY, VIEW_ALIAS.PROFILE_TOTAL_PAGE, b'statsSummary'),
                               self.__getSectionDataObject(PROFILE.SECTION_AWARDS_TITLE, PROFILE.PROFILE_TABS_TOOLTIP_AWARDS, VIEW_ALIAS.PROFILE_AWARDS, b'statsAwards'),
                               self.__getSectionDataObject(PROFILE.SECTION_STATISTICS_TITLE, PROFILE.PROFILE_TABS_TOOLTIP_STATISTICS, VIEW_ALIAS.PROFILE_STATISTICS, b'statsStatistics'),
                               self.__getSectionDataObject(PROFILE.SECTION_TECHNIQUE_TITLE, PROFILE.PROFILE_TABS_TOOLTIP_TECHNIQUE, VIEW_ALIAS.PROFILE_TECHNIQUE_WINDOW, b'statsTechnique')]}, {b'eventOwner': (self.__eventOwner)})
        else:
            super(ProfileWindow, self).registerFlashComponent(component, alias)
        return

    def __getSectionDataObject(self, label, tooltip, alias, uiId):
        return {b'label': (makeString(label)), b'alias': alias, 
           b'tooltip': tooltip, 
           b'enabled': True, 
           b'id': uiId}

    def userAddFriend(self):
        self.proto.contacts.addFriend(self.__databaseID, self.__userName)
        return

    @adisp_process
    def userAddToClan(self):
        self.as_showWaitingS(backport.msgid(R.strings.waiting.clans.invites.send()), {})
        profile = self.webCtrl.getAccountProfile()
        context = CreateInviteCtx(profile.getClanDbID(), [self.__databaseID])
        result = yield self.webCtrl.sendRequest(context, allowDelay=True)
        showClanInviteSystemMsg(self.__userName, result.isSuccess(), result.getCode(), result.data)
        self.__updateAddToClanBtn()
        self.as_hideWaitingS()
        return

    def userSetIgnored(self):
        self.proto.contacts.addIgnored(self.__databaseID, self.__userName)
        return

    def userCreatePrivateChannel(self):
        self.proto.contacts.createPrivateChannel(self.__databaseID, self.__userName)
        return

    def onWindowClose(self):
        self.destroy()
        return

    def onWindowCloseByIndex(self, *args):
        if self.__databaseID == args[0].ctx.get(b'databaseID'):
            self.onWindowClose()
        return
