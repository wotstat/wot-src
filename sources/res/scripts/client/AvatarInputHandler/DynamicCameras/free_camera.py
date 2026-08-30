import GUI, BigWorld, Settings, logging, ResMgr, BattleReplay, constants, Math, math_utils, Keys, random, math, CommandMapping
from gui.shared.utils.key_mapping import getVirtualKey
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from Math import Vector3
from AvatarInputHandler.VideoCamera import VideoCamera, _InertiaScalar, KeySensor, _AlignerToLand
from AvatarInputHandler.DynamicCameras import CameraWithSettings
from AvatarInputHandler.cameras import readFloat
from debug_utils import LOG_WARNING
from helpers import isPlayerAvatar
_logger = logging.getLogger(__name__)
_DEFAULT_SPEED_LEVEL_LIMITS = (7, 13, 19)

def getCameraAsSettingsHolder(settingsDataSec):
    return FreeVideoCamera(settingsDataSec)


class FreeVideoCamera(VideoCamera, CameraWithSettings):
    camera = property((lambda self: self._cam))
    aimingSystem = property((lambda self: None))

    def __init__(self, configDataSec):
        self._sensitivityLimit = None
        self.__selectedTargetID = None
        self._collisionKeys = set()
        self.__maxPitch = 0.0
        self.__minPitch = 0.0
        self.__speedIfCollision = 0.0
        self.__skipFlags = 2 | 4 | 1
        self.__randomDir = None
        self.__acObstacleForwardCheckDistance = 0.0
        self.__acCameraColliderRadius = 0.0
        self.__bounceMultiplier = 1.0
        self.__isCollisionBouncing = False
        self.__collisionDetected = False
        self._readConfigs(configDataSec)
        super(FreeVideoCamera, self).__init__(configDataSec)
        self.__updateProperties()
        return

    def getAlignerToLandClass(self):
        return _VariableHeightAlignerToLand

    def destroy(self):
        super(FreeVideoCamera, self).destroy()
        CommandMapping.g_instance.onMappingChanged -= self.__onMappingChanged
        self._sensitivityLimit = None
        return

    def enable(self, **args):
        super(FreeVideoCamera, self).enable(**args)
        self.__initMovementSensors()
        self._alignerToLand.updateLandHeight(self._position, 0.0)
        self._alignerToLand.enableWithFixedHeight(self._position, self.__heightAboveTerrain)
        self._alignerToLand.setCollisionSkipFlags(self.__skipFlags)
        self._isVerticalVelocitySeparated = True
        if isPlayerAvatar():
            BigWorld.player().positionControl.moveTo(self._cam.position)
            BigWorld.player().positionControl.followCamera(True)
        CommandMapping.g_instance.onMappingChanged += self.__onMappingChanged
        self.__onMappingChanged()
        return

    def disable(self):
        if self._heightAboveGroundSensor:
            self._heightAboveGroundSensor.reset(Math.Vector3())
        super(FreeVideoCamera, self).disable()
        return

    def setHeight(self, height):
        self._alignerToLand.enableWithFixedHeight(self._position, height)
        return

    def setMinMaxHeight(self, minHeight, maxHeight):
        self._alignerToLand.setMinMaxHeight(minHeight, maxHeight)
        return

    def handleKeyEvent(self, key, isDown):
        if key is None:
            return False
        else:
            if isDown:
                self._collisionKeys.add(key)
            elif key in self._collisionKeys:
                self._collisionKeys.remove(key)
            return self._heightAboveGroundSensor.handleKeyEvent(key, isDown) or self._sensitivityLimit.handleKeyEvent(key, isDown) or super(FreeVideoCamera, self)._handleMoveAndSensitivityKeys(key, isDown)

    def handleMouseEvent(self, dx, dy, dz):
        if self.getCameraTransition().isInTransition():
            return
        relativeSenseGrowth = self._rotationSensor.sensitivity / self._rotationSensor.defaultSensitivity
        self._rotationSensor.addVelocity(Math.Vector3(dx, dy, 0) * self._mouseSensitivity * relativeSenseGrowth)
        self._heightAboveGroundSensor.addVelocity(dz * self._heightAboveGroundSensor.sensitivity * self._scrollSensitivity)
        GUI.mcursor().position = Math.Vector2(0, 0)
        return

    def reload(self):
        if not constants.IS_DEVELOPMENT:
            return
        ResMgr.purge(b'gui/avatar_input_handler.xml')
        cameraSec = ResMgr.openSection(b'gui/avatar_input_handler.xml/freeVideoMode/camera/')
        self._readCfg(cameraSec)
        return

    def writeUserPreferences(self):
        ds = Settings.g_instance.userPrefs
        if not ds.has_key(Settings.KEY_CONTROL_MODE):
            ds.write(Settings.KEY_CONTROL_MODE, b'')
        ucfg = self._userCfg
        ds = ds[Settings.KEY_CONTROL_MODE]
        ds.writeBool(b'freeVideoMode/camera/horzInvert', ucfg[b'horzInvert'])
        ds.writeBool(b'freeVideoMode/camera/vertInvert', ucfg[b'vertInvert'])
        ds.writeFloat(b'freeVideoMode/camera/keySensitivity', ucfg[b'keySensitivity'])
        ds.writeFloat(b'freeVideoMode/camera/sensitivity', ucfg[b'sensitivity'])
        ds.writeFloat(b'freeVideoMode/camera/scrollSensitivity', ucfg[b'scrollSensitivity'])
        return

    def _readConfigs(self, dataSec):
        if dataSec is None:
            LOG_WARNING(b'Invalid section <freeVideoMode/camera> in avatar_input_handler.xml')
        super(FreeVideoCamera, self)._readConfigs(dataSec)
        return

    def _readCfg(self, configDataSec):
        super(FreeVideoCamera, self)._readCfg(configDataSec)
        self._inertiaEnabled = configDataSec.readBool(b'inertiaEnabled', True)
        self._heightInertia = _InertiaScalar(configDataSec.readFloat(b'linearFriction', 0.1))
        self._readRotationSettings(configDataSec, {})
        self._readZoomSettings(configDataSec, {})
        self.__heightAboveTerrain = configDataSec.readFloat(b'heightAboveTerrain', 50.0)
        self.setHeight(self.__heightAboveTerrain)
        self.setMinMaxHeight(configDataSec.readFloat(b'heightAboveTerrainMin', 10.0), configDataSec.readFloat(b'heightAboveTerrainMax', 120.0))
        self.__readCollisionSettings(configDataSec)
        return

    def _readBaseCfg(self, dataSec):
        bcfg = self._baseCfg
        bcfg[b'keySensitivity'] = readFloat(dataSec, b'keySensitivity', 0, 10, 0.01)
        bcfg[b'sensitivity'] = readFloat(dataSec, b'sensitivity', 0, 10, 0.01)
        bcfg[b'scrollSensitivity'] = readFloat(dataSec, b'scrollSensitivity', 0, 10, 0.01)
        return

    def _readUserCfg(self):
        ucfg = self._userCfg
        dataSec = Settings.g_instance.userPrefs[Settings.KEY_CONTROL_MODE]
        if dataSec is not None:
            dataSec = dataSec[b'freeVideoMode/camera']
        ucfg[b'horzInvert'] = False
        ucfg[b'vertInvert'] = False
        ucfg[b'sniperModeByShift'] = False
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
        cfg[b'horzInvert'] = ucfg[b'horzInvert']
        cfg[b'vertInvert'] = ucfg[b'vertInvert']
        cfg[b'keySensitivity'] *= ucfg[b'keySensitivity']
        cfg[b'sensitivity'] *= ucfg[b'sensitivity']
        cfg[b'scrollSensitivity'] *= ucfg[b'scrollSensitivity']
        return

    @staticmethod
    def _getConfigsKey():
        return FreeVideoCamera.__name__

    def setUserConfigValue(self, name, value):
        super(FreeVideoCamera, self).setUserConfigValue(name, value)
        self.__updateProperties()
        return

    def __updateProperties(self):
        self._mouseSensitivity = self._cfg[b'sensitivity']
        self._scrollSensitivity = self._cfg[b'scrollSensitivity']
        self._horzInvert = self._cfg[b'horzInvert']
        self._vertInvert = self._cfg[b'vertInvert']
        return

    def _readMovementSettings(self, configDataSec):
        movementMappings = dict()
        movementMappings[getattr(Keys, getVirtualKey(CommandMapping.CMD_ROTATE_LEFT))] = Math.Vector3(-1, 0, 0)
        movementMappings[getattr(Keys, getVirtualKey(CommandMapping.CMD_ROTATE_RIGHT))] = Math.Vector3(1, 0, 0)
        movementMappings[getattr(Keys, getVirtualKey(CommandMapping.CMD_MOVE_FORWARD))] = Math.Vector3(0, 0, 1)
        movementMappings[getattr(Keys, getVirtualKey(CommandMapping.CMD_MOVE_BACKWARD))] = Math.Vector3(0, 0, -1)
        linearSensitivity = configDataSec.readFloat(b'linearVelocity', 40.0)
        linearSensitivityAcc = configDataSec.readFloat(b'linearVelocityAcceleration', 10.0)
        self._movementSensor = _SensitivityLimitKeySensor(movementMappings, linearSensitivity, None, linearSensitivityAcc)
        self._movementSensor.currentVelocity = Math.Vector3()
        self._verticalMovementSensor = KeySensor({}, linearSensitivity, None, linearSensitivityAcc)
        speedVertical = configDataSec.readFloat(b'speedVertical', 1.0)
        heightChangeMappings = dict()
        heightChangeMappings[getattr(Keys, configDataSec.readString(b'keyMoveUp', b'KEY_SPACE'))] = speedVertical
        heightChangeMappings[getattr(Keys, configDataSec.readString(b'keyMoveDown', b'KEY_LSHIFT'))] = -speedVertical
        self._heightAboveGroundSensor = _SensitivityLimitKeySensor(heightChangeMappings, linearSensitivity, None, linearSensitivityAcc)
        self._heightAboveGroundSensor.reset(Math.Vector3())
        sensitivityLimits = map(int, configDataSec.readString(b'sensitivityLimits', b'').split())
        if not sensitivityLimits:
            sensitivityLimits = _DEFAULT_SPEED_LEVEL_LIMITS
        speedChangeKeyMappings = dict()
        speedChangeKeyMappings[getattr(Keys, configDataSec.readString(b'keySelectSpeed1', b'KEY_1'))] = sensitivityLimits[0]
        speedChangeKeyMappings[getattr(Keys, configDataSec.readString(b'keySelectSpeed2', b'KEY_2'))] = sensitivityLimits[1]
        speedChangeKeyMappings[getattr(Keys, configDataSec.readString(b'keySelectSpeed3', b'KEY_3'))] = sensitivityLimits[2]
        self._sensitivityLimit = _SensitivityLimit(sensitivityLimits[1], self._movementSensor, speedChangeKeyMappings)
        self._alignerToLand.avgLandHeightUpdateSpeed = configDataSec.readFloat(b'cameraHeightAdjustmentSpeed', 1)
        self._alignerToLand.setupLandFindingConfig(2, 1000)
        return

    def _readRotationSettings(self, configDataSec, rotationMappings):
        rotationSensitivity = configDataSec.readFloat(b'angularVelocity', 0.7)
        self._rotationSensor = KeySensor(rotationMappings, rotationSensitivity)
        self._rotationSensor.currentVelocity = Math.Vector3()
        return

    def _checkSpaceBounds(self, startPos, endPos):
        from ClientArena import CollisionResult
        if not isPlayerAvatar():
            return endPos
        moveDir = endPos - startPos
        moveDir.normalise()
        collisionResult, _ = BigWorld.player().arena.collideWithArenaBB(startPos, endPos)
        if collisionResult == CollisionResult.INTERSECTION:
            return BigWorld.player().arena.getClosestPointOnArenaBB(endPos)
        if collisionResult == CollisionResult.OUTSIDE:
            onBorder = BigWorld.player().arena.getClosestPointOnArenaBB(endPos)
            offset = onBorder - endPos
            offset.normalise()
            return onBorder + offset
        return endPos

    def _update(self):
        VideoCamera._update(self)
        self._ypr[1] = math_utils.clamp(self.__minPitch, self.__maxPitch, self._ypr[1])
        if BattleReplay.g_replayCtrl.isPlaying:
            avatarPosition = Math.Vector3(BigWorld.player().position)
            self._setupCameraViewProvider(self._ypr, avatarPosition)
        else:
            self._setupCameraViewProvider(self._ypr, self._position)
        return 0.0

    def _isKeyPressed(self, mapping, defaultKey):
        key = CommandMapping.g_instance.getCommandKeys(mapping)
        key = key[0] if key else defaultKey
        return key in self._collisionKeys

    def _handleCollision(self, vel):
        vel = super(FreeVideoCamera, self)._handleCollision(vel)
        vel.x = 0 if math_utils.almostZero(vel.x, 0.001) else vel.x
        vel.y = 0 if math_utils.almostZero(vel.y, 0.001) else vel.y
        vel.z = 0 if math_utils.almostZero(vel.z, 0.001) else vel.z
        forwardKeyPressed = self._isKeyPressed(CommandMapping.CMD_MOVE_FORWARD, Keys.KEY_W)
        backwardKeyPressed = self._isKeyPressed(CommandMapping.CMD_MOVE_BACKWARD, Keys.KEY_S)
        if not backwardKeyPressed and forwardKeyPressed:
            lookDir = Vector3(self._cam.direction.x, 0, self._cam.direction.z)
            lookDir.normalise()
            vel = self.__handleAdvancedCollision(self._position, lookDir, vel)
        delta = self.measureDeltaTime()
        collisionPreviouslyDetected = self.__collisionDetected
        self.__collisionDetected = self._cam.checkCollision(self._position, vel * delta)
        self.__collided = not collisionPreviouslyDetected and self.__collisionDetected
        if self.__collisionDetected:
            if self.__collided and not self.__isCollisionBouncing:
                self.__isCollisionBouncing = True
                bounceVal = 1.5 * self.__bounceMultiplier
                vel -= Vector3(vel.x * bounceVal, vel.y, vel.z * bounceVal)
            else:
                self.__isCollisionBouncing = False
                vel = Vector3(0, 0, 0)
        return vel

    def __readCollisionSettings(self, configDataSec):
        self.__speedIfCollision = configDataSec.readFloat(b'speedIfColliding', 20.0)
        self.__maxPitch = math.radians(configDataSec.readFloat(b'maxPitch', 80.0))
        self.__minPitch = math.radians(configDataSec.readFloat(b'minPitch', -80.0))
        self.__bounceMultiplier = configDataSec.readFloat(b'collisionBounceMultiplier', 1.0)
        advancedCollisionSettings = configDataSec[b'advancedCollision']
        self.__acObstacleForwardCheckDistance = advancedCollisionSettings.readFloat(b'obstacleForwardCheckDistance', 10.0)
        self.__acCameraColliderRadius = advancedCollisionSettings.readFloat(b'cameraColliderRadius', 3.0)
        return

    def __getSideCollisions(self, lookPoint, pos, rightVector, raycastSideOffset):
        leftRayEndPoint = lookPoint - rightVector * raycastSideOffset
        leftRayOffset = Vector3(leftRayEndPoint - pos)
        leftRayOffset.normalise()
        rightRayEndPoint = lookPoint + rightVector * raycastSideOffset
        rightRayOffset = Vector3(rightRayEndPoint - pos)
        rightRayOffset.normalise()
        for i in range(5):
            leftCol = self.__raycastTo(leftRayEndPoint + leftRayOffset * (i + 1), self.__skipFlags)
            rightCol = self.__raycastTo(rightRayEndPoint + rightRayOffset * (i + 1), self.__skipFlags)
            if leftCol is not None or rightCol is not None:
                return (leftCol, rightCol)

        leftRayEndPoint = self._position - rightVector * raycastSideOffset
        leftRayOffset = Vector3(leftRayEndPoint - pos)
        leftRayOffset.normalise()
        rightRayEndPoint = self._position + rightVector * raycastSideOffset
        rightRayOffset = Vector3(rightRayEndPoint - pos)
        rightRayOffset.normalise()
        for i in range(3):
            leftCol = self.__raycastTo(leftRayEndPoint + leftRayOffset * (i + 1), self.__skipFlags)
            rightCol = self.__raycastTo(rightRayEndPoint + rightRayOffset * (i + 1), self.__skipFlags)
            if leftCol is not None or rightCol is not None:
                return (leftCol, rightCol)

        return (None, None)

    def __initMovementSensors(self):
        specCtrl = self.guiSessionProvider.shared.spectator
        if specCtrl is None:
            return
        else:
            self._movementSensor.setCallback(specCtrl.freeCamMoved)
            self._heightAboveGroundSensor.setCallback(specCtrl.freeCamVerticalMoved)
            return

    def __handleAdvancedCollision(self, pos, lookDir, vel):
        frustumHeight = 2.0 * self.__acObstacleForwardCheckDistance * math.tan(BigWorld.projection().fov * 0.5)
        frustumWidth = frustumHeight * BigWorld.getAspectRatio()
        raycastOffset = frustumWidth / 4
        upVector = Vector3(0, 1, 0)
        rightVector = Vector3(lookDir * upVector)
        rightVector.normalise()
        lookPoint = Vector3(pos + lookDir * self.__acObstacleForwardCheckDistance)
        frontCol = self.__raycastTo(lookPoint, self.__skipFlags)
        leftCol, rightCol = self.__getSideCollisions(lookPoint, pos, rightVector, raycastOffset)
        leftKeyPressed = self._isKeyPressed(CommandMapping.CMD_ROTATE_LEFT, Keys.KEY_A)
        rightKeyPressed = self._isKeyPressed(CommandMapping.CMD_ROTATE_RIGHT, Keys.KEY_D)
        if frontCol:
            moveDir = Vector3(frontCol[5] * upVector)
            if leftCol and rightCol:
                leftCol, rightCol = self.__getSideCollisions(lookPoint, pos, rightVector, raycastOffset * 2)
            if not leftCol and not rightCol:
                if not self.__randomDir:
                    self.__randomDir = moveDir * (1 if random.random() < 0.5 else -1)
                return self.__randomDir * self.__speedIfCollision
            if not leftCol:
                return moveDir * self.__speedIfCollision
            if not rightCol:
                return moveDir * -self.__speedIfCollision
            if leftKeyPressed:
                return moveDir * -self.__speedIfCollision
            if rightKeyPressed:
                return moveDir * self.__speedIfCollision
            return Vector3(0, 0, 0)
        else:
            if leftKeyPressed and rightCol and not leftCol:
                moveDir = Vector3(rightCol[5] * upVector)
                return moveDir * self.__speedIfCollision
            if rightKeyPressed and leftCol and not rightCol:
                moveDir = Vector3(leftCol[5] * upVector)
                return moveDir * -self.__speedIfCollision
            self.__randomDir = None
            return vel

    def __raycastTo(self, end, skipFlags=0, ignoreDynamicId=0, ignorePart=-1):
        spaceID = BigWorld.player().spaceID
        start = self._position
        return BigWorld.wg_collideSphereDynamicStatic(spaceID, start, end, self.__acCameraColliderRadius, skipFlags, ignoreDynamicId, ignorePart)

    def __onMappingChanged(self, *args):
        movementMappings = dict()
        movementMappings[getattr(Keys, getVirtualKey(CommandMapping.CMD_ROTATE_LEFT))] = Math.Vector3(-1, 0, 0)
        movementMappings[getattr(Keys, getVirtualKey(CommandMapping.CMD_ROTATE_RIGHT))] = Math.Vector3(1, 0, 0)
        movementMappings[getattr(Keys, getVirtualKey(CommandMapping.CMD_MOVE_FORWARD))] = Math.Vector3(0, 0, 1)
        movementMappings[getattr(Keys, getVirtualKey(CommandMapping.CMD_MOVE_BACKWARD))] = Math.Vector3(0, 0, -1)
        self._movementSensor.reloadKeySettings(movementMappings)
        return


class _SensitivityLimit(object):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, defaultSensitivity, movementSensor, keyMappings):
        self.__movementSensor = movementSensor
        self.__movementSensor.sensitivity = defaultSensitivity
        self.__keyMappings = keyMappings
        self.__sensitivityIndex = 1
        self.__speedSensitivity = defaultSensitivity
        return

    def setSpeedSensitivity(self, index, sensitivity):
        self.__sensitivityIndex = index
        self.__speedSensitivity = sensitivity
        self.__applySpeedSensitivity()
        return

    def handleKeyEvent(self, key, isDown):
        if key in self.__keyMappings and isDown:
            self.setSpeedSensitivity(key - Keys.KEY_1, self.__keyMappings[key])
            return True
        return False

    def __applySpeedSensitivity(self):
        self.__movementSensor.sensitivity = self.__speedSensitivity
        if self.guiSessionProvider.shared.spectator is not None:
            self.guiSessionProvider.shared.spectator.freeCamSpeedLevelChanged(self.__sensitivityIndex)
        return


class _SensitivityLimitKeySensor(KeySensor):

    def setCallback(self, callback):
        self.__callback = callback
        return

    def evaluateSensitivityKeys(self, delta):
        return

    def handleKeyEvent(self, key, isDown):
        result = super(_SensitivityLimitKeySensor, self).handleKeyEvent(key, isDown)
        if result and callable(self.__callback):
            self.__callback()
        return result

    def reloadKeySettings(self, newKeyMappings):
        self.keyMappings = newKeyMappings
        return


class _VariableHeightAlignerToLand(_AlignerToLand):
    _DEFAULT_MIN_HEIGHT_CAMERA = 10.0
    _DEFAULT_MAX_HEIGHT_CAMERA = 120.0

    def __init__(self):
        super(_VariableHeightAlignerToLand, self).__init__()
        self._minHeight = _VariableHeightAlignerToLand._DEFAULT_MIN_HEIGHT_CAMERA
        self._maxHeight = _VariableHeightAlignerToLand._DEFAULT_MAX_HEIGHT_CAMERA
        self._distanceToCeilingAssets = 1.0
        self._distanceToFloorAssets = 1.0
        self._minHeightSafe = self._minHeight
        self._maxHeightSafe = self._maxHeight
        self._avgLandHeight = None
        self.avgLandHeightUpdateSpeed = 1
        self.__skipFlags = 0
        return

    def getAlignedPosition(self, position):
        if self.desiredHeightShift is None:
            return position
        else:
            if self._avgLandHeight is None:
                self.updateLandHeight(position, 0.0)
            if self._avgLandHeight is None:
                return position
            return Math.Vector3(position.x, self._avgLandHeight.y, position.z) + self.desiredHeightShift

    def updateLandHeight(self, pos, deltaTime):
        landHeight = self._getLandAt(pos)
        attempts = 5
        while attempts > 5 and landHeight is None:
            pos = Math.Vector3(pos.x, pos.y + 900, pos.z)
            landHeight = self._getLandAt(pos)
            attempts -= 1

        if landHeight is None:
            return
        else:
            if self._avgLandHeight is None:
                self._avgLandHeight = landHeight
            else:
                distance = landHeight - self._avgLandHeight
                factor = math_utils.clamp01(distance.length / 10.0)
                factor += self.avgLandHeightUpdateSpeed
                self._avgLandHeight = self._avgLandHeight + distance * factor * deltaTime
            traceStart = pos
            traceEndUp = traceStart + Math.Vector3(0, 1000.0, 0)
            traceEndDown = traceStart - Math.Vector3(0, 1000.0, 0)
            collisionResUp = BigWorld.wg_collideDynamicStatic(BigWorld.player().spaceID, pos, traceEndUp, self.__skipFlags, 0, -1)
            collisionResDown = BigWorld.wg_collideDynamicStatic(BigWorld.player().spaceID, pos, traceEndDown, self.__skipFlags, 0, -1)
            if collisionResUp:
                collisionPointUp = collisionResUp[0]
                maxHeightAssets = collisionPointUp.y - self._avgLandHeight.y - self._distanceToCeilingAssets
                self._maxHeightSafe = abs(min(self._maxHeight, maxHeightAssets))
            else:
                self._maxHeightSafe = self._maxHeight
            if collisionResDown:
                collisionPointDown = collisionResDown[0]
                minHeightAssets = collisionPointDown.y - self._avgLandHeight.y + self._distanceToFloorAssets
                self._minHeightSafe = abs(max(self._minHeight, minHeightAssets))
            else:
                self._minHeightSafe = self._minHeight
            if self._maxHeightSafe < self._minHeightSafe:
                self._maxHeightSafe = self._minHeightSafe
            if self._maxHeightSafe - self._minHeightSafe < 1.0:
                self._minHeightSafe = self._maxHeightSafe = self._maxHeightSafe * 0.1 + self._minHeightSafe * 0.9
            return

    def enableWithFixedHeight(self, currentPos, newHeight, aboveSeaLevel=False):
        newHeight = math_utils.clamp(self._minHeightSafe, self._maxHeightSafe, newHeight)
        super(_VariableHeightAlignerToLand, self).enableWithFixedHeight(currentPos, newHeight, aboveSeaLevel)
        return

    def setCollisionSkipFlags(self, flags):
        self.__skipFlags = flags
        return

    def setMinMaxHeight(self, minHeight, maxHeight):
        self._minHeight = self._minHeightSafe = minHeight
        self._maxHeight = self._maxHeightSafe = maxHeight
        return

    def _getLandAt(self, position):
        if self.ignoreTerrain:
            return Vector3(position.x, 0, position.z)
        else:
            spaceID = BigWorld.player().spaceID
            if spaceID is None:
                return
            downPoint = Math.Vector3(position)
            downPoint.y -= 1000
            waterDist = BigWorld.wg_collideWater(position, downPoint, False)
            terrainCollision = BigWorld.wg_collideSegment(spaceID, position, downPoint, self.__skipFlags)
            if self.__isWaterCloser(position, waterDist, terrainCollision):
                return Vector3(position.x, position.y - waterDist, position.z)
            if terrainCollision is None:
                return
            return terrainCollision.closestPoint

    def __isWaterCloser(self, position, waterDist, terrainCollision):
        if waterDist <= -1:
            return False
        else:
            if terrainCollision is None:
                return True
            terrainDist = position.distTo(terrainCollision.closestPoint)
            return waterDist < terrainDist
