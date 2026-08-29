import BigWorld
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent

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
        data.update({b'isInactivation': (self.isInactivation), b'isSourceVehicle': (self.getIsSourceVehicle())})
        super(VehicleHealingComponent, self)._updateTimer(data)
        return

    def _updateMarker(self, data, isHide=False):
        data.update({b'isSourceVehicle': (self.getIsSourceVehicle())})
        super(VehicleHealingComponent, self)._updateMarker(data, isHide)
        return

    def getIsSourceVehicle(self):
        return self.entity.id == BigWorld.player().getObservedVehicleID()
