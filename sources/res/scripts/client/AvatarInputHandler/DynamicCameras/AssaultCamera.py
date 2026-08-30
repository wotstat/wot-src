from math import pi, atan2
import BigWorld
from Math import Vector3, Matrix, MatrixProduct
import BattleReplay, Settings, math_utils
from AvatarInputHandler import aih_global_binding
from AvatarInputHandler.DynamicCameras import CameraWithSettings
from AvatarInputHandler.cameras import readFloat, readInt, readVec2
from ProjectileMover import collideDynamicAndStatic
from debug_utils import LOG_WARNING
from helpers.CallbackDelayer import CallbackDelayer
MAX_COLLISION_DISTANCE = 3500.0
COLLISION_EPS = 0.01
MAX_COLLISION_DISTANCE_FROM_SCREEN = 5500.0

def getCameraAsSettingsHolder(settingsDataSec):
    return AssaultCamera(settingsDataSec)


class BounceManager(object):

    def __init__(self, amplitude, time):
        self.__amplitude = amplitude
        self.__time = time
        self.__halfTime = time / 2.0
        self.__transitionTime = 0.0
        self.__inTransition = False
        self.__inverted = False
        return

    def inTransition(self):
        return self.__inTransition

    def startBounce(self, inverted=False):
        self.__inTransition = True
        self.__transitionTime = 0.0
        self.__inverted = inverted
        return

    def getBounceAmplitude(self, deltaTime):
        if self.__inTransition:
            amplitude = self.__update(deltaTime)
            if self.__inverted:
                return -amplitude
            return amplitude
        return 0.0

    def __reset(self):
        self.__inTransition = False
        self.__transitionTime = 0.0
        self.__inverted = False
        return

    def __update(self, deltaTime):
        self.__transitionTime += deltaTime
        if self.__transitionTime < self.__halfTime:
            transitionCoef = (self.__transitionTime / self.__halfTime) ** 2
            amplitude = math_utils.lerp(0.0, self.__amplitude, transitionCoef)
        else:
            transitionCoef = math_utils.clamp(0.0, 1.0, self.__transitionTime / self.__halfTime - 1.0)
            transitionCoef = (1.0 - transitionCoef) ** 2
            amplitude = math_utils.lerp(0.0, self.__amplitude, transitionCoef)
        if self.__transitionTime >= self.__time:
            self.__reset()
        return amplitude


class AssaultCamera(CameraWithSettings, CallbackDelayer):
    _DYNAMIC_ENABLED = True

    @staticmethod
    def enableDynamicCamera(enable):
        AssaultCamera._DYNAMIC_ENABLED = enable
        return

    @staticmethod
    def isCameraDynamic():
        return AssaultCamera._DYNAMIC_ENABLED

    camera = property((lambda self: self.__cam))
    aimingSystem = property((lambda self: self._aimingSystem))
    __aimOffset = aih_global_binding.bindRW(aih_global_binding.BINDING_ID.AIM_OFFSET)
    __assaultSpgCameraState = aih_global_binding.bindRW(aih_global_binding.BINDING_ID.ASSAULT_SPG_CAMERA_STATE)

    def __init__(self, dataSec):
        super(AssaultCamera, self).__init__()
        CallbackDelayer.__init__(self)
        self.isAimOffsetEnabled = True
        self._readConfigs(dataSec)
        self.__cam = BigWorld.CursorCamera()
        self.__curSense = self._cfg[b'sensitivity']
        self._aimingSystem = None
        self.__prevTime = 0.0
        self.__prevAimPoint = Vector3()
        self.__dxdydz = Vector3(0.0, 0.0, 0.0)
        self.__autoUpdatePosition = False
        self.__userTransition = False
        self.__sourceMatrix = None
        self.__targetMatrix = None
        self.__cameraDirection = Vector3(0.0, 0.0, 0.0)
        states = self._cfg[b'states']
        self.__countOfStates = self._cfg[b'statesCount']
        self.__currentState = self._cfg[b'initialStateIndex']
        self.__assaultSpgCameraState = self.__currentState
        self.__curDistRange = states[self.__currentState][b'distRange']
        self.__boundaryDistRange = (states[0][b'distRange'][0], states[len(states) - 1][b'distRange'][-1])
        self.__curPitchAngle = self._cfg[b'states'][self.__currentState][b'angle']
        self.__minPitchAngle = self._cfg[b'states'][0][b'angle']
        self.__maxPitchAngle = self._cfg[b'states'][self.__countOfStates - 1][b'angle']
        self.__collisionSphereRadius = self._cfg[b'collisionSphereRadius']
        self.__treeHidingRadius = self._cfg[b'treeHidingRadius']
        self.__treeHidingRadiusAlpha = self._cfg[b'treeHidingRadiusAlpha']
        self.__bounceManager = BounceManager(self._cfg[b'bounceAmplitude'], self._cfg[b'bounceTime'])
        self.__prevVehiclePosition = Vector3()
        return

    @staticmethod
    def _getConfigsKey():
        return AssaultCamera.__name__

    @staticmethod
    def _createAimingSystem():
        return BigWorld.AssaultAimingSystem()

    def __getCurrentStateBounds(self, pitch):
        left = 0
        if self._cfg[b'states'][left][b'angle'] < pitch:
            while left < self.__countOfStates - 2:
                if self._cfg[b'states'][left][b'angle'] <= pitch <= self._cfg[b'states'][left + 1][b'angle']:
                    break
                left += 1

        return (
         left, left + 1)

    def getZoom(self):
        leftState, rightState = self.__getCurrentStateBounds(-self.__sourceMatrix.pitch)
        leftPitch = self._cfg[b'states'][leftState][b'angle']
        rightPitch = self._cfg[b'states'][rightState][b'angle']
        pitchBoundLen = rightPitch - leftPitch
        state = (leftState - (self.__sourceMatrix.pitch + leftPitch) / pitchBoundLen) / float(self.__countOfStates - 1)
        return math_utils.clamp(0.0, 1.0, 1.0 - state)

    def __getTargetYawDirection(self, targetPos):
        position, _, _ = BigWorld.player().gunRotator.getShotParams(targetPos)
        vehToCamDir = targetPos - position
        vehToCamDir.normalise()
        cameraYaw = atan2(vehToCamDir.x, vehToCamDir.z)
        return cameraYaw

    def getMinStateDirection(self, targetPos):
        cameraYaw = self.__getTargetYawDirection(targetPos)
        direction = Vector3()
        direction.setPitchYaw(self.__minPitchAngle, cameraYaw)
        return direction

    def getMaxStateDirection(self, targetPos):
        cameraYaw = self.__getTargetYawDirection(targetPos)
        direction = Vector3()
        direction.setPitchYaw(self.__maxPitchAngle, cameraYaw)
        return direction

    def getTreeHidingParams(self):
        return (
         self.__treeHidingRadius, self.__treeHidingRadiusAlpha)

    def __getPrevState(self, pitch):
        if self.__curPitchAngle > pitch:
            curState = self.__currentState
            while curState > 0 and self._cfg[b'states'][curState][b'angle'] > pitch:
                curState -= 1

            return curState
        if self.__curPitchAngle < pitch:
            curState = 0
            while curState < self.__countOfStates - 1 and self._cfg[b'states'][curState][b'angle'] < pitch:
                curState += 1

            return curState
        return self.__currentState

    def teleport(self, pos):
        success = self.setup(pos, onlyHigherState=True)
        if not success:
            maxDirection = self.getMaxStateDirection(pos).scale(MAX_COLLISION_DISTANCE)
            sphereCollisionDist = self._aimingSystem.getSphereCollisionDist(pos - maxDirection, pos + maxDirection)
            if sphereCollisionDist >= 0.0:
                sphereCollisionDist -= COLLISION_EPS
                self.__cameraDirection = self.getMaxStateDirection(pos)
                self.__targetMatrix.translation = pos - maxDirection + self.__cameraDirection.scale(sphereCollisionDist)
                self.__setState(self.__countOfStates - 1)
            else:
                LOG_WARNING(b'AssaultCamera: Could not setup camera by teleporting!', pos)
        return

    def create(self, onChangeControlMode=None):
        super(AssaultCamera, self).create()
        self._aimingSystem = self._createAimingSystem()
        self._aimingSystem.setState(self.__curDistRange[0], self.__curDistRange[1], self.__curPitchAngle)
        self._aimingSystem.setCollisionSphereRadius(self.__collisionSphereRadius)
        self._aimingSystem.setPitchInterpolationSpeed(self._cfg[b'angleInterpolationSpeed'])
        self._aimingSystem.setDistInterpolationSpeedParams(self._cfg[b'rMinInterpolationSpeed'], self._cfg[b'rDefaultInterpolationSpeed'], self._cfg[b'rMaxInterpolationSpeed'])
        self.__cam.pivotMaxDist = 0.0
        self.__cam.maxDistHalfLife = 0.01
        self.__cam.movementHalfLife = 0.0
        self.__cam.turningHalfLife = -1
        self.__cam.pivotPosition = Vector3(0.0, 0.0, 0.0)
        self.__sourceMatrix = Matrix()
        self.__targetMatrix = Matrix()
        return

    def destroy(self):
        self.disable()
        self.__cam = None
        self.__bounceManager = None
        if self._aimingSystem is not None:
            self._aimingSystem.destroy()
            self._aimingSystem = None
        CallbackDelayer.destroy(self)
        CameraWithSettings.destroy(self)
        return

    def setup(self, targetPos, onlyHigherState=False):
        self._aimingSystem.setState(self.__curDistRange[0], self.__curDistRange[1], self.__curPitchAngle)
        success = self._aimingSystem.setup(targetPos)
        if success:
            return True
        startIndex = self.__currentState + 1 if onlyHigherState else 0
        for stateIndex in range(startIndex, self.__countOfStates):
            distRange = self._cfg[b'states'][stateIndex][b'distRange']
            pitchAngle = self._cfg[b'states'][stateIndex][b'angle']
            self._aimingSystem.setState(distRange[0], distRange[1], pitchAngle)
            if stateIndex != self.__currentState and self._aimingSystem.setup(targetPos):
                self.__setState(stateIndex)
                return True

        return False

    def enable(self, targetPos, saveDist, switchToPos=None, switchToPlace=None):
        BigWorld.trajectory_drawer().setStrategicMode(False)
        self.__prevTime = 0.0
        self.__prevVehiclePosition = BigWorld.player().getVehicleAttached().position
        camTarget = MatrixProduct()
        self.__cam.target = camTarget
        self.__cam.target.b = self.__targetMatrix
        cameraDirection = self._aimingSystem.direction
        self.__sourceMatrix = math_utils.createRotationMatrix((cameraDirection.yaw, -cameraDirection.pitch, 0.0))
        self.__cam.source = self.__sourceMatrix
        self.__cam.forceUpdate()
        self.__targetMatrix.translation = self._aimingSystem.position
        BigWorld.camera(self.__cam)
        BigWorld.player().positionControl.moveTo(targetPos)
        BigWorld.player().positionControl.followCamera(False)
        self.__cameraUpdate()
        self.delayCallback(0.01, self.__cameraUpdate)
        return

    def disable(self):
        if self._aimingSystem is not None:
            self._aimingSystem.disable()
        self.stopCallback(self.__cameraUpdate)
        return

    def update(self, dx, dy, dz, updateByKeyboard=False):
        self.__curSense = self._cfg[b'keySensitivity'] if updateByKeyboard else self._cfg[b'sensitivity']
        self.__autoUpdatePosition = updateByKeyboard
        self.__dxdydz = Vector3(dx if not self._cfg[b'horzInvert'] else -dx, dy if not self._cfg[b'vertInvert'] else -dy, dz)
        return

    def writeUserPreferences(self):
        ds = Settings.g_instance.userPrefs
        if not ds.has_key(Settings.KEY_CONTROL_MODE):
            ds.write(Settings.KEY_CONTROL_MODE, b'')
        ucfg = self._userCfg
        ds = ds[Settings.KEY_CONTROL_MODE]
        ds.writeBool(b'assaultSPG/camera/horzInvert', ucfg[b'horzInvert'])
        ds.writeBool(b'assaultSPG/camera/vertInvert', ucfg[b'vertInvert'])
        ds.writeFloat(b'assaultSPG/camera/keySensitivity', ucfg[b'keySensitivity'])
        ds.writeFloat(b'assaultSPG/camera/sensitivity', ucfg[b'sensitivity'])
        return

    def getCamDistRange(self):
        return self.__boundaryDistRange

    def getCamTransitionDist(self):
        return self.__boundaryDistRange[-1] / 2

    def getCurrentCamDist(self):
        return self.__targetMatrix.translation.y

    def getCountOfStates(self):
        return self.__countOfStates

    def __updateTrajectoryDrawer(self):
        shotDescr = BigWorld.player().getVehicleDescriptor().shot
        BigWorld.trajectory_drawer().setParams(shotDescr.maxDistance, Vector3(0, -shotDescr.gravity, 0), self.__aimOffset)
        return

    def __updateTime(self):
        curTime = BigWorld.timeExact()
        deltaTime = curTime - self.__prevTime
        self.__prevTime = curTime
        return deltaTime

    def __setState(self, stateIndex):
        self.__currentState = stateIndex
        self.__curDistRange = self._cfg[b'states'][self.__currentState][b'distRange']
        self.__curPitchAngle = self._cfg[b'states'][self.__currentState][b'angle']
        self._aimingSystem.setState(self.__curDistRange[0], self.__curDistRange[1], self.__curPitchAngle)
        self.__assaultSpgCameraState = self.__currentState
        return

    def __updateState(self):
        if self.__dxdydz.z == 0:
            return
        self.__userTransition = True
        if self._aimingSystem.transitionBlocked:
            if not self.__bounceManager.inTransition():
                self.__bounceManager.startBounce(inverted=self.__dxdydz.z > 0)
                return
        nextState = self.__currentState
        if self.__dxdydz.z < 0:
            nextState += 1
        elif self.__dxdydz.z > 0:
            nextState -= 1
        nextState = math_utils.clamp(0, self.__countOfStates - 1, nextState)
        newPitch = self._cfg[b'states'][nextState][b'angle']
        newMaxDist = self._cfg[b'states'][nextState][b'distRange'][1]
        newCameraDir = Vector3()
        newCameraDir.setPitchYaw(newPitch, self._aimingSystem.direction.yaw)
        newCameraPos = self._aimingSystem.aimPoint - newCameraDir.scale(newMaxDist)
        sphereCollisionDist = self._aimingSystem.getSphereCollisionDist(self._aimingSystem.position, newCameraPos)
        if sphereCollisionDist >= 0.0:
            if not self.__bounceManager.inTransition():
                self.__bounceManager.startBounce(inverted=self.__dxdydz.z > 0)
            return
        self.__setState(nextState)
        return

    def __handleMovement(self):
        vehiclePosition = BigWorld.player().getVehicleAttached().position
        vehicleMoveDiff = vehiclePosition - self.__prevVehiclePosition
        vehicleMoveDiff.y = 0.0
        self.__prevVehiclePosition = vehiclePosition
        rotMat = math_utils.createRotationMatrix((self.__sourceMatrix.yaw, 0, 0))
        moveVector = rotMat.applyVector(Vector3(self.__dxdydz.x * self.__curSense, 0, -self.__dxdydz.y * self.__curSense))
        moveVector += vehicleMoveDiff
        self._aimingSystem.handleMovement(moveVector.x, moveVector.z)
        return

    def __cameraUpdate(self):
        deltaTime = self.__updateTime()
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying and replayCtrl.isControllingCamera:
            self.__cam.forceUpdate()
            endPoint = self.camera.position + self.__cam.direction.scale(MAX_COLLISION_DISTANCE)
            collision = collideDynamicAndStatic(self.camera.position, endPoint, (
             BigWorld.player().playerVehicleID, 0))
            if collision is not None:
                self._aimingSystem.aimPoint = collision[0]
            waterCollisionDist = BigWorld.collideWater(self.camera.position, endPoint, False)
            if waterCollisionDist > -1.0 and (collision is None or waterCollisionDist < (collision[0] - self.camera.position).length):
                self._aimingSystem.aimPoint = self.camera.position + self.__cam.direction * waterCollisionDist
            self.__updateTrajectoryDrawer()
            return 0.01
        else:
            self.__handleMovement()
            self.__updateState()
            self._aimingSystem.update(deltaTime)
            self.__targetMatrix.translation = self._aimingSystem.position
            cameraDirection = self._aimingSystem.direction
            self.__targetMatrix.translation -= cameraDirection.scale(self.__bounceManager.getBounceAmplitude(deltaTime))
            if self.aimingSystem.aimPoint.distSqrTo(self.__prevAimPoint) > 0.010000000000000002:
                BigWorld.player().positionControl.moveTo(self._aimingSystem.aimPoint)
                self.__prevAimPoint = self._aimingSystem.aimPoint
            self.__sourceMatrix = math_utils.createRotationMatrix((
             cameraDirection.yaw, -cameraDirection.pitch, 0))
            self.__cam.source = self.__sourceMatrix
            if self._aimingSystem.transitionBlocked:
                if self.__userTransition:
                    self.__setState(self.__getPrevState(cameraDirection.pitch))
                    self.__userTransition = False
            self.__updateTrajectoryDrawer()
            self.__cam.forceUpdate()
            if not self.__autoUpdatePosition:
                self.__dxdydz = Vector3(0, 0, 0)
            return 0.01

    def _readConfigs(self, dataSec):
        if not dataSec:
            LOG_WARNING(b'Invalid section <assaultSPG/camera> in avatar_input_handler.xml')
        super(AssaultCamera, self)._readConfigs(dataSec)
        return

    def _readBaseCfg(self, dataSec):
        bcfg = self._baseCfg
        bcfg[b'keySensitivity'] = readFloat(dataSec, b'keySensitivity', 0.005, 10.0, 0.025)
        bcfg[b'sensitivity'] = readFloat(dataSec, b'sensitivity', 0.005, 10.0, 0.025)
        bcfg[b'collisionSphereRadius'] = readFloat(dataSec, b'collisionSphereRadius', 1.0, 5.0, 5.0)
        bcfg[b'rMinInterpolationSpeed'] = readFloat(dataSec, b'rMinInterpolationSpeed', 0.005, 10.0, 7.0)
        bcfg[b'rDefaultInterpolationSpeed'] = readFloat(dataSec, b'rDefaultInterpolationSpeed', 0.005, 10.0, 0.005)
        bcfg[b'rMaxInterpolationSpeed'] = readFloat(dataSec, b'rMaxInterpolationSpeed', 0.005, 10.0, 0.005)
        bcfg[b'angleInterpolationSpeed'] = readFloat(dataSec, b'angleInterpolationSpeed', 0.005, 10.0, 7.0)
        bcfg[b'treeHidingRadius'] = readFloat(dataSec, b'treeHidingRadius', 0.0, 1000.0, 15.0)
        bcfg[b'treeHidingRadiusAlpha'] = readFloat(dataSec, b'treeHidingRadiusAlpha', 0.0, 1000.0, 10.0)
        bcfg[b'bounceAmplitude'] = readFloat(dataSec, b'bounceAmplitude', 0.0, 10.0, 1.0)
        bcfg[b'bounceTime'] = readFloat(dataSec, b'bounceTime', 0.0, 10.0, 0.5)
        self._readStatesCfg(dataSec)
        return

    def _readStatesCfg(self, dataSec):
        bcfg = self._baseCfg
        stateSectionName = b'states/'
        bcfg[b'statesCount'] = readInt(dataSec, stateSectionName + b'count', 0, 100, 0)
        bcfg[b'initialStateIndex'] = readInt(dataSec, stateSectionName + b'initialStateIndex', 0, 100, 0)
        bcfg[b'states'] = {}
        for index in range(0, bcfg[b'statesCount']):
            subsectionStateName = b'state_' + str(index) + b'/'
            bcfg[b'states'][index] = {}
            bcfg[b'states'][index][b'distRange'] = readVec2(dataSec, stateSectionName + subsectionStateName + b'distRange', (0.0, 0.0), (1000.0, 1000.0), (0.0, 1000.0))
            bcfg[b'states'][index][b'angle'] = readFloat(dataSec, stateSectionName + subsectionStateName + b'angle', 0.0, 90.0, 45.0) / 180.0 * pi

        return

    def _readUserCfg(self):
        ucfg = self._userCfg
        dataSec = Settings.g_instance.userPrefs[Settings.KEY_CONTROL_MODE]
        if dataSec is not None:
            dataSec = dataSec[b'assaultSPG/camera']
        ucfg[b'horzInvert'] = False
        ucfg[b'vertInvert'] = False
        ucfg[b'keySensitivity'] = readFloat(dataSec, b'keySensitivity', 0.0, 10.0, 1.0)
        ucfg[b'sensitivity'] = readFloat(dataSec, b'sensitivity', 0.0, 10.0, 1.0)
        return

    def _makeCfg(self):
        bcfg = self._baseCfg
        ucfg = self._userCfg
        cfg = self._cfg
        cfg[b'keySensitivity'] = bcfg[b'keySensitivity']
        cfg[b'sensitivity'] = bcfg[b'sensitivity']
        cfg[b'statesCount'] = bcfg[b'statesCount']
        cfg[b'initialStateIndex'] = bcfg[b'initialStateIndex']
        cfg[b'states'] = bcfg[b'states']
        cfg[b'keySensitivity'] *= ucfg[b'keySensitivity']
        cfg[b'sensitivity'] *= ucfg[b'sensitivity']
        cfg[b'horzInvert'] = ucfg[b'horzInvert']
        cfg[b'vertInvert'] = ucfg[b'vertInvert']
        cfg[b'collisionSphereRadius'] = bcfg[b'collisionSphereRadius']
        cfg[b'rMinInterpolationSpeed'] = bcfg[b'rMinInterpolationSpeed']
        cfg[b'rDefaultInterpolationSpeed'] = bcfg[b'rDefaultInterpolationSpeed']
        cfg[b'rMaxInterpolationSpeed'] = bcfg[b'rMaxInterpolationSpeed']
        cfg[b'angleInterpolationSpeed'] = bcfg[b'angleInterpolationSpeed']
        cfg[b'treeHidingRadius'] = bcfg[b'treeHidingRadius']
        cfg[b'treeHidingRadiusAlpha'] = bcfg[b'treeHidingRadiusAlpha']
        cfg[b'bounceAmplitude'] = bcfg[b'bounceAmplitude']
        cfg[b'bounceTime'] = bcfg[b'bounceTime']
        return
