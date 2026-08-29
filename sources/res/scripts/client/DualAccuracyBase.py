import BigWorld, Event
from constants import DUAL_ACCURACY_STATE
from PlayerEvents import g_playerEvents
_DEFAULT_ACCURACY_FACTOR = 1.0

def getPlayerVehicleDualAccuracy():
    vehicle = BigWorld.player().getVehicleAttached()
    if vehicle is not None and vehicle.isPlayerVehicle and vehicle.isAlive():
        return vehicle.dynamicComponents.get(b'dualAccuracy', None)
    else:
        return


class DualAccuracyBase(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(DualAccuracyBase, self).__init__()
        self.__appearanceInited = False
        self.__dualAccuracyFactor = _DEFAULT_ACCURACY_FACTOR
        self.__coolingDelay = self.entity.typeDescriptor.gun.dualAccuracy.coolingDelay
        self.__eManager = Event.EventManager()
        self.onSetDualAccState = Event.Event(self.__eManager)
        self.onDualAccuracyDataUpdated = Event.Event(self.__eManager)
        self.__initDualAccuracyAppearance()
        self.__initDualAccuracyAvatar()
        return

    def getDualAccuracyFactor(self):
        return self.__dualAccuracyFactor

    def getCurrentDualAccuracyFactor(self):
        if self.isActive():
            return self.__dualAccuracyFactor
        return _DEFAULT_ACCURACY_FACTOR

    def getCoolingDelay(self):
        return self.__coolingDelay / self.coolingDelayFactor

    def isActive(self):
        return self.state == DUAL_ACCURACY_STATE.ACTIVE

    def set_state(self, _=None):
        if self.__isAvatarReady():
            withShot = 1 if self.__isDualgunVehicle and self.isActive() else 0
            self.__updateDualAccuracyAvatar(withShot)
        if self.__appearanceInited and self.__isAppearanceReady():
            self.updateDualAccuracyData()
            self.updateDualAccuracyState()
        return

    def onDestroy(self):
        self.entity.onAppearanceReady -= self.__onAppearanceReady
        self.__appearanceInited = False
        self.__eManager.clear()
        return

    def onLeaveWorld(self):
        self.onDestroy()
        return

    def onSiegeStateUpdated(self, typeDescriptor):
        if not self.__appearanceInited:
            return
        self.__collectDualAccuracyParams(typeDescriptor)
        self.__updateDualAccuracyAvatar()
        return

    def updateDualAccuracyData(self):
        self.onDualAccuracyDataUpdated()
        return

    def updateDualAccuracyState(self):
        self.onSetDualAccState(self.isActive())
        return

    def syncCoolingTimer(self, gunCtx=None):
        raise NotImplementedError
        return

    def getGunCoolingLeftTime(self):
        raise NotImplementedError
        return

    @staticmethod
    def __isAvatarReady():
        player = BigWorld.player()
        return player is not None and player.userSeesWorld()

    def __isAppearanceReady(self):
        player = BigWorld.player()
        if player is None or player.isDisableRespawnMode:
            return False
        appearance = self.entity.appearance
        return appearance is not None and appearance.isConstructed

    def __isPlayerVehicle(self, player=None):
        player = player or BigWorld.player()
        return player is not None and player.playerVehicleID == self.entity.id

    def __onAvatarReady(self):
        self.__updateDualAccuracyAvatar()
        return

    def __onAppearanceReady(self):
        if self.__appearanceInited:
            return
        self.__collectDualAccuracyParams()
        self.updateDualAccuracyData()
        self.__appearanceInited = True
        return

    def __updateDualAccuracyAvatar(self, withShot=0):
        player = BigWorld.player()
        if self.__isPlayerVehicle(player):
            player.getOwnVehicleShotDispersionAngle(player.gunRotator.turretRotationSpeed, withShot)
        return

    def __initDualAccuracyAvatar(self):
        if self.__isAvatarReady():
            self.__onAvatarReady()
        else:
            g_playerEvents.onAvatarReady += self.__onAvatarReady
        return

    def __initDualAccuracyAppearance(self):
        if self.__isAppearanceReady():
            self.__onAppearanceReady()
        else:
            self.entity.onAppearanceReady += self.__onAppearanceReady
        return

    def __collectDualAccuracyParams(self, typeDescriptor=None):
        typeDescriptor = typeDescriptor or self.entity.typeDescriptor
        params = typeDescriptor.gun
        self.__dualAccuracyFactor = params.dualAccuracy.afterShotDispersionAngle / params.shotDispersionAngle
        return

    @property
    def __isDualgunVehicle(self):
        vehicle = BigWorld.player().getVehicleAttached()
        return vehicle is not None and vehicle.typeDescriptor.isDualgunVehicle
