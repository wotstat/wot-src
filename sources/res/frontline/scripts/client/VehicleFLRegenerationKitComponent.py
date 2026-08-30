import BigWorld
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE

class VehicleFLRegenerationKitComponent(BigWorld.DynamicScriptComponent):

    def set_regenerationKit(self, _=None):
        attachedVehicle = BigWorld.player().getVehicleAttached()
        if attachedVehicle is None:
            return
        else:
            healPointEnter = {b'senderKey': b'healPoint', 
               b'isSourceVehicle': None, 
               b'isInactivation': (None if not self.regenerationKit[b'isActive'] else self.regenerationKit[b'isActive']), 
               b'endTime': (self.regenerationKit[b'endTime']), 
               b'duration': (self.regenerationKit[b'duration'])}
            if self.entity.id == attachedVehicle.id:
                self.entity.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.HEALING, healPointEnter)
            if not self.entity.isPlayerVehicle:
                ctrl = self.entity.guiSessionProvider.shared.feedback
                if ctrl is not None:
                    ctrl.invalidateFLRegenerationKit(self.entity.id, self.regenerationKit)
            return
