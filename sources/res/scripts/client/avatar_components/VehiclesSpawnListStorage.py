import logging, cPickle
from Event import Event
from VehiclesSpawnListStorageCommon import convertTuplesToVehicleSpawnData
_logger = logging.getLogger(__name__)

class VehiclesSpawnListStorage(object):

    def __init__(self):
        super(VehiclesSpawnListStorage, self).__init__()
        self.onSpawnListUpdated = Event()
        return

    def handleKey(self, isDown, key, mods):
        return

    def onBecomePlayer(self):
        return

    def onBecomeNonPlayer(self):
        return

    def updateSpawnList(self, spawnListData):
        spawnList = convertTuplesToVehicleSpawnData(cPickle.loads(spawnListData))
        self.onSpawnListUpdated(spawnList)
        return
