import logging, BigWorld, Math, Event, math_utils
from vehicle_systems.tankStructure import TankNodeNames
from VehicleGunRotator import VehicleGunRotator, MatrixAnimator
logger = logging.getLogger(__name__)

class SimpleTurretRotator(object):
    __slots__ = (b'__isStarted', b'__turretYaw', b'__targetTurretYaw', b'__rotationTime', b'__timerID', b'__turretMatrixAnimator', b'__easingCls', b'__easing', b'_eventsManager', b'onTurretRotated', b'onTurretRotationStarted', b'__turretTranslation', b'__turretPitch')
    __ROTATION_TICK_LENGTH = 0.05
    turretMatrix = property((lambda self: self.__turretMatrixAnimator.matrix))
    turretYaw = property((lambda self: self.__turretYaw))
    isStarted = property((lambda self: self.__isStarted))

    def __init__(self, compoundModel=None, currTurretYaw=0.0, turretTranslation=Math.Vector3(0.0, 0.0, 0.0), turretPitch=0.0, easingCls=math_utils.Easing.linearEasing):
        self.__isStarted = False
        self.__turretYaw = self.__targetTurretYaw = currTurretYaw
        self.__turretTranslation = turretTranslation
        self.__turretPitch = turretPitch
        self.__rotationTime = 0.0
        self.__timerID = None
        self.__turretMatrixAnimator = MatrixAnimator()
        self.__easingCls = easingCls
        self.__easing = None
        if compoundModel is not None:
            self.__updateTurretMatrix(currTurretYaw, 0.0)
            compoundModel.node(TankNodeNames.TURRET_JOINT).local = self.__turretMatrixAnimator.matrix
        else:
            logger.error(b'CompoundModel is not set!')
        self._eventsManager = Event.EventManager()
        self.onTurretRotationStarted = Event.Event(self._eventsManager)
        self.onTurretRotated = Event.Event(self._eventsManager)
        return

    def destroy(self):
        self.stop()
        self.__turretMatrixAnimator.destroy()
        self._eventsManager.clear()
        return

    def start(self, targetTurretYaw, rotationTime=None):
        if abs(targetTurretYaw - self.__targetTurretYaw) <= VehicleGunRotator.ANGLE_EPS:
            return
        else:
            self.__targetTurretYaw = targetTurretYaw
            if rotationTime is not None:
                self.__rotationTime = rotationTime
            if self.__rotationTime > 0.0:
                if self.__isStarted:
                    self.__easing.reset(self.__turretYaw, targetTurretYaw, self.__rotationTime)
                else:
                    self.__isStarted = True
                    self.__timerID = BigWorld.callback(self.__ROTATION_TICK_LENGTH, self.__onTick)
                    self.__easing = self.__easingCls(self.__turretYaw, targetTurretYaw, self.__rotationTime)
            else:
                self.__updateTurretMatrix(self.__targetTurretYaw, self.__rotationTime)
            self.onTurretRotationStarted()
            return

    def setEasing(self, easingCls):
        if self.__isStarted:
            logger.error(b'easing shall be set when turret is not rotating')
            return
        else:
            if easingCls is not None:
                self.__easingCls = easingCls
            return

    def stop(self):
        if self.__timerID is not None:
            BigWorld.cancelCallback(self.__timerID)
            self.__timerID = None
        self.__targetTurretYaw = self.__turretYaw
        self.__easing = None
        self.__isStarted = False
        return

    def reset(self):
        self.__turretYaw = self.__targetTurretYaw = 0.0
        self.__updateTurretMatrix(0.0, 0.0)
        self.stop()
        return

    def __onTick(self):
        self.__timerID = BigWorld.callback(self.__ROTATION_TICK_LENGTH, self.__onTick)
        if self.__easing.stopped:
            self.stop()
            self.onTurretRotated()
            return
        self.__easing.update(self.__ROTATION_TICK_LENGTH)
        self.__turretYaw = self.__easing.value
        self.__updateTurretMatrix(self.__turretYaw, self.__ROTATION_TICK_LENGTH)
        return

    def __updateTurretMatrix(self, yaw, time):
        m = Math.Matrix()
        m.setRotateX(self.__turretPitch)
        m.translation = self.__turretTranslation
        yawMatrix = Math.Matrix()
        yawMatrix.setRotateY(yaw)
        m.preMultiply(yawMatrix)
        self.__turretMatrixAnimator.update(m, time)
        self.__turretYaw = yaw
        return
