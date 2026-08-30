from __future__ import absolute_import
import typing, weakref
from events_containers.common.containers import ClientEventsContainer, ClientEventsContainerDebugger
from vehicles.entities.vehicle_events.interfaces import IVehicleEventsLogic
if typing.TYPE_CHECKING:
    from gui.battle_control.components_states.ammo import IComponentAmmoState
    from Vehicle import Vehicle

class VehicleEvents(ClientEventsContainer, IVehicleEventsLogic):

    def __init__(self, vehicle):
        super(VehicleEvents, self).__init__()
        self.__vehicle = weakref.proxy(vehicle)
        self.onAppearanceReady = self._createEvent()
        self.onAppearanceComponentsReady = self._createEvent()
        self.onAppearanceReset = self._createEvent()
        self.onSiegeStateUpdated = self._createEvent()
        self.onVehicleDestroyed = self._createEvent()
        self.onCollectAmmoStates = self._createEvent()
        self.onCollectShotParams = self._createEvent()
        self.onCurrentShellChanged = self._createEvent()
        self.onDynamicComponentCreated = self._createEvent()
        self.onDynamicComponentDestroyed = self._createEvent()
        self.onDiscreteShotDone = self._createEvent()
        self.onShowDamageFromShot = self._createEvent()
        self.onVehicleHealthChanged = self._createEvent()
        self.onObserverVehicleDataUpdated = self._createEvent()
        return

    def destroy(self):
        self.__vehicle = None
        self.onVehicleDestroyed()
        super(VehicleEvents, self).destroy()
        return

    def collectAmmoStates(self):
        ammoStates = {}
        self.onCollectAmmoStates(ammoStates)
        return ammoStates

    def _createEventsDebugger(self):
        return VehicleEventsDebugger(self, self.__vehicle.id)


class VehicleEventsDebugger(ClientEventsContainerDebugger):
    IGNORED_EVENTS = ClientEventsContainerDebugger.IGNORED_EVENTS + (b'onAppearanceReady', b'onAppearanceReset', b'onCollectAmmoStates', b'onCollectShotParams', b'onCurrentShellChanged', b'onDiscreteShotDone', b'onShowDamageFromShot', b'onVehicleHealthChanged')

    def __init__(self, events, vehicleID):
        super(VehicleEventsDebugger, self).__init__(events)
        self.__vehicleID = vehicleID
        return

    def _getDebugPrefix(self):
        return (b'[VEH_EVENT][{}]').format(self.__vehicleID)
