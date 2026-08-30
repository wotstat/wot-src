import math, logging, weakref, BigWorld, Math, math_utils
from AvatarInputHandler import cameras, keys_handlers
from AvatarInputHandler.control_modes import IControlMode
from AvatarInputHandler.rotating_cursor_camera import RotatingCoursorCamera
from aih_constants import CTRL_MODE_NAME
from constants import ARENA_PERIOD, VEHICLE_SELECTION_BLOCK_DELAY
from gui.battle_control import avatar_getter
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import GameEvent
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicle_systems.tankStructure import TankPartIndexes
_logger = logging.getLogger(__name__)

class _CameraManager(object):
    CAMERA_TRANSITION_DURATION = 2
    __CAMERA_PITCH = math.radians(30)
    __MIN_CAMERA_DISTANCE = 10
    __CAM_CHANGING_SETTINGS = {b'fov', b'windowSize'}
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, cfg):
        self.__initialCamSetup = None
        self.__camera = RotatingCoursorCamera(cfg)
        self.__cameraMover = _CameraMover(self.__camera)
        self.__pendingVehicles = set()
        return

    @property
    def camera(self):
        return self.__camera

    def start(self):
        self.__locateCameraOnAllVehicles()
        self.__settingsCore.onSettingsApplied += self.__onSettingsChanged
        return

    def stop(self):
        self.__camera.destroy()
        self.__settingsCore.onSettingsApplied -= self.__onSettingsChanged
        if self.__pendingVehicles:
            self.__pendingVehicles = set()
            BigWorld.player().onVehicleEnterWorld -= self.__onVehicleEnteredWorld
        return

    def reset(self):
        self.__locateCameraOnAllVehicles()
        return

    def moveCameraToDefault(self):
        _, rotations, distance = self.__initialCamSetup
        self.__cameraMover.startMovementTo(rotations.yaw, rotations.pitch, distance, self.CAMERA_TRANSITION_DURATION)
        return

    def handleMouseEvent(self, dx, dy, dz):
        self.__cameraMover.stop()
        self.__camera.handleMouseEvent(dx, dy, dz)
        return

    def __onSettingsChanged(self, diff):
        if self.__CAM_CHANGING_SETTINGS.intersection(diff.keys()):
            self.__locateCameraOnAllVehicles()
        return

    def __locateCameraOnAllVehicles(self):
        arenaDP = self.__sessionProvider.getArenaDP()
        numVehs = 0
        vehiclesBBPoints = []
        targetPos = Math.Vector3()
        rotationVector = Math.Vector3()

        def _makeAdditionalPoints(basePoint, extraPoint):
            yield (
             extraPoint[0], basePoint[1], basePoint[2])
            yield (basePoint[0], extraPoint[1], basePoint[2])
            yield (basePoint[0], basePoint[1], extraPoint[2])
            return

        for vehicleInfo in arenaDP.getVehiclesInfoIterator():
            if arenaDP.isAllyTeam(vehicleInfo.team):
                vehicleID = vehicleInfo.vehicleID
                if vehicleID in BigWorld.entities.keys():
                    vehicle = BigWorld.entities[vehicleID]
                else:
                    self.__pendingVehicles.add(vehicleID)
                    continue
                if vehicle.appearance is None:
                    self.__pendingVehicles.add(vehicleID)
                    continue
                if not vehicle.appearance.collisions:
                    continue
                vehMatrix = Math.Matrix(vehicle.matrix)
                targetPos += vehMatrix.translation
                hullBB = vehicle.appearance.collisions.getBoundingBox(TankPartIndexes.HULL)
                vehiclesBBPoints.extend([vehMatrix.applyPoint(hullBB[0]), vehMatrix.applyPoint(hullBB[1])])
                vehiclesBBPoints.extend(_makeAdditionalPoints(vehMatrix.applyPoint(hullBB[0]), vehMatrix.applyPoint(hullBB[1])))
                vehiclesBBPoints.extend(_makeAdditionalPoints(vehMatrix.applyPoint(hullBB[1]), vehMatrix.applyPoint(hullBB[0])))
                rotationVector += Math.createRotationMatrix((vehMatrix.yaw, 0, 0)).applyVector((0, 0, 1))
                numVehs += 1

        if self.__pendingVehicles:
            _logger.info(b'Not all vehicles are in the world at the moment of camera setup. Skipped vehicles IDS: %s', self.__pendingVehicles)
            BigWorld.player().onVehicleEnterWorld += self.__onVehicleEnteredWorld
        if numVehs == 0:
            return
        else:
            targetPosition = targetPos.scale(1.0 / numVehs)
            yawMatrix = math_utils.createRTMatrix((rotationVector.yaw, self.__CAMERA_PITCH, 0), targetPosition)
            yawMatrix.invert()
            rotatedPoints = [yawMatrix.applyPoint(p) for p in vehiclesBBPoints]
            maxX = max(p.x for p in rotatedPoints)
            minX = min(p.x for p in rotatedPoints)
            maxZ = max(p.z for p in rotatedPoints)
            minZ = min(p.z for p in rotatedPoints)
            maxY = max(rp.y for rp in rotatedPoints if rp.x in (minX, maxX) or rp.z in (minZ, maxZ))
            width = maxX - minX
            height = maxZ - minZ
            hFov = BigWorld.projection().fov
            ratio = cameras.getScreenAspectRatio()
            halfFOVTan = math.tan(hFov / 2)
            distanceToTarget = max(width / (2 * halfFOVTan * ratio), height / (2 * halfFOVTan)) + maxY
            initialRotations = math_utils.createRotationMatrix((rotationVector.yaw, -self.__CAMERA_PITCH, 0))
            self.__initialCamSetup = (
             targetPosition, initialRotations, distanceToTarget)
            self.__setCamera()
            return

    def __setCamera(self):
        self.__camera.setup(*self.__initialCamSetup)
        return

    def __onVehicleEnteredWorld(self, vehicle):
        if vehicle.id in self.__pendingVehicles:
            self.__pendingVehicles.remove(vehicle.id)
            if not self.__pendingVehicles:
                BigWorld.player().onVehicleEnterWorld -= self.__onVehicleEnteredWorld
                _logger.info(b'All vehicles have entered, repositioning the camera')
                self.__locateCameraOnAllVehicles()
        return


class _CameraMover(CallbackDelayer):
    __TICK_DELAY = 0.01

    def __init__(self, camera):
        super(_CameraMover, self).__init__()
        self.__camera = camera
        self.__startParams, self.__finalParams, self.__totalChanges = {}, {}, {}
        self.__startTime, self.__endTime = (None, None)
        return

    def startMovementTo(self, finalYaw, finalPitch, pivotDistance, transtitionTime):
        self.stopCallback(self.__tick)
        camMatrix = Math.Matrix(self.__camera.sourceMatrix)
        self.__startParams[b'yaw'] = camMatrix.yaw
        self.__startParams[b'pitch'] = camMatrix.pitch
        self.__startParams[b'distance'] = self.__camera.pivotDistance
        self.__finalParams[b'yaw'] = finalYaw
        self.__finalParams[b'pitch'] = finalPitch
        self.__finalParams[b'distance'] = self.__camera.clampDistance(pivotDistance)
        self.__totalChanges[b'yaw'] = self.__getYawTotalChange(self.__startParams[b'yaw'], self.__finalParams[b'yaw'])
        self.__totalChanges[b'pitch'] = self.__finalParams[b'pitch'] - self.__startParams[b'pitch']
        self.__totalChanges[b'distance'] = self.__finalParams[b'distance'] - self.__startParams[b'distance']
        self.__startTime = BigWorld.time()
        self.__endTime = self.__startTime + transtitionTime
        self.delayCallback(self.__TICK_DELAY, self.__tick)
        return

    def stop(self):
        self.stopCallback(self.__tick)
        return

    def __tick(self):
        currTime = BigWorld.time()
        timePassed = currTime - self.__startTime
        totalTime = self.__endTime - self.__startTime
        newYaw = self.__getNewValueForParameter(b'yaw', timePassed, totalTime)
        newPitch = self.__getNewValueForParameter(b'pitch', timePassed, totalTime)
        newDistance = self.__getNewValueForParameter(b'distance', timePassed, totalTime)
        self.__camera.move(math_utils.createRotationMatrix((newYaw, newPitch, 0)), newDistance)
        if currTime < self.__endTime:
            self.delayCallback(self.__TICK_DELAY, self.__tick)
        return

    def __getYawTotalChange(self, startYaw, finalYaw):
        adjustedStartYaw = startYaw if startYaw > 0 else math.pi + (math.pi - abs(startYaw))
        adjustedFinalYaw = finalYaw if finalYaw > 0 else math.pi + (math.pi - abs(finalYaw))
        adjustedDiff = adjustedFinalYaw - adjustedStartYaw
        if adjustedDiff == 0:
            return 0
        return min(adjustedDiff, math.copysign(1, -1 * adjustedDiff) * (2 * math.pi - abs(adjustedDiff)), key=abs)

    def __getNewValueForParameter(self, paramName, timePassed, totalTime):
        totalChange = self.__totalChanges[paramName]
        if timePassed > totalTime or totalChange == 0:
            return self.__finalParams[paramName]
        return self.__startParams[paramName] + math_utils.easeInOutCubic(timePassed, totalChange, totalTime)


class VehiclesSelectionControlMode(IControlMode):
    __dynamicObjectsCache = dependency.descriptor(IBattleDynamicObjectsCache)
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, config, avatarInputHandler):
        self.__aih = weakref.proxy(avatarInputHandler)
        self.__camManager = _CameraManager(config[b'camera'])
        self.__arenaPeriod = None
        self.__ownVehicleEffectGO = None
        self.__lockedState = False
        self.__lockStartTime = 0
        self.__callbackDelayer = CallbackDelayer()
        return

    @property
    def camera(self):
        return self.__camManager.camera

    def destroy(self):
        if self.__camManager is not None:
            self.__camManager.stop()
        self.__camManager = None
        self.__callbackDelayer.destroy()
        self.__callbackDelayer = None
        return

    def enable(self, **args):
        self.__camManager.start()
        arena = BigWorld.player().arena
        arena.onPeriodChange += self.__onArenaPeriodChanged
        self.__updateArenaPeriod(arena.period, arena.periodEndTime)
        return

    def disable(self):
        arena = BigWorld.player().arena
        arena.onPeriodChange -= self.__onArenaPeriodChanged
        self.__callbackDelayer.clearCallbacks()
        return

    def alwaysReceiveKeyEvents(self, isDown=True):
        return isDown

    def handleKeyEvent(self, isDown, key, mods, event=None):
        prbCtrl = self.__guiSessionProvider.dynamic.prebattleSetup
        if (prbCtrl is None or prbCtrl.isSelectionConfirmed()) and keys_handlers.processAmmoSelection(key):
            return True
        else:
            return

    def handleMouseEvent(self, dx, dy, dz):
        if self.__lockedState:
            return False
        self.__camManager.handleMouseEvent(dx, dy, math_utils.clamp(-1, 1, dz))
        return True

    def onRecreateDevice(self):
        return

    def moveCameraToDefault(self):
        lockIsSoon = 0 < self.__lockStartTime < BigWorld.serverTime() + self.__camManager.CAMERA_TRANSITION_DURATION
        if not self.__lockedState and not lockIsSoon:
            self.__camManager.moveCameraToDefault()
        return

    def __onLockedState(self):
        self.__lockedState = True
        g_eventBus.handleEvent(GameEvent(GameEvent.PREBATTLE_INPUT_STATE_LOCKED), scope=EVENT_BUS_SCOPE.BATTLE)
        if avatar_getter.isObserver():
            return
        self.__aih.ctrls[CTRL_MODE_NAME.ARCADE].camera.enable(camTransitionParams={b'cameraTransitionDuration': (self.__camManager.CAMERA_TRANSITION_DURATION)})
        return

    def __onArenaPeriodChanged(self, period, periodEndTime, *_):
        self.__updateArenaPeriod(period, periodEndTime)
        return

    def __updateArenaPeriod(self, period, periodEndTime):
        if period == ARENA_PERIOD.BATTLE:
            self.__aih.onControlModeChanged(CTRL_MODE_NAME.ARCADE)
        elif period == ARENA_PERIOD.PREBATTLE:
            self.__lockStartTime = periodEndTime - VEHICLE_SELECTION_BLOCK_DELAY
            timeTillEnd = periodEndTime - BigWorld.serverTime()
            self.__callbackDelayer.delayCallback(timeTillEnd - VEHICLE_SELECTION_BLOCK_DELAY, self.__onLockedState)
        self.__arenaPeriod = period
        return
