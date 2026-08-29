import datetime, time
from functools import partial
import BigWorld, account_helpers
from client_request_lib.exceptions import ResponseCodes
from constants import PREBATTLE_TYPE, QUEUE_TYPE
from debug_utils import LOG_DEBUG, LOG_ERROR
from gui import SystemMessages
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getStrongholdEventBattleModeSettings, getStrongholdEventEnabled
from gui.clans.clan_helpers import isStrongholdsEnabled, isLeaguesEnabled
from gui.clans.stronghold_forbidden_vehicle_requester import ForbiddenVehiclesRequester
from gui.clans.stronghold_event_requester import FrozenVehiclesRequester, FrozenVehiclesConstants
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control import prb_getters
from gui.prb_control import settings
from gui.prb_control.entities.base.unit.ctx import JoinUnitModeCtx
from gui.prb_control.entities.base.unit.entity import UnitEntity, UnitEntryPoint, UnitBrowserEntryPoint, UnitBrowserEntity
from gui.prb_control.entities.stronghold.unit.actions_handler import StrongholdActionsHandler
from gui.prb_control.entities.stronghold.unit.actions_validator import StrongholdActionsValidator
from gui.prb_control.entities.stronghold.unit.permissions import StrongholdPermissions, StrongholdBrowserPermissions
from gui.prb_control.entities.stronghold.unit.requester import StrongholdUnitRequestProcessor
from gui.prb_control.entities.base.external_battle_unit.base_external_battle_waiting_manager import BaseExternalUnitWaitingManager
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.formatters import messages
from gui.prb_control.items import SelectResult
from gui.prb_control.items import ValidationResult, unit_items
from gui.prb_control.items.stronghold_items import StrongholdSettings, StrongholdUnitStats
from gui.prb_control.items.unit_items import DynamicRosterSettings
from gui.prb_control.settings import PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG
from gui.prb_control.settings import UNIT_RESTRICTION
from gui.prb_control.storages import prequeue_storage_getter
from gui.clans.clan_cache import g_clanCache
from gui.Scaleform.daapi.view.dialogs.rally_dialog_meta import StrongholdConfirmDialogMeta
from gui.SystemMessages import SM_TYPE
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import StrongholdEvent
from gui.shared.notifications import NotificationPriorityLevel
from gui.shared.utils.requesters.abstract import Response
from gui.clientgw.strongholds.contexts import StrongholdJoinBattleCtx, StrongholdUpdateCtx, StrongholdMatchmakingInfoCtx, StrongholdLeaveModeCtx, SlotVehicleFiltersUpdateCtx, StrongholdEventGetFrozenVehiclesCtx, StrongholdGetForbiddenVehiclesCtx
from helpers import time_utils, dependency
from UnitBase import UNIT_ERROR, UNIT_ROLE
from skeletons.gui.game_control import IGameSessionController
_CREATION_TIMEOUT = 30
ERROR_MAX_RETRY_COUNT = 3
SUCCESS_STATUSES = (200, 201, 403, 409)
DEFAULT_OK_WEB_REQUEST_ID = 0
LEVELS_FROZEN_VEHICLES = (10,)

class StrongholdDynamicRosterSettings(DynamicRosterSettings):

    def __init__(self, unit, strongholdData):
        kwargs = self._extractSettings(unit, strongholdData)
        self._minClanMembersCount = kwargs.pop(b'minClanMembersCount', None)
        super(DynamicRosterSettings, self).__init__(**kwargs)
        return

    def _extractSettings(self, unit, strongholdData):
        if not strongholdData.isValid():
            LOG_DEBUG(b'Unit roster is not definded')
            return super(StrongholdDynamicRosterSettings, self)._extractSettings(unit)
        else:
            kwargs = {}
            roster = None
            if unit is not None:
                roster = unit.getRoster()
            if roster is None:
                LOG_DEBUG(b'Unit roster is not defined')
                return kwargs
            header = strongholdData.getHeader()
            maxSlots = header.getMaxPlayersCount() - 1
            maxEmptySlots = maxSlots - header.getMinPlayersCount()
            minClanMembersCount = header.getMinPlayersCount() - header.getMaxLegionariesCount()
            kwargs[b'minLevel'] = header.getMinLevel()
            kwargs[b'maxLevel'] = header.getMaxLevel()
            kwargs[b'maxSlots'] = maxSlots
            kwargs[b'maxClosedSlots'] = maxEmptySlots
            kwargs[b'maxEmptySlots'] = maxEmptySlots
            kwargs[b'minTotalLevel'] = roster.MIN_UNIT_POINTS_SUM
            kwargs[b'maxTotalLevel'] = roster.MAX_UNIT_POINTS_SUM
            kwargs[b'maxLegionariesCount'] = header.getMaxLegionariesCount()
            kwargs[b'minClanMembersCount'] = minClanMembersCount
            return kwargs

    def getMinClanMembersCount(self):
        return self._minClanMembersCount


class StrongholdJoinUnitModeCtx(JoinUnitModeCtx):
    __slots__ = (b'kwargs',)

    def __init__(self, prbType, waitingID=b'', flags=settings.FUNCTIONAL_FLAG.UNDEFINED, **kwargs):
        super(StrongholdJoinUnitModeCtx, self).__init__(prbType, waitingID, flags)
        self.kwargs = kwargs
        return


class StrongholdBrowserEntryPoint(UnitBrowserEntryPoint):

    def __init__(self):
        self.__openListExtra = b''
        super(StrongholdBrowserEntryPoint, self).__init__(FUNCTIONAL_FLAG.STRONGHOLD, PREBATTLE_TYPE.STRONGHOLD)
        return

    def setExtData(self, extData):
        self.__openListExtra = extData.get(b'openListExtra', b'')
        return

    def makeDefCtx(self):
        return StrongholdJoinUnitModeCtx(self._prbType, flags=self.getFunctionalFlags(), openListExtra=self.__openListExtra)


class StrongholdEntryPoint(UnitEntryPoint):

    def __init__(self, accountsToInvite=None):
        self.__timeout = None
        self.__currentCtx = None
        self.__isLegionary = False
        super(StrongholdEntryPoint, self).__init__(FUNCTIONAL_FLAG.STRONGHOLD, accountsToInvite)
        return

    def create(self, ctx, callback=None):
        self.__startProcessingCtx(ctx, callback)
        return

    def join(self, ctx, callback=None):
        self.__startProcessingCtx(ctx, callback)

        def onResponse(response):
            hasErrors = response.getCode() != ResponseCodes.NO_ERRORS
            if hasErrors:
                ctx.stopProcessing()
                self.__cancelProcessingTimeout()
                ctx.callErrorCallback(response.data)
            return

        processor = StrongholdUnitRequestProcessor()
        processor.doRequest(StrongholdJoinBattleCtx(ctx.getID()), b'join', callback=onResponse)
        return

    def onUnitJoined(self, unitMgrID, prbType):
        self.__cancelProcessingTimeout()
        return

    def __startProcessingCtx(self, ctx, callback):
        self.__currentCtx = ctx
        self.__currentCtx.startProcessing(callback)
        self.__timeout = BigWorld.callback(_CREATION_TIMEOUT, self.__ctxProcessingTimeout)
        unitMgr = prb_getters.getClientUnitMgr()
        if unitMgr:
            unitMgr.onUnitJoined += self.onUnitJoined
        return

    def __cancelProcessingTimeout(self):
        BigWorld.cancelCallback(self.__timeout)
        self.__clear()
        return

    def __ctxProcessingTimeout(self):
        if self.__currentCtx:
            self.__currentCtx.callTimeoutCallback()
            self.__currentCtx.stopProcessing()
        self.__clear()
        return

    def __clear(self):
        self.__timeout = None
        unitMgr = prb_getters.getClientUnitMgr()
        if unitMgr:
            unitMgr.onUnitJoined -= self.onUnitJoined
        return


class StrongholdBrowserEntity(UnitBrowserEntity):

    def __init__(self, openListExtra=b''):
        self.__openListExtra = openListExtra
        super(StrongholdBrowserEntity, self).__init__(FUNCTIONAL_FLAG.STRONGHOLD, PREBATTLE_TYPE.STRONGHOLD)
        return

    def getOpenListExtraParams(self):
        return self.__openListExtra

    def canKeepMode(self):
        return False

    def getPermissions(self, dbID=None, unitMgrID=None):
        return StrongholdBrowserPermissions(self.hasLockedState())

    def _loadUnit(self):
        g_eventDispatcher.loadStrongholds()
        return

    def _unloadUnit(self):
        g_eventDispatcher.removeUnitFromCarousel(self._prbType)
        return

    def _showWindow(self):
        g_eventDispatcher.showStrongholdsWindow()
        return

    def leave(self, ctx, callback=None):
        processor = StrongholdUnitRequestProcessor()
        processor.doRequest(StrongholdLeaveModeCtx(ctx.getID()), b'leave_mode')
        super(StrongholdBrowserEntity, self).leave(ctx, callback)
        return

    def getQueueType(self):
        return QUEUE_TYPE.STRONGHOLD_UNITS

    @staticmethod
    def isSortie():
        return True


class StrongholdEntity(UnitEntity):
    __gameSession = dependency.descriptor(IGameSessionController)
    MATCHMAKING_BATTLE_BUTTON_BATTLE = 10 * time_utils.ONE_MINUTE
    MATCHMAKING_BATTLE_BUTTON_SORTIE = 10 * time_utils.ONE_MINUTE
    MATCHMAKING_ZERO_TIME_WAITING_FOR_DATA = 5

    class SH_REQUEST_COOLDOWN(object):
        PREBATTLE_ASSIGN = 0.6

    def __init__(self):
        self.__strongholdSettings = StrongholdSettings()
        super(StrongholdEntity, self).__init__(FUNCTIONAL_FLAG.STRONGHOLD, PREBATTLE_TYPE.STRONGHOLD)
        self.__revisionId = 0
        self.__battleModeData = {}
        self.__waitingManager = BaseExternalUnitWaitingManager()
        self.__errorCount = 0
        self.__timerID = None
        self.__leaveInitiator = False
        self.__isInSlot = False
        self.__isInactiveMatchingButton = True
        self.__prevMatchmakingTimerState = None
        self.__strongholdUpdateEventsMapping = {}
        self.__playersMatchingStartedAt = None
        self.__slotVehicleFilters = []
        self.__eventFrozenVehiclesRequester = None
        self.__forbiddenVehiclesRequester = None
        self.storage = prequeue_storage_getter(QUEUE_TYPE.STRONGHOLD_UNITS)()
        return

    def init(self, ctx=None):
        self.__playersMatchingStartedAt = None
        self.__slotVehicleFilters = []
        self.storage.release()
        ret = super(StrongholdEntity, self).init(ctx)
        rev = self._getUnitRevision()
        if rev > 1:
            self.requestUpdateStronghold()
            self.requestSlotVehicleFilters()
        self.__checkStrongholdEvent()
        self.__initForbiddenVehiclesRequester()
        unitMgr = prb_getters.getClientUnitMgr()
        if unitMgr:
            unitMgr.onUnitResponseReceived += self.onUnitResponseReceived
            unitMgr.onUnitNotifyReceived += self.onUnitNotifyReceived
            unitMgr.onUnitErrorReceived += self.onUnitErrorReceived
        self.__strongholdSettings.init()
        self.__strongholdUpdateEventsMapping = {b'header': (self.__onUpdateHeader), 
           b'timer': (self.__onUpdateTimer), 
           b'state': (self.__onUpdateState), 
           b'reserve': (self.__onUpdateReserve)}
        playerInfo = self.getPlayerInfo()
        self.__isInSlot = playerInfo.isInSlot
        if self.canShowStrongholdsBattleQueue():
            g_eventDispatcher.showStrongholdsBattleQueue()
        else:
            g_eventDispatcher.loadStrongholds()
        self.__gameSession.onParentControlNotify += self.__onParentControlNotify
        self.__gameSession.onNotifyTimeTillKick += self.__onParentControlNotify
        return ret

    def fini(self, ctx=None, woEvents=False):
        self.__gameSession.onNotifyTimeTillKick -= self.__onParentControlNotify
        self.__gameSession.onParentControlNotify -= self.__onParentControlNotify
        if self.__eventFrozenVehiclesRequester is not None:
            self.__eventFrozenVehiclesRequester.stop()
            self.__eventFrozenVehiclesRequester = None
        if self.__forbiddenVehiclesRequester is not None:
            self.__forbiddenVehiclesRequester.stop()
            self.__forbiddenVehiclesRequester = None
        self.__cancelMatchmakingTimer()
        unitMgr = prb_getters.getClientUnitMgr()
        if unitMgr:
            unitMgr.onUnitErrorReceived -= self.onUnitErrorReceived
            unitMgr.onUnitResponseReceived -= self.onUnitResponseReceived
            unitMgr.onUnitNotifyReceived -= self.onUnitNotifyReceived
        self.__strongholdSettings.fini()
        self.__strongholdUpdateEventsMapping = {}
        self.__playersMatchingStartedAt = None
        self.__slotVehicleFilters = []
        self.storage.fini()
        super(StrongholdEntity, self).fini(ctx, woEvents)
        return

    def initEvents(self, listener):
        super(StrongholdEntity, self).initEvents(listener)
        if self.canShowMaintenance():
            self._invokeListeners(b'onStrongholdMaintenance', True)
        if self.inPlayersMatchingMode():
            self._invokeListeners(b'onPlayersMatching', True)
        return

    def onUnitResponseReceived(self, requestID):
        LOG_DEBUG(b'Unit response requestID = ' + str(requestID))
        self.__waitingManager.onResponseWebReqID(requestID)
        return

    def onUnitNotifyReceived(self, unitMgrID, notifyCode, notifyString, argsList):
        if notifyCode == UNIT_ERROR.NO_CLAN_MEMBERS and not self.__leaveInitiator:
            SystemMessages.pushMessage(backport.text(R.strings.tooltips.stronghold.prebattle.noClanMembers()), type=SM_TYPE.Warning)
        elif notifyCode == UNIT_ERROR.FAIL_EXT_UNIT_QUEUE_START and not self.getFlags().isInQueue():
            self.__waitingManager.onResponseError()
        elif notifyCode == UNIT_ERROR.EXPIRED_PLAY_LIMITS:
            SystemMessages.pushMessage(backport.text(R.strings.system_messages.unit.warnings.EXPIRED_PLAY_LIMITS(), expiredTime=backport.getShortTimeFormat(self.__gameSession.getKickAtTime())), type=SM_TYPE.Warning, priority=NotificationPriorityLevel.MEDIUM)
        elif notifyCode == UNIT_ERROR.EXPIRED_PLAY_LIMITS_TO_COMMANDER:
            SystemMessages.pushMessage(backport.text(R.strings.system_messages.unit.warnings.EXPIRED_PLAY_LIMITS_TO_COMMANDER()), type=SM_TYPE.Warning, priority=NotificationPriorityLevel.MEDIUM)
        return

    def onUnitErrorReceived(self, requestID, unitMgrID, errorCode, errorString):
        if errorCode == UNIT_ERROR.EXPIRED_PLAY_LIMITS:
            self.__waitingManager.onResponseError()
            g_eventDispatcher.updateUI()
            SystemMessages.pushMessage(backport.text(R.strings.system_messages.unit.warnings.EXPIRED_PLAY_LIMITS(), expiredTime=backport.getShortTimeFormat(self.__gameSession.getKickAtTime())), type=SM_TYPE.Warning, priority=NotificationPriorityLevel.MEDIUM)
        return

    def canShowMaintenance(self):
        return self.__errorCount >= ERROR_MAX_RETRY_COUNT

    def doSelectAction(self, action):
        name = action.actionName
        if name == PREBATTLE_ACTION_NAME.STRONGHOLD:
            g_eventDispatcher.showStrongholdsWindow()
            SelectResult(True)
        return super(StrongholdEntity, self).doSelectAction(action)

    def exitFromPlayersMatchingMode(self):
        self._actionsHandler.exitFromPlayersMatchingMode()
        return

    def getConfirmDialogMeta(self, ctx):
        if self.__errorCount == 0 and self.hasLockedState():
            meta = super(StrongholdEntity, self).getConfirmDialogMeta(ctx)
        else:
            pDbID = account_helpers.getAccountDatabaseID()
            members, clanMembers = self._getClanMembers()
            if ctx.hasFlags(FUNCTIONAL_FLAG.EXIT) or pDbID in members:
                isFirstBattle = self.__strongholdSettings.isFirstBattle()
                isLastClanMember = len(clanMembers) == 1 and clanMembers[0] == pDbID
                subKey = b'Defeat' if isLastClanMember and not isFirstBattle else b''
                meta = StrongholdConfirmDialogMeta(key=b'leave', subKey=subKey)
            else:
                meta = None
        return meta

    def getQueueType(self):
        return QUEUE_TYPE.STRONGHOLD_UNITS

    def rejoin(self):
        super(StrongholdEntity, self).rejoin()
        if self.isStrongholdUnitWaitingForData():
            LOG_DEBUG(b'force wgsh request on end of battle')
            self.__strongholdSettings.forceCleanData()
            self.requestUpdateStronghold()
        return

    def unit_onUnitFlagsChanged(self, prevFlags, nextFlags):
        _, unit = self.getUnit(safe=False)
        isReady = unit.arePlayersReady(ignored=[settings.CREATOR_SLOT_INDEX])
        flags = unit_items.UnitFlags(nextFlags, prevFlags, isReady)
        isInQueue = flags.isInQueue()
        if isInQueue:
            matchmakerNextTick = self.__doClockworkLogic(returnMatchmakerNextTick=True)
            if matchmakerNextTick is not None:
                unit.setModalTimestamp(matchmakerNextTick)
        if flags.isInQueueChanged() and self.isCommander() and not isInQueue:
            self.requestSlotVehicleFilters()
        regularBattleEnd = flags.isArenaFinishedChanged() and flags.isArenaFinished() and flags.isExternalLocked()
        wgshBattleEnd = flags.isExternalLockedStateChanged() and not flags.isExternalLocked()
        if regularBattleEnd or wgshBattleEnd:
            LOG_DEBUG(b'force wgsh request on end of battle (r,x):', regularBattleEnd, wgshBattleEnd)
            self.__strongholdSettings.forceCleanData()
            self.requestUpdateStronghold()
            self.requestSlotVehicleFilters()
        if flags.isExternalLegionariesMatchingChanged():
            self.__onExternalLegionariesMatchingToggle(flags.isInExternalLegionariesMatching())
            if not flags.isInExternalLegionariesMatching() and not self.isCommander() and self.getSlotsInPlayersMatching():
                self.requestUpdateStronghold()
        super(StrongholdEntity, self).unit_onUnitFlagsChanged(prevFlags, nextFlags)
        self.__doClockworkLogic(invokeListeners=True, forceUpdateBuildings=True)
        if not self.hasLockedState():
            self.resetCoolDown(settings.REQUEST_TYPE.BATTLE_QUEUE)
            self.resetCoolDown(settings.REQUEST_TYPE.DECLINE_SEARCH)
            self.resetCoolDown(settings.REQUEST_TYPE.AUTO_SEARCH)
        if isInQueue:
            self._invokeListeners(b'onCommanderIsReady', True)
        elif prevFlags != nextFlags and nextFlags == 0:
            self._invokeListeners(b'onCommanderIsReady', False)
        if self.canShowStrongholdsBattleQueue():
            g_eventDispatcher.showStrongholdsBattleQueue()
        return

    def unit_onUnitExtraChanged(self, extras):
        super(StrongholdEntity, self).unit_onUnitExtraChanged(extras)
        revisionId = extras[b'rev']
        if revisionId == self.__revisionId:
            return
        self.requestUpdateStronghold()
        self.__revisionId = revisionId
        return

    def unit_onUnitPlayerRemoved(self, playerID, playerData):
        super(StrongholdEntity, self).unit_onUnitPlayerRemoved(playerID, playerData)
        unitMgrID, unit = self.getUnit(safe=False)
        pInfo = self._buildPlayerInfo(unitMgrID, unit, playerID, -1, playerData)
        equipRoles = UNIT_ROLE.CAN_USE_EXTRA_EQUIPMENTS | UNIT_ROLE.CAN_USE_BOOST_EQUIPMENTS
        myPInfo = self.getPlayerInfo()
        if not pInfo.isCurrentPlayer() and pInfo.role & equipRoles and myPInfo.isCommander():
            SystemMessages.pushMessage(backport.text(R.strings.system_messages.unit.notification.PLAYER_BECOME_EQUIPMENT_COMMANDER()), type=SM_TYPE.Warning)
        return

    def unit_onUnitPlayerRoleChanged(self, playerID, prevRoleFlags, nextRoleFlags):
        super(StrongholdEntity, self).unit_onUnitPlayerRoleChanged(playerID, prevRoleFlags, nextRoleFlags)
        diff = prevRoleFlags ^ nextRoleFlags
        if diff & UNIT_ROLE.CREATOR > 0:
            self.__onCommanderChanged(playerID)
        equipRoles = UNIT_ROLE.CAN_USE_EXTRA_EQUIPMENTS | UNIT_ROLE.CAN_USE_BOOST_EQUIPMENTS
        prevEquipRoleFlags = prevRoleFlags & equipRoles
        nextEquipRoleFlags = nextRoleFlags & equipRoles
        userBecomesEquipmentCommander = self.__isEquipmentRoleChanged(prevEquipRoleFlags, nextEquipRoleFlags)
        userNoLongerEquipmentCommander = self.__isEquipmentRoleChanged(nextEquipRoleFlags, prevEquipRoleFlags)
        if not userBecomesEquipmentCommander and not userNoLongerEquipmentCommander:
            return
        pInfo = self.getPlayerInfo(dbID=playerID)
        if userNoLongerEquipmentCommander and pInfo.isCurrentPlayer():
            SystemMessages.pushMessage(backport.text(R.strings.system_messages.unit.warnings.ANOTHER_PLAYER_BECOME_EQUIPMENT_COMMANDER()), type=SM_TYPE.Warning)
            return
        if userBecomesEquipmentCommander and pInfo.isCurrentPlayer():
            SystemMessages.pushMessage(backport.text(R.strings.system_messages.unit.notification.PLAYER_BECOME_EQUIPMENT_COMMANDER()), type=SM_TYPE.Information)
            return
        myPInfo = self.getPlayerInfo()
        userEquipmentRoleChanged = userBecomesEquipmentCommander or userNoLongerEquipmentCommander
        if userEquipmentRoleChanged and not pInfo.isCurrentPlayer() and myPInfo.isCommander():
            SystemMessages.pushMessage(backport.text(R.strings.system_messages.unit.warnings.ANOTHER_PLAYER_BECOME_EQUIPMENT_COMMANDER()), type=SM_TYPE.Warning)
            return
        return

    def unit_onUnitMembersListChanged(self):
        playerInfo = self.getPlayerInfo()
        self.__isInSlot = playerInfo.isInSlot
        super(StrongholdEntity, self).unit_onUnitMembersListChanged()
        return

    def request(self, ctx, callback=None):
        self.__waitingManager.processRequest(ctx)

        def wrapper(response):
            if self.__processResponseMessage(response):
                isResponseSubclass = issubclass(type(response), Response)
                if not isResponseSubclass or response.getCode() != ResponseCodes.NO_ERRORS:
                    self.__waitingManager.stopRequest()
                if callback:
                    callback(response)
            else:
                BigWorld.callback(0.0, partial(self.request, ctx, callback))
            return

        super(StrongholdEntity, self).request(ctx, wrapper)
        return

    def leave(self, ctx, callback=None):
        self.storage.suspend()
        self.__leaveInitiator = True

        def callbackWrapper(response):
            if not self.__processResponseMessage(response):
                super(StrongholdEntity, self).leave(ctx, callback)
            return

        if self.__errorCount > 0:
            super(StrongholdEntity, self).leave(ctx, callback)
        else:
            ctx.startProcessing(callback)
            self._requestsProcessor.doRequest(ctx, b'leave', callback=callbackWrapper)
        return

    def doBattleQueue(self, ctx, callback=None):
        if ctx.isRequestToStart():
            self.setCoolDown(settings.REQUEST_TYPE.SET_PLAYER_STATE, ctx.getCooldown())
        elif self.isInCoolDown(ctx.getRequestType()):
            return
        self.setCoolDown(ctx.getRequestType(), ctx.getCooldown())
        self._invokeListeners(b'onStrongholdDoBattleQueue', self.isFirstBattle(), False, self.__strongholdSettings.getReserveOrder())
        super(StrongholdEntity, self).doBattleQueue(ctx, callback)
        return

    def getMatchmakingInfo(self, callback=None):
        ctx = StrongholdMatchmakingInfoCtx(prb_getters.getUnitMgrID())
        self._requestsProcessor.doRequest(ctx, b'matchmakingInfo', callback=callback)
        return

    def setReserve(self, ctx, callback=None):
        pPermissions = self.getPermissions()
        if not pPermissions.canChangeConsumables():
            LOG_ERROR(b'Player can not change consumables', pPermissions)
            if callback:
                callback(False)
            return
        self._requestsProcessor.doRequest(ctx, b'activateReserve', callback=callback)
        self.setCoolDown(settings.REQUEST_TYPE.SET_RESERVE, coolDown=ctx.getCooldown())
        return

    def unsetReserve(self, ctx, callback=None):
        pPermissions = self.getPermissions()
        if not pPermissions.canChangeConsumables():
            LOG_ERROR(b'Player can not change consumables', pPermissions)
            if callback:
                callback(False)
            return
        self._requestsProcessor.doRequest(ctx, b'deactivateReserve', callback=callback)
        self.setCoolDown(settings.REQUEST_TYPE.UNSET_RESERVE, coolDown=ctx.getCooldown())
        return

    def setEquipmentCommander(self, ctx, callback=None):
        self._requestsProcessor.doRequest(ctx, b'setEquipmentCommander', callback=callback)
        self.setCoolDown(settings.REQUEST_TYPE.SET_EQUIPMENT_COMMANDER, coolDown=ctx.getCooldown())
        return

    def assign(self, ctx, callback=None):
        if self.isInCoolDown(settings.REQUEST_TYPE.ASSIGN):
            return
        super(StrongholdEntity, self).assign(ctx, callback)
        self.setCoolDown(settings.REQUEST_TYPE.ASSIGN, coolDown=self.SH_REQUEST_COOLDOWN.PREBATTLE_ASSIGN)
        return

    def canKeepMode(self):
        if not isStrongholdsEnabled():
            return False
        return super(StrongholdEntity, self).canKeepMode()

    def changeOpened(self, ctx, callback=None):
        self._requestsProcessor.doRequest(ctx, b'openUnit', isOpen=ctx.isOpened(), callback=callback)
        self.setCoolDown(settings.REQUEST_TYPE.CHANGE_UNIT_STATE, coolDown=ctx.getCooldown())
        return

    def canPlayerDoAction(self):
        if self.__errorCount > 0:
            return ValidationResult(False, UNIT_RESTRICTION.UNIT_MAINTENANCE)
        else:
            if self.isStrongholdUnitFreezed() or self.isStrongholdUnitWaitingForData():
                isPlayerInSlot = self._isPlayerInSlot()
                if isPlayerInSlot and self.isStrongholdUnitWaitingForData():
                    return ValidationResult(False, UNIT_RESTRICTION.UNIT_WAITINGFORDATA)
                if isPlayerInSlot and self._hasInArenaMembers():
                    return ValidationResult(False, UNIT_RESTRICTION.IS_IN_ARENA)
                result = self._actionsValidator.canPlayerDoAction() or ValidationResult(False, UNIT_RESTRICTION.UNDEFINED)
                return ValidationResult(False, result.restriction, result.ctx)
            else:
                matchingCommanderRestriction = None
                isStrongholdSettingsValid = self.isStrongholdSettingsValid()
                self.__isInactiveMatchingButton = self.__doClockworkLogic(returnMatchingButtonIsInactive=True)
                if isStrongholdSettingsValid and self.__isInactiveMatchingButton and self.isCommander() and not self.getFlags().isInIdle():
                    resultId = UNIT_RESTRICTION.UNIT_INACTIVE_PERIPHERY_UNDEF
                    if isStrongholdSettingsValid:
                        if self.isSortie():
                            resultId = UNIT_RESTRICTION.UNIT_INACTIVE_PERIPHERY_SORTIE
                        else:
                            resultId = UNIT_RESTRICTION.UNIT_INACTIVE_PERIPHERY_BATTLE
                    matchingCommanderRestriction = ValidationResult(False, resultId)
                return matchingCommanderRestriction or self._actionsValidator.canPlayerDoAction() or ValidationResult(True, UNIT_RESTRICTION.UNDEFINED)

            return

    def isPlayerJoined(self, ctx):
        return ctx.getCtrlType() is settings.CTRL_ENTITY_TYPE.UNIT and ctx.getEntityType() == self._prbType and ctx.getID() == self.getID()

    def requestMaintenanceUpdate(self):
        self._invokeListeners(b'onStrongholdMaintenance', False)
        self.requestUpdateStronghold()
        return

    def requestUpdateStronghold(self):
        if self._requestsProcessor:
            unitMgrId = prb_getters.getUnitMgrID()
            rev = self._getUnitRevision()
            ctx = StrongholdUpdateCtx(unitMgrId=unitMgrId, rev=rev, waitingID=b'')
            self._requestsProcessor.doRequest(ctx, b'updateStronghold', callback=self.__onStrongholdUpdate)
        return

    def getMinLevel(self):
        header = self.__strongholdSettings.getHeader()
        return header.getMinLevel()

    def strongholdDataChanged(self):
        if self.isStrongholdSettingsValid():
            header = self.__strongholdSettings.getHeader()
            isFirstBattle = self.isFirstBattle()
            self.__checkBattleMode(header, isFirstBattle)
            self._updateMatchmakingTimer()
            self._invokeListeners(b'onStrongholdDataChanged', header, isFirstBattle, self.__strongholdSettings.getReserve(), self.__strongholdSettings.getReserveOrder())
        return

    def getCandidates(self, unitMgrID=None):
        unitMgrID, unit = self.getUnit(unitMgrID=unitMgrID, safe=True)
        if unit is None:
            return {}
        else:
            players = unit.getPlayers()
            memberIDs = set(value[b'accountDBID'] for value in unit.getMembers().itervalues())
            dbIDs = set(players.keys()).difference(memberIDs)
            result = {}
            for dbID, data in players.iteritems():
                if dbID not in dbIDs:
                    continue
                result[dbID] = self._buildPlayerInfo(unitMgrID, unit, dbID, -1, data)

            return result

    def getStrongholdSettings(self):
        return self.__strongholdSettings

    def isStrongholdSettingsValid(self):
        return self.__strongholdSettings.isValid()

    def isStrongholdUnitFreezed(self):
        return self.getFlags().isExternalLocked()

    def isStrongholdUnitWaitingForData(self):
        if self.isStrongholdSettingsValid():
            readyButtonEnabled = not self.__strongholdSettings.isStrongholdUnitFreezed()
        else:
            readyButtonEnabled = True
        flags = self.getFlags()
        return self.canShowMaintenance() or flags.isArenaFinished() and flags.isExternalLocked() or not flags.isInIdle() and not self.getFlags().isInArena() and not flags.isExternalLocked() and not readyButtonEnabled

    def isFirstBattle(self):
        return self.__strongholdSettings.isFirstBattle()

    def isSortie(self):
        return self.__strongholdSettings.isSortie()

    def getHeaderType(self):
        header = self.__strongholdSettings.getHeader()
        return header.getType()

    def getRosterSettings(self):
        if self.isStrongholdSettingsValid():
            return self.__updateRosterSettings()
        return self._rosterSettings

    def animationNotAvailable(self):
        battleIdx = self.__strongholdSettings.getHeader().getBattleIdx()
        if self.storage.getActiveAnimationIdx() != battleIdx and battleIdx != 0:
            self.storage.setActiveAnimationIdx(battleIdx)
            return False
        return True

    def updateStrongholdData(self):
        if self.isStrongholdSettingsValid():
            self.__onUpdateHeader()
            self.__onUpdateTimer()
            self.__onUpdateReserve()
            self.__onUpdateState()
        return

    def forceTimerEvent(self):
        self.__doClockworkLogic(returnMatchmakerNextTick=True, invokeListeners=True)
        return

    def setVehicleTypeFilter(self, ctx, callback=None):
        if self.isInCoolDown(ctx.getRequestType()):
            return

        def _callback(data):
            if callback is not None:
                callback(data)
            self._onPlayersMatchingDataUpdated(data)
            self.__waitingManager.onResponseWebReqID(DEFAULT_OK_WEB_REQUEST_ID)
            return

        self._requestsProcessor.doRequest(ctx, b'setVehicleTypeFilter', callback=_callback)
        self.setCoolDown(settings.REQUEST_TYPE.SET_SLOT_VEHICLE_TYPE_FILTER, coolDown=ctx.getCooldown())
        return

    def setVehiclesFilter(self, ctx, callback=None):
        if self.isInCoolDown(ctx.getRequestType()):
            return

        def _callback(data):
            if callback is not None:
                callback(data)
            self._onPlayersMatchingDataUpdated(data)
            self.__waitingManager.onResponseWebReqID(DEFAULT_OK_WEB_REQUEST_ID)
            return

        self._requestsProcessor.doRequest(ctx, b'setVehiclesFilter', callback=_callback)
        self.setCoolDown(settings.REQUEST_TYPE.SET_SLOT_VEHICLES_FILTER, coolDown=ctx.getCooldown())
        return

    def requestSlotVehicleFilters(self):
        if not self.isCommander():
            return
        if self._requestsProcessor:
            unitMgrId = prb_getters.getUnitMgrID()
            ctx = SlotVehicleFiltersUpdateCtx(unitMgrId=unitMgrId, waitingID=b'')
            self._requestsProcessor.doRequest(ctx, b'getSlotVehicleFilters', callback=self._onPlayersMatchingDataUpdated)
        return

    def stopPlayersMatching(self, ctx, callback=None):
        self._requestsProcessor.doRequest(ctx, b'stopPlayersMatching', callback=callback)
        self.setCoolDown(settings.REQUEST_TYPE.STOP_PLAYERS_MATCHING, coolDown=ctx.getCooldown())
        return

    def getSecondsCountInPlayersMatching(self):
        if self.__playersMatchingStartedAt is None:
            return 0
        else:
            delta = datetime.datetime.utcnow() - self.__playersMatchingStartedAt
            return abs(int(delta.total_seconds()))

    def isPlayersMatchingAvailable(self):
        return self.__strongholdSettings.isPlayersMatchingAvailable()

    def inPlayersMatchingMode(self):
        return self.getFlags().isInExternalLegionariesMatching()

    def getSlotsInPlayersMatching(self):
        if not self.isCommander():
            if not self.__strongholdSettings.isValid():
                return []
            return [item[b'slot_id'] for item in self.__strongholdSettings.getSlotsInPlayersMatching()]
        return [slot_id for slot_id in self.getSlotFilters().keys()]

    def getSlotFilters(self):
        slotFilters = {item[b'slot_id']: {b'vehicle_types': (item[b'vehicle_types']), b'vehicle_cds': (item[b'vehicle_cds'])} for item in self.__slotVehicleFilters}
        return slotFilters

    def hasLockedState(self):
        _hasLockedState = super(StrongholdEntity, self).hasLockedState()
        pInfo = self.getPlayerInfo()
        flags = self.getFlags()
        return _hasLockedState or pInfo.isInSlot and flags.isInExternalLegionariesMatching()

    def canShowStrongholdsBattleQueue(self):
        pInfo = self.getPlayerInfo()
        return isLeaguesEnabled() and self.isInQueue() and pInfo.isInSlot

    def getEventFrozenVehicles(self, spaID=None, vehLevel=None):
        if vehLevel is not None and vehLevel not in LEVELS_FROZEN_VEHICLES:
            return
        else:
            if self.__eventFrozenVehiclesRequester is not None:
                if spaID is None:
                    spaID = account_helpers.getAccountDatabaseID()
                return self.__eventFrozenVehiclesRequester.getCache().get(spaID)
            return

    def getFortBattleForbiddenVehicles(self):
        if self.__forbiddenVehiclesRequester is not None:
            return self.__forbiddenVehiclesRequester.getCache().get(b'fort_battle_forbidden_vehicles', [])
        else:
            return []

    def getSortieBattleForbiddenVehicles(self):
        if self.__forbiddenVehiclesRequester is not None:
            return self.__forbiddenVehiclesRequester.getCache().get(b'sortie_forbidden_vehicles', [])
        else:
            return []

    def hasEventFrozenVehicles(self):
        if not self.__isStrongholdEventEnabled():
            return False
        else:
            fullData = self.getUnitFullData()
            for slotInfo in fullData.slotsIterator:
                player = slotInfo.player
                vehicle = slotInfo.vehicle
                if player is not None and vehicle:
                    frozenVehicles = self.getEventFrozenVehicles(player.dbID)
                    isFrozen = frozenVehicles is not None and (frozenVehicles == FrozenVehiclesConstants.ALL_VEHICLES_FROZEN or vehicle.vehTypeCompDescr in frozenVehicles)
                    if isFrozen:
                        return True

            return False

    def _onPlayersMatchingDataUpdated(self, response):
        if not self.__processResponseMessage(response):
            return
        if response.getCode() != ResponseCodes.NO_ERRORS:
            return
        self.__slotVehicleFilters = response.getData()
        self._invokeListeners(b'onSlotVehileFiltersChanged')
        return

    @property
    def _showUnitActionNames(self):
        return (PREBATTLE_ACTION_NAME.STRONGHOLD,)

    def _createActionsValidator(self):
        return StrongholdActionsValidator(self)

    def _createRosterSettings(self):
        _, unit = self.getUnit()
        return StrongholdDynamicRosterSettings(unit, self.__strongholdSettings)

    def _isPlayerInSlot(self):
        return self.__isInSlot

    def _hasInArenaMembers(self):
        flags = self.getFlags()
        return not flags.isArenaFinished() and flags.isExternalLocked() and not self._isInQueue() or flags.isInArena()

    def _isInQueue(self):
        return self.getFlags().isInIdle() and not self.getFlags().isInArena()

    def _updateMatchmakingTimer(self):
        self.__cancelMatchmakingTimer()
        tempInactiveMatchingButton = self.__isInactiveMatchingButton
        self.__isInactiveMatchingButton = self.__doClockworkLogic(returnMatchingButtonIsInactive=True, regularMode=True, invokeListeners=True)
        if tempInactiveMatchingButton != self.__isInactiveMatchingButton:
            self._invokeListeners(b'onStrongholdOnReadyStateChanged')
        self.__timerID = BigWorld.callback(1.0, self._updateMatchmakingTimer)
        return

    def _createActionsHandler(self):
        return StrongholdActionsHandler(self)

    def _getClanMembers(self):
        _, unit = self.getUnit(safe=False)
        members = [member[b'accountDBID'] for member in unit.getMembers().itervalues()]
        clanMembers = []
        for memberDBID in members:
            pInfo = self.getPlayerInfo(dbID=memberDBID)
            if not pInfo.isLegionary():
                clanMembers.append(memberDBID)

        return (
         members, clanMembers)

    def _buildPermissions(self, roles, flags, isCurrentPlayer=False, isPlayerReady=False, hasLockedState=False):
        playerInfo = self.getPlayerInfo()
        myClanRole = g_clanCache.clanRole
        strongholdManageReservesRoles = None
        strongholdStealLeadershipRoles = None
        if self.isStrongholdSettingsValid():
            strongholdPermissions = self.__strongholdSettings.getReserve().getPermissions()
            strongholdManageReservesRoles = strongholdPermissions.get(b'manage_reserves')
            strongholdStealLeadershipRoles = strongholdPermissions.get(b'take_away_leadership')
        return StrongholdPermissions(roles, flags, isCurrentPlayer, isPlayerReady, clanRoles=myClanRole, strongholdManageReservesRoles=strongholdManageReservesRoles, strongholdStealLeadershipRoles=strongholdStealLeadershipRoles, isLegionary=playerInfo.isLegionary(), isInSlot=playerInfo.isInSlot, isFreezed=self.isStrongholdUnitFreezed(), isInIdle=self.getFlags().isInIdle())

    def _getRequestHandlers(self):
        RQ_TYPE = settings.REQUEST_TYPE
        handlers = super(StrongholdEntity, self)._getRequestHandlers()
        handlers.update({(RQ_TYPE.SET_RESERVE): (self.setReserve), 
           (RQ_TYPE.UNSET_RESERVE): (self.unsetReserve), 
           (RQ_TYPE.SET_EQUIPMENT_COMMANDER): (self.setEquipmentCommander), 
           (RQ_TYPE.SET_SLOT_VEHICLE_TYPE_FILTER): (self.setVehicleTypeFilter), 
           (RQ_TYPE.SET_SLOT_VEHICLES_FILTER): (self.setVehiclesFilter), 
           (RQ_TYPE.STOP_PLAYERS_MATCHING): (self.stopPlayersMatching)})
        return handlers

    def _buildPlayerInfo(self, unitMgrID, unit, dbID, slotIdx=-1, data=None):
        cmderDBID = unit.getCommanderDBID()
        commander = unit.getPlayer(cmderDBID)
        player = unit.getPlayer(dbID)
        if player and commander and data:
            if commander[b'clanDBID'] != player[b'clanDBID']:
                data[b'role'] |= UNIT_ROLE.LEGIONARY
            else:
                data[b'role'] &= ~UNIT_ROLE.LEGIONARY
        return super(StrongholdEntity, self)._buildPlayerInfo(unitMgrID, unit, dbID, slotIdx=slotIdx, data=data)

    def _buildStats(self, unitMgrID, unit):
        unitStats = super(StrongholdEntity, self)._buildStats(unitMgrID, unit)
        slotsIterator = self.getSlotsIterator(unitMgrID, unit)
        clanMembersInRoster = 0
        legionariesInRoster = 0
        slotsWithPlayers = []
        for slotInfo in slotsIterator:
            player = slotInfo.player
            if player is None:
                continue
            slotsWithPlayers.append(slotInfo.index)
            if not player.isLegionary():
                clanMembersInRoster += 1
            else:
                legionariesInRoster += 1

        playersMatchingSlotsCount = len([slotId for slotId in self.getSlotsInPlayersMatching() if slotId not in slotsWithPlayers])
        unitStatsDict = unitStats._asdict()
        return StrongholdUnitStats(clanMembersInRoster=clanMembersInRoster, legionariesInRoster=legionariesInRoster, playersMatchingSlotsCount=playersMatchingSlotsCount, **unitStatsDict)

    def _getRequestProcessor(self):
        return StrongholdUnitRequestProcessor()

    def _getCurrentUTCTime(self):
        return (
         time_utils.getDateTimeInUTC(time_utils.getServerUTCTime()), datetime.datetime.utcnow())

    def _convertUTCStructToLocalTimestamp(self, val):
        val = time_utils.utcToLocalDatetime(val).timetuple()
        return time_utils.getTimestampFromLocal(val)

    def _getUnitRevision(self):
        extra = self.getExtra()
        if extra is not None:
            return extra.rev
        else:
            return 0

    def __updateRosterSettings(self):
        _, unit = self.getUnit(safe=True)
        return StrongholdDynamicRosterSettings(unit, self.__strongholdSettings)

    def __getEventFrozenVehicles(self):
        ctx = StrongholdEventGetFrozenVehiclesCtx()
        self._requestsProcessor.doRequest(ctx, b'getFrozenVehicles', callback=self.__frozenVehiclesReceived)
        return

    def __getForbiddenVehicles(self):
        ctx = StrongholdGetForbiddenVehiclesCtx()
        self._requestsProcessor.doRequest(ctx, b'getForbiddenVehicles', callback=self.__forbiddenVehiclesReceived)
        return

    def __frozenVehiclesReceived(self, response):
        if not self.__processResponseMessage(response):
            BigWorld.callback(0.1, self.__getEventFrozenVehicles)
            return
        rawData = response.getData()
        if response.getCode() != ResponseCodes.NO_ERRORS:
            return
        self.__eventFrozenVehiclesRequester.setInitialDataAndStart(rawData)
        return

    def __forbiddenVehiclesReceived(self, response):
        if not self.__processResponseMessage(response):
            BigWorld.callback(0.1, self.__getForbiddenVehicles)
            return
        rawData = response.getData()
        if response.getCode() != ResponseCodes.NO_ERRORS:
            return
        self.__forbiddenVehiclesRequester.setInitialDataAndStart(rawData)
        return

    def __initForbiddenVehiclesRequester(self):
        if self.__forbiddenVehiclesRequester is None:
            self.__forbiddenVehiclesRequester = ForbiddenVehiclesRequester()
        if self.__forbiddenVehiclesRequester.isCacheEmpty():
            self.__getForbiddenVehicles()
        return

    def __frozenVehiclesUpdated(self, updatedSpaIDs):
        self._invokeListeners(b'onEventFrozenVehiclesChanged', updatedSpaIDs)
        return

    def __isStrongholdEventEnabled(self):
        if not getStrongholdEventEnabled():
            return False
        battleMode, lvl = getStrongholdEventBattleModeSettings()
        header = self.__strongholdSettings.getHeader()
        if header.getType() != battleMode:
            return False
        if not header.getMinLevel() <= lvl <= header.getMaxLevel():
            return False
        return True

    def __checkStrongholdEvent(self):
        if not g_clanCache.strongholdEventProvider.isRunning() or not self.__isStrongholdEventEnabled():
            return False
        if self.__eventFrozenVehiclesRequester is not None:
            self.__eventFrozenVehiclesRequester.stop()
        else:
            self.__eventFrozenVehiclesRequester = FrozenVehiclesRequester()
        self.__eventFrozenVehiclesRequester.onUpdated += self.__frozenVehiclesUpdated
        self.__getEventFrozenVehicles()
        return True

    def __onStrongholdUpdate(self, response):
        if not self.__processResponseMessage(response):
            BigWorld.callback(0.0, self.requestUpdateStronghold)
            return
        else:
            rawData = response.getData()
            if response.getCode() != ResponseCodes.NO_ERRORS and not rawData:
                return
            self.__waitingManager.onResponseWebReqID(DEFAULT_OK_WEB_REQUEST_ID)
            _, unit = self.getUnit(unitMgrID=None, safe=True)
            if unit is None:
                return
            diffToUpdate = self.__strongholdSettings.updateData(rawData)
            if diffToUpdate is None:
                self._invokeListeners(b'onStrongholdMaintenance', True)
                return
            LOG_DEBUG(b'onStrongholdUpdate, timer data (r,m): ', self.__strongholdSettings.getTimer().getTimeToReady(), self.__strongholdSettings.getTimer().getMatchmakerNextTick())
            if not self.__isMatchmakingTimerLoopExist():
                self._updateMatchmakingTimer()
            self.__doClockworkLogic(invokeListeners=True, forceUpdateBuildings=True)
            if self.isStrongholdSettingsValid():
                header = self.__strongholdSettings.getHeader()
                isFirstBattle = self.isFirstBattle()
                self.__checkBattleMode(header, isFirstBattle)
                self._invokeListeners(b'onStrongholdDataChanged', header, isFirstBattle, self.__strongholdSettings.getReserve(), self.__strongholdSettings.getReserveOrder())
            if b'all' in diffToUpdate:
                self.updateStrongholdData()
            else:
                for toUpdate in diffToUpdate:
                    listener = self.__strongholdUpdateEventsMapping.get(toUpdate)
                    if listener is not None:
                        listener()

            g_eventBus.handleEvent(StrongholdEvent(StrongholdEvent.STRONGHOLD_UPDATED), scope=EVENT_BUS_SCOPE.LOBBY)
            return

    def __checkBattleMode(self, header, isFirstBattle):
        if isFirstBattle:
            gettersMapping = {b'type': (header.getType), b'direction': (header.getDirection), 
               b'max_level': (header.getMaxLevel), 
               b'max_players_count': (header.getMaxPlayersCount)}
            battleModeFields = (
             (b'type', b'STRONGHOLDS_MODE_CHANGED'),
             (b'direction', b'STRONGHOLDS_DIRECTION_CHANGED'),
             (b'max_level', b'STRONGHOLDS_MODE_CHANGED'),
             (b'max_players_count', b'STRONGHOLDS_MODE_CHANGED'))
            if self.__battleModeData:
                for field, key in battleModeFields:
                    if self.__battleModeData.get(field) != gettersMapping[field]():
                        SystemMessages.pushI18nMessage(messages.getUnitWarningMessage(key), type=SystemMessages.SM_TYPE.Warning)
                        self.__slotVehicleFilters = {}
                        if key == b'STRONGHOLDS_MODE_CHANGED':
                            self.resetPlayerReadiness()
                            self.__checkStrongholdEvent()
                        break

            else:
                self.__checkStrongholdEvent()
            for field, _ in battleModeFields:
                self.__battleModeData[field] = gettersMapping[field]()

        return

    def __onUpdateHeader(self):
        header = self.__strongholdSettings.getHeader()
        isFirstBattle = self.isFirstBattle()
        battleIdx = header.getBattleIdx()
        flags = self.getFlags()
        if battleIdx == 0 or flags.isInArena() or flags.isInQueue():
            self.storage.setActiveAnimationIdx(battleIdx)
        self.__checkBattleMode(header, isFirstBattle)
        self._invokeListeners(b'onUpdateHeader', header, isFirstBattle, self.isStrongholdUnitFreezed())
        return

    def __onUpdateTimer(self):
        self._invokeListeners(b'onUpdateTimer', self.__strongholdSettings.getTimer())
        return

    def __onUpdateState(self):
        state = self.__strongholdSettings.getState()
        self._invokeListeners(b'onUpdateState', state)
        return

    def __onUpdateReserve(self):
        self._invokeListeners(b'onUpdateReserve', self.__strongholdSettings.getReserve(), self.__strongholdSettings.getReserveOrder())
        return

    def __processResponseMessage(self, response):
        if isinstance(response, Response):
            hasErrors = response.getCode() != ResponseCodes.NO_ERRORS
            if hasErrors and response.extraCode not in SUCCESS_STATUSES:
                self.__errorCount += 1
                if self.canShowMaintenance():
                    self._invokeListeners(b'onStrongholdMaintenance', True)
                    return True
                return False
            self.__errorCount = 0
            data = response.getData()
            if isinstance(data, dict):
                webReqID = data.get(b'web_request_id')
                if webReqID is not None:
                    LOG_DEBUG((b'Web response requestID = {}').format(webReqID))
                    self.__waitingManager.onResponseWebReqID(webReqID)
                if b'extra_data' in data:
                    data = data[b'extra_data']
                    if not isinstance(data, dict):
                        data = {b'description': data}
                txtMsg = data.get(b'description') or data.get(b'title')
                if txtMsg:
                    notificationType = SM_TYPE.lookup(data.get(b'notification_type'))
                    if notificationType not in [SM_TYPE.Error, SM_TYPE.Warning, SM_TYPE.Information]:
                        notificationType = SM_TYPE.Error
                    SystemMessages.pushMessage(txtMsg, type=notificationType)
            if response.getCode() != ResponseCodes.NO_ERRORS:
                self.__waitingManager.onResponseError()
        return True

    def __onReadyButtonEnabled(self):
        self._invokeListeners(b'onStrongholdOnReadyStateChanged')
        return

    def __isMatchmakingTimerLoopExist(self):
        return self.__timerID is not None

    def __cancelMatchmakingTimer(self):
        if self.__timerID is not None:
            BigWorld.cancelCallback(self.__timerID)
            self.__timerID = None
        return

    def __calculatePeripheryTimeHelper(self, baseTimeUTC):
        timer = self.__strongholdSettings.getTimer()
        peripheryStartTimeUTC = time.strptime(timer.getBattlesStartTime(), b'%H:%M')
        peripheryEndTimeUTC = time.strptime(timer.getBattlesEndTime(), b'%H:%M')
        peripheryStartTimeUTC = baseTimeUTC.replace(hour=peripheryStartTimeUTC.tm_hour, minute=peripheryStartTimeUTC.tm_min, second=0, microsecond=0)
        peripheryEndTimeUTC = baseTimeUTC.replace(hour=peripheryEndTimeUTC.tm_hour, minute=peripheryEndTimeUTC.tm_min, second=0, microsecond=0)
        if peripheryStartTimeUTC > peripheryEndTimeUTC:
            shiftedStartTimeUTC = peripheryStartTimeUTC - datetime.timedelta(days=1)
            if shiftedStartTimeUTC <= baseTimeUTC <= peripheryEndTimeUTC:
                peripheryStartTimeUTC = shiftedStartTimeUTC
            else:
                peripheryEndTimeUTC += datetime.timedelta(days=1)
        if baseTimeUTC > peripheryEndTimeUTC and baseTimeUTC > peripheryStartTimeUTC:
            peripheryEndTimeUTC += datetime.timedelta(days=1)
            peripheryStartTimeUTC += datetime.timedelta(days=1)
        return (peripheryStartTimeUTC, peripheryEndTimeUTC)

    def __doClockworkLogic(self, regularMode=False, invokeListeners=False, forceUpdateBuildings=False, returnMatchingButtonIsInactive=False, returnMatchmakerNextTick=False):
        if not self.isStrongholdSettingsValid():
            if returnMatchingButtonIsInactive:
                return True
            return
        isInBattle = self._hasInArenaMembers()
        isInQueue = self._isInQueue()
        dtime = None
        peripheryStartTimestampUTC = 0
        currentTimestampUTC = 0
        matchmakerNextTick = None
        inactiveMatchingButton = True
        currentTimeUTC, clientTimeUTC = self._getCurrentUTCTime()
        timer = self.__strongholdSettings.getTimer()
        peripheryStartTimeUTC = currentTimeUTC.replace(hour=0, minute=0, second=0, microsecond=0)
        peripheryEndTimeUTC = currentTimeUTC.replace(hour=0, minute=0, second=0, microsecond=0)
        if timer.getBattlesStartTime() and timer.getBattlesEndTime():
            isInactivePeriphery = False
            peripheryStartTimeUTC, peripheryEndTimeUTC = self.__calculatePeripheryTimeHelper(currentTimeUTC)
            peripheryStartTimestampUTC = int(time_utils.getTimestampFromUTC(peripheryStartTimeUTC.timetuple()))
            currentTimestampUTC = int(time_utils.getTimestampFromUTC(currentTimeUTC.timetuple()))
        else:
            peripheryEndTimeUTC -= datetime.timedelta(days=1)
            peripheryStartTimeUTC -= datetime.timedelta(days=1)
            isInactivePeriphery = True
            dtime = 0
        if self.__strongholdSettings.isSortie():
            if isInQueue:
                textid = TOOLTIPS.STRONGHOLDS_TIMER_SQUADINQUEUE
                dtime = peripheryStartTimestampUTC - currentTimestampUTC
                if dtime < 0 or dtime > timer.getSortiesBeforeStartLag():
                    dtime = 0
            elif isInBattle:
                textid = TOOLTIPS.STRONGHOLDS_TIMER_SQUADINBATTLE
            elif self.isStrongholdUnitWaitingForData():
                textid = TOOLTIPS.STRONGHOLDS_TIMER_WAITINGFORDATA
            elif peripheryStartTimeUTC <= currentTimeUTC <= peripheryEndTimeUTC:
                dtime = int((peripheryEndTimeUTC - currentTimeUTC).total_seconds())
                inactiveMatchingButton = False
                if dtime <= timer.getSortiesBeforeEndLag():
                    textid = FORTIFICATIONS.SORTIE_INTROVIEW_FORTBATTLES_ENDOFBATTLESOON
                else:
                    textid = FORTIFICATIONS.SORTIE_INTROVIEW_FORTBATTLES_AVAILABLE
            elif isInactivePeriphery:
                textid = FORTIFICATIONS.SORTIE_INTROVIEW_FORTBATTLES_UNAVAILABLE
                dtime = 0
            else:
                dtime = peripheryStartTimestampUTC - currentTimestampUTC
                if dtime <= timer.getSortiesBeforeStartLag():
                    if dtime < 0:
                        dtime = 0
                    textid = FORTIFICATIONS.SORTIE_INTROVIEW_FORTBATTLES_NEXTTIMEOFBATTLESOON
                    if dtime <= self.MATCHMAKING_BATTLE_BUTTON_SORTIE:
                        inactiveMatchingButton = False
                else:
                    peripheryStartTimeUTC, _ = self.__calculatePeripheryTimeHelper(clientTimeUTC)
                    peripheryStartTimestampUTC = int(time_utils.getTimestampFromUTC(peripheryStartTimeUTC.timetuple()))
                    currentTimestampUTC = int(time_utils.getTimestampFromUTC(clientTimeUTC.timetuple()))
                    peripheryStartTimestamp = self._convertUTCStructToLocalTimestamp(peripheryStartTimeUTC)
                    currentTimestamp = self._convertUTCStructToLocalTimestamp(clientTimeUTC)
                    dtime = peripheryStartTimestampUTC - currentTimestampUTC
                    currDayStart, currDayEnd = time_utils.getDayTimeBoundsForLocal(peripheryStartTimestamp)
                    if currDayStart - time_utils.ONE_DAY <= currentTimestamp <= currDayEnd - time_utils.ONE_DAY:
                        textid = FORTIFICATIONS.SORTIE_INTROVIEW_FORTBATTLES_NEXTTIMEOFBATTLETOMORROW
                    elif currDayStart <= currentTimestamp <= currDayEnd:
                        textid = FORTIFICATIONS.SORTIE_INTROVIEW_FORTBATTLES_NEXTTIMEOFBATTLETODAY
        else:
            textid = FORTIFICATIONS.ROSTERINTROWINDOW_INTROVIEW_FORTBATTLES_UNAVAILABLE
            dtime = isInactivePeriphery or time_utils.ONE_YEAR
            matchmakerNextTick = timer.getTimeToReady()
            if matchmakerNextTick is not None:
                dtime = int(matchmakerNextTick - currentTimestampUTC)
            else:
                matchmakerNextTick = timer.getMatchmakerNextTick()
                if matchmakerNextTick is not None:
                    dtime = int(matchmakerNextTick - currentTimestampUTC)
            battlesBeforeStartLag = timer.getFortBattlesBeforeStartLag()
            if regularMode and self.__prevMatchmakingTimerState == FORTIFICATIONS.ROSTERINTROWINDOW_INTROVIEW_FORTBATTLES_NEXTTIMEOFBATTLESOON:
                if 0 <= int(dtime - battlesBeforeStartLag) < self.MATCHMAKING_ZERO_TIME_WAITING_FOR_DATA:
                    dtime = battlesBeforeStartLag
                if isInQueue:
                    textid = TOOLTIPS.STRONGHOLDS_TIMER_SQUADINQUEUE
                    if dtime < 0 or dtime > battlesBeforeStartLag:
                        dtime = 0
                elif isInBattle:
                    textid = TOOLTIPS.STRONGHOLDS_TIMER_SQUADINBATTLE
                elif self.isStrongholdUnitWaitingForData():
                    textid = TOOLTIPS.STRONGHOLDS_TIMER_WAITINGFORDATA
                if dtime > battlesBeforeStartLag:
                    textid = FORTIFICATIONS.ROSTERINTROWINDOW_INTROVIEW_FORTBATTLES_UNAVAILABLE
                    if matchmakerNextTick is not None:
                        peripheryStartTimeUTC, _ = self.__calculatePeripheryTimeHelper(clientTimeUTC)
                        peripheryStartTimestampUTC = int(time_utils.getTimestampFromUTC(peripheryStartTimeUTC.timetuple()))
                        currentTimestampUTC = int(time_utils.getTimestampFromUTC(clientTimeUTC.timetuple()))
                        currentTimestamp = self._convertUTCStructToLocalTimestamp(clientTimeUTC)
                        dtime = int(matchmakerNextTick - currentTimestampUTC)
                        matchmakerNextTickLocal = time_utils.getDateTimeInUTC(matchmakerNextTick)
                        matchmakerNextTickLocal = self._convertUTCStructToLocalTimestamp(matchmakerNextTickLocal)
                        currDayStart, currDayEnd = time_utils.getDayTimeBoundsForLocal(matchmakerNextTickLocal)
                        if currDayStart - time_utils.ONE_DAY <= currentTimestamp <= currDayEnd - time_utils.ONE_DAY:
                            textid = FORTIFICATIONS.SORTIE_INTROVIEW_FORTBATTLES_NEXTTIMEOFBATTLETOMORROW
                        elif currDayStart <= currentTimestamp <= currDayEnd:
                            textid = FORTIFICATIONS.SORTIE_INTROVIEW_FORTBATTLES_NEXTTIMEOFBATTLETODAY
                elif dtime >= 0:
                    textid = FORTIFICATIONS.ROSTERINTROWINDOW_INTROVIEW_FORTBATTLES_NEXTTIMEOFBATTLESOON
                    if dtime <= self.MATCHMAKING_BATTLE_BUTTON_BATTLE or not self.__strongholdSettings.isFirstBattle():
                        inactiveMatchingButton = False
                else:
                    dtimeWD = dtime + self.MATCHMAKING_ZERO_TIME_WAITING_FOR_DATA
                    if dtimeWD >= 0:
                        textid = FORTIFICATIONS.ROSTERINTROWINDOW_INTROVIEW_FORTBATTLES_NEXTTIMEOFBATTLESOON
                    dtime = 0
        if regularMode:
            self.__prevMatchmakingTimerState = textid
        if invokeListeners:
            header = self.__strongholdSettings.getHeader()
            g_eventDispatcher.strongholdsOnTimer({b'peripheryStartTimestamp': peripheryStartTimestampUTC, 
               b'matchmakerNextTick': matchmakerNextTick, 
               b'clan': (header.getClan()), 
               b'enemyClan': (header.getEnemyClan()), 
               b'textid': textid, 
               b'dtime': dtime, 
               b'isSortie': (self.__strongholdSettings.isSortie()), 
               b'isFirstBattle': (self.__strongholdSettings.isFirstBattle()), 
               b'currentBattle': (header.getCurrentBattle()), 
               b'maxLevel': (header.getMaxLevel()), 
               b'direction': (header.getDirection()), 
               b'forceUpdateBuildings': forceUpdateBuildings})
        if returnMatchingButtonIsInactive:
            return inactiveMatchingButton
        else:
            if returnMatchmakerNextTick:
                return matchmakerNextTick
            return

    def __onExternalLegionariesMatchingToggle(self, inExternalLegionariesMatching):
        if inExternalLegionariesMatching:
            self.__playersMatchingStartedAt = datetime.datetime.utcnow()
        else:
            self.__playersMatchingStartedAt = None
        if self.isCommander() and not inExternalLegionariesMatching:
            self.requestSlotVehicleFilters()
        return

    def __onCommanderChanged(self, playerID):
        pInfo = self.getPlayerInfo(dbID=playerID)
        if pInfo.isCurrentPlayer():
            unitWarningRes = R.strings.system_messages.unit.warnings
            if not pInfo.isCommander():
                if self.__isAnyPlayerEquipmentCommander():
                    messageRes = unitWarningRes.ANOTHER_PLAYER_BECOME_COMMANDER()
                else:
                    messageRes = unitWarningRes.ANOTHER_PLAYER_BECOME_COMMANDER_WITH_EQUIPMENT_PERMISSION()
                messageType = SM_TYPE.Information
            else:
                if self.__isAnyPlayerEquipmentCommander():
                    messageRes = unitWarningRes.PLAYER_BECOME_COMMANDER()
                else:
                    messageRes = unitWarningRes.PLAYER_BECOME_COMMANDER_WITH_EQUIPMENT_PERMISSION()
                messageType = SM_TYPE.Warning
                self.requestSlotVehicleFilters()
            SystemMessages.pushMessage(backport.text(messageRes), type=messageType)
        return

    def __isAnyPlayerEquipmentCommander(self):
        equipRoles = UNIT_ROLE.CAN_USE_EXTRA_EQUIPMENTS | UNIT_ROLE.CAN_USE_BOOST_EQUIPMENTS
        return any(slot.player and slot.player.role & equipRoles > 0 for slot in self.getSlotsIterator(*self.getUnit()))

    @staticmethod
    def __isEquipmentRoleChanged(left, right):
        return (left ^ right) & right > 0

    def __onParentControlNotify(self):
        g_eventDispatcher.updateUI()
        return
