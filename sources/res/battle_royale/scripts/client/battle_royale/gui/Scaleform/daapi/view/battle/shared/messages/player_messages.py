from __future__ import absolute_import
import logging
from gui.Scaleform.daapi.view.battle.shared.messages import player_messages
from items import vehicles
_logger = logging.getLogger(__name__)

class SHPlayerMessages(player_messages.PlayerMessages):

    def _onShowPlayerMessageByCode(self, code, postfix, targetID, attackerID, equipmentID, ignoreMessages):
        _logger.debug(b'onShowPlayerMessage %r %r %r %r %r', code, postfix, targetID, attackerID, equipmentID)
        if ignoreMessages:
            return
        else:
            if equipmentID:
                equipment = vehicles.g_cache.equipments().get(equipmentID)
                if equipment is not None:
                    postfix = (b'_').join((postfix, equipment.name.split(b'_')[0].upper()))
            if postfix in (b'ENEMY_ENEMY', b'ENEMY_ALLY') and self.__isVehicleBot(attackerID) and code.startswith(b'DEATH'):
                code = b'DEATH_BY_BOT'
            self.showMessage(code, {b'target': (self._getFullName(targetID)), 
               b'attacker': (self._getFullName(attackerID))}, extra=(
             (
              b'target', targetID), (b'attacker', attackerID)), postfix=postfix)
            return

    def _getFullName(self, vehicleID):
        isBot = self.__isVehicleBot(vehicleID)
        getFullName = self.sessionProvider.getCtx().getPlayerFullName
        if isBot:
            return self.sessionProvider.getCtx().getPlayerFullNameParts(vehicleID, showClan=False).vehicleName
        return getFullName(vehicleID, showClan=False)

    def __isVehicleBot(self, vehicleID):
        return self.sessionProvider.getArenaDP().getVehicleInfo(vehicleID).team == 21
