from __future__ import absolute_import
import logging
from typing import TYPE_CHECKING
from constants import EQUIPMENT_STAGES, ARENA_GUI_TYPE
from battle_royale.gui.constants import BR_EQUIPMENTS_WITH_MESSAGES
from gui.Scaleform.daapi.view.battle.shared.messages import fading_messages
from items import vehicles
if TYPE_CHECKING:
    from items.artefacts import Equipment
_logger = logging.getLogger(__name__)

class PlayerMessages(fading_messages.FadingMessages):

    def __init__(self):
        super(PlayerMessages, self).__init__(b'PlayerMessagesPanel', b'player_messages_panel.xml')
        return

    def __del__(self):
        _logger.debug(b'PlayerMessages panel is deleted')
        return

    def _addGameListeners(self):
        super(PlayerMessages, self)._addGameListeners()
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowPlayerMessageByCode += self._onShowPlayerMessageByCode
            ctrl.onShowPlayerMessageByKey += self.__onShowPlayerMessageByKey
            ctrl.onShowDestructibleEntityMessageByCode += self.__onShowDestructibleEntityMessageByCode
        ctrl = self.sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated += self.__onCombatEquipmentUpdated
            ctrl.onCombatEquipmentUsed += self._onCombatEquipmentUsed
        return

    def _removeGameListeners(self):
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowPlayerMessageByCode -= self._onShowPlayerMessageByCode
            ctrl.onShowPlayerMessageByKey -= self.__onShowPlayerMessageByKey
            ctrl.onShowDestructibleEntityMessageByCode -= self.__onShowDestructibleEntityMessageByCode
        ctrl = self.sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated -= self.__onCombatEquipmentUpdated
            ctrl.onCombatEquipmentUsed -= self._onCombatEquipmentUsed
        super(PlayerMessages, self)._removeGameListeners()
        return

    def __onShowDestructibleEntityMessageByCode(self, code, entityID, attackerID):
        _logger.debug(b'onShowDestructibleEntityMessage %r %r %r', code, entityID, attackerID)
        getFullName = self.sessionProvider.getCtx().getPlayerFullName
        self.showMessage(code, {b'target': (str(entityID)), 
           b'attacker': (getFullName(attackerID, showClan=False))})
        return

    def _onShowPlayerMessageByCode(self, code, postfix, targetID, attackerID, equipmentID, ignoreMessages):
        _logger.debug(b'onShowPlayerMessage %r %r %r %r %r', code, postfix, targetID, attackerID, equipmentID)
        if ignoreMessages:
            return
        else:
            getFullName = self.sessionProvider.getCtx().getPlayerFullName
            if equipmentID:
                equipment = vehicles.g_cache.equipments().get(equipmentID)
                if equipment is not None:
                    postfix = (b'_').join((postfix, equipment.messagePostfix))
            self.showMessage(code, {b'target': (getFullName(targetID, showClan=False)), 
               b'attacker': (getFullName(attackerID, showClan=False))}, extra=(
             (
              b'target', targetID), (b'attacker', attackerID)), postfix=postfix)
            return

    def __onShowPlayerMessageByKey(self, key, args=None, extra=None):
        self.showMessage(key, args, extra)
        return

    def __onCombatEquipmentUpdated(self, _, item):
        if not item.becomeReady:
            return
        itemDescriptor = item.getDescriptor()
        if itemDescriptor.name in BR_EQUIPMENTS_WITH_MESSAGES:
            if item.getPrevStage() == EQUIPMENT_STAGES.COOLDOWN and item.getQuantity() == 0:
                return
            self.showMessage(b'COMBAT_BR_EQUIPMENT_READY', {b'equipment': (itemDescriptor.userString)})
        else:
            self.showMessage(b'COMBAT_EQUIPMENT_READY', {}, postfix=self._getPostfixFromEquipment(itemDescriptor))
        return

    def _onCombatEquipmentUsed(self, shooterID, eqID):
        if self.sessionProvider.arenaVisitor.getArenaGuiType() in ARENA_GUI_TYPE.EPIC_RANGE:
            return
        else:
            battleCxt = self.sessionProvider.getCtx()
            if not battleCxt.isCurrentPlayer(shooterID):
                equipment = vehicles.g_cache.equipments().get(eqID)
                getFullName = battleCxt.getPlayerFullName
                if equipment is None:
                    return
                self.showMessage(b'COMBAT_EQUIPMENT_USED', {b'player': (getFullName(shooterID, showClan=False))}, extra=(
                 (
                  b'player', shooterID),), postfix=self._getPostfixFromEquipment(equipment))
            return

    @staticmethod
    def _getPostfixFromEquipment(equipment):
        postfix = equipment.playerMessagesKey
        if postfix is None:
            postfix = equipment.name.split(b'_')[0].upper()
        return postfix
