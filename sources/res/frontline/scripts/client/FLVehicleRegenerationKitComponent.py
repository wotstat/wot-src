import BigWorld
from PlayerEvents import g_playerEvents
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from frontline import invalidateVehicleMarkerState, isAvatarReady
from vehicle_systems.stricted_loading import makeCallbackWeak

class FLVehicleRegenerationKitComponent(BigWorld.DynamicScriptComponent):
    _CALLBACK_DELAY = 0.5

    def __init__(self):
        super(FLVehicleRegenerationKitComponent, self).__init__()
        if isAvatarReady():
            self.__invalidateFLRegenerationKit()
        else:
            g_playerEvents.onAvatarReady += self.__onAvatarReady
        return

    def set_regenerationKit(self, _=None):
        self.__invalidateFLRegenerationKit()
        return

    def onLeaveWorld(self):
        return

    def __onAvatarReady(self):
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        BigWorld.callback(self._CALLBACK_DELAY, makeCallbackWeak(self.__invalidateFLRegenerationKit))
        return

    def __invalidateFLRegenerationKit(self):
        healPointEnter = {b'senderKey': b'healPoint', 
           b'isSourceVehicle': None, 
           b'isInactivation': (None if not self.regenerationKit[b'isActive'] else self.regenerationKit[b'isActive']), 
           b'endTime': (self.regenerationKit[b'endTime']), 
           b'duration': (self.regenerationKit[b'duration'])}
        invalidateVehicleMarkerState(self.entity, healPointEnter, self.regenerationKit, VEHICLE_VIEW_STATE.HEALING, b'invalidateFLRegenerationKit')
        return
