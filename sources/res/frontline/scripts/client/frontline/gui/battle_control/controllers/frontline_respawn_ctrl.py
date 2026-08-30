import BigWorld
from debug_utils import LOG_ERROR, LOG_DEBUG
from gui.battle_control import avatar_getter
from frontline.gui.battle_control.controllers.base_respawn_ctrl import BaseRespawnsController, IRespawnView
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
EB_MIN_RESPAWN_LANE_IDX = 1
EB_MAX_RESPAWN_LANE_IDX = 4

class IFrontlineRespawnView(IRespawnView):

    def setSelectedLane(self, laneId):
        return

    def setSelectedPoint(self, pointId):
        return

    def setRespawnInfo(self, respawnInfo):
        return

    def setLaneState(self, laneID, enabled, blockedText):
        return


class FrontlineRespawnsController(BaseRespawnsController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def startControl(self):
        super(FrontlineRespawnsController, self).startControl()
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
        super(FrontlineRespawnsController, self).stopControl()
        playerDataComp = getattr(self.sessionProvider.arenaVisitor.getComponentSystem(), b'playerDataComponent', None)
        if playerDataComp is not None:
            playerDataComp.onPlayerRespawnLaneUpdated -= self.__onPlayerRespawnLaneUpdated
            playerDataComp.onPlayerGroupsChanged -= self.__onPlayerGroupsChanged
            playerDataComp.onPlayerPhysicalLaneUpdated -= self.__onPlayerPhysicalLaneUpdated
        return

    def updateVehicleLimits(self, limits):
        super(FrontlineRespawnsController, self).updateVehicleLimits(limits)
        self.__onRespawnInfoUpdated()
        return

    def updateRespawnInfo(self, respawnInfo):
        super(FrontlineRespawnsController, self).updateRespawnInfo(respawnInfo)
        self.__onRespawnInfoUpdated()
        return

    def requestPointForRespawn(self, respawnZone):
        BigWorld.player().FLAvatarComponent.cell.chooseRespawnZone(respawnZone)
        return

    def chooseVehicleForRespawn(self, intCD):
        BigWorld.player().FLAvatarComponent.cell.chooseVehicleForRespawn(intCD)
        return

    def sendSwitchVehSetupsLayout(self, vehCD, groupID, layoutIdx):
        BigWorld.player().FLAvatarComponent.cell.switchSetup(vehCD, groupID, layoutIdx)
        return

    def respawnPlayer(self):
        BigWorld.player().FLAvatarComponent.cell.performRespawn()
        return

    def _show(self):
        super(FrontlineRespawnsController, self)._show()
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
            isVehicleBlocked = lane in vehicleLimits and selectedVehicleID in vehicleLimits[lane]
            isAvailableForPlayer = (isEnoughPlace or playerDataComp.respawnLane == lane and not availableLanes) and not isVehicleBlocked
            reasonText = b''
            if not isEnoughPlace:
                reasonText = backport.text(R.strings.epic_battle.deploymentMap.lanePlayerLimitReached())
            elif isVehicleBlocked:
                reasonText = backport.text(R.strings.epic_battle.deploymentMap.spgLimitReached())
            if not isEnoughPlace or isVehicleBlocked:
                LOG_DEBUG(b'lane %d is blocked for %d ', lane, selectedVehicleID, isVehicleBlocked, vehicleLimits.get(lane, 0))
            for viewCmp in self._viewComponents:
                viewCmp.setLaneState(lane, isAvailableForPlayer, reasonText)

        return
