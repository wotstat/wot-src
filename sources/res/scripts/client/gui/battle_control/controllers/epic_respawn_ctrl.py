import BigWorld, Event
from debug_utils import LOG_ERROR, LOG_DEBUG
from gui.battle_control import avatar_getter
from gui.battle_control.controllers.respawn_ctrl import RespawnsController, IRespawnView
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from shared_utils import first
from skeletons.gui.battle_session import IBattleSessionProvider
EB_MIN_RESPAWN_LANE_IDX = 1
EB_MAX_RESPAWN_LANE_IDX = 4
LIMITED_TEXT_BY_TAGS = {b'SPG': (backport.text(R.strings.epic_battle.deploymentMap.spgLimitReached())), 
   b'flamethrower': (backport.text(R.strings.epic_battle.deploymentMap.flamethrowerLimitReached())), 
   b'default': (backport.text(R.strings.epic_battle.deploymentMap.spgLimitReached()))}

class IEpicRespawnView(IRespawnView):

    def setSelectedLane(self, laneId):
        return

    def setSelectedPoint(self, pointId):
        return

    def setRespawnInfo(self, respawnInfo):
        return

    def setLaneState(self, laneID, enabled, blockedText):
        return


class EpicRespawnsController(RespawnsController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, setup):
        super(EpicRespawnsController, self).__init__(setup)
        self.onRequestPointForRespawn = Event.Event(self._eManager)
        return

    def startControl(self):
        super(EpicRespawnsController, self).startControl()
        playerDataComp = getattr(self.sessionProvider.arenaVisitor.getComponentSystem(), b'playerDataComponent', None)
        if playerDataComp is None:
            LOG_ERROR(b'Expected PlayerDataComponent not present!')
            return
        else:
            playerDataComp.onPlayerRespawnLaneUpdated += self.__onPlayerRespawnLaneUpdated
            playerDataComp.onPlayerGroupsChanged += self.__onPlayerGroupsChanged
            playerDataComp.onPlayerPhysicalLaneUpdated += self.__onPlayerPhysicalLaneUpdated
            return

    def stopControl(self):
        super(EpicRespawnsController, self).stopControl()
        playerDataComp = getattr(self.sessionProvider.arenaVisitor.getComponentSystem(), b'playerDataComponent', None)
        if playerDataComp is not None:
            playerDataComp.onPlayerRespawnLaneUpdated -= self.__onPlayerRespawnLaneUpdated
            playerDataComp.onPlayerGroupsChanged -= self.__onPlayerGroupsChanged
            playerDataComp.onPlayerPhysicalLaneUpdated -= self.__onPlayerPhysicalLaneUpdated
        return

    def updateVehicleLimits(self, limits):
        super(EpicRespawnsController, self).updateVehicleLimits(limits)
        self.__onRespawnInfoUpdated()
        return

    def updateRespawnInfo(self, respawnInfo):
        super(EpicRespawnsController, self).updateRespawnInfo(respawnInfo)
        self.__onRespawnInfoUpdated()
        return

    @staticmethod
    def requestLaneForRespawn(laneID):
        BigWorld.player().base.respawnController_requestRespawnGroupChange(laneID)
        return

    def requestPointForRespawn(self, respawnZone):
        self.onRequestPointForRespawn(respawnZone)
        BigWorld.player().base.respawnController_chooseRespawnZone(respawnZone)
        return

    def _show(self):
        super(EpicRespawnsController, self)._show()
        playerDataComp = getattr(self.sessionProvider.arenaVisitor.getComponentSystem(), b'playerDataComponent', None)
        if playerDataComp is not None:
            self.__onPlayerRespawnLaneUpdated(playerDataComp.respawnLane)
        return

    def __onPlayerRespawnLaneUpdated(self, laneID):
        for viewCmp in self._viewComponents:
            viewCmp.setSelectedLane(laneID)

        self.__onRespawnInfoUpdated()
        return

    def __onPlayerPhysicalLaneUpdated(self, laneID):
        self.__onRespawnInfoUpdated()
        return

    def __onPlayerGroupsChanged(self, _):
        self.__onRespawnInfoUpdated()
        return

    def __onRespawnInfoUpdated(self):
        arena = avatar_getter.getArena()
        playerDataComp = getattr(self.sessionProvider.arenaVisitor.getComponentSystem(), b'playerDataComponent', None)
        if not arena or not playerDataComp or not self.isRespawnVisible():
            return
        for viewCmp in self._viewComponents:
            viewCmp.setRespawnInfo(self.respawnInfo)

        vehicleLimits = self.getLimits()
        limit = arena.arenaType.playerGroupLimit
        selectedVehicleID = 0
        availableLanes = [lane for lane in range(EB_MIN_RESPAWN_LANE_IDX, EB_MAX_RESPAWN_LANE_IDX) if playerDataComp.getPlayersForTeamAndGroup(avatar_getter.getPlayerTeam(), lane) < limit]
        if self.respawnInfo:
            selectedVehicleID = self.respawnInfo.vehicleID
        for lane in range(EB_MIN_RESPAWN_LANE_IDX, EB_MAX_RESPAWN_LANE_IDX):
            if playerDataComp.respawnLane == lane:
                isEnoughPlace = True
            else:
                isEnoughPlace = playerDataComp.getPlayersForTeamAndGroup(avatar_getter.getPlayerTeam(), lane) < limit
            blockedTag = None
            if lane in vehicleLimits:
                vehicleLimitsTags = vehicleLimits[lane]
                blockedTag = first({tag for tag, limitedIds in vehicleLimitsTags.iteritems() if selectedVehicleID in limitedIds})
            isVehicleBlocked = blockedTag is not None
            isAvailableForPlayer = (isEnoughPlace or playerDataComp.respawnLane == lane and not availableLanes) and not isVehicleBlocked
            reasonText = b''
            if not isEnoughPlace:
                reasonText = backport.text(R.strings.epic_battle.deploymentMap.lanePlayerLimitReached())
            elif isVehicleBlocked:
                reasonText = LIMITED_TEXT_BY_TAGS.get(blockedTag, LIMITED_TEXT_BY_TAGS[b'default'])
            if not isEnoughPlace or isVehicleBlocked:
                LOG_DEBUG(b'lane %d is blocked for %d ', lane, selectedVehicleID, isVehicleBlocked, 0 if lane not in vehicleLimits else vehicleLimits[lane])
            for viewCmp in self._viewComponents:
                viewCmp.setLaneState(lane, isAvailableForPlayer, reasonText)

        return
