from __future__ import absolute_import
import typing
from gui.battle_control.controllers.interfaces import IBattleController

class ISoundsController(object):

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def start(self):
        raise NotImplementedError
        return

    def stop(self, isDisconnected=False):
        raise NotImplementedError
        return

    @property
    def system(self):
        raise NotImplementedError
        return

    def enable(self):
        raise NotImplementedError
        return

    def disable(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def setEnvForSpace(self, spaceID, newEnv):
        raise NotImplementedError
        return


class IShotsResultSoundController(IBattleController):

    def getBestSoundEventName(self, bestSound):
        raise NotImplementedError
        return

    def getBestShotResultSound(self, currBest, newSoundName, otherData):
        raise NotImplementedError
        return

    def getVehicleHitResultSound(self, enemyVehID, hitFlags, enemiesHitCount):
        raise NotImplementedError
        return
