from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener
if typing.TYPE_CHECKING:
    from gui.battle_control.components_states.ammo import IComponentAmmoState
    from items.components.gun_installation_components import GunInstallationSlot
    from vehicles.entities import ShotParams

class IVehicleEventsLogic(object):
    onAppearanceReady = None
    onAppearanceReset = None
    onSiegeStateUpdated = None
    onVehicleDestroyed = None
    onObserverVehicleDataUpdated = None
    onCollectAmmoStates = None
    onCollectShotParams = None
    onCurrentShellChanged = None
    onDynamicComponentCreated = None
    onDynamicComponentDestroyed = None
    onDiscreteShotDone = None
    onShowDamageFromShot = None
    onVehicleHealthChanged = None

    def collectAmmoStates(self):
        raise NotImplementedError
        return


class IVehicleEvents(IClientEventsContainer, IVehicleEventsLogic):
    pass


class IVehicleEventsListenerLogic(object):

    def onAppearanceReady(self):
        return

    def onAppearanceReset(self):
        return

    def onSiegeStateUpdated(self, newState, timeToNextMode):
        return

    def onVehicleDestroyed(self):
        return

    def onObserverVehicleDataUpdated(self):
        return

    def onCollectAmmoStates(self, ammoStates):
        return

    def onCollectShotParams(self, shotParamsList):
        return

    def onCurrentShellChanged(self, intCD):
        return

    def onDynamicComponentCreated(self, component):
        return

    def onDynamicComponentDestroyed(self, component):
        return

    def onDiscreteShotDone(self, gunInstallationSlot):
        return

    def onShowDamageFromShot(self, attackerID, hitPoints, effectsIndex, damageFactor, lastMaterialIsShield):
        return

    def onVehicleHealthChanged(self, vehicleID, newHealth, oldHealth):
        return


class IVehicleEventsListener(IClientEventsContainerListener, IVehicleEventsListenerLogic):
    pass
