from __future__ import absolute_import, division
import typing
from builtins import range
from collections import defaultdict
from collections import namedtuple
import BigWorld, BattleReplay, Event
from ReplayEvents import g_replayEvents
from constants import SECTOR_STATE, PLAYER_RANK
from debug_utils import verify, LOG_ERROR, LOG_DEBUG
from epic_constants import EPIC_BATTLE_TEAM_ID
from frontline_common.frontline_constants import FLBattleReservesModifier
from gui import makeHtmlString
from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE
from gui.battle_control import avatar_getter
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.game_messages_ctrl import PlayerMessageData
from gui.battle_control.controllers.game_notification_ctrl import EPIC_NOTIFICATION, OVERTIME_DURATION_WARNINGS
from gui.battle_control.view_components import IViewComponentsController
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency, i18n
from items.vehicles import getVehicleClassFromVehicleType
from shared_utils import first
from skeletons.gui.game_control import IEpicBattleMetaGameController
if typing.TYPE_CHECKING:
    from SectorBase import SectorBase
TIMER_WARNINGS = [(5, 0), (2, 0)]
RANK_TO_TRANSLATION = {0: b'', 
   1: (EPIC_BATTLE.RANK_RANK1), 
   2: (EPIC_BATTLE.RANK_RANK2), 
   3: (EPIC_BATTLE.RANK_RANK3), 
   4: (EPIC_BATTLE.RANK_RANK4), 
   5: (EPIC_BATTLE.RANK_RANK5), 
   6: (EPIC_BATTLE.RANK_RANK6)}
MSG_ID_TO_DURATION = defaultdict((lambda : 4.5))
MSG_ID_TO_DURATION.update({(GAME_MESSAGES_CONSTS.OVERTIME): 4.5})
MSG_ID_TO_PRIORITY = defaultdict((lambda : GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_LOW))
MSG_ID_TO_PRIORITY.update({(GAME_MESSAGES_CONSTS.WIN): (GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_HIGH), 
   (GAME_MESSAGES_CONSTS.DEFEAT): (GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_HIGH), 
   (GAME_MESSAGES_CONSTS.DRAW): (GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_HIGH), 
   (GAME_MESSAGES_CONSTS.TIME_REMAINING): (GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_HIGH), 
   (GAME_MESSAGES_CONSTS.TIME_REMAINING_POSITIVE): (GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_HIGH), 
   (GAME_MESSAGES_CONSTS.OVERTIME): (GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_HIGH)})
HQ_DAMAGE_DEBOUNCE_PERIOD = 120
CONTESTED_DEBOUNCE_PERIOD = 120
CONTESTED_CAPTURE_POINTS_THRESHOLD = 0.1

class PlayerMission(object):
    PlayerMissionData = namedtuple(b'PlayerMissionData', (b'objectiveType', b'objectiveID', b'missionText', b'subText'))

    def __init__(self):
        self.missionType = EPIC_CONSTS.PRIMARY_EMPTY_MISSION
        self.missionText = b''
        self.subText = b''
        self.id = -1
        return

    def generateData(self):
        return {b'objectiveType': (self.missionType), 
           b'objectiveID': (self.id), 
           b'missionText': (i18n.makeString(self.missionText)), 
           b'subText': (self.subText)}

    def isEmptyMission(self):
        return self.missionType == EPIC_CONSTS.PRIMARY_EMPTY_MISSION

    def isObjectivesMission(self):
        return self.missionType == EPIC_CONSTS.PRIMARY_HQ_MISSION

    def isBaseMission(self):
        return self.missionType == EPIC_CONSTS.PRIMARY_BASE_MISSION


MissionTriggerArgs = namedtuple(b'MissionTriggerArgs', (b'forceMissionUpdate', b'callback'))

class EpicMissionsController(IViewComponentsController):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)
    EMPTY_SUB_TITLE_TEXT = b''

    def __init__(self, setup):
        super(EpicMissionsController, self).__init__()
        self.__sessionProvider = setup.sessionProvider
        self.__ready = False
        self.__ui = None
        self.__currentMission = PlayerMission()
        self.__activeMissionData = {b'lane': 0, 
           b'bases': 0, 
           b'hqActive': False, 
           b'destroyedHQs': 0, 
           b'endTime': (-1), 
           b'sectorGroup': 0, 
           b'isInHQSector': False}
        self.__numDestructiblesToDestroy = None
        self.__currentEndTime = 0
        self.__currentLane = 0
        self.__nearestObjective = -1
        self.__nearestObjectiveDistance = -1
        self.__objMsgSent = False
        self.__overtimeCB = None
        self.__overTimeEnd = None
        self.__isRegisterEpicMissionPanel = False
        self.__missionPanelDelayQueue = set()
        self.__orderBattleAbilities = []
        self.__isLaneContested = [
         False, False, False]
        self.__contestedEndTime = [
         0, 0, 0]
        self.__lastTimeHQDamaged = defaultdict((lambda : 0))
        self.__retreatMissionResults = {}
        self.__activeMessages = [
         0] * (max(EPIC_NOTIFICATION.ALL()) + 1)
        self.__eManager = Event.EventManager()
        self.__capturedBases = set()
        self.onPlayerMissionUpdated = Event.Event(self.__eManager)
        self.onPlayerMissionReset = Event.Event(self.__eManager)
        self.onPlayerMissionTimerSet = Event.Event(self.__eManager)
        self.onNearestObjectiveChanged = Event.Event(self.__eManager)
        self.onObjectiveBattleStarted = Event.Event(self.__eManager)
        self.onIngameMessageReady = Event.Event(self.__eManager)
        self._notificationTypeToMissionTriggerArgs = {(EPIC_NOTIFICATION.ZONE_CAPTURED): (MissionTriggerArgs(forceMissionUpdate=True, callback=(lambda : self.__setNearestObjective() if self.__activeMissionData[b'bases'] == 0 else None))), 
           (EPIC_NOTIFICATION.HQ_ACTIVE): (MissionTriggerArgs(forceMissionUpdate=True, callback=self.__setNearestObjective)), 
           (EPIC_NOTIFICATION.BASE_ACTIVE): (MissionTriggerArgs(forceMissionUpdate=True, callback=None)), 
           (EPIC_NOTIFICATION.HQ_DESTROYED): (MissionTriggerArgs(forceMissionUpdate=False, callback=None)), 
           (EPIC_NOTIFICATION.RETREAT): (MissionTriggerArgs(forceMissionUpdate=False, callback=None))}
        return

    def epicMissionPanelDelayQueue(self, value):
        self.__isRegisterEpicMissionPanel = value
        if value:
            while self.__missionPanelDelayQueue:
                mission, additionalDescription = self.__missionPanelDelayQueue.pop()
                self.onPlayerMissionUpdated(mission, additionalDescription)

        else:
            self.__missionPanelDelayQueue.clear()
        return

    @staticmethod
    def isVehicleAliveAndStarted():
        vehicle = BigWorld.entities.get(BigWorld.player().playerVehicleID)
        return vehicle is not None and vehicle.isStarted and vehicle.isAlive()

    def setViewComponents(self, *components):
        self.__ui = components[0]
        ctrl = self.__sessionProvider.dynamic.gameNotifications
        ctrl.onGameNotificationRecieved += self.__onGameNotificationRecieved
        self.__ui.start()
        return

    def clearViewComponents(self):
        self.__ui = None
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.EPIC_MISSIONS

    def startControl(self):
        self.__numDestructiblesToDestroy = avatar_getter.getArena().arenaType.numDestructiblesToDestroyForWin
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        if sectorBaseComp is None:
            LOG_ERROR(b'Expected SectorBaseComponent not present!')
            return
        else:
            playerDataComp = getattr(componentSystem, b'playerDataComponent', None)
            if playerDataComp is None:
                LOG_ERROR(b'Expected PlayerDataComponent not present!')
                return
            destructibleEntityComp = getattr(componentSystem, b'destructibleEntityComponent', None)
            if destructibleEntityComp is None:
                LOG_ERROR(b'Expected DestructibleEntityComponent not present!')
                return
            sectorComp = getattr(componentSystem, b'sectorComponent', None)
            if sectorComp is None:
                LOG_ERROR(b'Expected SectorComponent not present!')
                return
            overTimeComp = getattr(componentSystem, b'overtimeComponent', None)
            if overTimeComp is None:
                LOG_ERROR(b'Expected OvertimeComponent not present!')
                return
            sectorBaseComp.onSectorBaseActiveStateChanged += self.__onSectorBaseActiveStateChanged
            sectorBaseComp.onSectorBasePointsUpdate += self.__onSectorBasePointsUpdate
            playerDataComp.onPlayerPhysicalLaneUpdated += self.__onPlayerPhysicalLaneUpdated
            destructibleEntityComp.onDestructibleEntityHealthChanged += self.__onDestructibleEntityHealthChanged
            destructibleEntityComp.onDestructibleEntityIsActiveChanged += self.__onDestructibleEntityIsActiveChanged
            sectorComp.onWaypointsForPlayerActivated += self.__onWaypointsForPlayerActivated
            sectorComp.onPlayerSectorGroupChanged += self.__onPlayerSectorGroupChanged
            sectorComp.onSectorTransitionTimeChanged += self.__onSectorTransitionTimeChanged
            playerDataComp.onCrewRolesFactorUpdated += self.__onCrewRoleFactorAndRankUpdate
            playerDataComp.onPlayerRankUpdated += self.__onPlayerRankUpdated
            overTimeComp.onOvertimeStart += self.__onOvertimeStart
            overTimeComp.onOvertimeOver += self.__onOvertimeOver
            hqs = destructibleEntityComp.destructibleEntities
            if hqs:
                firstHQ = first(hqs.values())
                self.__activeMissionData[b'hqActive'] = firstHQ.isActive
                self.__objMsgSent = firstHQ.isActive
            arena = self.__sessionProvider.arenaVisitor.getArenaSubscription()
            if arena is not None:
                arena.onPositionsUpdated += self.__updatePositions
            eqCtrl = self.__sessionProvider.shared.equipments
            if eqCtrl is not None:
                eqCtrl.onEquipmentAdded += self.__onEquipmentAdded
                eqCtrl.onEquipmentReset += self.__onEquipmentReset
                eqCtrl.onEquipmentsCleared += self.__onEquipmentsCleared
            if BattleReplay.g_replayCtrl.isPlaying:
                g_replayEvents.onTimeWarpStart += self.__onReplayTimeWarpStart
                g_replayEvents.onTimeWarpFinish += self.__onReplayTimeWarpFinished
            self.__capturedBases.clear()
            return

    def getUI(self):
        return self.__ui

    def stopControl(self):
        self.__eManager.clear()
        self.__eManager = None
        if self.__overtimeCB:
            BigWorld.cancelCallback(self.__overtimeCB)
            self.__overtimeCB = None
            self.__overTimeEnd = None
        ctrl = self.__sessionProvider.dynamic.gameNotifications
        if ctrl:
            ctrl.onGameNotificationRecieved -= self.__onGameNotificationRecieved
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        if sectorBaseComp is not None:
            sectorBaseComp.onSectorBasePointsUpdate -= self.__onSectorBaseActiveStateChanged
            sectorBaseComp.onSectorBasePointsUpdate -= self.__onSectorBasePointsUpdate
        playerDataComp = getattr(componentSystem, b'playerDataComponent', None)
        if playerDataComp is not None:
            playerDataComp.onPlayerPhysicalLaneUpdated -= self.__onPlayerPhysicalLaneUpdated
            playerDataComp.onPlayerRankUpdated -= self.__onPlayerRankUpdated
            playerDataComp.onCrewRolesFactorUpdated -= self.__onCrewRoleFactorAndRankUpdate
        destructibleEntityComp = getattr(componentSystem, b'destructibleEntityComponent', None)
        if destructibleEntityComp is not None:
            destructibleEntityComp.onDestructibleEntityHealthChanged -= self.__onDestructibleEntityHealthChanged
            destructibleEntityComp.onDestructibleEntityHealthChanged -= self.__onDestructibleEntityIsActiveChanged
        sectorComp = getattr(componentSystem, b'sectorComponent', None)
        if sectorComp is not None:
            sectorComp.onWaypointsForPlayerActivated -= self.__onWaypointsForPlayerActivated
            sectorComp.onPlayerSectorGroupChanged -= self.__onPlayerSectorGroupChanged
            sectorComp.onSectorTransitionTimeChanged -= self.__onSectorTransitionTimeChanged
        component = getattr(componentSystem, b'overtimeComponent', None)
        if component is not None:
            component.onOvertimeStart -= self.__onOvertimeStart
            component.onOvertimeOver -= self.__onOvertimeOver
        if BattleReplay.g_replayCtrl.isPlaying:
            g_replayEvents.onTimeWarpStart -= self.__onReplayTimeWarpStart
            g_replayEvents.onTimeWarpFinish -= self.__onReplayTimeWarpFinished
        if self.__nearestObjective != -1:
            arena = self.__sessionProvider.arenaVisitor.getArenaSubscription()
            if arena is not None:
                arena.onPositionsUpdated -= self.__updatePositions
        eqCtrl = self.__sessionProvider.shared.equipments
        if eqCtrl is not None:
            eqCtrl.onEquipmentAdded -= self.__onEquipmentAdded
            eqCtrl.onEquipmentReset -= self.__onEquipmentReset
            eqCtrl.onEquipmentsCleared -= self.__onEquipmentsCleared
        self.__sessionProvider = None
        self._notificationTypeToMissionTriggerArgs.clear()
        return

    def getCurrentMission(self):
        return self.__currentMission

    def getNearestObjectiveData(self):
        return (
         self.__nearestObjective, self.__nearestObjectiveDistance)

    def getRankUpdateData(self, newRank):
        if not self.__orderBattleAbilities:
            return (None, None)
        else:
            arena = self.__sessionProvider.arenaVisitor.getArenaSubscription()
            vehicle = self.__sessionProvider.shared.vehicleState.getControllingVehicle()
            vehClass = getVehicleClassFromVehicleType(vehicle.typeDescriptor.type)
            if arena is None:
                return (None, None)
            inBattleReserves = arena.settings.get(b'epic_config', {}).get(b'epicMetaGame', {}).get(b'inBattleReservesByRank')
            if not inBattleReserves:
                return (None, None)
            if newRank not in range(0, len(inBattleReserves[b'slotActions'][vehClass])):
                return (None, None)
            updateData = inBattleReserves[b'slotActions'][vehClass]
            updateList = inBattleReserves[b'slotActions'][vehClass][newRank]
            if updateList:
                firstSlot = updateList[0]
                firstUnlocked = next((i for i, x in enumerate(updateData) if firstSlot in x), 0) == newRank
                return (
                 firstUnlocked, self.__orderBattleAbilities[firstSlot])
            return (None, None)

    def __isAttacker(self):
        return avatar_getter.getPlayerTeam() == EPIC_BATTLE_TEAM_ID.TEAM_ATTACKER

    def __onReady(self):
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        sectorComp = getattr(componentSystem, b'sectorComponent', None)
        if sectorBaseComp is not None and sectorComp is not None:
            for sectorBase in sectorBaseComp.sectorBases:
                if sectorBase.isCaptured:
                    sector = sectorComp.getSectorById(sectorBase.sectorID)
                    if sector.state not in (SECTOR_STATE.TRANSITION, SECTOR_STATE.BOMBING) or self.__currentLane == sector.playerGroup and not self.__isInRetreatArea():
                        self.__retreatMissionResults[sector.groupID] = False

        else:
            LOG_ERROR(b'Expected SectorComponent and/or SectorBaseComponent not present!')
        if not self.__isWaitingForNotification():
            self.__invalidateMissionStatus()
        periodCtrl = self.__sessionProvider.shared.arenaPeriod
        for m, s in TIMER_WARNINGS:
            periodCtrl.addRemainingTimeNotification(m, s, self.__onSpecificTimeReached)

        return

    def __onGameNotificationRecieved(self, notificationType, data):
        if len(self.__activeMessages) > notificationType:
            self.__activeMessages[notificationType] -= 1
            verify(not any(count < 0 for count in self.__activeMessages))
        missionTriggerArgs = self._notificationTypeToMissionTriggerArgs.get(notificationType, None)
        if missionTriggerArgs and not any(self.__activeMessages[notificationId] != 0 for notificationId in self._notificationTypeToMissionTriggerArgs):
            self.__invalidateMissionStatus(force=missionTriggerArgs.forceMissionUpdate)
            if missionTriggerArgs.callback is not None:
                missionTriggerArgs.callback()
        if notificationType == EPIC_NOTIFICATION.HQ_BATTLE_START:
            self.onObjectiveBattleStarted()
        return

    def __onBeforeMissionInvalidation(self):
        if self.__currentMission.missionType == EPIC_CONSTS.PRIMARY_WAYPOINT_MISSION:
            if self.isVehicleAliveAndStarted() and self.__activeMissionData[b'lane'] == self.__currentLane:
                if not self.__isInRetreatArea() and self.__retreatMissionResults.get(self.__activeMissionData[b'sectorGroup'], None) is None:
                    self.__retreatMissionResults[self.__activeMissionData[b'sectorGroup']] = True
                    LOG_DEBUG(b'[MissionsCtrl] Retreat Successful!')
                    self.__sendNotification(GAME_MESSAGES_CONSTS.RETREAT_SUCCESSFUL)
            else:
                self.__retreatMissionResults[self.__activeMissionData[b'sectorGroup']] = False
        return

    def __onSectorBasePointsUpdate(self, baseId, isPlayerTeam, points, capturingStopped, invadersCount, expectedCaptureTime):
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        if sectorBaseComp is None:
            LOG_ERROR(b'Expected SectorBaseComponent not present!')
            return
        else:
            sectorComp = getattr(componentSystem, b'sectorComponent', None)
            if sectorComp is None:
                LOG_ERROR(b'Expected SectorComponent not present!')
                return
            baseLane = sectorBaseComp.getSectorForSectorBase(baseId).playerGroup
            baseLaneIdx = baseLane - 1
            sectorIdToCapture = sectorComp.playerGroups[baseLane].sectors[sectorBaseComp.getNumCapturedBasesByLane(baseLane) + 1]
            validBase = sectorBaseComp.getBaseBySectorId(sectorIdToCapture)
            onPlayerLane = baseLaneIdx == self.__currentLane - 1
            time = BigWorld.serverTime()
            if validBase and baseId == validBase.baseID and points and baseId not in self.__capturedBases:
                if self.__isLaneContested[baseLaneIdx]:
                    endTime = self.__contestedEndTime[baseLaneIdx]
                    if endTime < time:
                        self.__isLaneContested[baseLaneIdx] = False
                    else:
                        self.__contestedEndTime[baseLaneIdx] = time + CONTESTED_DEBOUNCE_PERIOD
                elif points >= CONTESTED_CAPTURE_POINTS_THRESHOLD:
                    self.__contestedEndTime[baseLaneIdx] = time + CONTESTED_DEBOUNCE_PERIOD
                    self.__isLaneContested[baseLaneIdx] = True
                    if not onPlayerLane:
                        self.__showBaseContestedMessage(points, baseId)
            return

    def __showBaseContestedMessage(self, points, baseId):
        self.__sendIngameMessage(self.__makeMessageData(GAME_MESSAGES_CONSTS.BASE_CONTESTED_POSITIVE if self.__isAttacker() else GAME_MESSAGES_CONSTS.BASE_CONTESTED, {b'baseID': baseId, 
           b'title': (EPIC_BATTLE.BASE_CONTESTED_ATK if self.__isAttacker() else EPIC_BATTLE.BASE_CONTESTED_DEF), 
           b'progress': points}))
        return

    def __onPlayerPhysicalLaneUpdated(self, laneID):
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        if not self.__ready:
            sectorComp = getattr(componentSystem, b'sectorComponent', None)
            if sectorComp is None:
                LOG_ERROR(b'Expected SectorComponent not present!')
                return
            self.__ready = sectorComp.currentPlayerSectorId is not None
            self.__currentLane = laneID
            if self.__ready:
                self.__onReady()
        invalidateMission = False
        if laneID != self.__currentLane:
            self.__currentLane = laneID
            invalidateMission = True
        if not invalidateMission:
            playerDataComp = getattr(componentSystem, b'playerDataComponent', None)
            if playerDataComp is None:
                LOG_ERROR(b'Expected PlayerDataComponent not present!')
                return
            invalidateMission = playerDataComp.getPlayerInHQSector() != self.__activeMissionData[b'isInHQSector']
        if invalidateMission and not self.__isWaitingForNotification():
            self.__invalidateMissionStatus()
        return

    def __invalidateMissionStatus(self, force=False):
        self.__onBeforeMissionInvalidation()
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        if sectorBaseComp is None:
            LOG_ERROR(b'Expected SectorBaseComponent not present!')
            return
        else:
            destructibleEntityComp = getattr(componentSystem, b'destructibleEntityComponent', None)
            if destructibleEntityComp is None:
                LOG_ERROR(b'Expected DestructibleEntityComponent not present!')
                return
            sectorComp = getattr(componentSystem, b'sectorComponent', None)
            if sectorComp is None:
                LOG_ERROR(b'Expected SectorComponent not present!')
                return
            playerDataComp = getattr(componentSystem, b'playerDataComponent', None)
            if destructibleEntityComp is None:
                LOG_ERROR(b'Expected PlayerDataComponent not present!')
                return
            laneID = self.__currentLane
            nonCapturedBases = sectorBaseComp.getNumNonCapturedBasesByLane(laneID)
            baseID = next(iter(sectorBaseComp.getCapturedSectorBaseIdsByLane(laneID)[-1:]), None)
            sectorGroupID = sectorBaseComp.getSectorForSectorBase(baseID).groupID if baseID else None
            hqActive = False
            destroyedHQs = 0
            hqs = destructibleEntityComp.destructibleEntities
            if hqs:
                hqActive = first(hqs.values()).isActive
                destroyedHQs = destructibleEntityComp.getNumDestroyedEntities()
                if destroyedHQs >= self.__numDestructiblesToDestroy:
                    return
            if nonCapturedBases == 0 and self.__isAttacker():
                if hqActive:
                    endTime = 0
                else:
                    criticalEndTimes = []
                    sector = sectorComp.getSectorById(playerDataComp.hqSectorID)
                    if sector is not None:
                        hqIdInPlayerGroup = sector.IDInPlayerGroup
                        for sector in sectorComp.sectors:
                            if sector.state == SECTOR_STATE.TRANSITION and sector.IDInPlayerGroup == hqIdInPlayerGroup - 1:
                                criticalEndTimes.append(sector.endOfTransitionPeriod)

                    endTime = min(criticalEndTimes) if criticalEndTimes else 0
            else:
                _, _, endTime = sectorComp.getActiveWaypointSectorGroupForPlayerGroup(self.__currentLane)
            if endTime - BigWorld.serverTime() > 0.5 and self.__currentEndTime != endTime:
                self.__currentEndTime = endTime
                self.onPlayerMissionTimerSet(self.__currentEndTime)
            isInHQSector = playerDataComp.getPlayerInHQSector()
            if self.__activeMissionData[b'lane'] == laneID and self.__activeMissionData[b'bases'] == nonCapturedBases and self.__activeMissionData[b'hqActive'] == hqActive and self.__activeMissionData[b'destroyedHQs'] == destroyedHQs and self.__activeMissionData[b'endTime'] == endTime and self.__activeMissionData[b'sectorGroup'] == sectorGroupID and self.__activeMissionData[b'isInHQSector'] == isInHQSector and not force:
                return
            self.__activeMissionData[b'lane'] = laneID
            self.__activeMissionData[b'bases'] = nonCapturedBases
            self.__activeMissionData[b'hqActive'] = hqActive
            destroyedHQUpdate = self.__activeMissionData[b'destroyedHQs'] != destroyedHQs
            self.__activeMissionData[b'destroyedHQs'] = destroyedHQs
            self.__activeMissionData[b'endTime'] = endTime
            self.__activeMissionData[b'sectorGroup'] = sectorGroupID
            self.__activeMissionData[b'isInHQSector'] = isInHQSector
            mission, additionalDescription = self.__generateMissionFromData()
            if mission.missionType == EPIC_CONSTS.PRIMARY_HQ_MISSION and self.__currentMission.missionType == EPIC_CONSTS.PRIMARY_HQ_MISSION and not destroyedHQUpdate and not force:
                return
            if mission.missionType != EPIC_CONSTS.PRIMARY_EMPTY_MISSION:
                self.__currentMission = mission
                if self.__isRegisterEpicMissionPanel:
                    self.onPlayerMissionUpdated(mission, additionalDescription)
                else:
                    self.__missionPanelDelayQueue.add((mission, additionalDescription))
            return

    def __generateMissionFromData(self):
        mission = PlayerMission()
        additionalDescription = None
        hqActive = self.__activeMissionData[b'hqActive']
        isInHQSector = self.__activeMissionData[b'isInHQSector']
        sectorGroup = self.__activeMissionData[b'sectorGroup']
        nonCapturedBases = self.__activeMissionData[b'bases']
        endTime = self.__activeMissionData[b'endTime']
        if self.isVehicleAliveAndStarted() and not self.__isAttacker() and endTime - BigWorld.serverTime() > 0 and self.__isInRetreatArea() and self.__retreatMissionResults.get(sectorGroup, None) is None:
            mission.missionType = EPIC_CONSTS.PRIMARY_WAYPOINT_MISSION
            mission.missionText = EPIC_BATTLE.RETREAT_MISSION_TXT
            mission.subText = EPIC_BATTLE.MISSION_ZONE_CLOSING_DEF
        elif isInHQSector and hqActive or nonCapturedBases == 0:
            componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
            destructibleEntityComp = getattr(componentSystem, b'destructibleEntityComponent', None)
            if destructibleEntityComp is None:
                LOG_ERROR(b'Expected DestructibleEntityComponent not present!')
                return (None, None)
            mission.missionType = EPIC_CONSTS.PRIMARY_HQ_MISSION
            destroyed = destructibleEntityComp.getNumDestroyedEntities()
            toDestroy = self.__numDestructiblesToDestroy
            if endTime > 0 and not hqActive:
                mission.subText = EPIC_BATTLE.MISSION_ZONE_CLOSING_ATK if self.__isAttacker() else EPIC_BATTLE.MISSION_ZONE_CLOSING_DEF
            else:
                mission.subText = EPIC_BATTLE.MISSIONS_PRIMARY_ATK_HQ_SUB_TITLE if self.__isAttacker() else EPIC_BATTLE.MISSIONS_PRIMARY_DEF_HQ_SUB_TITLE
                additionalDescription = makeHtmlString(path=b'html_templates:battle/epicBattle/additionalHqMissionInfo', key=b'attacker' if self.__isAttacker() else b'defender', ctx={b'destroyed': destroyed, 
                   b'toDestroy': toDestroy})
            mission.missionText = EPIC_BATTLE.MISSIONS_PRIMARY_ATK_HQ if self.__isAttacker() else EPIC_BATTLE.MISSIONS_PRIMARY_DEF_HQ
            self.__updatePositions()
        elif endTime > 0:
            mission.subText = EPIC_BATTLE.MISSION_ZONE_CLOSING_ATK if self.__isAttacker() else EPIC_BATTLE.MISSION_ZONE_CLOSING_DEF
        mission.missionType = EPIC_CONSTS.PRIMARY_BASE_MISSION
        mission.missionText = EPIC_BATTLE.MISSIONS_PRIMARY_ATK_BASE if self.__isAttacker() else EPIC_BATTLE.MISSIONS_PRIMARY_DEF_BASE
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        if sectorBaseComp is not None:
            mission.id = next(iter(sectorBaseComp.getNonCapturedSectorBaseIdsByLane(self.__currentLane)), None)
        else:
            LOG_ERROR(b'Expected SectorBaseComponent not present!')
        return (mission, additionalDescription)

    def __onWaypointsForPlayerActivated(self, waypointSectorTimeTuple):
        _, _, currentEndTime = waypointSectorTimeTuple
        if currentEndTime == 0:
            self.__currentEndTime = currentEndTime
            self.onPlayerMissionTimerSet(self.__currentEndTime)
        if self.__isAttacker() and self.__ready:
            componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
            sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
            if sectorBaseComp is not None:
                nonCapturedBases = sectorBaseComp.getNumNonCapturedBasesByLane(self.__currentLane)
                if nonCapturedBases == 0:
                    self.__sendNotification(GAME_MESSAGES_CONSTS.DESTROY_OBJECTIVE)
            else:
                LOG_ERROR(b'Expected SectorBaseComponent not present!')
                return
        return

    def __onPlayerSectorGroupChanged(self, *_):
        if self.__currentMission.missionType == EPIC_CONSTS.PRIMARY_WAYPOINT_MISSION and self.__activeMissionData[b'lane'] == self.__currentLane and not self.__isInRetreatArea():
            self.__nextObjectiveMessage(self.__isAttacker())
        return

    def __onSectorTransitionTimeChanged(self, sectorId, oldTime, newTime):
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorComp = getattr(componentSystem, b'sectorComponent', None)
        if sectorComp is None:
            LOG_ERROR(b'Expected SectorComponent not present!')
            return
        else:
            if self.__currentMission.missionType == EPIC_CONSTS.PRIMARY_WAYPOINT_MISSION:
                baseSector = sectorComp.getSectorById(sectorId)
                if baseSector.playerGroup == self.__currentLane and self.__isInRetreatArea():
                    self.__nextObjectiveMessage(self.__isAttacker())
            return

    def onSectorBaseCaptured(self, baseId, vehiclesUnlocked=False):
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        if sectorBaseComp is None:
            LOG_ERROR(b'Expected SectorBaseComponent not present!')
            return
        else:
            sectorComp = getattr(componentSystem, b'sectorComponent', None)
            if sectorComp is None:
                LOG_ERROR(b'Expected SectorComponent not present!')
                return
            epicPlayerDataComp = getattr(componentSystem, b'playerDataComponent', None)
            if epicPlayerDataComp is None:
                LOG_ERROR(b'Expected EpicPlayerDataComponent not present!')
                return
            self.__capturedBases.add(baseId)
            sectorBase = sectorBaseComp.getSectorBaseById(baseId)
            baseSectorId = sectorBase.sectorID
            sector = sectorComp.getSectorById(baseSectorId)
            baseLane = sector.playerGroup
            onPlayerLane = baseLane == self.__currentLane
            capturedBasesInCompanentSystem = sectorBaseComp.getCapturedBaseIDs()
            self.__capturedBases.update(capturedBasesInCompanentSystem)
            seconds = epicPlayerDataComp.getGameTimeToAddPerCapture(sector.IDInPlayerGroup)
            if len(self.__capturedBases) == len(sectorBaseComp.sectorBases):
                seconds += epicPlayerDataComp.getGameTimeToAddWhenAllCaptured()
            minutes = int(seconds / 60)
            seconds -= minutes * 60
            self.__sendIngameMessage(self.__makeMessageData(GAME_MESSAGES_CONSTS.BASE_CAPTURED_POSITIVE if self.__isAttacker() else GAME_MESSAGES_CONSTS.BASE_CAPTURED, {b'baseID': baseId, 
               b'title': (EPIC_BATTLE.ZONE_CAPTURED_TEXT if self.__isAttacker() else EPIC_BATTLE.ZONE_LOST_TEXT), 
               b'timerText': (backport.text(R.strings.epic_battle.zone.time_added(), minutes=(b':').join(((b'{:02d}').format(int(minutes)), (b'{:02d}').format(int(seconds)))))), 
               b'descriptionText': (backport.text(R.strings.epic_battle.missions.unlockTankLevel()) if vehiclesUnlocked else b'')}))
            if onPlayerLane:
                if self.__isAttacker():
                    self.__nextObjectiveMessage(self.__isAttacker())
                elif self.isVehicleAliveAndStarted() and sectorComp.getSectorById(sectorComp.currentPlayerSectorId).IDInPlayerGroup <= sector.IDInPlayerGroup:
                    self.__sendIngameMessage(self.__makeMessageData(GAME_MESSAGES_CONSTS.RETREAT, {b'title': (EPIC_BATTLE.ZONE_LEAVE_ZONE)}))
                else:
                    self.__nextObjectiveMessage(self.__isAttacker())
            self.__contestedEndTime[baseLane - 1] = 0
            self.__isLaneContested[baseLane - 1] = False
            return

    def __nextObjectiveMessage(self, isAttacker):
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        if sectorBaseComp is None:
            LOG_ERROR(b'Expected SectorBaseComponent not present!')
            return
        else:
            nonCapturedBases = sectorBaseComp.getNumNonCapturedBasesByLane(self.__currentLane)
            if nonCapturedBases == 0:
                msgType = GAME_MESSAGES_CONSTS.DESTROY_OBJECTIVE if isAttacker else GAME_MESSAGES_CONSTS.DEFEND_OBJECTIVE
            else:
                msgType = GAME_MESSAGES_CONSTS.CAPTURE_BASE if isAttacker else GAME_MESSAGES_CONSTS.DEFEND_BASE
            ctrl = self.__sessionProvider.dynamic.gameNotifications
            if ctrl is not None:
                notificationId = ctrl.translateMsgId(msgType)
                if notificationId != -1 and self.__activeMessages[notificationId] != 0:
                    return
            self.__sendNotification(msgType)
            return

    def __onSectorBaseActiveStateChanged(self, baseId, isActive):
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        if sectorBaseComp is None:
            LOG_ERROR(b'Expected SectorBaseComponent not present!')
            return
        else:
            baseSector = sectorBaseComp.getSectorForSectorBase(baseId)
            if not isActive or baseSector.IDInPlayerGroup > 2:
                return
            onPlayerLane = baseSector.playerGroup == self.__currentLane
            if onPlayerLane:
                self.__sendNotification(GAME_MESSAGES_CONSTS.CAPTURE_BASE if self.__isAttacker() else GAME_MESSAGES_CONSTS.DEFEND_BASE)
            return

    def __onDestructibleEntityIsActiveChanged(self, destructibleEntityID, isActive):
        if not isActive or self.__objMsgSent:
            return
        self.__sendNotification(GAME_MESSAGES_CONSTS.HQ_BATTLE_STARTED_POSITIVE if self.__isAttacker() else GAME_MESSAGES_CONSTS.HQ_BATTLE_STARTED)
        self.__objMsgSent = True
        return

    def __onDestructibleEntityHealthChanged(self, objID, newHealth, maxHealth, attackerID, attackReason, hitFlags):
        if newHealth == 0:
            msgType = GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED_POSITIVE if self.__isAttacker() else GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED
            msgData = {b'hqID': objID, 
               b'title': (EPIC_BATTLE.ZONE_DESTROYED_TEXT if self.__isAttacker() else EPIC_BATTLE.ZONE_LOST_TEXT)}
        elif self.__lastTimeHQDamaged[objID] + CONTESTED_DEBOUNCE_PERIOD <= BigWorld.serverTime():
            self.__lastTimeHQDamaged[objID] = BigWorld.serverTime()
            msgType = GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK_POSITIVE if self.__isAttacker() else GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK
            msgData = {b'hqID': objID, 
               b'title': (EPIC_BATTLE.HQ_UNDER_ATTACK_ATK if self.__isAttacker() else EPIC_BATTLE.HQ_UNDER_ATTACK_DEF), 
               b'destroyedProgress': (newHealth / maxHealth)}
        else:
            return
        self.__sendIngameMessage(self.__makeMessageData(msgType, msgData))
        return

    def __updatePositions(self):
        if self.__currentMission.missionType == EPIC_CONSTS.PRIMARY_HQ_MISSION or self.__activeMissionData[b'hqActive']:
            self.__setNearestObjective()
        return

    def __setNearestObjective(self):
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        destructibleEntityComp = getattr(componentSystem, b'destructibleEntityComponent', None)
        if destructibleEntityComp is None:
            LOG_ERROR(b'Expected DestructibleEntityComponent not present!')
            return
        else:
            position = BigWorld.player().position
            objID, objDistance = destructibleEntityComp.getNearestDestructibleEntityID(position)
            if objID is None:
                return
            self.__nearestObjectiveDistance = objDistance
            if objID == self.__nearestObjective:
                return
            self.__nearestObjective = objID
            self.onNearestObjectiveChanged(objID, objDistance)
            return

    def __onSpecificTimeReached(self, minutes, seconds):
        self.__sendIngameMessage(self.__makeMessageData(GAME_MESSAGES_CONSTS.TIME_REMAINING if self.__isAttacker() else GAME_MESSAGES_CONSTS.TIME_REMAINING_POSITIVE, {b'title': (i18n.makeString(EPIC_BATTLE.ZONE_TIME_LEFT, minutes=minutes))}))
        return

    def __onCrewRoleFactorAndRankUpdate(self, newFactor, allyVehID, allyNewRank):
        if not allyVehID and not allyNewRank:
            return
        arena = self.__sessionProvider.arenaVisitor.getArenaSubscription()
        crewRoleFactorConf = arena.settings.get(b'epic_config', {}).get(b'epicMetaGame', {}).get(b'inBattleModifiers').get(b'CrewRoleFactor')
        if BigWorld.player().playerVehicleID == allyVehID:
            factor = crewRoleFactorConf.get(b'ranks', {}).get(allyNewRank + 1, 0)
            self.__onPlayerRankUpdated(allyNewRank, factor)
            return
        maxImpact = crewRoleFactorConf.get(b'maxImpact', 0.0)
        if newFactor < maxImpact:
            subTitleAddition = i18n.makeString(EPIC_BATTLE.RANK_CREWROLESFACTORPROMOTION, percent=newFactor)
        else:
            subTitleAddition = i18n.makeString(EPIC_BATTLE.RANK_CREWROLESFACTORPROMOTION1, percent=maxImpact)
        subTitle = i18n.makeString(EPIC_BATTLE.RANK_PROMOTION, rank=i18n.makeString(RANK_TO_TRANSLATION[allyNewRank + 1]), placeholder=b'\n' + subTitleAddition)
        self.__sendIngameMessage(self.__makeMessageData(GAME_MESSAGES_CONSTS.GENERAL_RANK_REACHED, {b'title': (self.__sessionProvider.getCtx().getPlayerFullName(vID=allyVehID, showVehShortName=False, showClan=True, showRegion=False)), 
           b'subTitle': subTitle}))
        return

    def __onPlayerRankUpdated(self, rank, crewRoleFactor=0.0):
        subTitleText = self.EMPTY_SUB_TITLE_TEXT
        rankIdx = rank + 1
        rRank = R.strings.epic_battle.rank
        arenaDP = self.__sessionProvider.getArenaDP()
        if arenaDP and arenaDP.getReservesModifier() == FLBattleReservesModifier.RANDOM:
            subTitleText = backport.text(rRank.slotUnlocked(), slotNumber=backport.text(rRank.dyn((b'slot_{}').format(rankIdx))())) if rankIdx in [PLAYER_RANK.SERGEANT, PLAYER_RANK.LIEUTENANT] else backport.text(rRank.allReserveUpgraded()) if rankIdx != PLAYER_RANK.GENERAL else self.EMPTY_SUB_TITLE_TEXT
        else:
            firstUnlocked, updateInfo = self.getRankUpdateData(rank)
            eqCtrl = self.__sessionProvider.shared.equipments
            if firstUnlocked is not None and eqCtrl is not None and eqCtrl.hasEquipment(updateInfo):
                equipmentName = eqCtrl.getEquipment(updateInfo).getDescriptor().userString
                subTitleText = backport.text(rRank.recerveUnlocked() if firstUnlocked else rRank.reserveUpgraded(), reserveName=equipmentName)
            if rankIdx in self.__epicController.getLevelsToUpgradeAllReserves():
                if subTitleText:
                    subTitleText += b'\n'
                subTitleText += backport.text(rRank.allReserveUpgraded())
        if crewRoleFactor > 0:
            if subTitleText:
                subTitleText += b'\n'
            subTitleText += i18n.makeString(EPIC_BATTLE.RANK_CREWROLESFACTORSELF, percent=crewRoleFactor)
        self.__sendIngameMessage(self.__makeMessageData(GAME_MESSAGES_CONSTS.RANK_UP, {b'rank': rankIdx, 
           b'title': (RANK_TO_TRANSLATION[rankIdx]), 
           b'subTitle': subTitleText}))
        return

    def __onOvertimeStart(self, endTime):
        self.__overTimeEnd = endTime
        timeLeft = int(endTime - BigWorld.serverTime())
        self.__sendIngameMessage(self.__makeMessageData(GAME_MESSAGES_CONSTS.OVERTIME, {b'timestamp': timeLeft, 
           b'title': (EPIC_BATTLE.OVERTIME_LABEL)}))
        self.__overtimeCB = BigWorld.callback(1, self.__overtimeTick)
        return

    def __onOvertimeOver(self):
        if self.__overtimeCB:
            BigWorld.cancelCallback(self.__overtimeCB)
            self.__overtimeCB = None
            self.__overTimeEnd = None
        return

    def __overtimeTick(self):
        timeLeft = int(self.__overTimeEnd - BigWorld.serverTime())
        if timeLeft in OVERTIME_DURATION_WARNINGS:
            self.__sendIngameMessage(self.__makeMessageData(GAME_MESSAGES_CONSTS.OVERTIME, {b'timestamp': timeLeft, 
               b'title': (EPIC_BATTLE.OVERTIME_LABEL)}))
        if timeLeft > 0:
            self.__overtimeCB = BigWorld.callback(1, self.__overtimeTick)
        else:
            self.__overtimeCB = None
        return

    def __makeMessageData(self, msgType, data):
        return PlayerMessageData(messageType=str(msgType), length=MSG_ID_TO_DURATION[msgType], priority=MSG_ID_TO_PRIORITY[msgType], msgData=data)

    def __sendNotification(self, messageType):
        ctrl = self.__sessionProvider.dynamic.gameNotifications
        if ctrl is not None:
            notificationId = ctrl.translateMsgId(messageType)
            if notificationId != -1:
                self.__activeMessages[notificationId] += 1
            ctrl.notify(messageType, {})
        return

    def __sendIngameMessage(self, msgData):
        ctrl = self.__sessionProvider.dynamic.gameNotifications
        if ctrl is not None:
            notificationId = ctrl.translateMsgId(msgData.messageType)
            if notificationId != -1:
                self.__activeMessages[notificationId] += 1
            if not BattleReplay.g_replayCtrl.isTimeWarpInProgress and notificationId in self._notificationTypeToMissionTriggerArgs:
                self.__resetMission()
        self.onIngameMessageReady(msgData)
        return

    def __isWaitingForNotification(self):
        return any(self.__activeMessages[notificationId] > 0 for notificationId in self._notificationTypeToMissionTriggerArgs)

    def __onReplayTimeWarpStart(self):
        self.__resetMission()
        return

    def __onReplayTimeWarpFinished(self):
        self.__invalidateMissionStatus(force=True)
        return

    def __resetMission(self):
        self.onPlayerMissionReset()
        return

    def __isInRetreatArea(self):
        componentSystem = self.__sessionProvider.arenaVisitor.getComponentSystem()
        sectorBaseComp = getattr(componentSystem, b'sectorBaseComponent', None)
        if sectorBaseComp is None:
            LOG_ERROR(b'Expected SectorBaseComponent not present!')
            return False
        else:
            baseID = next(iter(sectorBaseComp.getCapturedSectorBaseIdsByLane(self.__currentLane)[-1:]), None)
            if baseID:
                sectorComp = getattr(componentSystem, b'sectorComponent', None)
                if sectorComp is None:
                    LOG_ERROR(b'Expected SectorComponent not present!')
                    return False
                lastCapturedBaseSector = sectorBaseComp.getSectorForSectorBase(baseID)
                currentIDInPlayerGroup = sectorComp.getSectorById(sectorComp.currentPlayerSectorId).IDInPlayerGroup
                return currentIDInPlayerGroup <= lastCapturedBaseSector.IDInPlayerGroup
            return False

    def __onEquipmentAdded(self, intCD, item):
        if item and item.isAvatar():
            self.__orderBattleAbilities.append(intCD)
        return

    def __onEquipmentReset(self, oldIntCD, newIntCD, _):
        if oldIntCD in self.__orderBattleAbilities:
            self.__orderBattleAbilities[self.__orderBattleAbilities.index(oldIntCD)] = newIntCD
        return

    def __onEquipmentsCleared(self):
        self.__orderBattleAbilities = []
        return
