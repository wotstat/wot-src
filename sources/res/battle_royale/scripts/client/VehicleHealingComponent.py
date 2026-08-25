from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent
from battle_royale.gui.constants import BattleRoyaleEquipments

class VehicleHealingComponent(VehicleAbilityBaseComponent):
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.HEALING
    __MARKER_ID = BATTLE_MARKER_STATES.HEALING_STATE

    def __init__(self):
        self._isDestroying = False
        super(VehicleHealingComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)
        return

    def set_isInactivation(self, prev):
        self._updateVisuals()
        return

    def _updateTimer(self, data):
        data.update(self._getHealingArgs())
        super(VehicleHealingComponent, self)._updateTimer(data)
        return

    def _updateMarker(self, data, isHide=False):
        data.update({b'isSourceVehicle': (self.isSourceVehicle)})
        super(VehicleHealingComponent, self)._updateMarker(data, isHide)
        return

    def _destroy(self):
        self._isDestroying = True
        super(VehicleHealingComponent, self)._destroy()
        return

    def _getDuration(self):
        return self._getEquipment(BattleRoyaleEquipments.HEAL_POINT).duration

    def _getHealingArgs(self):
        return {b'isInactivation': (self.isInactivation), 
           b'isSourceVehicle': (self.isSourceVehicle), 
           b'isDestroying': (self._isDestroying), 
           b'senderKey': (BattleRoyaleEquipments.HEAL_POINT)}
