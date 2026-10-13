from __future__ import absolute_import
import logging, typing
from events_containers.common.containers.interfaces import IClientEventsContainerListener
from events_handler import eventHandler, subscribeToEvents, unsubscribeFromEvents
from gui.battle_control.battle_constants import SHELL_QUANTITY_UNKNOWN, SHELL_SET_RESULT
from gui.impl.gen.view_models.views.battle.shared.clip.shell_calibration_clip_model import ClipState, ShellCalibrationClipModel
from gui.impl.pub.view_component import ViewComponent
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater
from helpers import dependency
from items.vehicle_mechanics_types import VehicleMechanicKeys
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic
from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListenerLogic
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.consumables.ammo_ctrl import _GunSettings
    from ShellCalibrationController import ShellCalibrationController, ShellCalibrationModeState
_logger = logging.getLogger(__name__)

class ShellCalibrationClipPresenter(ViewComponent, IClientEventsContainerListener, IMechanicStatesListenerLogic, IVehicleMechanicsTrackerListenerLogic):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(ShellCalibrationClipPresenter, self).__init__(model=ShellCalibrationClipModel)
        self.__clipCapacity = 1
        self.__statesUpdater = None
        return

    @property
    def viewModel(self):
        return super(ShellCalibrationClipPresenter, self).getViewModel()

    def subscribeTo(self, events):
        subscribeToEvents(self, events, raiseException=False)
        return

    def unsubscribeFrom(self, events):
        unsubscribeFromEvents(self, events)
        return

    def lateSubscribeTo(self, events):
        if events is not None:
            events.lateSubscribe(self)
        return

    @eventHandler
    def onEventsContainerDestroy(self, events):
        unsubscribeFromEvents(self, events)
        return

    def _initialize(self, *args, **kwargs):
        super(ShellCalibrationClipPresenter, self)._initialize(*args, **kwargs)
        self.__statesUpdater = VehicleMechanicStatesUpdater(VehicleMechanicKeys.SHELL_CALIBRATION, self)
        self.__statesUpdater.initialize()
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is None:
            _logger.warning(b'ShellCalibrationClipPresenter._initialize: AmmoController is not available')
            return
        else:
            gunSettings = ammoCtrl.getGunSettings()
            if gunSettings is not None:
                self.__applyGunSettings(gunSettings)
            quantity, quantityInClip = ammoCtrl.getCurrentShells()
            if (quantity, quantityInClip) != (SHELL_QUANTITY_UNKNOWN, SHELL_QUANTITY_UNKNOWN):
                clipState = self.__computeClipState(quantityInClip)
                self.__applyAmmoStock(quantity, quantityInClip, clipState)
            return

    def _finalize(self):
        if self.__statesUpdater is not None:
            self.__statesUpdater.finalize()
            self.__statesUpdater.destroy()
            self.__statesUpdater = None
        super(ShellCalibrationClipPresenter, self)._finalize()
        return

    def _getEvents(self):
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is None:
            _logger.warning(b'ShellCalibrationClipPresenter: AmmoController is not available')
            return ()
        else:
            return (
             (
              ammoCtrl.onGunSettingsSet, self.__onGunSettingsSet),
             (
              ammoCtrl.onShellsUpdated, self.__onShellsUpdated),
             (
              ammoCtrl.onCurrentShellChanged, self.__onCurrentShellChanged),
             (
              ammoCtrl.onCurrentShellReset, self.__onCurrentShellReset))

    @eventHandler
    def onMechanicComponentCatching(self, component):
        self.__applyCalibrationState(component.getMechanicState())
        return

    @eventHandler
    def onMechanicComponentReleasing(self, component):
        self.__resetCalibrationState()
        return

    @eventHandler
    def onStatePrepared(self, state):
        self.__applyCalibrationState(state)
        return

    @eventHandler
    def onStateTransition(self, prevState, newState):
        self.__applyCalibrationState(newState)
        return

    @eventHandler
    def onStateObservation(self, state):
        self.__applyCalibrationState(state)
        return

    def __onGunSettingsSet(self, gunSettings):
        self.__applyGunSettings(gunSettings)
        return

    def __onShellsUpdated(self, intCD, quantity, quantityInClip, result):
        if not result & SHELL_SET_RESULT.CURRENT:
            return
        clipState = self.__computeClipState(quantityInClip)
        self.__applyAmmoStock(quantity, quantityInClip, clipState)
        return

    def __onCurrentShellChanged(self, intCD):
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is None:
            return
        else:
            quantity, quantityInClip = ammoCtrl.getCurrentShells()
            clipState = self.__computeClipState(quantityInClip)
            self.__applyAmmoStock(quantity, quantityInClip, clipState)
            return

    def __onCurrentShellReset(self):
        self.__applyAmmoStock(0, 0, ClipState.NORMAL)
        return

    def __applyGunSettings(self, gunSettings):
        self.__clipCapacity = gunSettings.clip.size
        with self.viewModel as model:
            model.setClipCapacity(self.__clipCapacity)
        return

    def __computeClipState(self, quantityInClip):
        if quantityInClip == SHELL_QUANTITY_UNKNOWN:
            return ClipState.NONE
        clipCapacity = self.__clipCapacity
        criticalCount = 1
        if quantityInClip <= criticalCount and clipCapacity > 2:
            return ClipState.CRITICAL
        return ClipState.NORMAL

    def __applyAmmoStock(self, quantity, quantityInClip, clipState):
        with self.viewModel as model:
            model.setTotalAmmo(quantity)
            model.setQuantityInClip(quantityInClip)
            model.setClipState(clipState)
        return

    def __applyCalibrationState(self, state):
        with self.viewModel as model:
            model.setCalibrationState(int(state.status))
        return

    def __resetCalibrationState(self):
        with self.viewModel as model:
            model.setCalibrationState(0)
        return
