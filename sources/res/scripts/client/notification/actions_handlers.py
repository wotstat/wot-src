from collections import defaultdict
import typing, BigWorld
from CurrentVehicle import g_currentVehicle
from adisp import adisp_process
from armory_yard.skeletons.armory_yard_reroll_controller import IArmoryYardRerollController
from constants import EventPhase
from debug_utils import LOG_DEBUG, LOG_ERROR
from gui import DialogsInterface, SystemMessages, makeHtmlString
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.lobby.customization.shared import CustomizationTabs
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBattlePassPointsProductsUrl, getIntegratedAuctionUrl, getPlayerSeniorityAwardsUrl, getComp7ProductsUrl, getBlackMarketUrl
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.BARRACKS_CONSTANTS import BARRACKS_CONSTANTS
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.battle_results import RequestResultsContext
from gui.clans.clan_helpers import showAcceptClanInviteDialog
from gui.customization.constants import CustomizationModeSource, CustomizationModes
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.paragons.navigation_view_model import TabId
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_main_view_model import TabId as ArmoryTabId
from gui.impl.lobby.early_access.early_access_window_events import showEarlyAccessQuestsView, showEarlyAccessVehicleView
from gui.impl.lobby.paragons.paragons_window_events import showParagonsNavigationView, showParagonsSelectRewardsWindow
from gui.impl.lobby.poll.poll_browser_action import PollBrowserButtonHandler
from gui.platform.base.statuses.constants import StatusTypes
from gui.prb_control import prbDispatcherProperty, prbInvitesProperty
from gui.ranked_battles import ranked_helpers
from gui.server_events.events_dispatcher import showMissionsBattlePass, showMissionsMapboxProgression, showPersonalMission, showBattleMattersMainView
from gui.shared import EVENT_BUS_SCOPE, actions, event_dispatcher as shared_events, events, g_eventBus
from gui.shared.event_dispatcher import hideWebBrowserOverlay, showBlueprintsSalePage, showCollectionAwardsWindow, showCollectionWindow, showDelayedReward, showEpicBattlesAfterBattleWindow, showProgressiveRewardWindow, showRankedYearAwardWindow, showResourceWellProgressionWindow, showShop, showSteamConfirmEmailOverlay, showWotPlusIntroView, showBarracks
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID
from gui.shared.notifications import NotificationPriorityLevel
from gui.shared.system_factory import collectAllNotificationsActionsHandlers, registerNotificationsActionsHandlers
from gui.shared.utils import decorators
from gui.clientgw.clan import contexts as clan_ctxs
from gui.notify_center import g_notifyCenterProvider
from helpers import dependency
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from notification.settings import NOTIFICATION_BUTTON_STATE, NOTIFICATION_TYPE
from predefined_hosts import g_preDefinedHosts
from skeletons.gui.battle_results import IBattleResultsService
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.game_control import IBattlePassController, IBattleRoyaleController, IBrowserController, IMapboxController, ICollectionsSystemController, IRankedBattlesController, ISeniorityAwardsController, IReferralProgramController, IArmoryYardController, IShopSalesEventController, IParagonsController, ILimitedUIController
from skeletons.gui.impl import INotificationWindowController
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController
from skeletons.gui.web import IWebController
from soft_exception import SoftException
from uilogging.collections.loggers import CollectionsLogger
from uilogging.epic_battle.constants import EpicBattleLogActions, EpicBattleLogButtons, EpicBattleLogKeys
from uilogging.epic_battle.loggers import EpicBattleLogger
from uilogging.personal_reserves.loggers import PersonalReservesActivationScreenFlowLogger
from uilogging.seniority_awards.loggers import SeniorityAwardsLogger
from uilogging.wot_plus.loggers import WotPlusNotificationLogger
from uilogging.wot_plus.logging_constants import NotificationAdditionalData
from web.web_client_api import webApiCollection
from web.web_client_api.sound import HangarSoundWebApi
from th_async import th_async, th_await
from gui.shared.event_dispatcher import showVehicleTechTreeView
import logging
_logger = logging.getLogger(__name__)
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
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_MISSIONS), ctx={b'tab': (QUESTS_ALIASES.MISSIONS_EVENT_BOARDS_VIEW_PY_ALIAS)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class _ShowArenaResultHandler(ActionHandler):

    @proto_getter(PROTO_TYPE.BW)
    def proto(self):
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    def handleAction(self, model, entityID, action):
        super(_ShowArenaResultHandler, self).handleAction(model, entityID, action)
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
    luiController = dependency.descriptor(ILimitedUIController)

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
        isLuiLocked = not self.luiController.isRuleCompletedByPrebattleType(invite.type)
        if isLuiLocked:
            if entityID:
                self.prbInvites.declineInvite(entityID)
                self.luiController.sendPlatoonLockedMessage(invite.type, invite.senderFullName)
            else:
                LOG_ERROR(b'Invite is invalid', entityID)
            return
        if state.doLeaveToAcceptInvite(invite.type):
            postActions.append(actions.LeavePrbModalEntity())
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


class NotifyCenterActionsHandler(ActionHandler):

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.NOTIFY_CENTER_POP_UP

    def handleAction(self, model, entityID, action):
        if not self._canNavigate():
            return
        notification = model.collection.getItem(NOTIFICATION_TYPE.NOTIFY_CENTER_POP_UP, entityID)
        if notification:
            actorName = notification.getSavedData()
        else:
            actorName = b''
        g_notifyCenterProvider.doAction(entityID, action, actorName)
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
    __service = dependency.descriptor(ICustomizationService)

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
        vehicle = self.__service.getItemByCD(vehicleIntCD)

        def toCustomizationCallback():
            ctx = self.__service.getCtx()
            if savedData.get(b'toStyle'):
                ctx.changeMode(CustomizationModes.STYLED_2D, source=CustomizationModeSource.NOTIFICATION)
            elif savedData.get(b'toProjectionDecals'):
                itemCD = savedData.get(b'itemIntCD', 0)
                goToEditableStyle = ctx.canEditStyle(itemCD)
                style = None
                if ctx.modeId in CustomizationModes.STYLED:
                    style = ctx.mode.modifiedStyle
                if goToEditableStyle and style is not None:
                    ctx.editStyle(style.intCD, source=CustomizationModeSource.NOTIFICATION)
                else:
                    ctx.changeMode(CustomizationModes.CUSTOM, source=CustomizationModeSource.NOTIFICATION)
                ctx.changeTab(tabId=CustomizationTabs.PROJECTION_DECALS, itemCD=itemCD)
            return

        if vehicle.invID != NO_VEHICLE_ID:
            context = self.__service.getCtx()
            if context is not None and g_currentVehicle.isPresent() and g_currentVehicle.item.intCD == vehicleIntCD:
                toCustomizationCallback()
            else:
                g_eventBus.handleEvent(events.CustomizationEvent(events.CustomizationEvent.SHOW, ctx={b'vehInvID': (vehicle.invID), b'callback': toCustomizationCallback}), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class ProlongStyleRent(ActionHandler):
    __service = dependency.descriptor(ICustomizationService)

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
        vehicle = self.__service.getItemByCD(vehicleIntCD)
        style = self.__service.getItemByCD(styleIntCD)

        def prolongRentCallback():
            ctx = self.__service.getCtx()
            ctx.changeMode(CustomizationModes.STYLED_2D)
            ctx.mode.prolongRent(style)
            return

        if vehicle.invID != NO_VEHICLE_ID:
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

    @th_async
    def doAction(self, model, entityID, action):
        status = yield th_await(self.__wgnpSteamAccCtrl.getEmailStatus())
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
            showMissionsBattlePass(R.views.lobby.battle_pass.BattlePassProgressionsView(), savedData.get(b'chapterID'))
        else:
            showMissionsBattlePass()
        return


class _OpenBattlePassChapterChoiceView(NavigationDisabledActionHandler):
    __battlePassController = dependency.descriptor(IBattlePassController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openBattlePassChapterChoiceView',)

    def doAction(self, model, entityID, action):
        if self.__battlePassController.isSingleChapter():
            return showMissionsBattlePass(R.views.lobby.battle_pass.BattlePassProgressionsView(), self.__battlePassController.getCurrentChapterID())
        return showMissionsBattlePass(R.views.lobby.battle_pass.ChapterChoiceView())


class _OpenBPExtraWillEndSoon(NavigationDisabledActionHandler):
    __battlePassController = dependency.descriptor(IBattlePassController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openBPExtraWillEndSoon',)

    def doAction(self, model, entityID, action):
        chapterID = self.__battlePassController.getMarathonChapterID()
        if chapterID:
            showMissionsBattlePass(R.views.lobby.battle_pass.BattlePassProgressionsView(), chapterID)
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
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        rewardToken = savedData.get(b'rewardToken')
        showDelayedReward(delayedRewardToken=rewardToken, forceCreate=True)
        return


class _OpenBattlePassPointsShop(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openBattlePassPointsShop',)

    def doAction(self, model, entityID, action):
        showShop(getBattlePassPointsProductsUrl())
        return


class _OpenChapterChoiceView(_OpenBattlePassProgressionView):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.BATTLE_PASS_SWITCH_CHAPTER_REMINDER


class _OpenEpicBattlesAfterBattleWindow(NavigationDisabledActionHandler):
    __slots__ = (b'__uiEpicBattleLogger',)

    def __init__(self):
        super(_OpenEpicBattlesAfterBattleWindow, self).__init__()
        self.__uiEpicBattleLogger = EpicBattleLogger()
        return

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
        self.__uiEpicBattleLogger.log(EpicBattleLogActions.CLICK.value, EpicBattleLogButtons.LEVELUP_NOTIFICATION.value, EpicBattleLogKeys.HANGAR.value)
        return


class _OpenResourceWellProgressionStartWindow(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.RESOURCE_WELL_START

    @classmethod
    def getActions(cls):
        return (b'openResourceWellProgressionStartWindow',)

    def doAction(self, model, entityID, action):
        showResourceWellProgressionWindow()
        return


class _OpenResourceWellProgressionNoVehiclesWindow(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openResourceWellProgressionNoVehiclesWindow',)

    def doAction(self, model, entityID, action):
        showResourceWellProgressionWindow()
        return


class _OpenCustomizationStylesSection(NavigationDisabledActionHandler):
    __customizationService = dependency.descriptor(ICustomizationService)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openCustomizationStylesSection',)

    def doAction(self, model, entityID, action):
        if self.__customizationService.getCtx() is None:
            self.__customizationService.showCustomization(callback=self.__onCustomizationLoaded)
        else:
            self.__onCustomizationLoaded()
        return

    @classmethod
    def __onCustomizationLoaded(cls):
        cls.__customizationService.getCtx().changeMode(CustomizationModes.STYLED_2D)
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


class _OpenBlackMarket(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showBlackMarket',)

    def doAction(self, model, entityID, action):
        showShop(getBlackMarketUrl())
        return


class _OpenBlackMarketStart(_OpenBlackMarket):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.BLACK_MARKET_STAGE_START

    @classmethod
    def getActions(cls):
        return (b'showBlackMarketStartShop',)


class _OpenBlackMarketFinish(_OpenBlackMarket):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.BLACK_MARKET_STAGE_FINISH

    @classmethod
    def getActions(cls):
        return (b'showBlackMarketFinishShop',)


class _OpenPersonalReservesHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openPersonalReserves',)

    def doAction(self, model, entityID, action):
        uiLogger = PersonalReservesActivationScreenFlowLogger()
        uiLogger.logOpenFromNotification()
        shared_events.showPersonalReservesPage()
        return


class _SeniorityAwardsTokensHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.SENIORITY_AWARDS_TOKENS

    @classmethod
    def getActions(cls):
        return (b'seniorityAwardsTokens',)

    def doAction(self, model, entityID, action):
        SeniorityAwardsLogger().handleNotificationAction()
        showShop(getPlayerSeniorityAwardsUrl())
        return


class _OpenSeniorityAwards(NavigationDisabledActionHandler):
    __seniorityAwardCtrl = dependency.descriptor(ISeniorityAwardsController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.SENIORITY_AWARDS_QUEST

    @classmethod
    def getActions(cls):
        return (b'seniorityAwardsQuest',)

    def doAction(self, model, entityID, action):
        self.__seniorityAwardCtrl.claimReward()
        return


class _OpenAchievementsScreen(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'achievementsScreen',)

    def doAction(self, model, entityID, action):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_PROFILE), ctx={b'selectedAlias': (VIEW_ALIAS.PROFILE_SUMMARY_PAGE)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class _OpenEventLootBoxesShopHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openEventLootBoxesShop',)

    def doAction(self, model, entityID, action):
        _logger.error(b'NEEDS IMPLEMENT DO ACTION!!')
        return


class _OpenReferralProgramMainViewHandler(NavigationDisabledActionHandler):
    __referralProgramController = dependency.descriptor(IReferralProgramController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openReferralProgramMainView',)

    def doAction(self, model, entityID, action):
        self.__referralProgramController.showWindow()
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
        collectionID = model.getNotification(self.getNotType(), entityID).getSavedData()[b'collectionId']
        showCollectionWindow(collectionID)
        return


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
        collectionID = savedData[b'collectionId']
        CollectionsLogger().handleRewardNotificationAction(collectionID)
        showCollectionAwardsWindow(collectionID, savedData[b'bonuses'], savedData[b'isFinal'])
        return


class _OpenShopSalesEventMainView(NavigationDisabledActionHandler):
    __shopSales = dependency.descriptor(IShopSalesEventController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openShopSalesEventMainView',)

    def doAction(self, model, entityID, action):
        if self.__shopSales.currentEventPhase == EventPhase.IN_PROGRESS:
            self.__shopSales.openMainView()
        return


class _OpenTradingCaravanRefill(_OpenShopSalesEventMainView):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.TRADING_CARAVAN_REFILL

    @classmethod
    def getActions(cls):
        return (b'showTradingCaravanRefill',)


class _OpenArmoryYardMain(NavigationDisabledActionHandler):
    __ctrl = dependency.descriptor(IArmoryYardController)
    __rerollCtrl = dependency.descriptor(IArmoryYardRerollController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openArmoryYardMain',)

    def doAction(self, model, entityID, action):
        rerollContext = self.__rerollCtrl.getRerollContext()
        if rerollContext is not None:
            self.__ctrl.goToArmoryYard(tabId=ArmoryTabId.QUESTS, ctx=rerollContext)
        else:
            self.__ctrl.goToArmoryYard()
        return


class _OpenArmoryYardBuyView(NavigationDisabledActionHandler):
    __ctrl = dependency.descriptor(IArmoryYardController)
    __rerollCtrl = dependency.descriptor(IArmoryYardRerollController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openArmoryYardBuy',)

    def doAction(self, model, entityID, action):
        rerollContext = self.__rerollCtrl.getRerollContext()
        if rerollContext is not None:
            self.__ctrl.goToArmoryYard(tabId=ArmoryTabId.QUESTS, ctx=rerollContext)
        else:
            self.__ctrl.goToArmoryYard(ctx={b'loadBuyView': True})
        return


class _OpenArmoryYardQuest(NavigationDisabledActionHandler):
    __ctrl = dependency.descriptor(IArmoryYardController)
    __rerollCtrl = dependency.descriptor(IArmoryYardRerollController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openArmoryYardQuest',)

    def doAction(self, model, entityID, action):
        rerollContext = self.__rerollCtrl.getRerollContext()
        if rerollContext is not None:
            self.__ctrl.goToArmoryYard(tabId=ArmoryTabId.QUESTS, ctx=rerollContext)
        else:
            self.__ctrl.goToArmoryYardQuests()
        return


class _OpenArmoryYardRerollQuest(NavigationDisabledActionHandler):
    __ctrl = dependency.descriptor(IArmoryYardController)
    __rerollCtrl = dependency.descriptor(IArmoryYardRerollController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openArmoryYardRerollQuest',)

    def doAction(self, model, entityID, action):
        rerollContext = self.__rerollCtrl.getRerollContext()
        if rerollContext is not None:
            self.__ctrl.goToArmoryYard(tabId=ArmoryTabId.QUESTS, ctx=rerollContext)
        else:
            self.__ctrl.goToArmoryYard(tabId=ArmoryTabId.PROGRESS)
        return


class _OpenWotPlusIntroView(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.WOT_PLUS_INTRO

    @classmethod
    def getActions(cls):
        return (b'openWotPlusIntroView',)

    def handleAction(self, model, entityID, action):
        super(_OpenWotPlusIntroView, self).handleAction(model, entityID, action)
        WotPlusNotificationLogger().logDetailsButtonClickEvent(NotificationAdditionalData.SPECIAL_NOTIFICATION)
        showWotPlusIntroView()
        return


class _OpenWotDailyRewardView(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'goToWotPlusDetails',)

    def handleAction(self, model, entityID, action):
        super(_OpenWotDailyRewardView, self).handleAction(model, entityID, action)
        WotPlusNotificationLogger().logDetailsButtonClickEvent(NotificationAdditionalData.RELEASE_NOTIFICATION)
        showWotPlusIntroView()
        return


class _OpenPremShopHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openPremShop',)

    def handleAction(self, model, entityID, action):
        g_eventBus.handleEvent(events.OpenLinkEvent(events.OpenLinkEvent.PREM_SHOP))
        return


class _OpenComp7ShopHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openComp7Shop',)

    def doAction(self, model, entityID, action):
        showShop(getComp7ProductsUrl())
        return


class _OpenEarlyAccessVehicleHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openEarlyAccessVehicle',)

    def doAction(self, model, entityID, action):
        showEarlyAccessVehicleView()
        return


class _OpenEarlyAccessQuestsHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openEarlyAccessQuests',)

    def doAction(self, model, entityID, action):
        showEarlyAccessQuestsView()
        return


class _OpenPollBrowserHandler(ActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openPollBrowser',)

    def handleAction(self, model, entityID, action):
        super(_OpenPollBrowserHandler, self).handleAction(model, entityID, action)
        savedData = model.getNotification(self.getNotType(), entityID).getSavedData()
        if not savedData:
            LOG_ERROR(b'savedData is not found', entityID)
            return
        PollBrowserButtonHandler.invoke(**savedData)
        return


class ParagonsProjectViewHandler(NavigationDisabledActionHandler):
    __paragonsCtrl = dependency.descriptor(IParagonsController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showParagonsProjectView',)

    def doAction(self, model, entityID, action):
        chosenChapter = self.__paragonsCtrl.chapterID
        if chosenChapter is None and self.__paragonsCtrl.isAnyChapterAvailable:
            showParagonsNavigationView(tabId=TabId.CHAPTERS)
        else:
            showParagonsNavigationView(tabId=TabId.PROGRESS)
        return


class ParagonsSelectRewardViewHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showParagonsSelectRewardView',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        auxData = notification.getSettings().auxData
        if auxData is not None:
            showParagonsSelectRewardsWindow(auxData[b'chapter'], auxData[b'level'], auxData[b'entitlements'][0])
        return


class ParagonsCharaptersViewHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showParagonsStagesView',)

    def doAction(self, model, entityID, action):
        showParagonsNavigationView(tabId=TabId.CHAPTERS)
        return


class ShowParagonsResearchesViewHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'showParagonsResearchesView',)

    def doAction(self, model, entityID, action):
        showVehicleTechTreeView()
        return


class _OpenBattleMattersHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openBattleMatters',)

    def doAction(self, model, entityID, action):
        showBattleMattersMainView()
        return


class _BattleMattersTaskReminder(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.BATTLE_MATTERS_TASK_REMINDER

    @classmethod
    def getActions(cls):
        return (b'battleMattersTaskReminder',)

    def doAction(self, model, entityID, action):
        showBattleMattersMainView()
        return


_AVAILABLE_HANDLERS = (
 ShowBattleResultsHandler,
 ShowFortBattleResultsHandler,
 OpenPollHandler,
 AcceptPrbInviteHandler,
 DeclinePrbInviteHandler,
 ApproveFriendshipHandler,
 CancelFriendshipHandler,
 NotifyCenterActionsHandler,
 SecurityLinkHandler,
 ClanRulesHandler,
 ShowRankedSeasonCompleteHandler,
 ShowRankedFinalYearHandler,
 ShowRankedYearPositionHandler,
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
 _OpenShopSalesEventMainView,
 _OpenTradingCaravanRefill,
 _OpenBattlePassPointsShop,
 _OpenChapterChoiceView,
 _OpenEpicBattlesAfterBattleWindow,
 _OpenResourceWellProgressionStartWindow,
 _OpenResourceWellProgressionNoVehiclesWindow,
 _OpenCustomizationStylesSection,
 _OpenIntegratedAuction,
 _OpenIntegratedAuctionStart,
 _OpenIntegratedAuctionFinish,
 _OpenBlackMarket,
 _OpenBlackMarketStart,
 _OpenBlackMarketFinish,
 _OpenPersonalReservesHandler,
 _SeniorityAwardsTokensHandler,
 _OpenSeniorityAwards,
 _OpenMissingEventsHandler,
 _OpenReferralProgramMainViewHandler,
 _OpenEventLootBoxesShopHandler,
 _OpenCollectionHandler,
 _OpenCollectionRewardHandler,
 _OpenArmoryYardMain,
 _OpenArmoryYardQuest,
 _OpenArmoryYardRerollQuest,
 _OpenArmoryYardBuyView,
 _OpenAchievementsScreen,
 _OpenBarracksHandler,
 _OpenPremShopHandler,
 _OpenComp7ShopHandler,
 _OpenEarlyAccessVehicleHandler,
 _OpenEarlyAccessQuestsHandler,
 _OpenPollBrowserHandler,
 ParagonsProjectViewHandler,
 ParagonsCharaptersViewHandler,
 ShowParagonsResearchesViewHandler,
 ParagonsSelectRewardViewHandler,
 _OpenBattleMattersHandler,
 _BattleMattersTaskReminder)
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
