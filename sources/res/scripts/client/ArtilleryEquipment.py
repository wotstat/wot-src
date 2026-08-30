from __future__ import absolute_import
import math_utils, BigWorld

class ArtilleryEquipment(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        launchDir = math_utils.createRotationMatrix((self.__dict__[b'yaw'], self.__dict__[b'pitch'], 0)).applyToAxis(2)
        launchDir.normalise()
        self.__launchVelocity = launchDir * self.speed
        return

    @property
    def launchVelocity(self):
        return self.__launchVelocity
