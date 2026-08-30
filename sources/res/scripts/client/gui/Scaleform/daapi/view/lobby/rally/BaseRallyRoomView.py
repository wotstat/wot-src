from __future__ import absolute_import
import account_helpers
from CurrentVehicle import g_currentVehicle
from UnitBase import UNIT_SLOT
from adisp import adisp_process
from debug_utils import LOG_DEBUG
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.view.lobby.rally import vo_converters
from gui.Scaleform.daapi.view.meta.BaseRallyRoomViewMeta import BaseRallyRoomViewMeta
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.prb_control.entities.base.unit.ctx import AssignUnitCtx, CloseSlotUnitCtx, LockUnitCtx, KickPlayerUnitCtx, ChangeCommentUnitCtx, ChangeOpenedUnitCtx, SetRostersSlotsUnitCtx, SetVehicleUnitCtx, RosterSlotCtx
from gui.prb_control.settings import CTRL_ENTITY_TYPE, REQUEST_TYPE
from gui.shared import events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency
from helpers import i18n
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS
from messenger.proto.events import g_messengerEvents
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup
from skeletons.gui.shared import IItemsCache

class BaseRallyRoomView(BaseRallyRoomViewMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        super(BaseRallyRoomView, self).__init__()
        self._candidatesDP = None
        return

    def requestToAssign(self, pID, slotIdx):
        self.sendRequest(AssignUnitCtx(pID, slotIdx, b'prebattle/assign'))
        return

    def requestToUnassign(self, pID):
        self.sendRequest(AssignUnitCtx(pID, UNIT_SLOT.REMOVE, b'prebattle/assign'))
        return

    def requestToCloseSlot(self, slotIdx):
        slotState = self.prbEntity.getSlotState(slotIdx)
        self.sendRequest(CloseSlotUnitCtx(slotIdx, not slotState.isClosed, b'prebattle/change_settings'))
        return

    def requestToKickUser(self, databaseID):
        self.sendRequest(KickPlayerUnitCtx(databaseID, b'prebattle/kick'))
        return

    def requestToLock(self, isLocked):
        self.sendRequest(LockUnitCtx(isLocked, b'prebattle/change_settings'))
        return

    def requestToOpen(self, isOpened):
        self.sendRequest(ChangeOpenedUnitCtx(isOpened, b'prebattle/change_settings'))
        return

    def requestToChangeComment(self, comment):
        self.sendRequest(ChangeCommentUnitCtx(comment, b'prebattle/change_settings'))
        return

    def requestToUpdateRoster(self, data):
        c = SetRostersSlotsUnitCtx(b'prebattle/change_settings')
        for i, item in enumerate(data):
            c.addRosterSlot(i * 2, self.__getRosterSlotCtx(item[0]))
            c.addRosterSlot(i * 2 + 1, self.__getRosterSlotCtx(item[1]))

        self.sendRequest(c)
        return

    @adisp_process
    def sendRequest(self, request):
        yield self.prbDispatcher.sendPrbRequest(request)
        return

    def onUnitPlayersListChanged(self):
        if self._candidatesDP is not None:
            self._candidatesDP.rebuild(self.prbEntity.getCandidates())
        self._updateRallyData()
        return

    def onUnitPlayerInfoChanged(self, pInfo):
        if pInfo.isInSlot:
            self._updateMembersData()
        elif self._candidatesDP is not None:
            self._candidatesDP.rebuild(self.prbEntity.getCandidates())
        return

    def onUnitPlayerStateChanged(self, pInfo):
        self.__setMemberStatus(pInfo)
        if pInfo.isCurrentPlayer() or self.prbEntity.isCommander():
            self._setActionButtonState()
        return

    def onUnitPlayerRolesChanged(self, pInfo, pPermissions):
        if pInfo.isCurrentPlayer():
            self._setActionButtonState()
        self._updateMembersData()
        return

    def onUnitPlayerOnlineStatusChanged(self, pInfo):
        if pInfo.isInSlot:
            self.as_setMemberOfflineS(pInfo.slotIdx, pInfo.isOffline())
        elif self._candidatesDP is not None:
            self._candidatesDP.setOnline(pInfo)
        return

    def onUnitPlayerEnterOrLeaveArena(self, pInfo):
        self.__setMemberStatus(pInfo)
        return

    def onUnitPlayerBecomeCreator(self, pInfo):
        self._updateRallyData()
        return

    def onUnitRejoin(self):
        self._updateRallyData()
        self._setActionButtonState()
        return

    def onUnitPlayerVehDictChanged(self, pInfo):
        if pInfo.isCurrentPlayer():
            self._updateRallyData()
            self._setActionButtonState()
        return

    def onUnitRosterChanged(self):
        self._updateMembersData()
        return

    def onUnitCurfewChanged(self):
        LOG_DEBUG(b'%s : onUnitCurfewChanged' % self)
        self._setActionButtonState()
        return

    def _updateRallyData(self):
        return

    def setData(self, initialData):
        LOG_DEBUG(b'CyberSportUnitView.setItemId passed team id is:', initialData)
        return

    def getCoolDownRequests(self):
        return [
         REQUEST_TYPE.SET_PLAYER_STATE, REQUEST_TYPE.CHANGE_UNIT_STATE]

    def initCandidatesDP(self):
        return

    def rebuildCandidatesDP(self):
        return

    def _setActionButtonState(self):
        return

    def startListening(self):
        g_currentVehicle.onChanged += self.__handleCurrentVehicleChanged
        return

    def stopListening(self):
        g_currentVehicle.onChanged -= self.__handleCurrentVehicleChanged
        return

    def _populate(self):
        super(BaseRallyRoomView, self)._populate()
        self.initCandidatesDP()
        self.startListening()
        self.addListener(events.CSVehicleSelectEvent.VEHICLE_SELECTED, self.__onVehicleSelectHandler)
        self._updateRallyData()
        self._setActionButtonState()
        usersEvents = g_messengerEvents.users
        usersEvents.onUsersListReceived += self._onUsersReceived
        usersEvents.onUserActionReceived += self._onUserActionReceived
        self.itemsCache.onSyncCompleted += self._onCacheResync
        return

    def _dispose(self):
        usersEvents = g_messengerEvents.users
        usersEvents.onUsersListReceived -= self._onUsersReceived
        usersEvents.onUserActionReceived -= self._onUserActionReceived
        self.itemsCache.onSyncCompleted -= self._onCacheResync
        self._closeSendInvitesWindow()
        HideEvent = events.HideWindowEvent
        self.fireEvent(HideEvent(HideEvent.HIDE_VEHICLE_SELECTOR_WINDOW))
        if self._candidatesDP is not None:
            self._candidatesDP.fini()
            self._candidatesDP = None
        self.stopListening()
        self.removeListener(events.CSVehicleSelectEvent.VEHICLE_SELECTED, self.__onVehicleSelectHandler)
        super(BaseRallyRoomView, self)._dispose()
        return

    def assignSlotRequest(self, slotIndex, playerId):
        if playerId == -1:
            if self.prbEntity.isCommander():
                LOG_DEBUG(b'Request to assign is ignored. Creator can not move to another slots')
                return
            playerId = account_helpers.getAccountDatabaseID()
        elif not self.isPlayerInUnit(playerId):
            return
        self.requestToAssign(playerId, slotIndex)
        return

    def leaveSlotRequest(self, playerId):
        if self.isPlayerInSlot(playerId):
            self.requestToUnassign(playerId)
        return

    def _chooseVehicleRequest(self, levelsRange):
        playerInfo = self.prbEntity.getPlayerInfo()
        slotIdx = playerInfo.slotIdx
        vehicles = playerInfo.getSlotsToVehicles(True).get(slotIdx)
        if vehicles is not None:
            vehicles = self.itemsCache.items.getVehicles(REQ_CRITERIA.VEHICLE.SPECIFIC_BY_CD(vehicles))
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(CYBER_SPORT_ALIASES.VEHICLE_SELECTOR_POPUP_PY), ctx={b'isMultiSelect': False, 
           b'vehicles': vehicles, 
           b'titleText': (CYBERSPORT.WINDOW_VEHICLESELECTOR_TITLE), 
           b'selectButton': (CYBERSPORT.WINDOW_VEHICLESELECTOR_BUTTONS_SELECT), 
           b'cancelButton': (CYBERSPORT.WINDOW_VEHICLESELECTOR_BUTTONS_CANCEL), 
           b'infoText': (self._getVehicleSelectorDescription()), 
           b'compatibleOnlyLabel': (CYBERSPORT.WINDOW_VEHICLESELECTOR_FILTERS_MATCHES), 
           b'selectedVehicles': (self._getVehicleSelectorVehicles()), 
           b'section': b'cs_unit_view_vehicle', 
           b'levelsRange': levelsRange}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def chooseVehicleRequest(self):
        levelsRange = self.prbEntity.getRosterSettings().getLevelsRange()
        self._chooseVehicleRequest(levelsRange)
        return

    def inviteFriendRequest(self):
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(PREBATTLE_ALIASES.SEND_INVITES_WINDOW_PY), ctx={b'prbName': b'unit', 
           b'ctrlType': (CTRL_ENTITY_TYPE.UNIT)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def toggleReadyStateRequest(self):
        self.prbEntity.doAction()
        return

    def ignoreUserRequest(self, slotIndex):
        playerInfo = self.prbEntity.getPlayerInfo()
        if playerInfo.isCommander():
            self.requestToKickUser(slotIndex)
        return

    def onSlotsHighlihgtingNeed(self, databaseID):
        availableSlots = self.getAvailableSlots(databaseID)
        self.as_highlightSlotsS(availableSlots)
        return availableSlots

    def getAvailableSlots(self, databaseID):
        availableSlots = list(self.prbEntity.getPlayerInfo(databaseID).getAvailableSlots(True))
        return availableSlots

    def editDescriptionRequest(self, description):
        LOG_DEBUG(b'EDIT DESCRIPTION: ', description)
        self.requestToChangeComment(description)
        return

    def showFAQWindow(self):
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(MESSENGER_VIEW_ALIAS.FAQ_WINDOW)), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __onVehicleSelectHandler(self, event):
        self._selectVehicles(event.ctx)
        return

    def _selectVehicles(self, items):
        if items:
            self.sendRequest(SetVehicleUnitCtx(vTypeCD=items[0], waitingID=b'prebattle/change_settings'))
        return

    def _onUserActionReceived(self, _, user, shadowMode):
        self._updateRallyData()
        if self._candidatesDP is not None and self._candidatesDP.hasCandidate(user.getID()):
            self.rebuildCandidatesDP()
        return

    def _onUsersReceived(self, _):
        if self.prbEntity is not None:
            self._updateRallyData()
        return

    def _updateVehiclesLabel(self, minVal, maxVal):
        vehicleLvl = text_styles.main(i18n.makeString(CYBERSPORT.WINDOW_UNIT_RANGEVALUE, minVal=minVal, maxVal=maxVal))
        vehicleLbl = text_styles.standard(i18n.makeString(CYBERSPORT.WINDOW_UNIT_TEAMVEHICLESLBL, levelsRange=vehicleLvl))
        self.as_setVehiclesTitleS(vehicleLbl, {})
        return

    def _closeSendInvitesWindow(self):
        self._destroyRelatedView(WindowLayer.WINDOW, PREBATTLE_ALIASES.SEND_INVITES_WINDOW_PY)
        return

    def _destroyRelatedView(self, container, alias):
        container = self.app.containerManager.getContainer(container)
        if container is not None:
            view = container.getView(criteria={(POP_UP_CRITERIA.VIEW_ALIAS): alias})
            if view is not None:
                view.destroy()
        return

    def onUnitErrorReceived(self, errorCode):
        selected = self._getVehicleSelectorVehicles()
        if selected:
            vehicle = self.itemsCache.items.getItemByCD(selected[0])
            if vehicle.hasNationGroup:
                playerInfo = self.prbEntity.getPlayerInfo()
                slotIdx = playerInfo.slotIdx
                self.as_setMemberVehicleS(slotIdx, 0, None)
        return

    def isPlayerInUnit(self, databaseID):
        result = False
        players = self.prbEntity.getPlayers()
        for dbId in players:
            if dbId == databaseID:
                result = True
                break

        return result

    def isPlayerInSlot(self, databaseID=None):
        pInfo = self.prbEntity.getPlayerInfo(dbID=databaseID)
        return pInfo.isInSlot

    def isPlayerReady(self, databaseID=None):
        pInfo = self.prbEntity.getPlayerInfo(dbID=databaseID)
        return pInfo.isReady

    def _getVehicleSelectorDescription(self):
        return b''

    def _getVehicleSelectorVehicles(self):
        selected = []
        for vInfo in self.prbEntity.getVehiclesInfo():
            if not vInfo.isEmpty():
                selected.append(vInfo.vehTypeCD)

        return selected

    def __getRosterSlotCtx(self, item):
        if item is None:
            return RosterSlotCtx()
        else:
            if item.selectedVehicle > 0:
                return RosterSlotCtx(item.selectedVehicle)
            else:
                settings = self.prbEntity.getRosterSettings()
                levels = (settings.getMinLevel(), settings.getMaxLevel())
                if len(item.vLevelRange) == 2:
                    i0 = int(item.vLevelRange[0])
                    i1 = int(item.vLevelRange[1])
                    levels = (i0, i1) if i0 != i1 else i0
                elif len(item.vLevelRange) == 1:
                    levels = int(item.vLevelRange[0])
                return RosterSlotCtx(nationNames=item.nationIDRange, levels=levels, vehClassNames=item.vTypeRange)

            return

    def __setMemberStatus(self, pInfo):
        if pInfo.isInSlot:
            slotIdx = pInfo.slotIdx
            slotState = self.prbEntity.getSlotState(slotIdx)
            self.as_setMemberStatusS(slotIdx, vo_converters.getPlayerStatus(slotState, pInfo))
        return

    def _updateMembersData(self):
        entity = self.prbEntity
        self.as_setMembersS(*vo_converters.makeSlotsVOs(entity, entity.getID()))
        self._setActionButtonState()
        return

    def __handleCurrentVehicleChanged(self):
        self._setActionButtonState()
        self._updateMembersData()
        return

    def _onCacheResync(self, reason, diff):
        if reason != CACHE_SYNC_REASON.CLIENT_UPDATE:
            return
        else:
            selected = self._getVehicleSelectorVehicles()
            if selected:
                if diff is not None and GUI_ITEM_TYPE.VEHICLE in diff:
                    vehDiff = diff[GUI_ITEM_TYPE.VEHICLE]
                    for changedVehCD in vehDiff:
                        vehicle = self.itemsCache.items.getItemByCD(changedVehCD)
                        if not vehicle.activeInNationGroup and selected[0] == changedVehCD:
                            itemCD = next(iterVehTypeCDsInNationGroup(vehicle.intCD))
                            self._selectVehicles([itemCD])

            return
