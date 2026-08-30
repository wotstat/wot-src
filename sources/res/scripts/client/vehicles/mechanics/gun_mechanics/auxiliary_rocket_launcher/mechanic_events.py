from __future__ import absolute_import
import typing
from cache import last_cached_method
from cgf_events import gun_events
from events_handler import eventHandler
from vehicles.components.component_events import VehicleComponentEventsCoreIntegration
from vehicles.mechanics.mechanic_states import MechanicStatesEvents, IMechanicStatesListenerLogic
if typing.TYPE_CHECKING:
    from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher.mechanic_models import AuxiliaryRocketLauncherState

class AuxiliaryRocketLauncherStatesEvents(MechanicStatesEvents):

    def _createCoreIntegration(self):
        return AuxiliaryRocketLauncherStatesCoreIntegration(self, self._getComponent())


class AuxiliaryRocketLauncherStatesCoreIntegration(VehicleComponentEventsCoreIntegration, IMechanicStatesListenerLogic):

    @eventHandler
    def onStatePrepared(self, state):
        self.__postReloadEvent(state.isReloaded, state.reloadStartTime)
        return

    @eventHandler
    def onStateObservation(self, state):
        self.__postReloadEvent(state.isReloaded, state.reloadStartTime)
        return

    @last_cached_method(key=(lambda *args: args[0]))
    def __postReloadEvent(self, isReloaded, reloadStartTime):
        gun_events.postVehicularVariablesChangedEvent(self._spaceID, self._vehicleID, self._slotName, {b'vehicle/secondaryGun/isReloaded': isReloaded, 
           b'vehicle/secondaryGun/reloadStartTime': reloadStartTime})
        return
