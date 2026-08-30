from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from helpers.EffectsList import RespawnDestroyEffect
from debug_utils import LOG_DEBUG_DEV

class AvatarRespawnMechanic(object):
    respawnEnabled = property((lambda self: self.__enabled))

    def __init__(self):
        self.__enabled = False
        return

    def onBecomePlayer(self):
        self.__enabled = BONUS_CAPS.checkAny(self.arenaBonusType, BONUS_CAPS.RESPAWN)
        if not self.__enabled:
            return
        return

    def handleKey(self, isDown, key, mods):
        return False

    def onBecomeNonPlayer(self):
        if not self.__enabled:
            return
        return

    def updateRespawnVehicles(self, vehsList):
        if not self.__enabled:
            return
        else:
            ctrl = self.guiSessionProvider.dynamic.respawn
            if ctrl is not None:
                ctrl.updateRespawnVehicles(vehsList)
            return

    def updateRespawnCooldowns(self, cooldowns):
        if not self.__enabled:
            return
        else:
            LOG_DEBUG_DEV(b'updateRespawnCooldowns ', cooldowns)
            cooldowns = {item[b'vehTypeCompDescr']: item[b'endOfCooldownPiT'] for item in cooldowns}
            ctrl = self.guiSessionProvider.dynamic.respawn
            if ctrl is not None:
                ctrl.updateRespawnCooldowns(cooldowns)
            return

    def updateRespawnInfo(self, respawnInfo):
        if not self.__enabled:
            return
        else:
            ctrl = self.guiSessionProvider.dynamic.respawn
            if ctrl is not None:
                ctrl.updateRespawnInfo(respawnInfo)
            return

    def updateVehicleLimits(self, respawnLimits):
        if not self.__enabled:
            return
        else:
            respawnLimits = {item[b'group']: item[b'vehTypeCompDescrs'] for item in respawnLimits}
            ctrl = self.guiSessionProvider.dynamic.respawn
            if ctrl is not None:
                ctrl.updateVehicleLimits(respawnLimits)
            return

    def explodeVehicleBeforeRespawn(self, vehID):
        RespawnDestroyEffect.play(vehID)
        return

    def updatePlayerLives(self, lives):
        LOG_DEBUG_DEV(b'updatePlayerLives', lives)
        ctrl = self.guiSessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.updatePlayerRespawnLives(lives)
        return

    def onTeamLivesRestored(self, teams):
        LOG_DEBUG_DEV(b'onTeamLivesRestored', teams)
        ctrl = self.guiSessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.restoredTeamRespawnLives(teams)
        return
