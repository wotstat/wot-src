from gui.Scaleform.daapi.view.battle.shared.messages import VehicleMessages
from gui.doc_loaders import messages_panel_reader
_VEHICLE_MESSAGES_FILE = b'gui/wt_vehicle_messages_panel.xml'

class WTVehicleMessages(VehicleMessages):

    def _populate(self):
        super(WTVehicleMessages, self)._populate()
        _, _, messages = messages_panel_reader.readXML(_VEHICLE_MESSAGES_FILE)
        self._messages.update(messages)
        return

    def _addGameListeners(self):
        super(WTVehicleMessages, self)._addGameListeners()
        ctrl = self.sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated += self.__onEquipmentUpdated
        return

    def _removeGameListeners(self):
        ctrl = self.sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated -= self.__onEquipmentUpdated
        super(WTVehicleMessages, self)._removeGameListeners()
        return

    def __onEquipmentUpdated(self, _, item):
        if item is None:
            return
        else:
            postfix = b''
            if item.becomeActive:
                postfix = b'ACTIVATE'
            if postfix:
                self.showMessage(item.getDescriptor().name.upper(), {}, postfix=postfix)
            return
