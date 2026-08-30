from __future__ import absolute_import
import BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent
import Event
from debug_utils import LOG_DEBUG

class VehicleBRStPatrickComponent(DynamicScriptComponent):
    onCoinsAdded = Event.Event()

    def set_coinsCount(self, prev):
        LOG_DEBUG(b'VehicleBRStPatrickComponent.set_coinsCount prev', prev, b'coinsCount', self.coinsCount)
        if self.__observedVehicleMatches():
            self.onCoinsAdded(self.coinsCount - prev, self.totalCoins, False)
        return

    def set_teammateCoinsCount(self, prev):
        LOG_DEBUG(b'VehicleBRStPatrickComponent.set_teammateCoinsCount prev', prev, b'teammateCoinsCount', self.teammateCoinsCount)
        if self.__observedVehicleMatches():
            self.onCoinsAdded(self.teammateCoinsCount - prev, self.totalCoins, True)
        return

    @property
    def totalCoins(self):
        return self.coinsCount + self.teammateCoinsCount

    def __observedVehicleMatches(self):
        attachedVehicle = BigWorld.player().getVehicleAttached()
        if attachedVehicle:
            return attachedVehicle.id == self.entity.id
        return False
