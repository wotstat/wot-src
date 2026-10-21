import logging
from gui.doc_loaders import messages_panel_reader
from gui.Scaleform.daapi.view.battle.shared.messages import player_messages
from items import vehicles
_logger = logging.getLogger(__name__)
_PORTAL_PLAYER_MESSAGES_PATH = b'portal/gui/player_messages_panel.xml'
_SENTRY_GUN_EQUIPMENT_NAME = b'sentry_gun_portal'

class PortalPlayerMessages(player_messages.PlayerMessages):

    def _addGameListeners(self):
        super(PortalPlayerMessages, self)._addGameListeners()
        ctrl = self.sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated += self.__onEquipmentUpdated
        return

    def _removeGameListeners(self):
        ctrl = self.sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated -= self.__onEquipmentUpdated
        super(PortalPlayerMessages, self)._removeGameListeners()
        return

    def _populate(self):
        super(PortalPlayerMessages, self)._populate()
        _, _, messages = messages_panel_reader.readXML(_PORTAL_PLAYER_MESSAGES_PATH)
        self._messages.update(messages)
        return

    def _onShowPlayerMessageByCode(self, code, postfix, targetID, attackerID, equipmentID, ignoreMessages):
        _logger.debug(b'onShowPlayerMessage %r %r %r %r %r', code, postfix, targetID, attackerID, equipmentID)
        if ignoreMessages:
            return
        else:
            if equipmentID:
                equipment = vehicles.g_cache.equipments().get(equipmentID)
                if equipment is not None:
                    postfix = (b'_').join((postfix, self.__getPostfixFromEquipment(equipment)))
            self.showMessage(code, {b'target': (self._getFullName(targetID)), 
               b'attacker': (self._getFullName(attackerID))}, extra=(
             (
              b'target', targetID), (b'attacker', attackerID)), postfix=postfix)
            return

    def showMessage(self, key, args=None, extra=None, postfix=b''):
        if key == b'ALLY_HIT' and args and extra:
            vehicleID = dict(extra).get(b'entity')
            if vehicleID is not None:
                sentryGunName = self.__getSentryGunFullName(vehicleID)
                if sentryGunName is not None:
                    args = dict(args, entity=sentryGunName)
        super(PortalPlayerMessages, self).showMessage(key, args, extra, postfix)
        return

    def _getFullName(self, vehicleID):
        avatarSessionID = self.sessionProvider.getArenaDP().getVehicleInfo(vehicleID).player.avatarSessionID
        getFullName = self.sessionProvider.getCtx().getPlayerFullName
        if not avatarSessionID:
            return self.sessionProvider.getCtx().getPlayerFullNameParts(vehicleID, showClan=False).vehicleName
        return getFullName(vehicleID, showClan=False)

    def __getSentryGunFullName(self, vehicleID):
        equipment = vehicles.g_cache.getEquipmentByName(_SENTRY_GUN_EQUIPMENT_NAME)
        if equipment is None:
            return
        else:
            sentryGunVehicleCD = vehicles.makeVehicleTypeCompDescrByName(equipment.sentryGunVehicle)
            vInfo = self.sessionProvider.getArenaDP().getVehicleInfo(vehicleID)
            if vInfo.vehicleType.compactDescr != sentryGunVehicleCD:
                return
            return self.sessionProvider.getCtx().getPlayerFullNameParts(vehicleID, pName=equipment.userString, showClan=False).playerFullName

    def __onEquipmentUpdated(self, _, item):
        if not item or not self.__isEquipmentBecomeActive(item):
            return
        itemDescriptor = item.getDescriptor()
        self.showMessage(b'COMBAT_EQUIPMENT_ACTIVATED', {}, postfix=self.__getPostfixFromEquipment(itemDescriptor))
        return

    @staticmethod
    def __getPostfixFromEquipment(equipment):
        postfix = equipment.playerMessagesKey
        if postfix is None:
            postfix = equipment.name.split(b'_')[0].upper()
        return postfix

    @staticmethod
    def __isEquipmentBecomeActive(equipment):
        if hasattr(equipment, b'becomeAppointed'):
            return equipment.becomeAppointed
        if hasattr(equipment, b'becomeActive'):
            return equipment.becomeActive
        return False
