from __future__ import absolute_import
import typing
from events_containers.common.containers import ContainersListener
from gui.Scaleform.daapi.view.meta.ChargeableBurstWidgetMeta import ChargeableBurstWidgetMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicles.mechanics.mechanic_constants import VehicleMechanic
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic
from events_handler import eventHandler
if typing.TYPE_CHECKING:
    from ChargeableBurstComponent import ChargeableBurstModeState
    from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater
    from gui.battle_control.controllers.consumables.ammo_ctrl import ReloadingTimeSnapshot

class ChargeableBurstMechanicWidget(ChargeableBurstWidgetMeta, ContainersListener, IMechanicStatesListenerLogic):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    @eventHandler
    def onStatePrepared(self, state):
        self.as_setupS(state.penetrationCount, state.burstCount)
        self.__invalidateAll(state, isInstantly=True)
        return

    @eventHandler
    def onStateTransition(self, prevState, newState):
        self.__invalidateMode(newState)
        return

    @eventHandler
    def onStateObservation(self, state):
        self.__invalidateCharges(state)
        return

    def _getViewUpdaters(self):
        return [
         VehicleMechanicPassengerUpdater(VehicleMechanic.CHARGEABLE_BURST, self),
         VehicleMechanicStatesUpdater(VehicleMechanic.CHARGEABLE_BURST, self)]

    def _populate(self):
        super(ChargeableBurstMechanicWidget, self)._populate()
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is not None:
            ammoCtrl.onShellsUpdated += self.__onShellsUpdated
            ammoCtrl.onCurrentShellChanged += self.__onCurrentShellChanged
            ammoCtrl.onCurrentShellReset += self.__onCurrentShellReset
            ammoCtrl.onGunReloadTimeSet += self.__onGunReloadTimeSet
        return

    def _dispose(self):
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is not None:
            ammoCtrl.onShellsUpdated -= self.__onShellsUpdated
            ammoCtrl.onCurrentShellChanged -= self.__onCurrentShellChanged
            ammoCtrl.onCurrentShellReset -= self.__onCurrentShellReset
            ammoCtrl.onGunReloadTimeSet -= self.__onGunReloadTimeSet
        super(ChargeableBurstMechanicWidget, self)._dispose()
        return

    def __onShellsUpdated(self, intCD, quantity, quantityInClip, result):
        self.__invalidateShells()
        return

    def __onCurrentShellChanged(self, intCD):
        self.__invalidateShells()
        return

    def __onCurrentShellReset(self):
        self.__invalidateShells()
        return

    def __onGunReloadTimeSet(self, currShellCD, state, skipAutoLoader):
        self.as_updateBurstReloadingStateS(not state.isReloadingFinished())
        return

    def __invalidateAll(self, state, isInstantly=False):
        self.__invalidateMode(state, isInstantly)
        self.__invalidateCharges(state, isInstantly)
        return

    def __invalidateMode(self, state, isInstantly=False):
        if state.isBurstActive:
            self.__invalidateShells()
        self.as_setModeS(state.isBurstActive, isInstantly)
        return

    def __invalidateCharges(self, state, isInstantly=False):
        self.as_setChargesS(state.charges, state.shots, isInstantly)
        return

    def __invalidateShells(self):
        ammoCtrl = self.__sessionProvider.shared.ammo
        quantity, _ = ammoCtrl.getCurrentShells()
        self.as_setShellsQuantityLeftS(quantity)
        return
