from gui.ClientHangarSpace import hangarCFG
from skeletons.gui.turret_gun_angles import ITurretAndGunAngles

class TurretAndGunAngles(ITurretAndGunAngles):

    def __init__(self):
        self.__gunPitch = 0.0
        self.__turretYaw = 0.0
        return

    def init(self):
        self.reset()
        return

    def reset(self):
        cfg = hangarCFG()
        self.__gunPitch = cfg.get(b'vehicle_gun_pitch', 0.0)
        self.__turretYaw = cfg.get(b'vehicle_turret_yaw', 0.0)
        return

    def destroy(self):
        self.__gunPitch = 0.0
        self.__turretYaw = 0.0
        return

    def set(self, gunPitch=0.0, turretYaw=0.0):
        self.__gunPitch = gunPitch
        self.__turretYaw = turretYaw
        return

    def getTurretYaw(self):
        return self.__turretYaw

    def getGunPitch(self):
        return self.__gunPitch
