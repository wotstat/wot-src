class ITurretAndGunAngles(object):

    def init(self):
        raise NotImplementedError
        return

    def destroy(self):
        raise NotImplementedError
        return

    def reset(self):
        raise NotImplementedError
        return

    def set(self, gunPitch=0.0, turretYaw=0.0):
        raise NotImplementedError
        return

    def getGunPitch(self):
        raise NotImplementedError
        return

    def getTurretYaw(self):
        raise NotImplementedError
        return
