from __future__ import absolute_import
from future.utils import viewvalues
import BigWorld
from adisp import adisp_process
import ArenaType
from constants import PREBATTLE_MAX_OBSERVERS_IN_TEAM, OBSERVERS_BONUS_TYPES, PREBATTLE_ERRORS, PREBATTLE_TYPE
from frameworks.wulf import WindowLayer
from gui import SystemMessages, GUI_SETTINGS
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.trainings import formatters
from gui.Scaleform.daapi.view.lobby.trainings.sound_constants import TRAININGS_SOUND_SPACE
from gui.Scaleform.daapi.view.meta.TrainingRoomBaseMeta import TrainingRoomBaseMeta
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.BATTLE_TYPES import BATTLE_TYPES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.Scaleform.settings import ICONS_SIZES
from gui.impl import backport
from gui.prb_control.entities.base.ctx import LeavePrbAction
from gui.prb_control.entities.base.legacy.ctx import SetTeamStateCtx, AssignLegacyCtx, SwapTeamsCtx, SetPlayerStateCtx
from gui.prb_control.entities.base.legacy.listener import ILegacyListener
from gui.prb_control.entities.training.legacy.ctx import SetPlayerObserverStateCtx, ChangeArenaVoipCtx, ChangeArenaGuiCtx
from gui.prb_control.entities.training.legacy.entity import TrainingEntity
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.items.prb_items import getPlayersSortKey
from gui.prb_control.settings import PREBATTLE_ROSTER, PREBATTLE_SETTING_NAME
from gui.prb_control.settings import REQUEST_TYPE, CTRL_ENTITY_TYPE
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.events import CoolDownEvent
from gui.shared.formatters import text_styles
from gui.sounds.ambients import LobbySubViewEnv
from gui.training_room_external_handlers import getAllTrainingRoomHandlers, getTrainingRoomHandler
from helpers import dependency
from helpers import int2roman, i18n
from helpers.statistics import HANGAR_LOADING_STATE
from messenger.ext import passCensor
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.events import g_messengerEvents
from messenger.storage import MessengerStorageDescriptor, UsersStorage
from prebattle_shared import decodeRoster
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from skeletons.helpers.statistics import IStatisticsCollector
BATTLE_TYPES_ICONS = {(PREBATTLE_TYPE.TRAINING): (BATTLE_TYPES.TRAINING), 
   (PREBATTLE_TYPE.EPIC_TRAINING): (BATTLE_TYPES.EPIC_TRAINING)}

class TrainingRoomBase(LobbySubView, TrainingRoomBaseMeta, ILegacyListener):
    __sound_env__ = LobbySubViewEnv
    _COMMON_SOUND_SPACE = TRAININGS_SOUND_SPACE
    itemsCache = dependency.descriptor(IItemsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)
    statsCollector = dependency.descriptor(IStatisticsCollector)
    usersStorage = MessengerStorageDescriptor(UsersStorage)

    def __init__(self, _=None):
        super(TrainingRoomBase, self).__init__()
        self.__currentPlayerIsOut = False
        return

    def onEscape(self):
        dialogsContainer = self.app.containerManager.getContainer(WindowLayer.TOP_WINDOW)
        if not dialogsContainer.getView(criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (VIEW_ALIAS.LOBBY_MENU)}):
            self.fireEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_MENU)), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def onFocusIn(self, alias):
        super(TrainingRoomBase, self).onFocusIn(alias)
        self.__currentPlayerEntered()
        return

    def showTrainingSettings(self):
        return

    def onWindowMinimize(self):
        g_eventDispatcher.loadHangar()
        return

    def onTryClosing(self):
        self._dispose()
        return True

    def canSendInvite(self):
        if self.prbEntity:
            return self.prbEntity.getPermissions().canSendInvite()
        return False

    def canChangePlayerTeam(self):
        if self.prbEntity:
            return self.prbEntity.getPermissions().canChangePlayerTeam()
        return False

    def canChangeSetting(self):
        if self.prbEntity:
            return self.prbEntity.getPermissions().canChangeSetting()
        return False

    def canStartBattle(self):
        if self.prbEntity:
            return self.prbEntity.getPermissions().canStartBattle()
        return False

    def canAssignToTeam(self, team):
        if self.prbEntity:
            return self.prbEntity.getPermissions().canAssignToTeam(int(team))
        return False

    def canDestroyRoom(self):
        if self.prbEntity:
            settings = self.prbEntity.getSettings()
            playerName = BigWorld.player().name
            return settings[PREBATTLE_SETTING_NAME.CREATOR] == playerName and settings[PREBATTLE_SETTING_NAME.DESTROY_IF_CREATOR_OUT]
        return False

    def getPlayerTeam(self, accID):
        return self.prbEntity.getPlayerTeam(accID)

    def showPrebattleInvitationsForm(self):
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(PREBATTLE_ALIASES.SEND_INVITES_WINDOW_PY), ctx={b'prbName': b'training', 
           b'ctrlType': (CTRL_ENTITY_TYPE.LEGACY)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def startTraining(self):
        self._closeWindows()
        self.__doStartTraining()
        return

    def onTeamStatesReceived(self, entity, team1State, team2State):
        _, assigned = decodeRoster(entity.getRosterKey())
        if team1State.isInQueue() and team2State.isInQueue() and assigned:
            self.as_disableControlsS(True)
        elif assigned is False:
            self.as_enabledCloseButtonS(True)
        return

    def closeTrainingRoom(self):
        self._doLeave(isExit=False, parent=self.getParentWindow())
        return

    @adisp_process
    def onSettingUpdated(self, entity, settingName, settingValue):
        if settingName in (PREBATTLE_SETTING_NAME.ARENA_TYPE_ID, PREBATTLE_SETTING_NAME.LIMITS):
            settings = entity.getSettings()
            if settingName == PREBATTLE_SETTING_NAME.ARENA_TYPE_ID:
                arenaTypeID = settingValue
            else:
                arenaTypeID = settings[PREBATTLE_SETTING_NAME.ARENA_TYPE_ID]
            arenaType = ArenaType.g_cache.get(arenaTypeID)
            self.as_updateMapS(arenaTypeID, self.__getMaxPlayersInTeam() * 2, arenaType.name, formatters.getTrainingRoomTitle(arenaType), formatters.getArenaSubTypeString(arenaTypeID), arenaType.description, self.__battleTypeIcon(settings[PREBATTLE_SETTING_NAME.BATTLE_TYPE]), self.__getAdditionalInfo(), self._isObserverModeEnabled())
        elif settingName == PREBATTLE_SETTING_NAME.ROUND_LENGTH:
            self.as_updateTimeoutS(formatters.getRoundLenString(settingValue))
        elif settingName == PREBATTLE_SETTING_NAME.COMMENT:
            self.as_updateCommentS(settingValue)
        elif settingName == PREBATTLE_SETTING_NAME.ARENA_VOIP_CHANNELS:
            self.as_setArenaVoipChannelsS(settingValue)
        elif settingName == PREBATTLE_SETTING_NAME.ARENA_GUI_TYPE:
            yield self.prbDispatcher.sendPrbRequest(ChangeArenaGuiCtx(waitingID=b'prebattle/change_arena_gui'))
        self._updateStartButton(entity)
        return

    def onRostersChanged(self, entity, rosters, full):
        self._updateStartButton(entity)
        return

    def onPlayerStateChanged(self, entity, roster, accountInfo):
        if not self.__currentPlayerIsOut and accountInfo.isCurrentPlayer() and not accountInfo.isReady():
            self.__currentPlayerIsOut = True
        stateString = formatters.getPlayerStateString(accountInfo.state)
        vContourIcon = b''
        vShortName = b''
        vLevel = b''
        if accountInfo.isVehicleSpecified():
            vehicle = accountInfo.getVehicle()
            vContourIcon = vehicle.iconContour
            vShortName = vehicle.shortUserName
            vLevel = int2roman(vehicle.level)
        badge = accountInfo.getBadge()
        badgeVO = badge.getBadgeVO(ICONS_SIZES.X24, {b'isAtlasSource': False}) if badge else {}
        if roster == PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1:
            self.as_setPlayerStateInTeam1S(accountInfo.dbID, stateString, vContourIcon, vShortName, vLevel, accountInfo.igrType, badgeVO)
        elif roster == PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2:
            self.as_setPlayerStateInTeam2S(accountInfo.dbID, stateString, vContourIcon, vShortName, vLevel, accountInfo.igrType, badgeVO)
        else:
            self.as_setPlayerStateInOtherS(accountInfo.dbID, stateString, vContourIcon, vShortName, vLevel, accountInfo.igrType, badgeVO)
        creator = self.__getCreatorFromRosters()
        if accountInfo.dbID == creator.dbID:
            self.__showSettings(entity)
        if isinstance(self.prbEntity, TrainingEntity) and accountInfo.isCurrentPlayer():
            if self._isObserverModeEnabled():
                self.as_setObserverS(self.prbEntity.storage.isObserver)
        self.__currentPlayerEntered(accountInfo.isReady())
        self._updateStartButton(entity)
        return

    def onPlayerTeamNumberChanged(self, entity, team):
        if VIEW_ALIAS.MINIMAP_LOBBY in self.components:
            self.components[VIEW_ALIAS.MINIMAP_LOBBY].swapTeams(team)
        return

    @adisp_process
    def changeTeam(self, accID, slot):
        roster = int(slot)
        if not slot:
            roster = self.prbEntity.getRosterKey(accID)
            if not roster & PREBATTLE_ROSTER.UNASSIGNED:
                roster |= PREBATTLE_ROSTER.UNASSIGNED
        ctx = AssignLegacyCtx(accID, roster, waitingID=b'prebattle/assign')
        result = yield self.prbDispatcher.sendPrbRequest(ctx)
        if not result:
            self._showActionErrorMessage(ctx.getLastErrorString())
        return

    @adisp_process
    def swapTeams(self):
        result = yield self.prbDispatcher.sendPrbRequest(SwapTeamsCtx(waitingID=b'prebattle/swap'))
        if not result:
            self._showActionErrorMessage()
        return

    @adisp_process
    def selectObserver(self, isObserver):
        if not isObserver:
            playersCount = 0
            roster = self.prbEntity.getRosterKey()
            if roster != PREBATTLE_ROSTER.UNKNOWN and roster & PREBATTLE_ROSTER.UNASSIGNED == 0:
                accounts = self.prbEntity.getRosters()[roster]
                for account in accounts:
                    if account.isVehicleSpecified():
                        vehicle = account.getVehicle()
                        if not vehicle.isObserver:
                            playersCount += 1

            playersMaxCount = self.__getPlayersMaxCount()
            if playersCount >= playersMaxCount:
                event = CoolDownEvent()
                self.as_startCoolDownObserverS(event.coolDown)
                self.as_setObserverS(True)
                self._showActionErrorMessage(PREBATTLE_ERRORS.PLAYERS_LIMIT)
                return
        result = yield self.prbDispatcher.sendPrbRequest(SetPlayerObserverStateCtx(isObserver, True, waitingID=b'prebattle/change_user_status'))
        if not result:
            self.as_setObserverS(False)
            self._showActionErrorMessage()
        return

    @adisp_process
    def selectCommonVoiceChat(self, index):
        result = yield self.prbDispatcher.sendPrbRequest(ChangeArenaVoipCtx(int(index), waitingID=b'prebattle/change_arena_voip'))
        if not result:
            prbSettings = self.prbEntity.getSettings()
            self.as_setArenaVoipChannelsS(prbSettings[PREBATTLE_SETTING_NAME.ARENA_VOIP_CHANNELS])
            self._showActionErrorMessage()
        return

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return

    def _populate(self):
        super(TrainingRoomBase, self)._populate()
        entity = self.prbEntity
        if entity.getEntityType():
            self.__showSettings(entity)
            self._showRosters(entity, entity.getRosters())
            self.__swapTeamsInMinimap(entity.getPlayerTeam())
        self.startPrbListening()
        self._addListeners()
        isObserver = False
        if entity.getPlayerInfo().isVehicleSpecified():
            isObserver = entity.getPlayerInfo().getVehicle().isObserver
        self.as_setObserverS(isObserver)
        self.statsCollector.noteHangarLoadingState(HANGAR_LOADING_STATE.TRAINING_UI_READY)
        return

    def _addListeners(self):
        g_messengerEvents.users.onUserActionReceived += self.__me_onUserActionReceived
        self.addListener(events.CoolDownEvent.PREBATTLE, self._handleSetPrebattleCoolDown, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _removeListeners(self):
        g_messengerEvents.users.onUserActionReceived -= self.__me_onUserActionReceived
        self.removeListener(events.CoolDownEvent.PREBATTLE, self._handleSetPrebattleCoolDown, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _dispose(self):
        self.stopPrbListening()
        self._removeListeners()
        self._closeWindows()
        super(TrainingRoomBase, self)._dispose()
        return

    def _handleSetPrebattleCoolDown(self, event):
        if event.requestID is REQUEST_TYPE.CHANGE_SETTINGS:
            self.as_startCoolDownSettingS(event.coolDown)
        elif event.requestID is REQUEST_TYPE.CHANGE_ARENA_VOIP:
            self.as_startCoolDownVoiceChatS(event.coolDown)
        elif event.requestID is REQUEST_TYPE.CHANGE_USER_STATUS:
            self.as_startCoolDownObserverS(event.coolDown)
        return

    def _showRosters(self, entity, rosters):
        self._updateStartButton(entity)
        return

    def _updateStartButton(self, entity):
        if entity.getPermissions().canStartBattle() and self.__isActorAssigned(entity):
            validationResult = entity.getLimits().isTeamsValid()
            if validationResult is None or validationResult.isValid:
                self.as_enabledCloseButtonS(True)
                self.as_setStartButtonStateS(True)
            else:
                self.as_setStartButtonStateS(False)
        else:
            self.as_setStartButtonStateS(False)
        return

    def _closeWindows(self):
        return

    def _closeWindow(self, windowAlias):
        window = self.app.containerManager.getView(WindowLayer.WINDOW, criteria={(POP_UP_CRITERIA.VIEW_ALIAS): windowAlias})
        if window is not None:
            window.destroy()
        return

    def _makeAccountsData(self, accounts, rLabel=None):
        listData = []
        isPlayerSpeaking = self.bwProto.voipController.isPlayerSpeaking
        accounts = sorted(accounts, key=getPlayersSortKey())
        getUser = self.usersStorage.getUser
        for account in accounts:
            vContourIcon = b''
            vShortName = b''
            vLevel = b''
            dbID = account.dbID
            user = getUser(dbID)
            if account.isVehicleSpecified():
                vehicle = account.getVehicle()
                vContourIcon = vehicle.iconContour
                vShortName = vehicle.shortUserName
                vLevel = int2roman(vehicle.level)
            badge = account.getBadge()
            badgeVO = badge.getBadgeVO(ICONS_SIZES.X24, {b'isAtlasSource': False}) if badge else {}
            listData.append({b'accID': (account.accID), 
               b'dbID': (account.dbID), 
               b'userName': (account.name), 
               b'fullName': (account.getFullName()), 
               b'stateString': (formatters.getPlayerStateString(account.state)), 
               b'icon': vContourIcon, 
               b'vShortName': vShortName, 
               b'vLevel': vLevel, 
               b'tags': (list(user.getTags()) if user else []), 
               b'isPlayerSpeaking': (bool(isPlayerSpeaking(account.dbID))), 
               b'clanAbbrev': (account.clanAbbrev), 
               b'region': (self.lobbyContext.getRegionCode(account.dbID)), 
               b'igrType': (account.igrType), 
               b'badgeVisualVO': badgeVO})

        label = b''
        if rLabel is not None:
            label = text_styles.main(backport.text(rLabel, total=text_styles.stats(str(len(listData)))))
        result = {b'listData': listData, 
           b'teamLabel': label}
        return result

    def _showActionErrorMessage(self, errType=None):
        errors = {(PREBATTLE_ERRORS.ROSTER_LIMIT): (
                                           SYSTEM_MESSAGES.TRAINING_ERROR_ADDPLAYER, {}), 
           (PREBATTLE_ERRORS.PLAYERS_LIMIT): (
                                            SYSTEM_MESSAGES.TRAINING_ERROR_SELECTOBSERVER, {b'numPlayers': (self.__getPlayersMaxCount())})}
        errMsg = self.__getErrorClientMessageData(errType)
        if errMsg is None:
            errMsg = errors.get(errType, (SYSTEM_MESSAGES.TRAINING_ERROR_DOACTION, {}))
        SystemMessages.pushMessage(i18n.makeString(errMsg[0], **errMsg[1]), type=SystemMessages.SM_TYPE.Error)
        return

    def _isObserverModeEnabled(self):
        observerValidator = getTrainingRoomHandler(self.__trainingArenaGuiType()).getObserverValidator()
        if observerValidator is not None and not observerValidator():
            return False
        else:
            minCount = self.prbEntity.getSettings().getTeamLimits(1)[b'minCount']
            return GUI_SETTINGS.trainingObserverModeEnabled and minCount > 0

    def _updateTrainingRoom(self, event):
        self.__changeTrainingRoomSettings(event.ctx.get(b'settings', None))
        return

    @adisp_process
    def _doLeave(self, isExit=True, parent=None):
        yield self.prbDispatcher.doLeaveAction(LeavePrbAction(isExit=isExit, parent=parent))
        return

    @adisp_process
    def __changeTrainingRoomSettings(self, settings):
        if settings and settings.areSettingsChanged(self.prbEntity.getSettings()):
            settings.setWaitingID(b'prebattle/change_settings')
            result = yield self.prbDispatcher.sendPrbRequest(settings)
            if not result:
                self._showActionErrorMessage()
        return

    def __getPlayersMaxCount(self):
        playersMaxCount = self.prbEntity.getTeamLimits()[b'maxCount'][0]
        if self.prbEntity.getSettings()[b'bonusType'] in OBSERVERS_BONUS_TYPES:
            playersMaxCount -= PREBATTLE_MAX_OBSERVERS_IN_TEAM
        return playersMaxCount

    def __showSettings(self, entity):
        settings = entity.getSettings()
        if settings is None:
            return
        else:
            isCreator = entity.isCommander()
            permissions = entity.getPermissions()
            arenaTypeID = settings[b'arenaTypeID']
            arenaType = ArenaType.g_cache.get(arenaTypeID)
            comment = passCensor(settings[b'comment'])
            creatorFullName, creatorClan, creatorRegion, creatorIgrType = (None, None, None, 0)
            creator = self.__getCreatorFromRosters()
            badgeVO = {}
            if creator:
                creatorFullName = creator.getFullName()
                creatorClan = creator.clanAbbrev
                creatorRegion = self.lobbyContext.getRegionCode(creator.dbID)
                creatorIgrType = creator.igrType
                badge = creator.getBadge()
                badgeVO = badge.getBadgeVO(ICONS_SIZES.X24, {b'isAtlasSource': False}) if badge else {}
            self.as_setInfoS({b'isCreator': isCreator, 
               b'creator': (settings[PREBATTLE_SETTING_NAME.CREATOR]), 
               b'creatorFullName': creatorFullName, 
               b'creatorClan': creatorClan, 
               b'creatorRegion': creatorRegion, 
               b'creatorIgrType': creatorIgrType, 
               b'title': (formatters.getTrainingRoomTitle(arenaType)), 
               b'arenaName': (arenaType.name), 
               b'arenaTypeID': arenaTypeID, 
               b'arenaSubType': (formatters.getArenaSubTypeString(arenaTypeID)), 
               b'battleTypeIco': (self.__battleTypeIcon(settings[PREBATTLE_SETTING_NAME.BATTLE_TYPE])), 
               b'additionalInfo': (self.__getAdditionalInfo()), 
               b'description': (arenaType.description), 
               b'maxPlayersCount': (self.__getMaxPlayersInTeam() * 2), 
               b'roundLenString': (formatters.getRoundLenString(settings[b'roundLength'])), 
               b'comment': comment, 
               b'arenaVoipChannels': (settings[PREBATTLE_SETTING_NAME.ARENA_VOIP_CHANNELS]), 
               b'canChangeArenaVOIP': (permissions.canChangeArenaVOIP()), 
               b'isObserverModeEnabled': (self._isObserverModeEnabled()), 
               b'badgeVisualVO': badgeVO})
            return

    def __getCreatorFromRosters(self):
        rosters = self.prbEntity.getRosters()
        for roster in viewvalues(rosters):
            for account in roster:
                if account.isCreator:
                    return account

        return

    def __getAdditionalInfo(self):
        additionalInfo = getTrainingRoomHandler(self.__trainingArenaGuiType()).getAdditionalInfo()
        if additionalInfo is not None:
            return additionalInfo
        else:
            return b''

    def __battleTypeIcon(self, prebattleType):
        icon = getTrainingRoomHandler(self.__trainingArenaGuiType()).getIcon()
        if icon is not None:
            return icon
        else:
            return BATTLE_TYPES_ICONS.get(prebattleType, BATTLE_TYPES.TRAINING)

    def __getMaxPlayersInTeam(self):
        maxPlayersInTeam = getTrainingRoomHandler(self.__trainingArenaGuiType()).getMaxPlayersInTeam()
        if maxPlayersInTeam is not None:
            return maxPlayersInTeam
        else:
            arenaTypeID = self.prbEntity.getSettings()[b'arenaTypeID']
            arenaType = ArenaType.g_cache.get(arenaTypeID)
            return arenaType.maxPlayersInTeam

    def __trainingArenaGuiType(self):
        if not isinstance(self.prbEntity, TrainingEntity):
            return None
        else:
            return self.prbEntity.getSettings()[b'arenaGuiType']

    def __getErrorClientMessageData(self, errorType):
        handlers = getAllTrainingRoomHandlers()
        for handler in handlers:
            messageData = handler.getClientMessageData(errorType)
            if messageData is not None:
                return messageData

        return

    def __swapTeamsInMinimap(self, team):
        if VIEW_ALIAS.MINIMAP_LOBBY in self.components:
            self.components[VIEW_ALIAS.MINIMAP_LOBBY].swapTeams(team)
        return

    def __isActorAssigned(self, entity):
        _, assigned = decodeRoster(entity.getRosterKey())
        return assigned

    def __me_onUserActionReceived(self, _, user, shadowMode):
        dbID = user.getID()
        playerInfo = self.prbEntity.getPlayerInfoByDbID(dbID)
        if playerInfo is None:
            return
        else:
            roster = playerInfo.roster
            tags = list(user.getTags())
            if roster == PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1:
                self.as_setPlayerTagsInTeam1S(dbID, tags)
            elif roster == PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2:
                self.as_setPlayerTagsInTeam2S(dbID, tags)
            else:
                self.as_setPlayerTagsInOtherS(dbID, tags)
            return

    @adisp_process
    def __doStartTraining(self):
        result = yield self.prbDispatcher.sendPrbRequest(SetTeamStateCtx(1, True))
        if result:
            result = yield self.prbDispatcher.sendPrbRequest(SetTeamStateCtx(2, True))
            if not result:
                yield self.prbDispatcher.sendPrbRequest(SetTeamStateCtx(1, False))
        if not result:
            self._showActionErrorMessage()
            self.as_disableControlsS(False)
            self._updateStartButton(self.prbEntity)
        return

    @adisp_process
    def __currentPlayerEntered(self, playerReadyState=True):
        if self.__currentPlayerIsOut:
            if self.prbEntity.storage.isObserver:
                yield self.prbDispatcher.sendPrbRequest(SetPlayerObserverStateCtx(isObserver=True, isReadyState=True, waitingID=b'prebattle/change_user_status'))
            else:
                waitingID = b'prebattle/player_ready' if playerReadyState else b'prebattle/player_not_ready'
                yield self.prbDispatcher.sendPrbRequest(SetPlayerStateCtx(playerReadyState, waitingID=waitingID))
            self.as_setObserverS(self.prbEntity.storage.isObserver)
            self.__currentPlayerIsOut = False
        return
