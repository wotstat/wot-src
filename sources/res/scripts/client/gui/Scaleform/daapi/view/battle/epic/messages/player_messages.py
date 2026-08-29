import logging
from gui.Scaleform.daapi.view.battle.shared.messages import player_messages
from items import vehicles
from supply_shared import Supply
_logger = logging.getLogger(__name__)
_ATTAKER_SUPPLY = b'SUPPLY_'
_TARGET_SUPPLY = b'_SUPPLY'

class EpicPlayerMessages(player_messages.PlayerMessages):

    def _onShowPlayerMessageByCode(self, code, postfix, targetID, attackerID, equipmentID, ignoreMessages):
        _logger.debug(b'onShowEpicPlayerMessage %r %r %r %r %r', code, postfix, targetID, attackerID, equipmentID)
        if ignoreMessages:
            return
        else:
            if equipmentID:
                equipment = vehicles.g_cache.equipments().get(equipmentID)
                if equipment is not None:
                    postfix = (b'_').join((postfix, equipment.name.split(b'_')[0].upper()))
            attackerName, isAttackerSupply = self._getSupplyName(attackerID)
            targetName, isTargetSupply = self._getSupplyName(targetID)
            if isAttackerSupply:
                postfix = _ATTAKER_SUPPLY + postfix
            if isTargetSupply:
                postfix = postfix + _TARGET_SUPPLY
            self.showMessage(code, {b'target': targetName, 
               b'attacker': attackerName}, extra=(
             (
              b'target', targetID), (b'attacker', attackerID)), postfix=postfix)
            return

    def _getSupplyName(self, vehicleID):
        vehicleType = self.sessionProvider.getArenaDP().getVehicleInfo(vehicleID).vehicleType
        if Supply.isSupply(vehicleType.tags):
            return ((b'({})').format(vehicleType.shortNameWithPrefix), True)
        getFullName = self.sessionProvider.getCtx().getPlayerFullName
        return (getFullName(vehicleID, showClan=False), False)
