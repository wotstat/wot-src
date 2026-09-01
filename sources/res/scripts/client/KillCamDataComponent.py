from __future__ import absolute_import, division
import logging, BigWorld, CGF, Math
from GenericComponents import Sequence, StateSwitcherComponent
from cgf_components_common.vehicle_components import VehicleSequenceParamsAttachedComponent
from avatar_components.avatar_postmortem_component import SimulatedVehicleType
from constants import KILL_CAM_STATUS_CODE, BATTLE_LOG_SHELL_TYPES
from gun_rotation_shared import decodeGunAngles
from items.vehicles import getItemByCompactDescr
from AvatarInputHandler.kill_cam_mode_helpers.kill_cam_helpers import calculateSPGTrajectory
from vehicles.mechanics.mechanic_constants import VehicleMechanic
from shared_utils import first
_logger = logging.getLogger(__name__)
_UNSPOTTED_PIVOT_DISTANCE_FACTOR = 12
_UNSPOTTED_MARKER_DISTANCE_FACTOR = 4
_MECHANICS_WITH_DYN_ATTACHMENTS = (
 VehicleMechanic.STATIONARY_RELOAD,)

class KillCamDataComponent(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(KillCamDataComponent, self).__init__()
        self.processedData = None
        return

    @property
    def __killerIsSpotted(self):
        return self.processedData[b'attacker'] and self.processedData[b'attacker'][b'spotted']

    @property
    def __isRicochet(self):
        return self.processedData[b'projectile'][b'ricochetCount'] > 0

    def set_capturedKillCamData(self, _=None):
        self.__updateSimulationData()
        return

    def getSimulationData(self):
        self.__updateLateAttackerData()
        if self.processedData is not None and self.processedData.get(b'trajectoryData') is None:
            self.processedData[b'trajectoryData'], self.processedData[b'unspottedOrigin'] = self.__setupTrajectory()
        return self.processedData

    def __updateSimulationData(self):
        statusCode = self.capturedKillCamData[b'statusCode']
        if statusCode != KILL_CAM_STATUS_CODE.SUCCESS:
            _logger.debug(b'Data from server were not received, error reason %s', KILL_CAM_STATUS_CODE(statusCode).name)
            return
        avatar = BigWorld.player()
        vehicles = avatar.vehicles
        self.__captureKillCamSimulationData(vehicles, avatar.playerVehicleID)
        return

    def __captureKillCamSimulationData(self, vehicles, playerID):
        playerData = self.__captureVehSimulationData(BigWorld.entity(playerID))
        if not playerData:
            return
        serverKillCamData = self.capturedKillCamData
        attackerID = serverKillCamData[b'attacker'][b'attackerID']
        playerServerData = serverKillCamData[b'victim']
        playerData.update(playerServerData)
        playerData[b'simulationType'] = SimulatedVehicleType.PLAYER
        playerData[b'damageStickers'] = list(playerData.get(b'damageStickers', []))
        projectileData = {}
        projectileData.update(serverKillCamData[b'projectile'][b'unspottedData'])
        shellData = self.__unpackShellData(projectileData[b'shellCompDescr'])
        projectileData.update(shellData)
        projectileDataSpotted = serverKillCamData[b'projectile'][b'spottedData']
        if projectileDataSpotted:
            projectileData.update(projectileDataSpotted)
        self.processedData = {b'attacker': (self.__getAttackerData()), 
           b'player': playerData, 
           b'projectile': projectileData, 
           b'others': (self.__collectOtherVehiclesForKillCam(vehicles, attackerID, playerID)), 
           b'time': (BigWorld.time())}
        return

    def __getAttackerData(self):
        serverKillCamData = self.capturedKillCamData
        attackerID = serverKillCamData[b'attacker'][b'attackerID']
        attackerData = self.__captureVehSimulationData(BigWorld.entity(attackerID))
        if attackerData is None:
            attackerData = self.__captureUnspottedVehSimulationData(attackerID)
        attackerServerData = serverKillCamData[b'attacker'][b'spottedData']
        attackerData[b'hasSpottedData'] = attackerServerData is not None
        if attackerServerData:
            attackerData.update(attackerServerData)
        attackerServerData = serverKillCamData[b'attacker'][b'unspottedData']
        if attackerServerData:
            attackerData.update(attackerServerData)
        attackerServerData = serverKillCamData[b'attacker'][b'mechanicsInfo']
        if attackerServerData:
            attackerData.update({b'mechanicsInfo': attackerServerData})
        attackerData[b'simulationType'] = SimulatedVehicleType.ATTACKER
        return attackerData

    def __updateLateAttackerData(self):
        if not self.processedData:
            return
        attackerData = self.processedData[b'attacker']
        if attackerData[b'spotted']:
            return
        if not attackerData[b'hasSpottedData']:
            return
        self.processedData[b'attacker'] = self.__getAttackerData()
        return

    def __collectOtherVehiclesForKillCam(self, vehicles, attackerID, playerID):
        return [self.__captureVehSimulationData(veh) for veh in vehicles if veh.id not in (attackerID, playerID) and not veh.isDestroyed and veh.isStarted]

    def __captureVehSimulationData(self, vehicle):
        if vehicle is None or vehicle.isDestroyed or not vehicle.isStarted:
            return
        matrix = Math.Matrix(vehicle.matrix)
        return {b'vehicleID': (vehicle.id), 
           b'position': (matrix.translation.tuple()), 
           b'dynAttachmentsInfo': (self.__getDynAttachmentsInfo(vehicle)), 
           b'rotation': (
                       matrix.roll, matrix.pitch, matrix.yaw), 
           b'health': (vehicle.health), 
           b'gunAngles': (self.__getGunAngles(vehicle)), 
           b'turretAndGunSpeed': (self.__getTurretAndGunSpeed(vehicle)), 
           b'burnoutLevel': (vehicle.burnoutLevel), 
           b'simulationType': (SimulatedVehicleType.VEHICLE), 
           b'damageStickers': (vehicle.damageStickers), 
           b'velocity': (vehicle.filter.velocity), 
           b'spotted': True, 
           b'publicInfo': (dict(vehicle.publicInfo)), 
           b'brokenTracks': (vehicle.appearance.getTrackStates()), 
           b'siegeState': (vehicle.siegeState), 
           b'wheelsState': (vehicle.appearance.wheelsState), 
           b'wheelsSteering': (vehicle.appearance.wheelsSteering), 
           b'trackInAir': (
                         vehicle.appearance.isLeftSideFlying, vehicle.appearance.isRightSideFlying)}

    def __captureUnspottedVehSimulationData(self, vehicleID):
        return {b'vehicleID': vehicleID, 
           b'position': (0, 0, 0), 
           b'dynAttachmentsInfo': [], b'rotation': (0, 0, 0), 
           b'health': 0, 
           b'gunAngles': (0, 0), 
           b'burnoutLevel': 0, 
           b'simulationType': (SimulatedVehicleType.VEHICLE), 
           b'damageStickers': (frozenset()), 
           b'velocity': 0, 
           b'spotted': False}

    def __getGunAngles(self, veh):
        if veh.typeDescriptor:
            turretYaw, gunPitch = decodeGunAngles(veh.gunAnglesPacked, veh.typeDescriptor.gun.pitchLimits[b'absolute'])
        else:
            turretYaw = gunPitch = 0.0
        return (
         turretYaw, gunPitch)

    def __getTurretAndGunSpeed(self, veh):
        if veh.typeDescriptor:
            turretVelocity = veh.typeDescriptor.turret.rotationSpeed
            gunVelocity = veh.typeDescriptor.gun.rotationSpeed
        else:
            turretVelocity = gunVelocity = 0.0
        return (
         turretVelocity, gunVelocity)

    def __getDynAttachmentsInfo(self, vehicle):
        parentGameObject = vehicle.entityGameObject
        result = CGF.findInHierarchyWithComponent(parentGameObject, VehicleSequenceParamsAttachedComponent)
        if not result:
            return
        else:
            if len(result) > 1:
                _logger.warning(b'Multiple VehicleDynamicPartAttachedComponent is not supported in death cam')
                return
            gameObject = first(result).object
            if not gameObject.valid:
                return
            sequence = gameObject.findRead(Sequence)
            stateSwitcher = gameObject.findRead(StateSwitcherComponent)
            if sequence is None or stateSwitcher is None:
                return
            return {b'activeSequenceLayer': (sequence.activeLayerIdx), b'sequenceTime': (sequence.time), 
               b'attachmentState': (stateSwitcher.getState())}

    def __unpackShellData(self, shellCompDescr):
        shellDescr = getItemByCompactDescr(shellCompDescr)
        return {b'shellType': (BATTLE_LOG_SHELL_TYPES.getShellType(shellDescr)), 
           b'shellKind': (shellDescr.kind), 
           b'shellIcon': (shellDescr.iconName), 
           b'shellCaliber': (shellDescr.caliber)}

    def __setupTrajectory(self):
        projectileData = self.processedData[b'projectile']
        projectileTrajectoryData = projectileData[b'trajectoryData']
        origin = Math.Vector3(projectileTrajectoryData[0][0])
        impactPoint = Math.Vector3(projectileData[b'impactPoint'])
        gravity = Math.Vector3(0.0, -projectileData[b'gravity'], 0.0)
        velocity = Math.Vector3(projectileData[b'velocity'])
        unspottedOrigin = None
        if not self.__killerIsSpotted:
            directionVector = origin - impactPoint
            directionVector *= 1.0 / directionVector.length
            unspottedOrigin = impactPoint + directionVector * _UNSPOTTED_MARKER_DISTANCE_FACTOR
            origin = impactPoint + directionVector * _UNSPOTTED_PIVOT_DISTANCE_FACTOR
        elif self.processedData[b'attacker'][b'vehicleType'] == b'SPG':
            trajectoryPoints = calculateSPGTrajectory(origin, impactPoint, velocity, gravity)
            if self.__killerIsSpotted:
                return (trajectoryPoints, unspottedOrigin)
            trajectoryEndVector = Math.Vector3(trajectoryPoints[-1] - trajectoryPoints[-2])
            halfLength = trajectoryEndVector.length / 2.0
            trajectoryEndVector.normalise()
            trajectoryPoints = [trajectoryPoints[-2] + trajectoryEndVector * halfLength, trajectoryPoints[-1]]
            unspottedOrigin = trajectoryPoints[-2]
            return (
             trajectoryPoints, unspottedOrigin)
        if self.__isRicochet:
            trajectoryPoints = []
            for index in range(len(projectileTrajectoryData) - 1):
                nPointOrigin, nPointVelocity = projectileTrajectoryData[index]
                n1PointOrigin, _ = projectileTrajectoryData[index + 1]
                trajectoryPoints += calculateSPGTrajectory(nPointOrigin, n1PointOrigin, nPointVelocity, gravity)

            trajectoryPoints += calculateSPGTrajectory(projectileTrajectoryData[-1][0], impactPoint, projectileTrajectoryData[-1][1], gravity)
            return (
             trajectoryPoints, unspottedOrigin)
        else:
            trajectoryPoints = calculateSPGTrajectory(origin, impactPoint, velocity, gravity)
            return (trajectoryPoints, unspottedOrigin)
