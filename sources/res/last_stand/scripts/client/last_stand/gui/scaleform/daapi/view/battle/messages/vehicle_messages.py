from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.messages import VehicleMessages

class LSVehicleMessages(VehicleMessages):
    _SKIP_EVENT_KEYS = (b'DEVICE_CRITICAL_AT_WORLD_COLLISION', b'DEVICE_DESTROYED_AT_WORLD_COLLISION', b'DEVICE_CRITICAL_AT_RAMMING', b'DEVICE_DESTROYED_AT_RAMMING', b'DEVICE_STARTED_FIRE_AT_RAMMING', b'TANKMAN_HIT_AT_WORLD_COLLISION', b'DEVICE_CRITICAL_AT_SHOT', b'DEVICE_DESTROYED_AT_SHOT', b'DEVICE_STARTED_FIRE_AT_SHOT', b'TANKMAN_HIT_AT_SHOT', b'TANKMAN_RESTORED', b'TANKMAN_HIT_AT_MEDKIT_OVER', b'DEVICE_CRITICAL_AT_FIRE', b'DEVICE_DESTROYED_AT_FIRE', b'DEVICE_REPAIRED_TO_CRITICAL', b'DEVICE_REPAIRED', b'DEVICE_CRITICAL_AT_REPAIRKIT_OVER', b'ENGINE_CRITICAL_AT_UNLIMITED_RPM', b'ENGINE_DESTROYED_AT_UNLIMITED_RPM', b'ENGINE_CRITICAL_AT_BURNOUT', b'ENGINE_DESTROYED_AT_BURNOUT', b'FIRE_STOPPED', b'OPT_DEVICE_USED', b'SCREENSHOT_CREATED', b'DRR_SCALE_STEP_UP', b'DRR_SCALE_STEP_DOWN')

    def showMessage(self, key, args=None, extra=None, postfix=b''):
        if any(key.startswith(event) for event in self._SKIP_EVENT_KEYS):
            return
        super(LSVehicleMessages, self).showMessage(key, args, extra, postfix)
        return

    def _addGameListeners(self):
        super(LSVehicleMessages, self)._addGameListeners()
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched += self._onPostMortemSwitched
        return

    def _removeGameListeners(self):
        super(LSVehicleMessages, self)._removeGameListeners()
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched -= self._onPostMortemSwitched
        return

    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        self.clear()
        return

    def _getPlayerInfo(self, entityID):
        ctx = self.sessionProvider.getCtx()
        vInfo = ctx.getArenaDP().getVehicleInfo(entityID)
        if vInfo.isEnemy():
            return vInfo.vehicleType.name
        return super(LSVehicleMessages, self)._getPlayerInfo(entityID)
