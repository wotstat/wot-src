import typing
from collections import defaultdict
import BigWorld
from adisp import adisp_process
from CurrentVehicle import g_currentVehicle
from battle_pass_common import isPostProgressionChapter
from constants import PREBATTLE_TYPE, PENALTY_TYPES, FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA, IS_CHINA
from debug_utils import LOG_DEBUG, LOG_ERROR
from gui import DialogsInterface, SystemMessages, makeHtmlString
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getIntegratedAuctionUrl, getWotPlusShopUrl
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.BARRACKS_CONSTANTS import BARRACKS_CONSTANTS
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.battle_results import RequestResultsContext
from gui.clans.clan_helpers import showAcceptClanInviteDialog
from gui.customization.constants import CustomizationModeSource, CustomizationModes
from gui.impl import backport
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache
from gui.impl.gen import R
from gui.impl.lobby.achievements.profile_utils import createAdvancedAchievementsCatalogInitAchievementIDs
from gui.impl.lobby.battle_pass.common import isExtraChapterSeen
from gui.lootbox_system.base.common import ViewID, Views
from gui.platform.base.statuses.constants import StatusTypes
from gui.prb_control import prbDispatcherProperty, prbInvitesProperty
from gui.prestige.prestige_helpers import showPrestigeOnboardingWindow, showPrestigeVehicleStats
from gui.ranked_battles import ranked_helpers
from gui.server_events.events_dispatcher import showMissionsMapboxProgression, showPersonalMission, showBanWindow, showPenaltyWindow, showWarningWindow, showBattleMatters, showChallenges
from gui.shared import EVENT_BUS_SCOPE, actions, event_dispatcher as shared_events, events, g_eventBus
from gui.shared.event_dispatcher import hideWebBrowserOverlay, showBattlePass, showBlueprintsSalePage, showCollectionAwardsWindow, showCollectionWindow, showCollectionsMainPage, showDelayedReward, showEpicBattlesAfterBattleWindow, showProgressiveRewardWindow, showRankedYearAwardWindow, showShop, showSteamConfirmEmailOverlay, showWinbackSelectRewardView, showBarracks, showSeniorityRewardVehiclesWindow, showAdvancedAchievementsView, showTrophiesView, showAdvancedAchievementsCatalogView, showExchangeGoldWindow, showExchangeFreeXPWindow, showCrewPostProgressionView, showPersonalMissionMainWindow, showPetStorageView, showSubscriptionsPage
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.processors.common import ClaimRewardForPostProgression
from gui.shared.notifications import NotificationPriorityLevel
from gui.shared.system_factory import collectAllNotificationsActionsHandlers, registerNotificationsActionsHandlers
from gui.shared.utils import decorators
from gui.wgcg.clan import contexts as clan_ctxs
from gui.wgnc import g_wgncProvider
from helpers import dependency
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from notification.settings import NOTIFICATION_BUTTON_STATE, NOTIFICATION_TYPE
from predefined_hosts import g_preDefinedHosts
from shared_utils import first
from skeletons.gui.battle_results import IBattleResultsService
from skeletons.gui.challenges import IChallengesController
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.game_control import IBattlePassController, IBattleRoyaleController, IBrowserController, ICollectionsSystemController, IMapboxController, IRankedBattlesController, ISeniorityAwardsController, IWinbackController, ISteamCompletionController
from skeletons.gui.impl import INotificationWindowController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController
from skeletons.gui.shared.utils import IHangarSpace
from skeletons.gui.web import IWebController
from soft_exception import SoftException
from uilogging.advanced_achievement.logger import AdvancedAchievementLogger
from uilogging.advanced_achievement.logging_constants import AdvancedAchievementButtons, AdvancedAchievementViewKey
from uilogging.seniority_awards.loggers import VehicleSelectionNotificationLogger
from web.web_client_api import webApiCollection
from web.web_client_api.sound import HangarSoundWebApi
from wg_async import wg_async, wg_await
if typing.TYPE_CHECKING:
    from typing import Tuple
    from notification.NotificationsModel import NotificationsModel
    from gui.platform.wgnp.steam_account.statuses import SteamAccEmailStatus

class ActionHandler(object):

    @classmethod
    def getNotType(cls):
        return NotImplementedError

    @classmethod
    def getActions(cls):
        return ()

    def handleAction(self, model, entityID, action):
        if action not in self.getActions():
            raise SoftException((b'Handler does not handle action {0}').format(action))
        return


class NavigationDisabledActionHandler(ActionHandler):

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def handleAction(self, model, entityID, action):
        super(NavigationDisabledActionHandler, self).handleAction(model, entityID, action)
        if not self._canNavigate():
            return
        self.doAction(model, entityID, action)
        return

    def doAction(self, model, entityID, action):
        raise NotImplementedError
        return

    def _canNavigate(self):
        prbDispatcher = self.prbDispatcher
        if prbDispatcher is not None and prbDispatcher.getFunctionalState().isNavigationDisabled():
            BigWorld.callback(0.0, self.__showMessage)
            return False
        else:
            return True

    @staticmethod
    def __showMessage():
        SystemMessages.pushI18nMessage(b'#system_messages:queue/isInQueue', type=SystemMessages.SM_TYPE.Error, priority=b'high')
        return


class _OpenEventBoardsHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openEventBoards',)

    def handleAction(self, model, entityID, action):
        super(_OpenEventBoardsHandler, self).handleAction(model, entityID, action)
        from gui.Scaleform.daapi.view.lobby.missions.regular.states import MissionsState
        MissionsState.goTo(ctx={b'tab': (QUESTS_ALIASES.MISSIONS_EVENT_BOARDS_VIEW_PY_ALIAS)})
        return


class _ShowArenaResultHandler(NavigationDisabledActionHandler):

    @proto_getter(PROTO_TYPE.BW)
    def proto(self):
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    def handleAction(self, model, entityID, action):
        if not self._canNavigate():
            return
        notification = model.collection.getItem(NOTIFICATION_TYPE.MESSAGE, entityID)
        if not notification:
            LOG_ERROR(b'Notification not found', NOTIFICATION_TYPE.MESSAGE, entityID)
            return
        savedData = notification.getSavedData()
        if not savedData:
            self._updateNotification(notification)
            LOG_ERROR(b'arenaUniqueID not found', notification)
            return
        self._showWindow(notification, savedData)
        return

    def _updateNotification(self, notification):
        _, formatted, settings = self.proto.serviceChannel.getMessage(notification.getID())
        if formatted and settings:
            formatted[b'buttonsStates'].update({b'submit': (NOTIFICATION_BUTTON_STATE.HIDDEN)})
            formatted[b'message'] += makeHtmlString(b'html_templates:lobby/system_messages', b'infoNoAvailable')
            notification.update(formatted)
        return

    def _showWindow(self, notification, arenaUniqueID):
        return

    def _showI18nMessage(self, key, msgType):

        def showMessage():
            SystemMessages.pushI18nMessage(key, type=msgType)
            return

        BigWorld.callback(0.0, showMessage)
        return


class _ShowClanSettingsHandler(ActionHandler):

    @classmethod
    def getActions(cls):
        return (b'showClanSettingsAction',)

    def handleAction(self, model, entityID, action):
        super(_ShowClanSettingsHandler, self).handleAction(model, entityID, action)
        LOG_DEBUG(b'_ShowClanSettingsHandler handleAction:')
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.SETTINGS_WINDOW), ctx={b'redefinedKeyMode': False}), EVENT_BUS_SCOPE.LOBBY)
        return


class _ShowClanSettingsFromAppsHandler(_ShowClanSettingsHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_APPS


class _ShowClanSettingsFromInvitesHandler(_ShowClanSettingsHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_INVITES


class _ShowClanAppsHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_APPS

    @classmethod
    def getActions(cls):
        return (b'showClanStaffProfile',)

    def handleAction(self, model, entityID, action):
        super(_ShowClanAppsHandler, self).handleAction(model, entityID, action)
        return shared_events.showClanInvitesWindow()


class _ShowClanInvitesHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_INVITES

    @classmethod
    def getActions(cls):
        return (b'showClanPersonalInvites',)

    def handleAction(self, model, entityID, action):
        super(_ShowClanInvitesHandler, self).handleAction(model, entityID, action)
        shared_events.showClanPersonalInvitesWindow()
        return


class _ClanAppHandler(ActionHandler):
    clanCtrl = dependency.descriptor(IWebController)

    def _getAccountID(self, model, entityID):
        return model.getNotification(self.getNotType(), entityID).getAccountID()

    def _getApplicationID(self, model, entityID):
        return model.getNotification(self.getNotType(), entityID).getApplicationID()


class _AcceptClanAppHandler(_ClanAppHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_APP

    @classmethod
    def getActions(cls):
        return (b'acceptClanAppAction',)

    @adisp_process
    def handleAction(self, model, entityID, action):
        super(_AcceptClanAppHandler, self).handleAction(model, entityID, action)
        yield self.clanCtrl.sendRequest(clan_ctxs.AcceptApplicationCtx(self._getApplicationID(model, entityID)), allowDelay=True)
        return


class _DeclineClanAppHandler(_ClanAppHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_APP

    @classmethod
    def getActions(cls):
        return (b'declineClanAppAction',)

    @adisp_process
    def handleAction(self, model, entityID, action):
        super(_DeclineClanAppHandler, self).handleAction(model, entityID, action)
        yield self.clanCtrl.sendRequest(clan_ctxs.DeclineApplicationCtx(self._getApplicationID(model, entityID)), allowDelay=True)
        return


class _ShowClanAppUserInfoHandler(_ClanAppHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_APP

    @classmethod
    def getActions(cls):
        return (b'showUserProfileAction',)

    def handleAction(self, model, entityID, action):
        super(_ShowClanAppUserInfoHandler, self).handleAction(model, entityID, action)
        accID = self._getAccountID(model, entityID)

        def onDossierReceived(databaseID, userName):
            shared_events.showProfileWindow(databaseID, userName)
            return

        shared_events.requestProfile(accID, model.getNotification(self.getNotType(), entityID).getUserName(), successCallback=onDossierReceived)
        return


class _ClanInviteHandler(ActionHandler):
    clanCtrl = dependency.descriptor(IWebController)

    def _getInviteID(self, model, entityID):
        return model.getNotification(self.getNotType(), entityID).getInviteID()


class _AcceptClanInviteHandler(_ClanInviteHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_INVITE

    @classmethod
    def getActions(cls):
        return (b'acceptClanInviteAction',)

    @adisp_process
    def handleAction(self, model, entityID, action):
        super(_AcceptClanInviteHandler, self).handleAction(model, entityID, action)
        entity = model.getNotification(self.getNotType(), entityID).getEntity()
        clanName = entity.getClanName()
        clanTag = entity.getClanTag()
        result = yield showAcceptClanInviteDialog(clanName, clanTag)
        if result:
            yield self.clanCtrl.sendRequest(clan_ctxs.AcceptInviteCtx(self._getInviteID(model, entityID)), allowDelay=True)
        return


class _DeclineClanInviteHandler(_ClanInviteHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_INVITE

    @classmethod
    def getActions(cls):
        return (b'declineClanInviteAction',)

    @adisp_process
    def handleAction(self, model, entityID, action):
        super(_DeclineClanInviteHandler, self).handleAction(model, entityID, action)
        yield self.clanCtrl.sendRequest(clan_ctxs.DeclineInviteCtx(self._getInviteID(model, entityID)), allowDelay=True)
        return


class _ShowClanProfileHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CLAN_INVITE

    @classmethod
    def getActions(cls):
        return (b'showClanProfileAction',)

    def handleAction(self, model, entityID, action):
        super(_ShowClanProfileHandler, self).handleAction(model, entityID, action)
        clan = model.getNotification(self.getNotType(), entityID)
        shared_events.showClanProfileWindow(clan.getClanID(), clan.getClanAbbrev())
        return


class ShowRankedSeasonCompleteHandler(ActionHandler):
    rankedController = dependency.descriptor(IRankedBattlesController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showRankedSeasonComplete',)

    def handleAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None:
            self.__showSeasonAward(savedData[b'quest'], savedData[b'awards'])
        return

    def __showSeasonAward(self, quest, data):
        seasonID, _, _ = ranked_helpers.getDataFromSeasonTokenQuestID(quest.getID())
        season = self.rankedController.getSeason(seasonID)
        if season is not None:
            shared_events.showRankedSeasonCompleteView({b'quest': quest, b'awards': data})
        return


class ShowRankedFinalYearHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showRankedFinalYearAward',)

    def handleAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None:
            self.__showFinalAward(savedData[b'questID'], savedData[b'awards'])
        return

    def __showFinalAward(self, questID, data):
        points = ranked_helpers.getDataFromFinalTokenQuestID(questID)
        showRankedYearAwardWindow(data, points)
        return


class ShowRankedYearPositionHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showRankedYearPosition',)

    def handleAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None and isinstance(savedData, dict):
            playerPosition = savedData.get(b'yearPosition')
            rewardsData = savedData.get(b'rewardsData')
            if playerPosition is not None and rewardsData:
                shared_events.showRankedYearLBAwardWindow(playerPosition, rewardsData)
        return


class ShowRankedBattlePageHandler(ActionHandler):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showRankedBattlePage',)

    def handleAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None and isinstance(savedData, dict):
            ctx = savedData.get(b'ctx')
            if ctx is not None and ctx.get(b'selectedItemID') is not None:
                self.__rankedController.showRankedBattlePage(ctx)
        return


class SelectBattleRoyaleMode(ActionHandler):
    battleRoyale = dependency.descriptor(IBattleRoyaleController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'selectBattleRoyaleMode',)

    def handleAction(self, model, entityID, action):
        self.battleRoyale.selectRoyaleBattle()
        return


class ShowBattleResultsHandler(_ShowArenaResultHandler):
    battleResults = dependency.descriptor(IBattleResultsService)

    def _updateNotification(self, notification):
        super(ShowBattleResultsHandler, self)._updateNotification(notification)
        self._showI18nMessage(b'#battle_results:noData', SystemMessages.SM_TYPE.Warning)
        return

    @classmethod
    def getActions(cls):
        return (b'showBattleResults',)

    def _canNavigate(self):
        return True

    @decorators.adisp_process(b'loadStats')
    def _showWindow(self, notification, arenaUniqueID):
        uniqueID = long(arenaUniqueID)
        result = yield self.battleResults.requestResults(RequestResultsContext(uniqueID, showImmediately=False, showIfPosted=True, resetCache=False))
        if not result:
            self._updateNotification(notification)
        return


class ShowFortBattleResultsHandler(_ShowArenaResultHandler):

    @classmethod
    def getActions(cls):
        return (b'showFortBattleResults',)

    def _updateNotification(self, notification):
        super(ShowFortBattleResultsHandler, self)._updateNotification(notification)
        self._showI18nMessage(b'#battle_results:noData', SystemMessages.SM_TYPE.Warning)
        return

    def _showWindow(self, notification, data):
        if data:
            battleResultData = data.get(b'battleResult', None)
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(FORTIFICATION_ALIASES.FORT_BATTLE_RESULTS_WINDOW_ALIAS), ctx={b'data': battleResultData}), scope=EVENT_BUS_SCOPE.LOBBY)
        else:
            self._updateNotification(notification)
        return


class OpenPollHandler(ActionHandler):
    browserCtrl = dependency.descriptor(IBrowserController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openPollInBrowser',)

    def handleAction(self, model, entityID, action):
        super(OpenPollHandler, self).handleAction(model, entityID, action)
        notification = model.collection.getItem(NOTIFICATION_TYPE.MESSAGE, entityID)
        if not notification:
            LOG_ERROR(b'Notification is not found', NOTIFICATION_TYPE.MESSAGE, entityID)
            return
        link, title = notification.getSettings().auxData
        if not link:
            LOG_ERROR(b'Poll link is not found', notification)
            return
        self.__doOpen(link, title)
        return

    @adisp_process
    def __doOpen(self, link, title):
        browserID = yield self.browserCtrl.load(link, title, showActionBtn=False, handlers=webApiCollection(HangarSoundWebApi))
        browser = self.browserCtrl.getBrowser(browserID)
        if browser is not None:
            browser.setIsAudioMutable(True)
        return


class AcceptPrbInviteHandler(ActionHandler):
    __winbackController = dependency.descriptor(IWinbackController)

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @prbInvitesProperty
    def prbInvites(self):
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.INVITE

    @classmethod
    def getActions(cls):
        return (b'acceptInvite',)

    @adisp_process
    def handleAction(self, model, entityID, action):
        super(AcceptPrbInviteHandler, self).handleAction(model, entityID, action)
        yield lambda callback: callback(None)
        postActions = []
        invite = self.prbInvites.getInvite(entityID)
        state = self.prbDispatcher.getFunctionalState()
        if state.doLeaveToAcceptInvite(invite.type):
            postActions.append(actions.LeavePrbModalEntity())
            if self.__winbackController.isModeAvailable() and invite.type == PREBATTLE_TYPE.SQUAD:
                postActions.append(actions.LeaveWinbackModeEntity())
        if invite and invite.anotherPeriphery:
            success = True
            if g_preDefinedHosts.isRoamingPeriphery(invite.peripheryID):
                success = yield DialogsInterface.showI18nConfirmDialog(b'changeRoamingPeriphery')
            if not success:
                return
            postActions.append(actions.DisconnectFromPeriphery(loginViewPreselectedPeriphery=invite.peripheryID))
            postActions.append(actions.ConnectToPeriphery(invite.peripheryID))
            postActions.append(actions.PrbInvitesInit())
            postActions.append(actions.LeavePrbEntity())
        g_eventBus.handleEvent(events.PrbInvitesEvent(events.PrbInvitesEvent.ACCEPT, inviteID=entityID, postActions=postActions), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class DeclinePrbInviteHandler(ActionHandler):

    @prbInvitesProperty
    def prbInvites(self):
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.INVITE

    @classmethod
    def getActions(cls):
        return (b'declineInvite',)

    def handleAction(self, model, entityID, action):
        super(DeclinePrbInviteHandler, self).handleAction(model, entityID, action)
        if entityID:
            self.prbInvites.declineInvite(entityID)
        else:
            LOG_ERROR(b'Invite is invalid', entityID)
        return


class ApproveFriendshipHandler(ActionHandler):

    @proto_getter(PROTO_TYPE.XMPP)
    def proto(self):
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.FRIENDSHIP_RQ

    @classmethod
    def getActions(cls):
        return (b'approveFriendship',)

    def handleAction(self, model, entityID, action):
        super(ApproveFriendshipHandler, self).handleAction(model, entityID, action)
        self.proto.contacts.approveFriendship(entityID)
        return


class CancelFriendshipHandler(ActionHandler):

    @proto_getter(PROTO_TYPE.XMPP)
    def proto(self):
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.FRIENDSHIP_RQ

    @classmethod
    def getActions(cls):
        return (b'cancelFriendship',)

    def handleAction(self, model, entityID, action):
        super(CancelFriendshipHandler, self).handleAction(model, entityID, action)
        self.proto.contacts.cancelFriendship(entityID)
        return


class WGNCActionsHandler(ActionHandler):

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.WGNC_POP_UP

    def handleAction(self, model, entityID, action):
        if not self._canNavigate():
            return
        notification = model.collection.getItem(NOTIFICATION_TYPE.WGNC_POP_UP, entityID)
        if notification:
            actorName = notification.getSavedData()
        else:
            actorName = b''
        g_wgncProvider.doAction(entityID, action, actorName)
        return

    def _canNavigate(self):
        prbDispatcher = self.prbDispatcher
        if prbDispatcher is not None and prbDispatcher.getFunctionalState().isNavigationDisabled():
            BigWorld.callback(0.0, self.__showMessage)
            return False
        else:
            return True

    @staticmethod
    def __showMessage():
        SystemMessages.pushI18nMessage(b'#system_messages:queue/isInQueue', type=SystemMessages.SM_TYPE.Error, priority=b'high')
        return


class SecurityLinkHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'securityLink',)

    def handleAction(self, model, entityID, action):
        g_eventBus.handleEvent(events.OpenLinkEvent(events.OpenLinkEvent.SECURITY_SETTINGS))
        return


class ClanRulesHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'clanRulesLink',)

    def handleAction(self, model, entityID, action):
        g_eventBus.handleEvent(events.OpenLinkEvent(events.OpenLinkEvent.CLAN_RULES))
        return


class OpenCustomizationHandler(ActionHandler):
    service = dependency.descriptor(ICustomizationService)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openCustomization',)

    def handleAction(self, model, entityID, action):
        super(OpenCustomizationHandler, self).handleAction(model, entityID, action)
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        vehicleIntCD = savedData.get(b'vehicleIntCD')
        vehicle = self.service.getItemByCD(vehicleIntCD)

        def toCustomizationCallback():
            ctx = self.service.getCtx()
            if savedData.get(b'toStyle'):
                if ctx.modeId not in CustomizationModes.BASE_STYLES:
                    ctx.changeMode(CustomizationModes.STYLE_2D, source=CustomizationModeSource.NOTIFICATION)
            elif savedData.get(b'toProjectionDecals'):
                itemCD = savedData.get(b'itemIntCD', 0)
                goToEditableStyle = ctx.canEditStyle(itemCD)
                style = None
                if ctx.modeId in CustomizationModes.BASE_STYLES:
                    style = ctx.mode.modifiedStyle
                if goToEditableStyle and style is not None:
                    ctx.editStyle(style.intCD, source=CustomizationModeSource.NOTIFICATION)
                else:
                    ctx.changeMode(CustomizationModes.CUSTOM, source=CustomizationModeSource.NOTIFICATION)
                ctx.mode.changeTab(tabId=CustomizationTabs.PROJECTION_DECALS, itemCD=itemCD)
            return

        if vehicle.invID != -1:
            context = self.service.getCtx()
            if context is not None and g_currentVehicle.isPresent() and g_currentVehicle.item.intCD == vehicleIntCD:
                toCustomizationCallback()
            else:
                g_eventBus.handleEvent(events.CustomizationEvent(events.CustomizationEvent.SHOW, ctx={b'vehInvID': (vehicle.invID), b'callback': toCustomizationCallback}), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class ProlongStyleRent(ActionHandler):
    service = dependency.descriptor(ICustomizationService)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'prolongStyleRent',)

    def handleAction(self, model, entityID, action):
        super(ProlongStyleRent, self).handleAction(model, entityID, action)
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        vehicleIntCD = savedData.get(b'vehicleIntCD')
        styleIntCD = savedData.get(b'styleIntCD')
        vehicle = self.service.getItemByCD(vehicleIntCD)
        style = self.service.getItemByCD(styleIntCD)

        def prolongRentCallback():
            ctx = self.service.getCtx()
            ctx.changeMode(CustomizationModes.STYLE_3D if style.is3D else CustomizationModes.STYLE_2D)
            ctx.mode.prolongRent(style)
            return

        if vehicle.invID != -1:
            g_eventBus.handleEvent(events.CustomizationEvent(events.CustomizationEvent.SHOW, ctx={b'vehInvID': (vehicle.invID), b'callback': prolongRentCallback}), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class _OpenMissingEventsHandler(ActionHandler):
    __notification = dependency.descriptor(INotificationWindowController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MISSING_EVENTS

    @classmethod
    def getActions(cls):
        return (b'openMissingEvents',)

    def handleAction(self, model, entityID, action):
        notification = self.__notification
        if notification.isEnabled():
            notification.releasePostponed()
        else:
            BigWorld.callback(0, self.__showErrorMessage)
        return

    @staticmethod
    def __showErrorMessage():
        SystemMessages.pushI18nMessage(backport.text(R.strings.system_messages.queue.isInQueue()), type=SystemMessages.SM_TYPE.Error, priority=NotificationPriorityLevel.HIGH)
        return


class _OpenNotrecruitedHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.RECRUIT_REMINDER

    @classmethod
    def getActions(cls):
        return (b'openNotrecruited',)

    def doAction(self, model, entityID, action):
        showBarracks(location=BARRACKS_CONSTANTS.LOCATION_FILTER_NOT_RECRUITED)
        return


class _OpenNotrecruitedSysMessageHandler(_OpenNotrecruitedHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE


class _OpenBarracksHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openBarracks',)

    def doAction(self, model, entityID, action):
        showBarracks()
        return


class _OpenConfirmEmailHandler(NavigationDisabledActionHandler):
    __wgnpSteamAccCtrl = dependency.descriptor(IWGNPSteamAccRequestController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.EMAIL_CONFIRMATION_REMINDER

    @classmethod
    def getActions(cls):
        return (b'openConfirmEmail',)

    @wg_async
    def doAction(self, model, entityID, action):
        status = yield wg_await(self.__wgnpSteamAccCtrl.getEmailStatus())
        if status.typeIs(StatusTypes.ADDED):
            showSteamConfirmEmailOverlay(email=status.email)
        return


class OpenPersonalMissionHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openPersonalMission',)

    def handleAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None:
            showPersonalMission(missionID=savedData[b'questID'])
        return


class _OpenLootBoxesHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openLootBoxes',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None:
            pass
        return


class _LootBoxesAutoOpenHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'lootBoxesAutoOpen',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None and b'rewards' in savedData:
            pass
        return


class _OpenLootBoxSystemHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openLootBoxSystem',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData and b'eventName' in savedData:
            Views.load(ViewID.MAIN, eventName=savedData[b'eventName'])
        return


class _LootBoxSystemAutoOpenHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'lootBoxSystemAutoOpen',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None and b'rewards' in savedData:
            Views.load(ViewID.AUTOOPEN, savedData[b'eventName'], savedData[b'rewards'], savedData[b'boxIDs'])
        return


class _OpenProgressiveRewardView(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.PROGRESSIVE_REWARD

    @classmethod
    def getActions(cls):
        return (b'openProgressiveRewardView',)

    def doAction(self, model, entityID, action):
        showProgressiveRewardWindow()
        return


class _OpenBattlePassProgressionView(NavigationDisabledActionHandler):
    __battlePass = dependency.descriptor(IBattlePassController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openBattlePassProgressionView',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        hideWebBrowserOverlay()
        if savedData is not None:
            chapterID = savedData.get(b'chapterID')
            showBattlePass(R.aliases.battle_pass.PostProgression() if isPostProgressionChapter(chapterID) else (self.__battlePass.isHoliday() or R.aliases.battle_pass.Progression)() if 1 else R.invalid(), chapterID)
        else:
            showBattlePass()
        return


class _OpenBattlePassChapterChoiceView(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openBattlePassChapterChoiceView',)

    def doAction(self, model, entityID, action):
        shared_events.showBattlePass()
        return


class _OpenBPExtraWillEndSoon(NavigationDisabledActionHandler):
    __battlePassController = dependency.descriptor(IBattlePassController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openBPExtraWillEndSoon',)

    def doAction(self, model, entityID, action):
        chapterID = model.getNotification(self.getNotType(), entityID).getSavedData().get(b'chapterID')
        if chapterID is not None and self.__battlePassController.isChapterExists(chapterID):
            if isExtraChapterSeen():
                shared_events.showBattlePass(R.aliases.battle_pass.Progression(), chapterID)
            else:
                shared_events.showBattlePass()
        return


class _OpentBlueprintsConvertSale(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'opentBlueprintsConvertSale',)

    def doAction(self, model, entityID, action):
        showBlueprintsSalePage()
        return


class _OpenMapboxProgression(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openMapboxProgressionScreen',)

    def doAction(self, model, entityID, action):
        showMissionsMapboxProgression()
        return


class _OpenMapboxSurvey(NavigationDisabledActionHandler):
    __mapboxCtrl = dependency.descriptor(IMapboxController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openMapboxSurvey',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        if self.__mapboxCtrl.getProgressionData() is not None:
            self.__mapboxCtrl.showSurvey(notification.getSavedData())
        else:
            showMissionsMapboxProgression()
        return


class _OpenDelayedReward(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openDelayedReward',)

    def doAction(self, model, entityID, action):
        showDelayedReward()
        return


class _OpenChapterChoiceView(_OpenBattlePassProgressionView):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.BATTLE_PASS_SWITCH_CHAPTER_REMINDER


class _OpenEpicBattlesAfterBattleWindow(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showEpicBattlesAfterBattleWindow',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        levelUpInfo = notification.getSavedData()
        showEpicBattlesAfterBattleWindow(levelUpInfo)
        return


class _OpenCustomizationStylesSection(NavigationDisabledActionHandler):
    __customizationService = dependency.descriptor(ICustomizationService)
    __hangarSpace = dependency.descriptor(IHangarSpace)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openCustomizationStylesSection',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        notificationData = notification.getSavedData() or {}
        styleID = notificationData.get(b'styleID')
        if styleID:
            style = self.__customizationService.getItemByID(GUI_ITEM_TYPE.STYLE, styleID)
            self.__customizationService.showCustomization(modeId=CustomizationModes.STYLE_3D if style.is3D else CustomizationModes.STYLE_2D, tabId=CustomizationTabs.STYLES_3D if style.is3D else CustomizationTabs.STYLES_2D, itemCD=style.intCD)
        return


class _OpenIntegratedAuction(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showAuction',)

    def doAction(self, model, entityID, action):
        showShop(getIntegratedAuctionUrl())
        return


class _OpenIntegratedAuctionStart(_OpenIntegratedAuction):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.AUCTION_STAGE_START

    @classmethod
    def getActions(cls):
        return (b'showAuctionStartShop',)


class _OpenIntegratedAuctionFinish(_OpenIntegratedAuction):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.AUCTION_STAGE_FINISH

    @classmethod
    def getActions(cls):
        return (b'showAuctionFinishShop',)


class _OpenPersonalReservesHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openPersonalReserves',)

    def doAction(self, model, entityID, action):
        shared_events.showBoostersActivation()
        return


class _OpenSeniorityAwardsVehicleSelection(NavigationDisabledActionHandler):
    __slots__ = (b'__uiVehicleSelectionNotificationLogger',)
    __seniorityAwardCtrl = dependency.descriptor(ISeniorityAwardsController)

    def __init__(self):
        super(_OpenSeniorityAwardsVehicleSelection, self).__init__()
        self.__uiVehicleSelectionNotificationLogger = VehicleSelectionNotificationLogger()
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'seniorityAwardsVehicleSelection',)

    def doAction(self, model, entityID, action):
        self.__uiVehicleSelectionNotificationLogger.handleClickAction()
        if self.__seniorityAwardCtrl.isVehicleSelectionAvailable:
            showSeniorityRewardVehiclesWindow()
        return


class _OpenWinbackSelectableRewardView(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.WINBACK_SELECTABLE_REWARD_AVAILABLE

    @classmethod
    def getActions(cls):
        return (b'openWinbackSelectableRewardView',)

    def doAction(self, model, entityID, action):
        showWinbackSelectRewardView()
        return


class _OpenWinbackSelectableRewardViewFromQuest(_OpenWinbackSelectableRewardView):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE


class _OpenAchievementsScreen(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'achievementsScreen',)

    def doAction(self, model, entityID, action):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_PROFILE), ctx={b'selectedAlias': (VIEW_ALIAS.PROFILE_TOTAL_PAGE)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class _OpenAdvancedAchievementsScreen(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'advancedAchievementsScreen',)

    def doAction(self, model, entityID, action):
        data = model.getNotification(self.getNotType(), entityID).getSavedData() or {}
        isTrophy = data.get(b'isTrophy')
        target = data.get(b'target')
        uiLogger = AdvancedAchievementLogger(AdvancedAchievementViewKey.NOTIFICATION_CENTER)
        closeCallbackPlaceholder = lambda *args, **kwargs: None
        uiLogger.logClick(AdvancedAchievementButtons.TO_ACHIEVEMENT)
        if isTrophy:
            showTrophiesView(closeCallback=closeCallbackPlaceholder, parentScreen=AdvancedAchievementViewKey.NOTIFICATION_CENTER)
        elif target:
            id, category = target
            initAchievementsIds = createAdvancedAchievementsCatalogInitAchievementIDs(id, category)
            showAdvancedAchievementsCatalogView(initAchievementsIds, category, closeCallback=closeCallbackPlaceholder, parentScreen=AdvancedAchievementViewKey.NOTIFICATION_CENTER)
        else:
            showAdvancedAchievementsView()
        return


class _OpenCollectionHandler(NavigationDisabledActionHandler):
    __collections = dependency.descriptor(ICollectionsSystemController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openCollection',)

    def doAction(self, model, entityID, action):
        collectionID = (model.getNotification(self.getNotType(), entityID).getSavedData() or {}).get(b'collectionId')
        if collectionID:
            showCollectionWindow(collectionID)
        else:
            showCollectionsMainPage()
        return


class _OpenCollectionEntryHandler(_OpenCollectionHandler):
    __collections = dependency.descriptor(ICollectionsSystemController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.COLLECTIONS_ENTRY

    @classmethod
    def getActions(cls):
        return (b'openCollectionEntry',)


class _OpenCollectionRenewHandler(_OpenCollectionHandler):
    __collections = dependency.descriptor(ICollectionsSystemController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.COLLECTIONS_RENEW

    @classmethod
    def getActions(cls):
        return (b'openCollectionRenew',)


class _OpenCollectionRewardHandler(NavigationDisabledActionHandler):
    __collections = dependency.descriptor(ICollectionsSystemController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openCollectionRewards',)

    def doAction(self, model, entityID, action):
        savedData = model.getNotification(self.getNotType(), entityID).getSavedData()
        showCollectionAwardsWindow(savedData[b'collectionId'], savedData[b'bonuses'])
        return


class _OpenPrestigeVehicleStats(NavigationDisabledActionHandler):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openPrestige',)

    def doAction(self, model, entityID, action):
        savedData = model.getNotification(self.getNotType(), entityID).getSavedData()
        showPrestigeVehicleStats(savedData[b'vehCD'])
        return


class _OpenCrewPostProgression(NavigationDisabledActionHandler):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showPostProgress',)

    def doAction(self, model, entityID, action):
        showCrewPostProgressionView()
        return


class _ClaimRewardPostProgression(NavigationDisabledActionHandler):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'claimRewardPostProgress',)

    @decorators.adisp_process(b'updating')
    def doAction(self, model, entityID, action):
        processor = ClaimRewardForPostProgression(crewBooksViewedCache().xppToConvert())
        result = yield processor.request()
        if result.userMsg:

            def showMessage():
                SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType, messageData=result.auxData)
                return

            BigWorld.callback(0, showMessage)
        return


class _OpenPrestigeOnboardingWindow(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.PRESTIGE_FIRST_ENTRY

    @classmethod
    def getActions(cls):
        return (b'openPrestige',)

    def doAction(self, model, entityID, action):
        showPrestigeOnboardingWindow()
        return


class _OpenPunishmentWindowHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openPunishmentWindow',)

    def handleAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None:
            penaltyType = savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.PENALTY_TYPE]
            if penaltyType == PENALTY_TYPES.BAN:
                showBanWindow(savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.ARENA_TYPE_ID], savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.ARENA_TIME], savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.BAN_DURATION], force=True)
            if penaltyType == PENALTY_TYPES.PENALTY:
                showPenaltyWindow(savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.ARENA_TYPE_ID], savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.ARENA_TIME], savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.PUNISHMENT_REASON], savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.IS_AFK_VIOLATION], force=True)
            if penaltyType == PENALTY_TYPES.WARNING:
                showWarningWindow(savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.ARENA_TYPE_ID], savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.ARENA_TIME], savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.PUNISHMENT_REASON], savedData[FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA.IS_AFK_VIOLATION], force=True)
        return


class _OpenGoldExchangeWindow(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.EXCHANGE_RATE_GOLD_DISCOUNT

    @classmethod
    def getActions(cls):
        return (b'openExchangeRateWindow',)

    def doAction(self, model, entityID, action):
        showExchangeGoldWindow()
        return


class _OpenXpExchangeWindow(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.EXCHANGE_RATE_XP_DISCOUNT

    @classmethod
    def getActions(cls):
        return (b'openExchangeRateWindow',)

    def doAction(self, model, entityID, action):
        showExchangeFreeXPWindow()
        return


class _OpenPM3Operation(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'toOperationPM3',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData is not None:
            showPersonalMissionMainWindow(operationID=savedData[b'operationID'])
        return


class _AffirmativePM3Notification(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'affirmativePM3Notification',)

    def doAction(self, model, entityID, action):
        return


class _BattleMattersTaskReminder(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.BATTLE_MATTERS_TASK_REMINDER

    @classmethod
    def getActions(cls):
        return (b'battleMattersTaskReminder',)

    def doAction(self, model, entityID, action):
        showBattleMatters()
        return


class _PetSystemPetAddedNotification(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openPetStorage',)

    def doAction(self, model, entityID, action):
        showPetStorageView()
        return


class _WotPlusExpiredNotification(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'wotPlusExtend',)

    def doAction(self, model, entityID, action):
        steamRegistrationCtrl = dependency.instance(ISteamCompletionController)
        if IS_CHINA or steamRegistrationCtrl.isSteamAccount:
            showShop(getWotPlusShopUrl())
        else:
            showSubscriptionsPage()
        return


class _ChallengesReminderNotification(NavigationDisabledActionHandler):
    __challenges = dependency.descriptor(IChallengesController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.CHALLENGES_REMINDER

    @classmethod
    def getActions(cls):
        return (b'openExpiringChallenge',)

    def doAction(self, model, entityID, action):
        expiringChallenge = first(self.__challenges.getSoonEndingChallenges())
        if expiringChallenge is not None and expiringChallenge.isExpiringSoon:
            showChallenges(expiringChallenge.challengeID)
        return


_AVAILABLE_HANDLERS = [
 ShowBattleResultsHandler, 
 ShowFortBattleResultsHandler, 
 OpenPollHandler, 
 AcceptPrbInviteHandler, 
 DeclinePrbInviteHandler, 
 ApproveFriendshipHandler, 
 CancelFriendshipHandler, 
 WGNCActionsHandler, 
 SecurityLinkHandler, 
 ClanRulesHandler, 
 ShowRankedSeasonCompleteHandler, 
 ShowRankedFinalYearHandler, 
 ShowRankedYearPositionHandler, 
 ShowRankedBattlePageHandler, 
 SelectBattleRoyaleMode, 
 _ShowClanAppsHandler, 
 _ShowClanInvitesHandler, 
 _AcceptClanAppHandler, 
 _DeclineClanAppHandler, 
 _ShowClanAppUserInfoHandler, 
 _ShowClanProfileHandler, 
 _ShowClanSettingsFromAppsHandler, 
 _ShowClanSettingsFromInvitesHandler, 
 _AcceptClanInviteHandler, 
 _DeclineClanInviteHandler, 
 _OpenEventBoardsHandler, 
 OpenCustomizationHandler, 
 _OpenNotrecruitedHandler, 
 OpenPersonalMissionHandler, 
 _OpenLootBoxesHandler, 
 _LootBoxesAutoOpenHandler, 
 _OpenLootBoxSystemHandler, 
 _LootBoxSystemAutoOpenHandler, 
 _OpenProgressiveRewardView, 
 ProlongStyleRent, 
 _OpenBattlePassProgressionView, 
 _OpenBattlePassChapterChoiceView, 
 _OpenBPExtraWillEndSoon, 
 _OpenMissingEventsHandler, 
 _OpenNotrecruitedSysMessageHandler, 
 _OpentBlueprintsConvertSale, 
 _OpenConfirmEmailHandler, 
 _OpenMapboxProgression, 
 _OpenMapboxSurvey, 
 _OpenDelayedReward, 
 _OpenChapterChoiceView, 
 _OpenEpicBattlesAfterBattleWindow, 
 _OpenCustomizationStylesSection, 
 _OpenIntegratedAuction, 
 _OpenIntegratedAuctionStart, 
 _OpenIntegratedAuctionFinish, 
 _OpenPersonalReservesHandler, 
 _OpenMissingEventsHandler, 
 _OpenCollectionHandler, 
 _OpenCollectionEntryHandler, 
 _OpenCollectionRenewHandler, 
 _OpenCollectionRewardHandler, 
 _OpenWinbackSelectableRewardView, 
 _OpenWinbackSelectableRewardViewFromQuest, 
 _OpenAchievementsScreen, 
 _OpenAdvancedAchievementsScreen, 
 _OpenBarracksHandler, 
 _OpenPrestigeVehicleStats, 
 _OpenPrestigeOnboardingWindow, 
 _OpenSeniorityAwardsVehicleSelection, 
 _OpenPunishmentWindowHandler, 
 _OpenXpExchangeWindow, 
 _OpenGoldExchangeWindow, 
 _OpenCrewPostProgression, 
 _ClaimRewardPostProgression, 
 _OpenPM3Operation, 
 _AffirmativePM3Notification, 
 _BattleMattersTaskReminder, 
 _PetSystemPetAddedNotification, 
 _WotPlusExpiredNotification, 
 _ChallengesReminderNotification]
registerNotificationsActionsHandlers(_AVAILABLE_HANDLERS)

class NotificationsActionsHandlers(object):
    __slots__ = (b'__single', b'__multi')

    def __init__(self, handlers=None):
        super(NotificationsActionsHandlers, self).__init__()
        self.__single = {}
        self.__multi = defaultdict(set)
        if not handlers:
            handlers = collectAllNotificationsActionsHandlers()
        for clazz in handlers:
            actionsList = clazz.getActions()
            if actionsList:
                if len(actionsList) == 1:
                    self.__single[(clazz.getNotType(), actionsList[0])] = clazz
                else:
                    LOG_ERROR(b'Handler is not added to collection', clazz)
            else:
                self.__multi[clazz.getNotType()].add(clazz)

        return

    def handleAction(self, model, typeID, entityID, actionName):
        key = (
         typeID, actionName)
        if key in self.__single:
            clazz = self.__single[key]
            clazz().handleAction(model, entityID, actionName)
        elif typeID in self.__multi:
            for clazz in self.__multi[typeID]:
                clazz().handleAction(model, entityID, actionName)

        else:
            LOG_ERROR(b'Action handler not found', typeID, entityID, actionName)
        return

    def cleanUp(self):
        self.__single.clear()
        self.__multi.clear()
        return
