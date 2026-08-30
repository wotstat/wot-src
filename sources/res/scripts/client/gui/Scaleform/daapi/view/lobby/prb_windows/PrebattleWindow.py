from __future__ import absolute_import
from CurrentVehicle import g_currentVehicle
from adisp import adisp_process
from constants import MODULE_NAME_SEPARATOR
from debug_utils import LOG_ERROR
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.view.meta.PrebattleWindowMeta import PrebattleWindowMeta
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from skeletons.gui.game_control import ICraftmachineController
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE, TARGET_ID
from gui.Scaleform.managers.windows_stored_data import stored_window
from gui.prb_control.entities.base.ctx import LeavePrbAction
from gui.prb_control.entities.base.legacy.ctx import SetPlayerStateCtx
from gui.prb_control.entities.base.legacy.listener import ILegacyListener
from gui.prb_control.formatters import messages
from gui.prb_control.items import prb_items
from gui.prb_control.settings import CTRL_ENTITY_TYPE, PREBATTLE_PLAYERS_SORT_TYPES
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.events import FocusEvent
from helpers import dependency
from helpers import int2roman
from messenger import g_settings, MessengerEntry
from messenger.ext import channel_num_gen
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS
from messenger.m_constants import USER_GUI_TYPE, PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.events import g_messengerEvents
from messenger.storage import storage_getter
from prebattle_shared import decodeRoster
from skeletons.gui.lobby_context import ILobbyContext

@stored_window(DATA_TYPE.CAROUSEL_WINDOW, TARGET_ID.CHANNEL_CAROUSEL)
class PrebattleWindow(PrebattleWindowMeta, ILegacyListener):
    lobbyContext = dependency.descriptor(ILobbyContext)
    __craftmacineConrtoller = dependency.descriptor(ICraftmachineController)

    def __init__(self, prbName=b'prebattle'):
        super(PrebattleWindow, self).__init__()
        self.__prbName = prbName
        self.__clientID = channel_num_gen.getClientID4Prebattle(self.prbEntity.getEntityType())
        return

    def onFocusIn(self, alias):
        self.fireEvent(FocusEvent(FocusEvent.COMPONENT_FOCUSED, {b'clientID': (self.__clientID)}))
        return

    def onWindowClose(self):
        self._doLeave()
        return

    def onWindowMinimize(self):
        chat = self.chat
        if chat:
            chat.minimize()
        self.destroy()
        return

    def onSourceLoaded(self):
        if not self._isInLegacyPreBattle():
            self.destroy()
        return

    @storage_getter(b'users')
    def usersStorage(self):
        return

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return

    @adisp_process
    def requestToReady(self, value):
        if value:
            waitingID = b'prebattle/player_ready'
        else:
            waitingID = b'prebattle/player_not_ready'
        result = yield self.prbDispatcher.sendPrbRequest(SetPlayerStateCtx(value, waitingID=waitingID))
        if result:
            self.as_toggleReadyBtnS(not value)
        return

    def requestToLeave(self):
        self._doLeave(False)
        return

    def showPrebattleSendInvitesWindow(self):
        if self.canSendInvite():
            self.fireEvent(events.LoadViewEvent(SFViewLoadParams(PREBATTLE_ALIASES.SEND_INVITES_WINDOW_PY), ctx={b'prbName': (self.__prbName), 
               b'ctrlType': (CTRL_ENTITY_TYPE.LEGACY)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def showFAQWindow(self):
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(MESSENGER_VIEW_ALIAS.FAQ_WINDOW)), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def getClientID(self):
        return self.__clientID

    def requestToKickPlayer(self, value):
        return

    def canSendInvite(self):
        return self.prbEntity.getPermissions().canSendInvite()

    def isPlayerReady(self):
        return self.prbEntity.getPlayerInfo().isReady()

    def isPlayerCreator(self):
        return self.prbEntity.isCommander()

    def isReadyBtnEnabled(self):
        entity = self.prbEntity
        _, assigned = decodeRoster(entity.getRosterKey())
        return g_currentVehicle.isReadyToPrebattle() and not (entity.getTeamState().isInQueue() and assigned) and entity.canPlayerDoAction().isValid

    def isLeaveBtnEnabled(self):
        entity = self.prbEntity
        _, assigned = decodeRoster(entity.getRosterKey())
        return not (entity.getTeamState().isInQueue() and entity.getPlayerInfo().isReady() and assigned)

    def startListening(self):
        if self._isInLegacyPreBattle():
            self.startPrbListening()
        g_currentVehicle.onChanged += self._handleCurrentVehicleChanged
        g_messengerEvents.users.onUserActionReceived += self._onUserActionReceived
        return

    def stopListening(self):
        self.stopPrbListening()
        self.removeListener(events.MessengerEvent.PRB_CHANNEL_CTRL_INITED, self.__handlePrbChannelControllerInited, scope=EVENT_BUS_SCOPE.LOBBY)
        g_currentVehicle.onChanged -= self._handleCurrentVehicleChanged
        g_messengerEvents.users.onUserActionReceived -= self._onUserActionReceived
        return

    @property
    def chat(self):
        chat = None
        if MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT in self.components:
            chat = self.components[MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT]
        return chat

    def onPlayerAdded(self, entity, playerInfo):
        chat = self.chat
        if chat and not playerInfo.isCurrentPlayer():
            chat.as_addMessageS(messages.getPlayerAddedMessage(self.__prbName, playerInfo))
        return

    def onPlayerRemoved(self, entity, playerInfo):
        chat = self.chat
        if chat and not playerInfo.isCurrentPlayer():
            chat.as_addMessageS(messages.getPlayerRemovedMessage(self.__prbName, playerInfo))
        return

    def onPlayerRosterChanged(self, entity, actorInfo, playerInfo):
        chat = self.chat
        if chat:
            chat.as_addMessageS(messages.getPlayerAssignFlagChanged(actorInfo, playerInfo))
        return

    def onPlayerStateChanged(self, entity, roster, accountInfo):
        playerInfo = accountInfo
        team, assigned = decodeRoster(roster)
        data = {b'dbID': (playerInfo.dbID), 
           b'state': (playerInfo.state), 
           b'igrType': (playerInfo.igrType), 
           b'icon': b'', 
           b'vShortName': b'', 
           b'vLevel': b'', 
           b'vType': b'', 
           b'isCurrentPayer': (playerInfo.isCurrentPlayer())}
        if playerInfo.isVehicleSpecified():
            moduleName = b''
            vehicle = playerInfo.getVehicle()
            badgeVisibility = playerInfo.getEnhancementVisibility()
            if badgeVisibility:
                moduleName = MODULE_NAME_SEPARATOR.join([self.__craftmacineConrtoller.getModuleName(module) for module in playerInfo.getEnhancementModules()])
            data.update({b'icon': (vehicle.iconContour), 
               b'vShortName': (vehicle.shortUserName), 
               b'vLevel': (int2roman(vehicle.level)), 
               b'vType': (vehicle.type), 
               b'isExperimentalModule': (bool(badgeVisibility)), 
               b'experimentalModuleName': moduleName})
        self.as_setPlayerStateS(team, assigned, data)
        if playerInfo.isCurrentPlayer():
            self.as_toggleReadyBtnS(not playerInfo.isReady())
        else:
            chat = self.chat
            if chat:
                chat.as_addMessageS(messages.getPlayerStateChangedMessage(self.__prbName, playerInfo))
        return

    def _populate(self):
        super(PrebattleWindow, self)._populate()
        self.startListening()
        self.as_enableReadyBtnS(self.isReadyBtnEnabled())
        return

    def _dispose(self):
        super(PrebattleWindow, self)._dispose()
        self.stopListening()
        return

    def _closeSendInvitesWindow(self):
        container = self.app.containerManager.getContainer(WindowLayer.WINDOW)
        if container is not None:
            window = container.getView(criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (PREBATTLE_ALIASES.SEND_INVITES_WINDOW_PY)})
            if window is not None:
                window.destroy()
        return

    def _isInLegacyPreBattle(self):
        dispatcher = self.prbDispatcher
        return dispatcher is not None and dispatcher.getFunctionalState().isInLegacy()

    def _setRosterList(self, rosters):
        raise NotImplementedError
        return

    def _makeAccountsData(self, accounts, playerSortKeyType=PREBATTLE_PLAYERS_SORT_TYPES.REGULAR):
        result = []
        isPlayerSpeaking = self.bwProto.voipController.isPlayerSpeaking
        getUser = self.usersStorage.getUser
        getColors = g_settings.getColorScheme(b'rosters').getColors
        accounts = sorted(accounts, key=prb_items.getPlayersSortKey(playerSortKeyType))
        for account in accounts:
            vContourIcon = b''
            vShortName = b''
            vLevel = b''
            vType = b''
            moduleName = b''
            badgeVisibility = False
            user = getUser(account.dbID)
            if user is not None:
                key = user.getGuiType()
            else:
                key = USER_GUI_TYPE.OTHER
            if account.isVehicleSpecified():
                vehicle = account.getVehicle()
                badgeVisibility = account.getEnhancementVisibility()
                if badgeVisibility:
                    moduleName = MODULE_NAME_SEPARATOR.join([self.__craftmacineConrtoller.getModuleName(module) for module in account.getEnhancementModules()])
                vContourIcon = vehicle.iconContour
                vShortName = vehicle.shortUserName
                vLevel = int2roman(vehicle.level)
                vType = vehicle.type
            result.append({b'accID': (account.accID), 
               b'dbID': (account.dbID), 
               b'userName': (account.name), 
               b'clanAbbrev': (account.clanAbbrev), 
               b'region': (self.lobbyContext.getRegionCode(account.dbID)), 
               b'fullName': (account.getFullName()), 
               b'igrType': (account.igrType), 
               b'time': (account.time), 
               b'isCreator': (account.isCreator), 
               b'state': (account.state), 
               b'icon': vContourIcon, 
               b'vShortName': vShortName, 
               b'isCurrentPayer': (account.isCurrentPlayer()), 
               b'vLevel': vLevel, 
               b'vType': vType, 
               b'tags': (list(user.getTags()) if user else []), 
               b'isPlayerSpeaking': (isPlayerSpeaking(account.dbID)), 
               b'colors': (getColors(key)), 
               b'isExperimentalModule': (bool(badgeVisibility)), 
               b'experimentalModuleName': moduleName, 
               b'hasPermissions': False})

        return result

    def _handleCurrentVehicleChanged(self):
        self.as_enableReadyBtnS(self.isReadyBtnEnabled())
        return

    def _onUserActionReceived(self, actionIndex, user, shadowMode):
        self._setRosterList(self.prbEntity.getRosters())
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT:
            channels = MessengerEntry.g_instance.gui.channelsCtrl
            controller = None
            if channels:
                controller = channels.getController(self.__clientID)
            if controller is not None:
                controller.setView(viewPy)
            else:
                self.addListener(events.MessengerEvent.PRB_CHANNEL_CTRL_INITED, self.__handlePrbChannelControllerInited, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    @adisp_process
    def _doLeave(self, isExit=True, parent=None):
        yield self.prbDispatcher.doLeaveAction(LeavePrbAction(isExit=isExit, parent=parent))
        return

    def __handlePrbChannelControllerInited(self, event):
        ctx = event.ctx
        prbType = ctx.get(b'prbType')
        if not prbType:
            LOG_ERROR(b'Prebattle type is not defined', ctx)
            return
        else:
            controller = ctx.get(b'controller')
            if controller is None:
                LOG_ERROR(b'Channel controller is not defined', ctx)
                return
            if prbType is self.prbEntity.getEntityType():
                chat = self.chat
                if chat is not None:
                    controller.setView(chat)
            return
