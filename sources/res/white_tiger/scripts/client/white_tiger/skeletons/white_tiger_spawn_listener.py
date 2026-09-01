from __future__ import absolute_import
from enum import IntEnum

class SpawnType(IntEnum):
    DEFAULT = 1
    TELEPORT = 2


class ISpawnListener(object):

    def setSpawnPoints(self, points, pointId=None):
        return

    def showSpawnPoints(self):
        return

    def closeSpawnPoints(self):
        return

    def updatePoint(self, vehicleId, pointId, prevPointId):
        return

    def updateCloseTime(self, timeLeft, state):
        return

    def onSelectPoint(self, pointId):
        return

    def setSpawnType(self, spawnType):
        return
