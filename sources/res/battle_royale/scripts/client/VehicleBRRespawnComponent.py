import logging, BigWorld
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class VehicleBRRespawnComponent(DynamicScriptComponent):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _onAvatarReady(self):
        if not self.checkCurrentVehicle():
            return
        else:
            self.componentChanged()
            prevLives = self.lives if self.resurrectTime or self.teammateResurrectTime else None
            self.__updateLives(self.lives, prevLives)
            self.__updateResurrectTime(self.resurrectTime)
            self.__updateTeammateResurrectTime(self.teammateResurrectTime)
            self.__updateTimeBlockToResurrect()
            return

    def set_resurrectTime(self, prev):
        if self.checkCurrentVehicle():
            self.__updateResurrectTime(self.resurrectTime)
        return

    def componentChanged(self):
        spawnCtrl = self.sessionProvider.dynamic.spawn
        spawnCtrl.componentChanged()
        return

    def __updateResurrectTime(self, resurrectTime):
        spawnCtrl = self.sessionProvider.dynamic.spawn
        respawnTime = resurrectTime - BigWorld.serverTime() if resurrectTime else 0.0
        spawnCtrl.updateRespawnTimer(respawnTime)
        return

    def __updateTeammateResurrectTime(self, teammateResurrectTime):
        spawnCtrl = self.sessionProvider.dynamic.spawn
        respawnTime = teammateResurrectTime - BigWorld.serverTime() if teammateResurrectTime else 0.0
        spawnCtrl.updateTeammateRespawnTime(respawnTime)
        return

    def __updateTimeBlockToResurrect(self):
        spawnCtrl = self.sessionProvider.dynamic.spawn
        blockTime = self.timeBlockToResurrect - BigWorld.serverTime() if self.timeBlockToResurrect else 0.0
        spawnCtrl.updateBlockToResurrectTimer(blockTime)
        return

    def checkCurrentVehicle(self):
        vehicle = BigWorld.entity(BigWorld.player().playerVehicleID)
        isObserver = b'observer' in vehicle.typeDescriptor.type.tags if vehicle else False
        return self.entity.id == BigWorld.player().playerVehicleID or isObserver

    def set_teammateResurrectTime(self, prev):
        if self.checkCurrentVehicle():
            self.__updateTeammateResurrectTime(self.teammateResurrectTime)
            _logger.info(b'set_teammateResurrectTime %s', self.teammateResurrectTime)
        return

    def set_timeBlockToResurrect(self, prev):
        if self.checkCurrentVehicle():
            self.__updateTimeBlockToResurrect()
            _logger.info(b'set_timeBlockToResurrect %s', self.timeBlockToResurrect)
        return

    def set_lives(self, prev):
        self.__updateLives(self.lives, prev)
        _logger.info(b'set_lives %s, %s', self.lives, prev)
        return

    def __updateLives(self, lives, prev):
        ctrl = self.sessionProvider.dynamic.vehicleCount
        if ctrl:
            ctrl.updateLives(lives)
        spawnCtrl = self.sessionProvider.dynamic.spawn
        if spawnCtrl:
            spawnCtrl.updateLives(lives, prev)
        return
