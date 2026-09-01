import math
from collections import namedtuple
import BigWorld, Math
from Math import Vector2, Vector3
import BattleReplay, Settings, constants, math_utils
from AvatarInputHandler import cameras, aih_global_binding
from BigWorld import StrategicAimingSystem, StrategicAimingSystemRemote
from AvatarInputHandler.DynamicCameras import createOscillatorFromSection, CameraDynamicConfig, CameraWithSettings, SPGScrollSmoother
from AvatarInputHandler.DynamicCameras.camera_switcher import CameraSwitcher, SwitchTypes, CameraSwitcherCollection, SwitchToPlaces, TRANSITION_DIST_HYSTERESIS
from AvatarInputHandler.cameras import getWorldRayAndPoint, readFloat, readVec2, ImpulseReason, FovExtended
from account_helpers.settings_core import settings_constants
from aih_constants import CTRL_MODE_NAME
from debug_utils import LOG_WARNING
from helpers.CallbackDelayer import CallbackDelayer
_DistRangeSetting = namedtuple(b'_DistRangeSetting', [14, 15, 16, 
 17, 18, 19])
_CAM_YAW_ROUND = 4

def getCameraAsSettingsHolder(settingsDataSec):
    return StrategicCamera(settingsDataSec)


class StrategicCamera(CameraWithSettings, CallbackDelayer):
    _DYNAMIC_ENABLED = True
    ABSOLUTE_VERTICAL_FOV = math.radians(60.0)
    _SMOOTHING_PIVOT_DELTA_FACTOR = 6.0

    @staticmethod
    def enableDynamicCamera(enable):
        StrategicCamera._DYNAMIC_ENABLED = enable
        return

    @staticmethod
    def isCameraDynamic():
        return StrategicCamera._DYNAMIC_ENABLED

    camera = property((lambda self: self.__cam))
    aimingSystem = property((lambda self: self.__aimingSystem))
    __aimOffset = aih_global_binding.bindRW(aih_global_binding.BINDING_ID.AIM_OFFSET)

    def __init__(self, dataSec):
        super(StrategicCamera, self).__init__()
        CallbackDelayer.__init__(self)
        self.isAimOffsetEnabled = True
        self.__positionOscillator = None
        self.__positionNoiseOscillator = None
        self.__activeDistRangeSettings = None
        self.__dynamicCfg = CameraDynamicConfig()
        self.__cameraYaw = 0.0
        self.__switchers = CameraSwitcherCollection(cameraSwitchers=[
         CameraSwitcher(switchType=SwitchTypes.FROM_TRANSITION_DIST_AS_MIN, switchToName=CTRL_MODE_NAME.ARTY, switchToPos=1.0)], isEnabled=True)
        self._readConfigs(dataSec)
        self.__cam = BigWorld.CursorCamera()
        self.__cam.isHangar = False
        self.__curSense = self._cfg[b'sensitivity']
        self.__onChangeControlMode = None
        self.__aimingSystem = None
        self.__prevTime = BigWorld.time()
        self.__autoUpdatePosition = False
        self.__dxdydz = Vector3(0, 0, 0)
        self.__needReset = 0
        self.__smoothingPivotDelta = 0
        self.__transitionEnabled = True
        self.__camDist = 0.0
        self.__scrollSmoother = SPGScrollSmoother(0.3)
        self.__saveDist = False
        return

    def getCurSense(self):
        return self.__curSense

    @staticmethod
    def _getConfigsKey():
        return StrategicCamera.__name__

    def create(self, onChangeControlMode=None):
        aimingSystemClass = StrategicAimingSystemRemote if BigWorld.player().isObserver() else StrategicAimingSystem
        self.__aimingSystem = aimingSystemClass(self._cfg[b'distRange'][0], self.__cameraYaw)
        super(StrategicCamera, self).create()
        self.__onChangeControlMode = onChangeControlMode
        self.__camDist = self._cfg[b'camDist']
        self.__cam.pivotMaxDist = 0.0
        self.__cam.maxDistHalfLife = 0.01
        self.__cam.movementHalfLife = 0.0
        self.__cam.turningHalfLife = -1
        self.__cam.pivotPosition = Math.Vector3(0.0, self.__camDist, 0.0)
        self.__scrollSmoother.setTime(self._cfg[b'scrollSmoothingTime'])
        self.__enableSwitchers()
        return

    def destroy(self):
        self.__saveDist = False
        self.disable()
        self.__onChangeControlMode = None
        self.__cam = None
        if self.__aimingSystem is not None:
            self.__aimingSystem.destroy()
            self.__aimingSystem = None
        CallbackDelayer.destroy(self)
        CameraWithSettings.destroy(self)
        return

    def enable(self, targetPos, saveDist, switchToPos=None, switchToPlace=None):
        self.__prevTime = BigWorld.time()
        self.__aimingSystem.enable(targetPos)
        self.__activeDistRangeSettings = self.__getActiveDistRangeForArena()
        if self.__activeDistRangeSettings is not None:
            self.__aimingSystem.height = self.__getDistRange()[0]
        minDist, maxDist = self.__getDistRange()
        maxPivotHeight = maxDist - minDist
        self.__updateCameraYaw()
        if switchToPlace == SwitchToPlaces.TO_TRANSITION_DIST:
            self.__camDist = self.__getTransitionCamDist()
        elif switchToPlace == SwitchToPlaces.TO_RELATIVE_POS and switchToPos is not None:
            self.__camDist = maxPivotHeight * switchToPos
        elif switchToPlace == SwitchToPlaces.TO_NEAR_POS and switchToPos is not None:
            switchToPos = math_utils.clamp(minDist, maxDist, switchToPos)
            self.__camDist = switchToPos - minDist
        elif self.settingsCore.getSetting(settings_constants.SPGAim.AUTO_CHANGE_AIM_MODE):
            self.__camDist = math_utils.clamp(self.__getTransitionCamDist(), maxPivotHeight, self.__camDist)
        self.__saveDist = saveDist
        self.__camDist = math_utils.clamp(0, maxPivotHeight, self.__camDist)
        self.__cam.pivotPosition = Math.Vector3(0.0, self.__camDist, 0.0)
        self.__scrollSmoother.start(self.__camDist)
        self.__enableSwitchers()
        camTarget = Math.MatrixProduct()
        camTarget.b = self.__aimingSystem.matrixProvider
        self.__cam.target = camTarget
        self.__cam.forceUpdate()
        BigWorld.camera(self.__cam)
        BigWorld.player().positionControl.moveTo(self.__aimingSystem.matrixProvider.translation)
        BigWorld.player().positionControl.followCamera(True)
        FovExtended.instance().enabled = False
        BigWorld.projection().fov = StrategicCamera.ABSOLUTE_VERTICAL_FOV
        self.__cameraUpdate()
        self.delayCallback(0.0, self.__cameraUpdate)
        self.__needReset = 1
        return

    def disable(self):
        self.__scrollSmoother.stop()
        if self.__aimingSystem is not None:
            self.__aimingSystem.disable()
        self.__switchers.clear()
        self.stopCallback(self.__cameraUpdate)
        positionControl = BigWorld.player().positionControl
        if positionControl is not None:
            positionControl.followCamera(False)
        self.__positionOscillator.reset()
        FovExtended.instance().resetFov()
        FovExtended.instance().enabled = True
        return

    def teleport(self, pos):
        self.moveToPosition(pos)
        return

    def setMaxDist(self):
        distRange = self.__getDistRange()
        if len(distRange) > 1:
            self.__camDist = distRange[1]
        return

    def getDistRatio(self):
        distRange = self.__getDistRange()
        maxPivotHeight = distRange[1] - distRange[0]
        return self.__camDist / maxPivotHeight

    def getCurrentCamDist(self):
        return self.__camDist + self.__getDistRange()[0]

    def getCamDistRange(self):
        return self.__getDistRange()

    def getCamTransitionDist(self):
        return self._cfg[b'transitionDist']

    def update(self, dx, dy, dz, rotateMode=True, zoomMode=True, updatedByKeyboard=False):
        self.__curSense = self._cfg[b'keySensitivity'] if updatedByKeyboard else self._cfg[b'sensitivity']
        standardMaxDist = self._cfg[b'distRange'][1]
        if self.__camDist > standardMaxDist:
            self.__curSense *= self.__getCameraScrollMultiplier() + (self.__camDist - self._cfg[b'distRange'][1]) * self.__getCameraAcceleration()
        self.__autoUpdatePosition = updatedByKeyboard
        self.__dxdydz = Vector3(dx, dy, dz)
        return

    def moveToPosition(self, pos):
        self.__aimingSystem.enable(pos)
        self.update(0.0, 0.0, 0.0)
        return

    def calcVisibleAreaRatio(self):
        from ClientArena import Plane
        points = [
         Math.Vector2(1, 1), Math.Vector2(1, -1), Math.Vector2(-1, -1), Math.Vector2(-1, 1)]
        dirsPos = [getWorldRayAndPoint(point.x, point.y) for point in points]
        planeXZ = Plane(Math.Vector3(0, 1, 0), 0)
        collisionPoints = []
        for direction, begPos in dirsPos:
            endPos = begPos + direction * 1000
            testResult = BigWorld.wg_collideSegment(BigWorld.player().spaceID, begPos, endPos, 3)
            collPoint = Math.Vector3(0, 0, 0)
            if collPoint is not None:
                collPoint = testResult.closestPoint
            else:
                collPoint = planeXZ.intersectSegment(begPos, endPos)
            collisionPoints.append(collPoint)

        x0 = abs(collisionPoints[1].x - collisionPoints[2].x)
        x1 = abs(collisionPoints[0].x - collisionPoints[3].x)
        z0 = abs(collisionPoints[0].z - collisionPoints[1].z)
        z1 = abs(collisionPoints[3].z - collisionPoints[2].z)
        bb = BigWorld.player().arena.arenaType.boundingBox
        arenaBottomLeft = bb[0]
        arenaUpperRight = bb[1]
        arenaX = arenaUpperRight[0] - arenaBottomLeft[0]
        arenaZ = arenaUpperRight[1] - arenaBottomLeft[1]
        return (
         (x0 + x1) * 0.5 / arenaX, (z0 + z1) * 0.5 / arenaZ)

    def applyImpulse(self, position, impulse, reason=ImpulseReason.ME_HIT):
        adjustedImpulse, noiseMagnitude = self.__dynamicCfg.adjustImpulse(impulse, reason)
        impulseFlatDir = Vector3(adjustedImpulse.x, 0, adjustedImpulse.z)
        impulseFlatDir.normalise()
        cameraYawMat = math_utils.createRotationMatrix(Vector3(-self.__cameraYaw, 0.0, 0.0))
        impulseLocal = cameraYawMat.applyVector(impulseFlatDir * (-1 * adjustedImpulse.length))
        self.__positionOscillator.applyImpulse(impulseLocal)
        self.__applyNoiseImpulse(noiseMagnitude)
        return

    def applyDistantImpulse(self, position, impulseValue, reason=ImpulseReason.ME_HIT):
        if reason != ImpulseReason.SPLASH and reason != ImpulseReason.PROJECTILE_HIT:
            return
        impulse = BigWorld.player().getOwnVehiclePosition() - position
        distance = impulse.length
        if distance <= 1.0:
            distance = 1.0
        impulse.normalise()
        if reason == ImpulseReason.PROJECTILE_HIT:
            if not cameras.isPointOnScreen(position):
                return
            distance = 1.0
        impulse *= impulseValue / distance
        self.applyImpulse(position, impulse, reason)
        return

    def __applyNoiseImpulse(self, noiseMagnitude):
        noiseImpulse = math_utils.RandomVectors.random3Flat(noiseMagnitude)
        self.__positionNoiseOscillator.applyImpulse(noiseImpulse)
        return

    def writeUserPreferences(self):
        ds = Settings.g_instance.userPrefs
        if not ds.has_key(Settings.KEY_CONTROL_MODE):
            ds.write(Settings.KEY_CONTROL_MODE, b'')
        ucfg = self._userCfg
        ds = ds[Settings.KEY_CONTROL_MODE]
        ds.writeFloat(b'strategicMode/camera/keySensitivity', ucfg[b'keySensitivity'])
        ds.writeFloat(b'strategicMode/camera/sensitivity', ucfg[b'sensitivity'])
        ds.writeFloat(b'strategicMode/camera/scrollSensitivity', ucfg[b'scrollSensitivity'])
        ds.writeFloat(b'strategicMode/camera/camDist', self._cfg[b'camDist'])
        return

    def __cameraUpdate(self):
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying and replayCtrl.isControllingCamera:
            aimOffset = replayCtrl.getAimClipPosition()
        else:
            aimOffset = self.__calcAimOffset()
            if replayCtrl.isRecording:
                replayCtrl.setAimClipPosition(aimOffset)
        self.__aimOffset = aimOffset
        self.__updateCameraYaw()
        shotDescr = BigWorld.player().getVehicleDescriptor().shot
        BigWorld.wg_trajectory_drawer().setParams(shotDescr.maxDistance, Math.Vector3(0, -shotDescr.gravity, 0), aimOffset)
        curTime = BigWorld.time()
        deltaTime = curTime - self.__prevTime
        self.__prevTime = curTime
        self.__aimingSystem.update(deltaTime)
        if replayCtrl.isPlaying:
            if self.__needReset != 0:
                if self.__needReset > 1:
                    from helpers import isPlayerAvatar
                    player = BigWorld.player()
                    if isPlayerAvatar():
                        if player.inputHandler.ctrl is not None:
                            player.inputHandler.ctrl.resetGunMarkers()
                    self.__needReset = 0
                else:
                    self.__needReset += 1
            if replayCtrl.isControllingCamera:
                self.__aimingSystem.updateTargetPos(replayCtrl.getGunRotatorTargetPoint())
            else:
                self.__aimingSystem.handleMovement(self.__dxdydz.x * self.__curSense, -self.__dxdydz.y * self.__curSense)
                if self.__dxdydz.x != 0 or self.__dxdydz.y != 0 or self.__dxdydz.z != 0:
                    self.__needReset = 2
        else:
            self.__aimingSystem.handleMovement(self.__dxdydz.x * self.__curSense, -self.__dxdydz.y * self.__curSense)
        self.__calcSmoothingPivotDelta(deltaTime)
        self.__camDist -= self.__dxdydz.z * float(self.__curSense)
        self.__camDist = self.__aimingSystem.overrideCamDist(self.__camDist)
        distRange = self.__getDistRange()
        maxPivotHeight = distRange[1] - distRange[0]
        transitionDist = self._cfg[b'transitionDist'] - distRange[0]
        if self.__switchers.isEnabled():
            self.__camDist = math_utils.clamp(transitionDist, maxPivotHeight, self.__camDist)
            scrollLimits = (transitionDist, maxPivotHeight)
        else:
            self.__camDist = math_utils.clamp(0, maxPivotHeight, self.__camDist)
            scrollLimits = (0, maxPivotHeight)
        if self.__saveDist:
            self._cfg[b'camDist'] = self.__camDist
        self.__scrollSmoother.moveTo(self.__camDist, scrollLimits)
        currentCamDist = self.__scrollSmoother.update(deltaTime)
        camDistWithSmoothing = currentCamDist + self.__smoothingPivotDelta - self.__aimingSystem.heightFromPlane
        self.__cam.pivotPosition = Math.Vector3(0.0, camDistWithSmoothing, 0.0)
        if self.__onChangeControlMode is not None and self.__switchers.needToSwitch(self.__dxdydz.z, self.__camDist, 0, maxPivotHeight, transitionDist):
            self.__onChangeControlMode(*self.__switchers.getSwitchParams())
        if not self.__transitionEnabled and self.__camDist + TRANSITION_DIST_HYSTERESIS >= transitionDist:
            self.__transitionEnabled = True
            self.__enableSwitchers(False)
        self.__updateOscillator(deltaTime)
        if not self.__autoUpdatePosition:
            self.__dxdydz = Vector3(0, 0, 0)
        return 0.0

    def _handleSettingsChange(self, diff):
        if settings_constants.SPGAim.SPG_STRATEGIC_CAM_MODE in diff:
            self.__aimingSystem.setParallaxModeEnabled(diff[settings_constants.SPGAim.SPG_STRATEGIC_CAM_MODE] == 1)
        if settings_constants.SPGAim.AUTO_CHANGE_AIM_MODE in diff:
            self.__enableSwitchers()
        if settings_constants.GAME.SCROLL_SMOOTHING in diff:
            self.__scrollSmoother.setIsEnabled(self.settingsCore.getSetting(settings_constants.GAME.SCROLL_SMOOTHING))
        return

    def _updateSettingsFromServer(self):
        if self.settingsCore.isReady:
            if self.__aimingSystem is not None:
                self.__aimingSystem.setParallaxModeEnabled(self.settingsCore.getSetting(settings_constants.SPGAim.SPG_STRATEGIC_CAM_MODE) == 1)
            self.__enableSwitchers()
            self.__scrollSmoother.setIsEnabled(self.settingsCore.getSetting(settings_constants.GAME.SCROLL_SMOOTHING))
        return

    def __calcSmoothingPivotDelta(self, deltaTime):
        heightsDy = self.__aimingSystem.heightFromPlane - self.__smoothingPivotDelta
        smoothFactor = math_utils.clamp(0, 1, StrategicCamera._SMOOTHING_PIVOT_DELTA_FACTOR * deltaTime)
        smoothingPivotDeltaDy = smoothFactor * heightsDy
        self.__smoothingPivotDelta += smoothingPivotDeltaDy
        return

    def __calcAimOffset(self):
        if not self.isAimOffsetEnabled:
            return Vector2(0.0, 0.0)
        aimWorldPos = self.__aimingSystem.matrixProvider.applyPoint(Vector3(0, -self.__aimingSystem.height, 0))
        aimOffset = cameras.projectPoint(aimWorldPos)
        return Vector2(math_utils.clamp(-0.95, 0.95, aimOffset.x), math_utils.clamp(-0.95, 0.95, aimOffset.y))

    def __updateOscillator(self, deltaTime):
        if StrategicCamera.isCameraDynamic():
            self.__positionOscillator.update(deltaTime)
            self.__positionNoiseOscillator.update(deltaTime)
        else:
            self.__positionOscillator.reset()
            self.__positionNoiseOscillator.reset()
        self.__cam.target.a = math_utils.createTranslationMatrix(self.__positionOscillator.deviation + self.__positionNoiseOscillator.deviation)
        return

    def __updateCameraYaw(self):
        altModeEnabled = self.settingsCore.getSetting(settings_constants.SPGAim.SPG_STRATEGIC_CAM_MODE) == 1
        pitch = (altModeEnabled or -math.pi) * 0.499 if 1 else math.radians(-88.0)
        self.__cameraYaw = round(self.aimingSystem.getCamYaw(), _CAM_YAW_ROUND)
        srcMat = math_utils.createRotationMatrix((self.__cameraYaw, pitch, 0.0))
        self.__cam.source = srcMat
        return

    def __getTransitionCamDist(self):
        minDist, maxDist = self.__getDistRange()
        maxPivotHeight = maxDist - minDist
        transitionDist = self._cfg[b'transitionDist'] - minDist
        return math_utils.clamp(0, maxPivotHeight, transitionDist)

    def reload(self):
        if not constants.IS_DEVELOPMENT:
            return
        import ResMgr
        ResMgr.purge(b'gui/avatar_input_handler.xml')
        cameraSec = ResMgr.openSection(b'gui/avatar_input_handler.xml/strategicMode/camera/')
        self._reloadConfigs(cameraSec)
        return

    def _readConfigs(self, dataSec):
        if not dataSec or dataSec[b'strategic']:
            LOG_WARNING(b'Invalid section <strategicMode/camera> in avatar_input_handler.xml')
        super(StrategicCamera, self)._readConfigs(dataSec)
        dynamicsSection = dataSec[b'dynamics']
        self.__dynamicCfg.readImpulsesConfig(dynamicsSection)
        self.__positionOscillator = createOscillatorFromSection(dynamicsSection[b'oscillator'], False)
        self.__positionNoiseOscillator = createOscillatorFromSection(dynamicsSection[b'randomNoiseOscillatorFlat'], False)
        return

    def _readBaseCfg(self, dataSec):
        bcfg = self._baseCfg
        bcfg[b'keySensitivity'] = readFloat(dataSec, b'keySensitivity', 0.005, 10, 0.025)
        bcfg[b'sensitivity'] = readFloat(dataSec, b'sensitivity', 0.005, 10, 0.025)
        bcfg[b'scrollSensitivity'] = readFloat(dataSec, b'scrollSensitivity', 0.005, 10, 0.025)
        bcfg[b'distRange'] = readVec2(dataSec, b'distRange', (1, 1), (10000, 10000), (2, 30))
        bcfg[b'transitionDist'] = readFloat(dataSec, b'transitionDist', 1.0, 10000.0, 60.0)
        bcfg[b'distRangeForArenaSize'] = self.__readDynamicDistRangeData(dataSec)
        bcfg[b'scrollSmoothingTime'] = readFloat(dataSec, b'scrollSmoothingTime', 0.0, 1.0, 0.3)
        return

    def _readUserCfg(self):
        ucfg = self._userCfg
        dataSec = Settings.g_instance.userPrefs[Settings.KEY_CONTROL_MODE]
        if dataSec is not None:
            dataSec = dataSec[b'strategicMode/camera']
        ucfg[b'horzInvert'] = False
        ucfg[b'vertInvert'] = False
        ucfg[b'keySensitivity'] = readFloat(dataSec, b'keySensitivity', 0.0, 10.0, 1.0)
        ucfg[b'sensitivity'] = readFloat(dataSec, b'sensitivity', 0.0, 10.0, 1.0)
        ucfg[b'scrollSensitivity'] = readFloat(dataSec, b'scrollSensitivity', 0.0, 10.0, 1.0)
        ucfg[b'camDist'] = readFloat(dataSec, b'camDist', 0.0, 60.0, 0)
        return

    def _makeCfg(self):
        bcfg = self._baseCfg
        ucfg = self._userCfg
        cfg = self._cfg
        cfg[b'keySensitivity'] = bcfg[b'keySensitivity']
        cfg[b'sensitivity'] = bcfg[b'sensitivity']
        cfg[b'scrollSensitivity'] = bcfg[b'scrollSensitivity']
        cfg[b'distRange'] = bcfg[b'distRange']
        cfg[b'transitionDist'] = bcfg[b'transitionDist']
        cfg[b'distRangeForArenaSize'] = bcfg[b'distRangeForArenaSize']
        cfg[b'scrollSmoothingTime'] = bcfg[b'scrollSmoothingTime']
        cfg[b'camDist'] = ucfg[b'camDist']
        cfg[b'keySensitivity'] *= ucfg[b'keySensitivity']
        cfg[b'sensitivity'] *= ucfg[b'sensitivity']
        cfg[b'scrollSensitivity'] *= ucfg[b'scrollSensitivity']
        cfg[b'horzInvert'] = ucfg[b'horzInvert']
        cfg[b'vertInvert'] = ucfg[b'vertInvert']
        return

    def __readDynamicDistRangeData(self, dataSec):
        section = dataSec[b'dynamicDistRanges']
        dynamicDistRanges = []
        if section is None:
            return dynamicDistRanges
        else:
            for value in section.values():
                minArenaSize = readFloat(value, b'minArenaSize', 0.1, 2000, 2000.0)
                distRange = readVec2(value, b'distRangeOverride', (1, 1), (2000, 2000), (40, 300))
                acceleration = readFloat(value, b'acceleration', 0.0, 100.0, 0.0)
                scrollMultiplier = readFloat(value, b'scrollMultiplier', 0.0, 100.0, 1.0)
                gameplayIDSec = value[b'gameplayID']
                gameplayID = gameplayIDSec.asString.strip() if gameplayIDSec is not None else None
                requiresPoiTypeSec = value[b'requiresPoiType']
                requiresPoiType = requiresPoiTypeSec.asInt if requiresPoiTypeSec is not None else None
                dynamicDistRanges.append(_DistRangeSetting(minArenaSize, distRange, scrollMultiplier, acceleration, gameplayID, requiresPoiType))

            return dynamicDistRanges

    def __getActiveDistRangeForArena(self):
        arenaType = BigWorld.player().arena.arenaType
        bb = arenaType.boundingBox
        arenaBottomLeft = bb[0]
        arenaUpperRight = bb[1]
        arenaX = arenaUpperRight[0] - arenaBottomLeft[0]
        arenaZ = arenaUpperRight[1] - arenaBottomLeft[1]
        arenaSize = min(arenaX, arenaZ)
        gameplayName = arenaType.gameplayName
        poiTypes = {poi[b'type'] for poi in arenaType.pointsOfInterest}
        availableDistRanges = self._cfg[b'distRangeForArenaSize']
        filtered = [pt for pt in availableDistRanges if pt.gameplayID is not None or pt.requiresPoiType is not None]
        unfiltered = [pt for pt in availableDistRanges if pt.gameplayID is None and pt.requiresPoiType is None]
        currentDistRange = None
        choosenArenaMinSize = -1
        for pt in filtered:
            if pt.gameplayID is not None and pt.gameplayID != gameplayName:
                continue
            if pt.requiresPoiType is not None and pt.requiresPoiType not in poiTypes:
                continue
            if arenaSize >= pt.minArenaSize and pt.minArenaSize > choosenArenaMinSize:
                choosenArenaMinSize = pt.minArenaSize
                currentDistRange = pt

        if currentDistRange is not None:
            return currentDistRange
        else:
            choosenArenaMinSize = 0
            for pt in unfiltered:
                if arenaSize >= pt.minArenaSize and pt.minArenaSize > choosenArenaMinSize:
                    choosenArenaMinSize = pt.minArenaSize
                    currentDistRange = pt

            return currentDistRange

    def __getDistRange(self):
        if not self.__activeDistRangeSettings:
            return self._cfg[b'distRange']
        return self.__activeDistRangeSettings.distRange

    def __getCameraAcceleration(self):
        if not self.__activeDistRangeSettings:
            return 0.0
        return self.__activeDistRangeSettings.acceleration

    def __getCameraScrollMultiplier(self):
        if not self.__activeDistRangeSettings:
            return 1.0
        return self.__activeDistRangeSettings.scrollMultiplier

    def __enableSwitchers(self, updateTransitionEnabled=True):
        minDist, _ = self.__getDistRange()
        if updateTransitionEnabled and self.__camDist + minDist + TRANSITION_DIST_HYSTERESIS <= self._cfg[b'transitionDist']:
            self.__transitionEnabled = False
        if self.settingsCore.isReady:
            self.__switchers.setIsEnabled(self.settingsCore.getSetting(settings_constants.SPGAim.AUTO_CHANGE_AIM_MODE) and self.__transitionEnabled)
        return
