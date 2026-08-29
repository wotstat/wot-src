import math
from collections import defaultdict
import BigWorld, Math
from Math import Vector3, Matrix
import math_utils
from AvatarInputHandler.cameras import readVec3, ICamera, readFloat, ImpulseReason
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

def createCrosshairMatrix(offsetFromNearPlane):
    nearPlane = BigWorld.projection().nearPlane
    return math_utils.createTranslationMatrix(Vector3(0, 0, nearPlane + offsetFromNearPlane))


def createOscillatorFromSection(oscillatorSection, constraintsAsAngle=True):
    constraints = readVec3(oscillatorSection, b'constraints', (0.0, 0.0, 0.0), (175.0, 175.0, 175.0), 10.0)
    if constraintsAsAngle:
        constraints = Vector3((math.radians(constraints.x),
         math.radians(constraints.y),
         math.radians(constraints.z)))
    constructorParams = {b'oscillator': __getOscillatorParams, 
       b'noiseOscillator': __getNoiseOscillatorParams, 
       b'randomNoiseOscillatorFlat': __getRandomNoiseOscillatorFlatParams, 
       b'randomNoiseOscillatorSpherical': __getRandomNoiseOscillatorSphericalParams}.get(oscillatorSection.name, __getOscillatorParams)(oscillatorSection)
    oscillator = None
    if oscillatorSection.name == b'noiseOscillator':
        oscillator = Math.PyNoiseOscillator(*constructorParams)
    elif oscillatorSection.name == b'randomNoiseOscillatorFlat':
        oscillator = Math.PyRandomNoiseOscillatorFlat(*constructorParams)
    elif oscillatorSection.name == b'randomNoiseOscillatorSpherical':
        oscillator = Math.PyRandomNoiseOscillatorSpherical(*constructorParams)
    else:
        constructorParams.append(constraints)
        oscillator = Math.PyOscillator(*constructorParams)
    return oscillator


def calcYawPitchDelta(cfg, curSense, dx, dy):
    return (
     dx * curSense * (-1 if cfg[b'horzInvert'] else 1),
     dy * curSense * (-1 if cfg[b'vertInvert'] else 1))


def __getOscillatorParams(oscillatorSection):
    return [
     readFloat(oscillatorSection, b'mass', 1e-05, 9000, 3.5),
     readVec3(oscillatorSection, b'stiffness', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 60.0),
     readVec3(oscillatorSection, b'drag', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 9.0)]


def __getNoiseOscillatorParams(oscillatorSection):
    return [
     readFloat(oscillatorSection, b'mass', 1e-05, 9000, 3.5),
     readVec3(oscillatorSection, b'stiffness', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 60.0),
     readVec3(oscillatorSection, b'drag', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 9.0)]


def __getRandomNoiseOscillatorFlatParams(oscillatorSection):
    return [
     readFloat(oscillatorSection, b'mass', 1e-05, 9000, 3.5),
     readFloat(oscillatorSection, b'stiffness', 1e-05, 9000, 3.5),
     readFloat(oscillatorSection, b'drag', 1e-05, 9000, 3.5)]


def __getRandomNoiseOscillatorSphericalParams(oscillatorSection):
    oscillatorParams = __getRandomNoiseOscillatorFlatParams(oscillatorSection)
    oscillatorParams.append(readVec3(oscillatorSection, b'scaleCoeff', Vector3(0.0), Vector3(9000), Vector3(1.0)))
    return oscillatorParams


class CameraDynamicConfig(dict):
    REASONS_AS_STR = {(ImpulseReason.MY_SHOT): b'shot', 
       (ImpulseReason.ME_HIT): b'hit', 
       (ImpulseReason.OTHER_SHOT): b'otherShot', 
       (ImpulseReason.SPLASH): b'splash', 
       (ImpulseReason.COLLISION): b'collision', 
       (ImpulseReason.VEHICLE_EXPLOSION): b'vehicleExplosion', 
       (ImpulseReason.PROJECTILE_HIT): b'projectileHit', 
       (ImpulseReason.HE_EXPLOSION): b'vehicleExplosion'}

    def readImpulsesConfig(self, rootDataSec):
        self.__readReasonProjection(b'impulseSensitivities', rootDataSec)
        self.__readReasonProjection(b'noiseSensitivities', rootDataSec)
        self.__readReasonProjection(b'impulseLimits', rootDataSec, True)
        self.__readReasonProjection(b'noiseLimits', rootDataSec, True)
        return

    def __readReasonProjection(self, projectionName, rootDataSec, asMinMax=False):
        self[projectionName] = impulseDict = {}
        projectionDataSec = rootDataSec[projectionName]
        if projectionDataSec is None:
            return
        else:
            for reason, reasonStr in CameraDynamicConfig.REASONS_AS_STR.iteritems():
                reasonLimitSec = projectionDataSec[reasonStr]
                if reasonLimitSec is not None:
                    if asMinMax:
                        impulseDict[reason] = reasonLimitSec.asVector2
                    else:
                        impulseDict[reason] = reasonLimitSec.asFloat

            return

    def adjustImpulse(self, impulse, reason):
        impulseSensitivity = self[b'impulseSensitivities'].get(reason, 0.0)
        noiseImpulseSensitivity = self[b'noiseSensitivities'].get(reason, 0.0)
        resultImpulse = impulse * impulseSensitivity
        impulseMinMax = self[b'impulseLimits'].get(reason, None)
        if impulseMinMax is not None:
            resultImpulse = math_utils.clampVectorLength(impulseMinMax[0], impulseMinMax[1], resultImpulse)
        noiseMagnitude = impulse.length * noiseImpulseSensitivity
        noiseMinMax = self[b'noiseLimits'].get(reason, None)
        if noiseMinMax is not None:
            noiseMagnitude = math_utils.clamp(noiseMinMax[0], noiseMinMax[1], noiseMagnitude)
        return (resultImpulse, noiseMagnitude)


class AccelerationSmoother(object):

    def __setMaxAllowedAcc(self, value):
        self.__accelerationFilter.maxLength = value
        return

    acceleration = property((lambda self: self.__acceleration))
    maxAllowedAcceleration = property((lambda self: self.__accelerationFilter.maxLength), __setMaxAllowedAcc)
    hasChangedDirection = property((lambda self: self.__hasChangedDirection))
    timeLapsed = property((lambda self: self.__timeLapsedSinceDirChange))

    def __init__(self, accelerationFilter, maxAccelerationDuration):
        self.__accelerationFilter = accelerationFilter
        self.__acceleration = Vector3(0)
        self.__prevMovementFlags = 0
        self.__prevVelocity = Vector3(0)
        self.__hasChangedDirection = False
        self.__maxAccelerationDuration = maxAccelerationDuration
        self.__timeLapsedSinceDirChange = 0.0
        return

    def reset(self):
        self.__accelerationFilter.reset()
        self.__acceleration = Vector3(0)
        self.__prevMovementFlags = 0
        self.__hasChangedDirection = False
        return

    def update(self, vehicle, deltaTime):
        try:
            curVelocity = vehicle.filter.velocity
            acceleration = vehicle.filter.acceleration
            acceleration = self.__accelerationFilter.add(acceleration)
            movementFlags = vehicle.engineMode[1]
            moveMask = 3
            self.__hasChangedDirection = movementFlags & moveMask ^ self.__prevMovementFlags & moveMask or curVelocity.dot(self.__prevVelocity) <= 0.01
            self.__prevMovementFlags = movementFlags
            self.__prevVelocity = curVelocity
            self.__timeLapsedSinceDirChange += deltaTime
            if self.__hasChangedDirection:
                self.__timeLapsedSinceDirChange = 0.0
            elif self.__timeLapsedSinceDirChange > self.__maxAccelerationDuration:
                invVehMat = Matrix(vehicle.matrix)
                invVehMat.invert()
                accelerationRelativeToVehicle = invVehMat.applyVector(acceleration)
                accelerationRelativeToVehicle.x = 0.0
                accelerationRelativeToVehicle.z = 0.0
                acceleration = Matrix(vehicle.matrix).applyVector(accelerationRelativeToVehicle)
            self.__acceleration = acceleration
            return acceleration
        except Exception:
            return Math.Vector3(0.0, 0.0, 0.0)

        return


class CameraWithSettings(ICamera):
    settingsCore = dependency.descriptor(ISettingsCore)
    __baseConfigs = defaultdict(dict)
    __userConfigs = defaultdict(dict)
    __configs = defaultdict(dict)

    @property
    def _baseCfg(self):
        return CameraWithSettings.__baseConfigs[self._getConfigsKey()]

    @property
    def _userCfg(self):
        return CameraWithSettings.__userConfigs[self._getConfigsKey()]

    @property
    def _cfg(self):
        return CameraWithSettings.__configs[self._getConfigsKey()]

    def create(self, **args):
        self._updateSettingsFromServer()
        self.settingsCore.onSettingsChanged += self._handleSettingsChange
        self.settingsCore.onSettingsReady += self._updateSettingsFromServer
        return

    def destroy(self):
        self.settingsCore.onSettingsChanged -= self._handleSettingsChange
        self.settingsCore.onSettingsReady -= self._updateSettingsFromServer
        return

    def getConfigValue(self, name):
        return self._cfg.get(name)

    def getUserConfigValue(self, name):
        return self._userCfg.get(name)

    def setUserConfigValue(self, name, value):
        if name not in self._userCfg:
            return
        self._userCfg[name] = value
        if name not in (b'keySensitivity', b'sensitivity', b'scrollSensitivity'):
            self._cfg[name] = self._userCfg[name]
        else:
            self._cfg[name] = self._baseCfg[name] * self._userCfg[name]
        return

    @staticmethod
    def _getConfigsKey():
        raise NotImplementedError
        return

    def _handleSettingsChange(self, diff):
        return

    def _updateSettingsFromServer(self):
        if self.settingsCore.isReady:
            ucfg = self._userCfg
            ucfg[b'horzInvert'] = self.settingsCore.getSetting(b'mouseHorzInvert')
            ucfg[b'vertInvert'] = self.settingsCore.getSetting(b'mouseVertInvert')
            cfg = self._cfg
            cfg[b'horzInvert'] = ucfg[b'horzInvert']
            cfg[b'vertInvert'] = ucfg[b'vertInvert']
        return

    def _readConfigs(self, dataSection):
        if not self._baseCfg:
            self._readBaseCfg(dataSection)
        if not self._userCfg:
            self._readUserCfg()
        if not self._cfg:
            self._makeCfg()
        return

    def _readBaseCfg(self, dataSection):
        return

    def _readUserCfg(self):
        return

    def _makeCfg(self):
        return

    def _reloadConfigs(self, dataSection):
        self._baseCfg.clear()
        self._userCfg.clear()
        self._cfg.clear()
        self._readConfigs(dataSection)
        return


class SPGScrollSmoother(object):
    __slots__ = (b'__smoothingTime', b'__easing', b'__isEnabled', b'__targetValue', b'__isStarted')

    def __init__(self, smoothingTime):
        self.__smoothingTime = smoothingTime
        self.__easing = math_utils.Easing.exponentialEasing(0.0, 0.0, self.__smoothingTime)
        self.__isEnabled = False
        self.__targetValue = 0.0
        self.__isStarted = False
        return

    def start(self, value):
        self.__isStarted = True
        self.__easing.reset(value, value, self.__smoothingTime)
        self.__targetValue = value
        return

    def stop(self):
        self.__isStarted = False
        self.__easing.reset(self.__targetValue, self.__targetValue, self.__smoothingTime)
        return

    def setIsEnabled(self, isEnabled):
        self.__isEnabled = isEnabled
        if self.__isStarted:
            self.__easing.reset(self.__targetValue, self.__targetValue, self.__smoothingTime)
        return

    def moveTo(self, value, limits):
        value = math_utils.clamp(limits[0], limits[1], value)
        if self.__isEnabled and self.__isStarted:
            if not math_utils.almostZero(value - self.__targetValue):
                self.__easing.reset(self.getCurrentValue(), value, self.__smoothingTime)
                self.__targetValue = value
        else:
            self.__targetValue = value
        return

    def update(self, dt):
        if self.__isEnabled and self.__isStarted:
            return self.__easing.update(dt)
        return self.__targetValue

    def setTime(self, smoothingTime):
        self.__smoothingTime = smoothingTime
        return

    def getCurrentValue(self):
        if self.__isEnabled and self.__isStarted:
            return self.__easing.value
        return self.__targetValue
