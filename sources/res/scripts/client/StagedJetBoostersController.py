from __future__ import absolute_import, division
import logging, typing, BigWorld
from CommandMapping import CMD_CM_SPECIAL_ABILITY, CMD_CM_VEHICLE_SWITCH_AUTOROTATION
from cgf_components_common.vehicle_mechanics.staged_jet_boosters import StagedJetBoostersControllerDescriptor
from cgf_script.registration import registerReplicableComponent
from constants import PHASED_MECHANIC_STATE, IS_CLIENT, AcceleratorStatus
from gui.shared.utils.decorators import ReprInjector
from items.components.shared_components import StagedJetBoostersParams
from shared_utils import skipInEditor
from vehicles.components.component_wrappers import ifPlayerVehicle
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.mechanics.common import IMechanicComponent
from vehicles.mechanics.mechanic_commands import createMechanicCommandsEvents, IMechanicCommandsEvents, IMechanicCommandsComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanic, VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_logging import createMechanicInputLogger, IMechanicInputLoggingComponent
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent, createMechanicStatesEvents, IMechanicStatesEvents, IMechanicState
from wotdecorators import noexcept
if IS_CLIENT:
    import Input
    from Input import TriggerEvent
_logger = logging.getLogger(__name__)

@ReprInjector.simple(b'state', b'endTime', b'duration', b'count', b'acceleratorStatus', b'params')
class StagedJetBoostersState(typing.NamedTuple(b'StagedJetBoostersState', (
 (
  b'state', PHASED_MECHANIC_STATE),
 (
  b'endTime', float),
 (
  b'duration', float),
 (
  b'count', int),
 (
  b'acceleratorStatus', AcceleratorStatus),
 (
  b'params', typing.Optional[StagedJetBoostersParams]))), IMechanicState):

    @classmethod
    def fromComponentStatus(cls, status, acceleratorStatus, params):
        return cls(status.status, status.endTime, status.timeLeft, status.reuseCount, acceleratorStatus, params)

    @property
    def progress(self):
        progress = 1.0 if self.state == PHASED_MECHANIC_STATE.READY else 0.0
        if self.duration:
            timeLeft = self.timeLeft
            if self.state == PHASED_MECHANIC_STATE.ACTIVE:
                progress = timeLeft / self.duration
            else:
                progress = 1.0 - timeLeft / self.duration
        return progress

    @property
    def timeLeft(self):
        return max(0.0, self.endTime - BigWorld.serverTime())

    def isTransition(self, other):
        return self.state != other.state


@registerReplicableComponent
class StagedJetBoostersController(VehicleDynamicComponent, StagedJetBoostersControllerDescriptor, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent, IMechanicInputLoggingComponent):
    _INPUT_ACTION_NAME = b'ABILITY_0_INPUT_ACTION'
    _INPUT_PROFILE_NAME = b'ABILITY_0_INPUT_PROFILE'

    @skipInEditor
    def __init__(self):
        super(StagedJetBoostersController, self).__init__()
        _logger.debug(b'StagedJetBoostersController.__init__()')
        self.__params = None
        self.__currentState = StagedJetBoostersState(PHASED_MECHANIC_STATE.NOT_RUNNING, 0.0, 0.0, 0, AcceleratorStatus.NONE, None)
        self.__commandsEvents = createMechanicCommandsEvents(self)
        self.__statesEvents = createMechanicStatesEvents(self)
        self.__mechanicInputLogger = None
        self._initComponent()
        return

    def onDestroy(self):
        self.detachInput()
        self.__commandsEvents.destroy()
        self.__statesEvents.destroy()
        super(StagedJetBoostersController, self).onDestroy()
        return

    @property
    def vehicleMechanic(self):
        return VehicleMechanic.STAGED_JET_BOOSTERS

    @property
    def commandsEvents(self):
        return self.__commandsEvents

    @property
    def statesEvents(self):
        return self.__statesEvents

    @ifPlayerVehicle
    def attachInput(self, *_, **__):
        if not Input.inputSystem().hasProfile(self._INPUT_PROFILE_NAME):
            _logger.error(b'[INPUT] InputProfile %s is not loaded', self._INPUT_PROFILE_NAME)
            return
        inputAction = Input.inputSystem().findAction(self._INPUT_PROFILE_NAME, self._INPUT_ACTION_NAME)
        if inputAction:
            inputAction.bindEventReaction(TriggerEvent.Triggered, self.tryActivate)
        else:
            _logger.error(b"[INPUT] Can't find InputAction %s/%s", self._INPUT_PROFILE_NAME, self._INPUT_ACTION_NAME)
        Input.inputSystem().activateProfile(self._INPUT_PROFILE_NAME)
        return

    @ifPlayerVehicle
    def detachInput(self, *_, **__):
        if Input.inputSystem().hasProfile(self._INPUT_PROFILE_NAME):
            Input.inputSystem().deactivateProfile(self._INPUT_PROFILE_NAME, unbindAllReactions=True)
        return

    @ifPlayerVehicle
    def createInputLogger(self, *_, **__):
        if self.__mechanicInputLogger is not None:
            self.__mechanicInputLogger.destroy()
        self.__mechanicInputLogger = createMechanicInputLogger(self, CMD_CM_SPECIAL_ABILITY, CMD_CM_VEHICLE_SWITCH_AUTOROTATION)
        self.__mechanicInputLogger.start()
        return

    def getMechanicLogState(self):
        return {b'state': (self.__currentState.state), 
           b'time_left': (self.__currentState.timeLeft), 
           b'duration': (self.__currentState.duration), 
           b'mechanic_name': (self.vehicleMechanic.name)}

    def getMechanicState(self):
        return self.__currentState

    def tryActivate(self):
        if self.stateStatus.status == PHASED_MECHANIC_STATE.READY:
            self.cell.tryActivate()
        self.__commandsEvents.processMechanicCommand(VehicleMechanicCommand.ACTIVATE)
        return

    @noexcept
    def set_stateStatus(self, _=None):
        self._updateComponentAppearance()
        return

    @noexcept
    def set_acceleratorStatus(self, prev=None):
        self._updateComponentAppearance()
        return

    def _onAppearanceReady(self):
        super(StagedJetBoostersController, self)._onAppearanceReady()
        self.__updateMechanicState()
        self.__statesEvents.processStatePrepared()
        return

    def _collectComponentParams(self, typeDescriptor):
        super(StagedJetBoostersController, self)._collectComponentParams(typeDescriptor)
        self.__params = getVehicleDescrMechanicParams(typeDescriptor, self.vehicleMechanic)
        return

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(StagedJetBoostersController, self)._onComponentAppearanceUpdate(**kwargs)
        self.__updateMechanicState()
        self.__statesEvents.updateMechanicState(self.__currentState)
        return

    def __updateMechanicState(self):
        self.__currentState = StagedJetBoostersState.fromComponentStatus(self.stateStatus, self.acceleratorStatus, self.__params) if self.stateStatus else self.__currentState
        return
