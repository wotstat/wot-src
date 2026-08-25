import logging, math, BigWorld, GUI
from Math import Vector2, Vector3, Matrix
import BattleReplay, Settings, constants, math_utils
from AvatarInputHandler import AimingSystems
from AvatarInputHandler import cameras, aih_global_binding
from BigWorld import SniperAimingSystem, SniperAimingSystemRemote
from AvatarInputHandler.DynamicCameras import CameraDynamicConfig, CameraWithSettings, calcYawPitchDelta
from AvatarInputHandler.DynamicCameras import createCrosshairMatrix, createOscillatorFromSection, AccelerationSmoother
from AvatarInputHandler.cameras import readFloat, readVec3, ImpulseReason, FovExtended
from BattleReplay import CallbackDataNames
from debug_utils import LOG_WARNING, LOG_DEBUG
from helpers.CallbackDelayer import CallbackDelayer
_logger = logging.getLogger(__name__)

def getCameraAsSettingsHolder(settingsDataSec):
    return SniperCamera(settingsDataSec)


class SniperCamera(CameraWithSettings, CallbackDelayer):
    _DYNAMIC_ENABLED = True
    _SNIPER_ZOOM_LEVEL = -1

    @staticmethod
    def enableDynamicCamera(enable):
        SniperCamera._DYNAMIC_ENABLED = enable
        return

    @staticmethod
    def isCameraDynamic():
        return SniperCamera._DYNAMIC_ENABLED

    @staticmethod
    def setSniperZoomSettings(value):
        SniperCamera._SNIPER_ZOOM_LEVEL = value
        return

    _FILTER_LENGTH = 5
    _DEFAULT_MAX_ACCELERATION_DURATION = 1.5
    _MIN_REL_SPEED_ACC_SMOOTHING = 0.7
    _DEFAULT_FOV = math.pi / 3
    _DEFAULT_CLIP_PLANE_SCALE = math.tan(_DEFAULT_FOV / 2)
    camera = property((lambda self: self.__cam))
    aimingSystem = property((lambda self: self.__aimingSystem))
    __aimOffset = aih_global_binding.bindRW(aih_global_binding.BINDING_ID.AIM_OFFSET)
    __zoomFactor = aih_global_binding.bindRW(aih_global_binding.BINDING_ID.ZOOM_FACTOR)

    def __init__(self, dataSec, defaultOffset=None, binoculars=None):
        super(SniperCamera, self).__init__()
        CallbackDelayer.__init__(self)
        self.__impulseOscillator = None
        self.__movementOscillator = None
        self.__noiseOscillator = None
        self.__dynamicCfg = CameraDynamicConfig()
        self.__accelerationSmoother = None
        self._readConfigs(dataSec)
        if binoculars is None:
            return
        else:
            self.__cam = BigWorld.FreeCamera()
            self.__zoom = self._cfg[b'zoom']
            self.__curSense = 0
            self.__curScrollSense = 0
            self.__waitVehicleCallbackId = None
            self.__onChangeControlMode = None
            self.__aimingSystem = None
            self.__binoculars = binoculars
            self.__defaultAimOffset = defaultOffset or Vector2()
            self.__aimMarkerDistance = self.__dynamicCfg[b'aimMarkerDistance']
            self.__crosshairMatrix = createCrosshairMatrix(offsetFromNearPlane=self.__aimMarkerDistance)
            self.__prevTime = BigWorld.time()
            self.__autoUpdateDxDyDz = Vector3(0, 0, 0)
            if BattleReplay.g_replayCtrl.isPlaying:
                BattleReplay.g_replayCtrl.setDataCallback(CallbackDataNames.APPLY_ZOOM, self.__applySerializedZoom)
            return

    @staticmethod
    def _getConfigsKey():
        return SniperCamera.__name__

    def _handleSettingsChange(self, diff):
        if b'increasedZoom' in diff:
            self._cfg[b'increasedZoom'] = diff[b'increasedZoom']
            self.__updateZoom()
        if (b'fov' in diff or b'dynamicFov' in diff) and self.camera is BigWorld.camera():
            self.delayCallback(0.01, self.__applyZoom, self._cfg[b'zoom'])
        return

    def create(self, onChangeControlMode=None):
        super(SniperCamera, self).create()
        self.__onChangeControlMode = onChangeControlMode
        self.__aimingSystem = self._aimingSystemClass()()
        return

    def _aimingSystemClass(self):
        if BigWorld.player().isObserver():
            return SniperAimingSystemRemote
        return SniperAimingSystem

    def destroy(self):
        self.disable()
        self.__onChangeControlMode = None
        self.__cam = None
        if self.__aimingSystem is not None:
            self.__aimingSystem.destroy()
            self.__aimingSystem = None
        CallbackDelayer.destroy(self)
        CameraWithSettings.destroy(self)
        return

    def enable(self, targetPos, saveZoom):
        self.__prevTime = BigWorld.time()
        player = BigWorld.player()
        if SniperCamera._SNIPER_ZOOM_LEVEL == -1:
            if saveZoom:
                self.__zoom = self._cfg[b'zoom']
            else:
                self._cfg[b'zoom'] = self.__zoom = self._cfg[b'zooms'][0]
        elif len(self._cfg[b'zooms']) > SniperCamera._SNIPER_ZOOM_LEVEL:
            self.__zoom = self._cfg[b'zooms'][SniperCamera._SNIPER_ZOOM_LEVEL]
        else:
            _logger.warning(b'zooms should always have enough length to use _SNIPER_ZOOM_LEVEL, using default now')
            self._cfg[b'zoom'] = self.__zoom = self._cfg[b'zooms'][0]
        self.__applyZoom(self.__zoom)
        self.__setupCamera(targetPos)
        vehicle = player.getVehicleAttached()
        if self.__waitVehicleCallbackId is not None:
            BigWorld.cancelCallback(self.__waitVehicleCallbackId)
        if vehicle is None:
            self.__waitVehicleCallbackId = BigWorld.callback(0.1, self.__waitVehicle)
        else:
            self.__showVehicle(False)
        BigWorld.camera(self.__cam)
        if self.__cameraUpdate(False) >= 0.0:
            self.delayCallback(0.0, self.__cameraUpdate)
        return

    def disable(self):
        if self.__waitVehicleCallbackId is not None:
            BigWorld.cancelCallback(self.__waitVehicleCallbackId)
            self.__waitVehicleCallbackId = None
        self.__showVehicle(True)
        self.__applyZoom(1.0)
        self.stopCallback(self.__cameraUpdate)
        if self.__aimingSystem is not None:
            self.__aimingSystem.disable()
        self.__movementOscillator.reset()
        self.__impulseOscillator.reset()
        self.__noiseOscillator.reset()
        self.__accelerationSmoother.reset()
        self.__autoUpdateDxDyDz.set(0)
        FovExtended.instance().resetFov()
        return

    def update(self, dx, dy, dz, updatedByKeyboard=False):
        self.__curSense = self._cfg[b'keySensitivity'] if updatedByKeyboard else self._cfg[b'sensitivity']
        self.__curScrollSense = self._cfg[b'keySensitivity'] if updatedByKeyboard else self._cfg[b'scrollSensitivity']
        self.__curSense *= 1.0 / self.__zoom
        if updatedByKeyboard:
            self.__autoUpdateDxDyDz.set(dx, dy, dz)
        else:
            self.__autoUpdateDxDyDz.set(0, 0, 0)
            self.__rotateAndZoom(dx, dy, dz)
        return

    def onRecreateDevice(self):
        self.__applyZoom(self.__zoom)
        return

    def applyImpulse(self, position, impulse, reason=ImpulseReason.ME_HIT):
        adjustedImpulse, noiseMagnitude = self.__dynamicCfg.adjustImpulse(impulse, reason)
        camMatrix = Matrix(self.__cam.matrix)
        impulseLocal = camMatrix.applyVector(adjustedImpulse)
        impulseAsYPR = Vector3(impulseLocal.x, -impulseLocal.y + impulseLocal.z, 0)
        rollPart = self.__dynamicCfg[b'impulsePartToRoll']
        impulseAsYPR.z = -rollPart * impulseAsYPR.x
        impulseAsYPR.x *= 1 - rollPart
        self.__impulseOscillator.applyImpulse(impulseAsYPR)
        self.__applyNoiseImpulse(noiseMagnitude)
        return

    def applyDistantImpulse(self, position, impulseValue, reason=ImpulseReason.ME_HIT):
        impulse = self.__cam.position - position
        distance = impulse.length
        if distance < 1.0:
            distance = 1.0
        impulse.normalise()
        if reason == ImpulseReason.OTHER_SHOT and distance <= self.__dynamicCfg[b'maxShotImpulseDistance']:
            impulse *= impulseValue / distance
        elif reason == ImpulseReason.SPLASH or reason == ImpulseReason.HE_EXPLOSION:
            impulse *= impulseValue / distance
        elif reason == ImpulseReason.VEHICLE_EXPLOSION and distance <= self.__dynamicCfg[b'maxExplosionImpulseDistance']:
            impulse *= impulseValue / distance
        else:
            return
        self.applyImpulse(position, impulse, reason)
        return

    def setMaxZoom(self):
        zooms = self.__getZooms()
        self.__zoom = zooms[-1]
        self._cfg[b'zoom'] = self.__zoom
        self.__applyZoom(self.__zoom)
        return

    def __applyNoiseImpulse(self, noiseMagnitude):
        noiseImpulse = math_utils.RandomVectors.random3(noiseMagnitude)
        self.__noiseOscillator.applyImpulse(noiseImpulse)
        return

    def __rotateAndZoom(self, dx, dy, dz):
        self.__aimingSystem.handleMovement(*calcYawPitchDelta(self._cfg, self.__curSense, dx, dy))
        self.__setupZoom(dz)
        return

    def __showVehicle(self, show):
        player = BigWorld.player()
        vehicle = player.getVehicleAttached()
        if vehicle is not None:
            LOG_DEBUG(b'__showVehicle: ', vehicle.id, show)
            vehicle.show(show)
        return

    def __setupCamera(self, targetPos):
        vehicleTypeDescriptor = BigWorld.player().vehicleTypeDescriptor
        playerGunMatFunction = AimingSystems.getPlayerGunMat
        if vehicleTypeDescriptor is not None and vehicleTypeDescriptor.isYawHullAimingAvailable:
            playerGunMatFunction = AimingSystems.getCenteredPlayerGunMat
        self.__aimingSystem.enable(targetPos, playerGunMatFunction)
        return

    def __waitVehicle(self):
        player = BigWorld.player()
        vehicle = player.getVehicleAttached()
        if vehicle is not None and vehicle.isStarted:
            self.__waitVehicleCallbackId = None
        else:
            self.__waitVehicleCallbackId = BigWorld.callback(0.1, self.__waitVehicle)
            return
        self.__showVehicle(False)
        return

    def __applySerializedZoom(self, zoomFactor):
        if BattleReplay.g_replayCtrl.isPlaying:
            if BattleReplay.g_replayCtrl.isControllingCamera:
                self.__applyZoom(zoomFactor)
        return

    def __updateZoom(self):
        cfg = self._cfg
        zooms = self.__getZooms()
        self.__zoom = cfg[b'zoom'] = math_utils.clamp(zooms[0], zooms[-1], self.__zoom)
        if self.camera is BigWorld.camera():
            self.delayCallback(0.0, self.__applyZoom, self.__zoom)
        return

    def __applyZoom(self, zoomFactor):
        self.__zoomFactor = zoomFactor
        if BattleReplay.g_replayCtrl.isRecording:
            BattleReplay.g_replayCtrl.serializeCallbackData(CallbackDataNames.APPLY_ZOOM, (zoomFactor,))
        FovExtended.instance().setFovByMultiplier(1 / zoomFactor)
        self.__updateCrosshairMatrix()
        return

    def __updateCrosshairMatrix(self):
        currentFov = BigWorld.projection().fov
        curClipPlaneScale = math.tan(currentFov / 2)
        aimMarkerDistance = self.__aimMarkerDistance * self._DEFAULT_CLIP_PLANE_SCALE / curClipPlaneScale
        self.__crosshairMatrix = createCrosshairMatrix(offsetFromNearPlane=aimMarkerDistance)
        return

    def __getZooms(self):
        zooms = self._cfg[b'zooms']
        if not self._cfg[b'increasedZoom']:
            zooms = zooms[:3]
        return zooms

    def __setupZoom(self, dz):
        if dz == 0:
            return
        else:
            zooms = self.__getZooms()
            prevZoom = self.__zoom
            if self.__zoom == zooms[0] and dz < 0 and self.__onChangeControlMode is not None:
                self.__onChangeControlMode(True)
            if dz > 0:
                for elem in zooms:
                    if self.__zoom < elem:
                        self.__zoom = elem
                        self._cfg[b'zoom'] = self.__zoom
                        break

            elif dz < 0:
                for i in range(len(zooms) - 1, -1, -1):
                    if self.__zoom > zooms[i]:
                        self.__zoom = zooms[i]
                        self._cfg[b'zoom'] = self.__zoom
                        break

            if prevZoom != self.__zoom:
                self.__applyZoom(self.__zoom)
            return

    def __cameraUpdate(self, allowModeChange=True):
        curTime = BigWorld.time()
        deltaTime = curTime - self.__prevTime
        self.__prevTime = curTime
        if not self.__autoUpdateDxDyDz.isZero():
            self.__rotateAndZoom(*self.__autoUpdateDxDyDz.tuple())
        self.__aimingSystem.update(deltaTime)
        localTransform, impulseTransform = self.__updateOscillators(deltaTime)
        zoom = self.__aimingSystem.overrideZoom(self.__zoom)
        aimMatrix = cameras.getAimMatrix(self.__defaultAimOffset.x, self.__defaultAimOffset.y)
        camMat = Matrix(aimMatrix)
        rodMat = math_utils.createTranslationMatrix(-self.__dynamicCfg[b'pivotShift'])
        antiRodMat = math_utils.createTranslationMatrix(self.__dynamicCfg[b'pivotShift'])
        camMat.postMultiply(rodMat)
        camMat.postMultiply(localTransform)
        camMat.postMultiply(antiRodMat)
        camMat.postMultiply(self.__aimingSystem.matrixProvider)
        camMat.invert()
        self.__cam.set(camMat)
        if zoom != self.__zoom:
            self.__zoom = zoom
            self.__applyZoom(self.__zoom)
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying and replayCtrl.isControllingCamera:
            aimOffset = replayCtrl.getAimClipPosition()
            binocularsOffset = aimOffset
            if not BigWorld.player().isForcedGuiControlMode() and GUI.mcursor().inFocus:
                GUI.mcursor().position = aimOffset
        else:
            aimOffset = self.__calcAimOffset(impulseTransform)
            binocularsOffset = self.__calcAimOffset()
            if replayCtrl.isRecording:
                replayCtrl.setAimClipPosition(aimOffset)
        self.__aimOffset = aimOffset
        self.__binoculars.setMaskCenter(binocularsOffset.x, binocularsOffset.y)
        player = BigWorld.player()
        if allowModeChange and (self.__isPositionUnderwater(self.__aimingSystem.matrixProvider.translation) or player.isGunLocked and not player.isObserverFPV):
            self.__onChangeControlMode(False)
            return -1
        return 0.0

    def __calcAimOffset(self, aimLocalTransform=None):
        aimingSystemMatrix = self.__aimingSystem.matrix
        worldCrosshair = Matrix(self.__crosshairMatrix)
        if aimLocalTransform is not None:
            worldCrosshair.postMultiply(aimLocalTransform)
        worldCrosshair.postMultiply(aimingSystemMatrix)
        aimOffset = cameras.projectPoint(worldCrosshair.translation)
        return Vector2(math_utils.clamp(-0.95, 0.95, aimOffset.x), math_utils.clamp(-0.95, 0.95, aimOffset.y))

    def __calcCurOscillatorAcceleration(self, deltaTime):
        vehicle = BigWorld.player().vehicle
        if vehicle is None or not vehicle.isAlive():
            return Vector3(0, 0, 0)
        else:
            curVelocity = vehicle.filter.velocity
            relativeSpeed = curVelocity.length / vehicle.typeDescriptor.physics[b'speedLimits'][0]
            if relativeSpeed >= SniperCamera._MIN_REL_SPEED_ACC_SMOOTHING:
                self.__accelerationSmoother.maxAllowedAcceleration = self.__dynamicCfg[b'accelerationThreshold']
            else:
                self.__accelerationSmoother.maxAllowedAcceleration = self.__dynamicCfg[b'accelerationMax']
            acceleration = self.__accelerationSmoother.update(vehicle, deltaTime)
            camMat = Matrix(self.__cam.matrix)
            acceleration = camMat.applyVector(-acceleration)
            accelSensitivity = self.__dynamicCfg[b'accelerationSensitivity']
            acceleration.x *= accelSensitivity.x
            acceleration.y *= accelSensitivity.y
            acceleration.z *= accelSensitivity.z
            oscillatorAcceleration = Vector3(0, -acceleration.y + acceleration.z, -acceleration.x)
            return oscillatorAcceleration

    def __updateOscillators(self, deltaTime):
        if not SniperCamera.isCameraDynamic():
            self.__impulseOscillator.reset()
            self.__movementOscillator.reset()
            self.__noiseOscillator.reset()
            return (
             math_utils.createRotationMatrix(math_utils.VectorConstant.Vector3Zero),
             math_utils.createRotationMatrix(math_utils.VectorConstant.Vector3Zero))
        oscillatorAcceleration = self.__calcCurOscillatorAcceleration(deltaTime)
        self.__movementOscillator.externalForce += oscillatorAcceleration
        self.__impulseOscillator.update(deltaTime)
        self.__movementOscillator.update(deltaTime)
        self.__noiseOscillator.update(deltaTime)
        noiseDeviation = Vector3(self.__noiseOscillator.deviation)
        deviation = self.__impulseOscillator.deviation + self.__movementOscillator.deviation + noiseDeviation
        oscVelocity = self.__impulseOscillator.velocity + self.__movementOscillator.velocity + self.__noiseOscillator.velocity
        if abs(deviation.x) < 1e-05 and abs(oscVelocity.x) < 0.0001:
            deviation.x = 0
        if abs(deviation.y) < 1e-05 and abs(oscVelocity.y) < 0.0001:
            deviation.y = 0
        if abs(deviation.z) < 1e-05 and abs(oscVelocity.z) < 0.0001:
            deviation.z = 0
        curZoomIdx = 0
        zooms = self._cfg[b'zooms']
        for idx in xrange(len(zooms)):
            if self.__zoom == zooms[idx]:
                curZoomIdx = idx
                break

        zoomExposure = self.__zoom * self.__dynamicCfg[b'zoomExposure'][curZoomIdx]
        deviation /= zoomExposure
        impulseDeviation = (self.__impulseOscillator.deviation + noiseDeviation) / zoomExposure
        self.__impulseOscillator.externalForce = Vector3(0)
        self.__movementOscillator.externalForce = Vector3(0)
        self.__noiseOscillator.externalForce = Vector3(0)
        return (
         math_utils.createRotationMatrix(Vector3(deviation.x, deviation.y, deviation.z)),
         math_utils.createRotationMatrix(impulseDeviation))

    def __isPositionUnderwater(self, position):
        return BigWorld.wg_collideWater(position, position + Vector3(0, 1, 0), False) > -1.0

    def reload(self):
        if not constants.IS_DEVELOPMENT:
            return
        import ResMgr
        ResMgr.purge(b'gui/avatar_input_handler.xml')
        cameraSec = ResMgr.openSection(b'gui/avatar_input_handler.xml/sniperMode/camera/')
        self._reloadConfigs(cameraSec)
        return

    def _readConfigs(self, dataSec):
        if not dataSec:
            LOG_WARNING(b'Invalid section <sniperMode/camera> in avatar_input_handler.xml')
        super(SniperCamera, self)._readConfigs(dataSec)
        dynamicsSection = dataSec[b'dynamics']
        self.__impulseOscillator = createOscillatorFromSection(dynamicsSection[b'impulseOscillator'])
        self.__movementOscillator = createOscillatorFromSection(dynamicsSection[b'movementOscillator'])
        self.__noiseOscillator = createOscillatorFromSection(dynamicsSection[b'randomNoiseOscillatorSpherical'])
        self.__dynamicCfg.readImpulsesConfig(dynamicsSection)
        self.__dynamicCfg[b'accelerationSensitivity'] = readVec3(dynamicsSection, b'accelerationSensitivity', (-1000, -1000, -1000), (1000, 1000, 1000), (0.5, 0.5, 0.5))
        accelerationThreshold = readFloat(dynamicsSection, b'accelerationThreshold', 0.0, 1000.0, 0.1)
        self.__dynamicCfg[b'accelerationThreshold'] = accelerationThreshold
        self.__dynamicCfg[b'accelerationMax'] = readFloat(dynamicsSection, b'accelerationMax', 0.0, 1000.0, 0.1)
        self.__dynamicCfg[b'maxShotImpulseDistance'] = readFloat(dynamicsSection, b'maxShotImpulseDistance', 0.0, 1000.0, 10.0)
        self.__dynamicCfg[b'maxExplosionImpulseDistance'] = readFloat(dynamicsSection, b'maxExplosionImpulseDistance', 0.0, 1000.0, 10.0)
        self.__dynamicCfg[b'impulsePartToRoll'] = readFloat(dynamicsSection, b'impulsePartToRoll', 0.0, 1000.0, 0.3)
        self.__dynamicCfg[b'pivotShift'] = Vector3(0, readFloat(dynamicsSection, b'pivotShift', -1000, 1000, -0.5), 0)
        self.__dynamicCfg[b'aimMarkerDistance'] = readFloat(dynamicsSection, b'aimMarkerDistance', -1000, 1000, 1.0)
        rawZoomExposure = dynamicsSection.readString(b'zoomExposure', b'0.6 0.5 0.4 0.3 0.2')
        self.__dynamicCfg[b'zoomExposure'] = [float(x) for x in rawZoomExposure.split()]
        accelerationFilter = math_utils.RangeFilter(self.__dynamicCfg[b'accelerationThreshold'], self.__dynamicCfg[b'accelerationMax'], 100, math_utils.SMAFilter(SniperCamera._FILTER_LENGTH))
        maxAccelerationDuration = readFloat(dynamicsSection, b'maxAccelerationDuration', 0.0, 10000.0, SniperCamera._DEFAULT_MAX_ACCELERATION_DURATION)
        self.__accelerationSmoother = AccelerationSmoother(accelerationFilter, maxAccelerationDuration)
        return

    def _readBaseCfg(self, dataSec):
        bcfg = self._baseCfg
        bcfg[b'keySensitivity'] = readFloat(dataSec, b'keySensitivity', 0, 10, 0.005)
        bcfg[b'sensitivity'] = readFloat(dataSec, b'sensitivity', 0, 10, 0.005)
        bcfg[b'scrollSensitivity'] = readFloat(dataSec, b'scrollSensitivity', 0, 10, 0.005)
        zooms = dataSec.readString(b'zooms', b'2 4 8 16 25')
        bcfg[b'zooms'] = [float(x) for x in zooms.split()]
        return

    def _readUserCfg(self):
        bcfg = self._baseCfg
        ucfg = self._userCfg
        dataSec = Settings.g_instance.userPrefs[Settings.KEY_CONTROL_MODE]
        if dataSec is not None:
            dataSec = dataSec[b'sniperMode/camera']
        ucfg[b'horzInvert'] = False
        ucfg[b'vertInvert'] = False
        ucfg[b'increasedZoom'] = True
        ucfg[b'sniperModeByShift'] = False
        ucfg[b'zoom'] = readFloat(dataSec, b'zoom', bcfg[b'zooms'][0], bcfg[b'zooms'][-1], bcfg[b'zooms'][0])
        ucfg[b'keySensitivity'] = readFloat(dataSec, b'keySensitivity', 0.0, 10.0, 1.0)
        ucfg[b'sensitivity'] = readFloat(dataSec, b'sensitivity', 0.0, 10.0, 1.0)
        ucfg[b'scrollSensitivity'] = readFloat(dataSec, b'scrollSensitivity', 0.0, 10.0, 1.0)
        return

    def _makeCfg(self):
        bcfg = self._baseCfg
        ucfg = self._userCfg
        cfg = self._cfg
        cfg[b'keySensitivity'] = bcfg[b'keySensitivity']
        cfg[b'sensitivity'] = bcfg[b'sensitivity']
        cfg[b'scrollSensitivity'] = bcfg[b'scrollSensitivity']
        cfg[b'zooms'] = bcfg[b'zooms']
        cfg[b'keySensitivity'] *= ucfg[b'keySensitivity']
        cfg[b'sensitivity'] *= ucfg[b'sensitivity']
        cfg[b'scrollSensitivity'] *= ucfg[b'scrollSensitivity']
        cfg[b'horzInvert'] = ucfg[b'horzInvert']
        cfg[b'vertInvert'] = ucfg[b'vertInvert']
        cfg[b'zoom'] = ucfg[b'zoom']
        cfg[b'increasedZoom'] = ucfg[b'increasedZoom']
        cfg[b'sniperModeByShift'] = ucfg[b'sniperModeByShift']
        return

    def writeUserPreferences(self):
        ds = Settings.g_instance.userPrefs
        if not ds.has_key(Settings.KEY_CONTROL_MODE):
            ds.write(Settings.KEY_CONTROL_MODE, b'')
        ucfg = self._userCfg
        ds = ds[Settings.KEY_CONTROL_MODE]
        ds.writeBool(b'sniperMode/camera/horzInvert', ucfg[b'horzInvert'])
        ds.writeBool(b'sniperMode/camera/vertInvert', ucfg[b'vertInvert'])
        ds.writeFloat(b'sniperMode/camera/keySensitivity', ucfg[b'keySensitivity'])
        ds.writeFloat(b'sniperMode/camera/sensitivity', ucfg[b'sensitivity'])
        ds.writeFloat(b'sniperMode/camera/scrollSensitivity', ucfg[b'scrollSensitivity'])
        ds.writeFloat(b'sniperMode/camera/zoom', self._cfg[b'zoom'])
        return

    def _updateSettingsFromServer(self):
        super(SniperCamera, self)._updateSettingsFromServer()
        if self.settingsCore.isReady:
            ucfg = self._userCfg
            ucfg[b'increasedZoom'] = self.settingsCore.getSetting(b'increasedZoom')
            ucfg[b'sniperModeByShift'] = self.settingsCore.getSetting(b'sniperModeByShift')
            cfg = self._cfg
            cfg[b'increasedZoom'] = ucfg[b'increasedZoom']
            cfg[b'sniperModeByShift'] = ucfg[b'sniperModeByShift']
            self.__updateZoom()
        return
